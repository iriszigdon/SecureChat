import argparse
import base64
import socket
import threading
import uuid
from typing import Optional

from secure_chat.config import DEFAULT_HOST, DEFAULT_PORT, LOG_PATH, MAX_FILE_SIZE, UPLOAD_DIR
from secure_chat.models import ChatMessage, ClientInfo, now_iso
from secure_chat.protocol import ChatProtocol, ProtocolError
from secure_chat.security import InputValidator, TLSContextFactory, ValidationError
from secure_chat.storage import ChatDatabase


class ClientHandler(threading.Thread):
    def __init__(
        self,
        server: "SecureChatServer",
        connection: socket.socket,
        address: tuple[str, int],
    ) -> None:
        super().__init__(daemon=True)
        self.server = server
        self.connection = connection
        self.address = f"{address[0]}:{address[1]}"
        self.username: Optional[str] = None
        self.room = "general"
        self.running = True

    def run(self) -> None:
        try:
            ChatProtocol.send(self.connection, "welcome", message="Connected to SecureChat")
            while self.running:
                packet = ChatProtocol.receive(self.connection)
                self._handle_packet(packet)
        except (ConnectionError, OSError, ProtocolError, ValidationError) as exc:
            self.server.log(f"Client {self.address} disconnected: {exc}")
        finally:
            self.running = False
            self.server.remove_client(self)
            self._safe_close()

    def send(self, packet_type: str, **fields: object) -> None:
        ChatProtocol.send(self.connection, packet_type, **fields)

    def _handle_packet(self, packet: dict[str, object]) -> None:
        packet_type = packet["type"]

        try:
            if packet_type == "register":
                self._register(packet)
            elif packet_type == "login":
                self._login(packet)
            elif packet_type == "join":
                self._require_login()
                self._join(packet)
            elif packet_type == "create_room":
                self._require_login()
                self._create_room(packet)
            elif packet_type == "rooms":
                self._require_login()
                self._rooms()
            elif packet_type == "message":
                self._require_login()
                self._message(packet)
            elif packet_type == "file":
                self._require_login()
                self._file(packet)
            elif packet_type == "users":
                self._require_login()
                self._users()
            elif packet_type == "history":
                self._require_login()
                self._history()
            elif packet_type == "logout":
                self.running = False
            else:
                raise ProtocolError(f"Unknown packet type: {packet_type}")
        except ValidationError as exc:
            self.send("error", action=packet_type, message=str(exc))

    def _register(self, packet: dict[str, object]) -> None:
        username = InputValidator.username(str(packet.get("username", "")))
        password = InputValidator.password(str(packet.get("password", "")))
        created = self.server.database.create_user(username, password)

        if not created:
            self.send("error", action="register", message="Username already exists")
            return

        self.send("ok", action="register", message="Registration successful")

    def _login(self, packet: dict[str, object]) -> None:
        username = InputValidator.username(str(packet.get("username", "")))
        password = InputValidator.password(str(packet.get("password", "")))

        if not self.server.database.authenticate(username, password):
            self.server.database.log_event("login_failed", f"Failed login for {username}")
            self.send("error", action="login", message="Invalid username or password")
            return

        self.username = username
        self.server.add_client(self)
        self.send("ok", action="login", message=f"Logged in as {username}")
        self._rooms()
        self._history()
        self.server.broadcast_system(f"{username} joined {self.room}", self.room)

    def _join(self, packet: dict[str, object]) -> None:
        old_room = self.room
        requested_room = InputValidator.room(str(packet.get("room", "general")))
        if not self.server.database.room_exists(requested_room):
            self.send("error", action="join", message="Room does not exist. Create it first.")
            return

        self.room = requested_room
        self.send("ok", action="join", room=self.room, message=f"Joined room {self.room}")
        self._rooms()
        self._history()
        self.server.broadcast_system(f"{self.username} left {old_room}", old_room)
        self.server.broadcast_system(f"{self.username} joined {self.room}", self.room)

    def _create_room(self, packet: dict[str, object]) -> None:
        assert self.username is not None
        room = InputValidator.room(str(packet.get("room", "")))
        created = self.server.database.create_room(room, self.username)

        if not created:
            self.send("error", action="create_room", message="Room already exists")
            return

        self.send("ok", action="create_room", room=room, message=f"Room {room} created")
        self.server.broadcast_rooms()

    def _message(self, packet: dict[str, object]) -> None:
        body = InputValidator.message(str(packet.get("body", "")))
        assert self.username is not None

        message = ChatMessage(
            sender=self.username,
            room=self.room,
            body=body,
            created_at=now_iso(),
        )
        self.server.database.save_message(message)
        self.server.broadcast_chat(message)

    def _file(self, packet: dict[str, object]) -> None:
        assert self.username is not None

        filename = InputValidator.filename(str(packet.get("filename", "")))
        kind = str(packet.get("kind", "file"))
        encoded_data = str(packet.get("data", ""))

        try:
            file_data = base64.b64decode(encoded_data.encode("ascii"), validate=True)
        except Exception as exc:
            raise ValidationError("File data is not valid base64") from exc

        if len(file_data) > MAX_FILE_SIZE:
            raise ValidationError(f"File is too large. Maximum size is {MAX_FILE_SIZE // (1024 * 1024)} MB")

        room_upload_dir = UPLOAD_DIR / self.room
        room_upload_dir.mkdir(parents=True, exist_ok=True)
        stored_filename = f"{uuid.uuid4().hex}_{filename}"
        (room_upload_dir / stored_filename).write_bytes(file_data)

        created_at = now_iso()
        message = ChatMessage(
            sender=self.username,
            room=self.room,
            body=f"[{kind}] {filename}",
            created_at=created_at,
        )
        self.server.database.save_message(message)
        self.server.broadcast_file(
            sender=self.username,
            room=self.room,
            filename=filename,
            kind=kind,
            size=len(file_data),
            data=encoded_data,
            created_at=created_at,
        )

    def _users(self) -> None:
        users = [user.username for user in self.server.database.list_users()]
        online = self.server.online_clients()
        self.send("users", registered=users, online=online)

    def _rooms(self) -> None:
        self.send("rooms", rooms=self.server.database.list_rooms(), current=self.room)

    def _history(self) -> None:
        messages = [
            {
                "sender": message.sender,
                "room": message.room,
                "body": message.body,
                "created_at": message.created_at,
            }
            for message in self.server.database.recent_messages(self.room)
        ]
        self.send("history", room=self.room, messages=messages)

    def _require_login(self) -> None:
        if self.username is None:
            raise ProtocolError("Login required")

    def _safe_close(self) -> None:
        try:
            self.connection.close()
        except OSError:
            pass


class SecureChatServer:
    def __init__(self, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> None:
        self.host = host
        self.port = port
        self.database = ChatDatabase()
        self.clients: set[ClientHandler] = set()
        self.clients_lock = threading.Lock()
        self.running = False

    def start(self) -> None:
        context = TLSContextFactory.server_context()
        self.running = True

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((self.host, self.port))
            server_socket.listen()
            self.log(f"Server listening on {self.host}:{self.port}")

            while self.running:
                raw_connection, address = server_socket.accept()
                try:
                    tls_connection = context.wrap_socket(raw_connection, server_side=True)
                except OSError as exc:
                    self.log(f"TLS handshake failed from {address}: {exc}")
                    raw_connection.close()
                    continue

                ClientHandler(self, tls_connection, address).start()

    def add_client(self, client: ClientHandler) -> None:
        with self.clients_lock:
            self.clients.add(client)
        self.database.log_event("login", f"{client.username} logged in from {client.address}")

    def remove_client(self, client: ClientHandler) -> None:
        removed = False
        with self.clients_lock:
            if client in self.clients:
                self.clients.remove(client)
                removed = True

        if removed and client.username:
            self.broadcast_system(f"{client.username} disconnected", client.room)
            self.database.log_event("disconnect", f"{client.username} disconnected")

    def broadcast_chat(self, message: ChatMessage) -> None:
        payload = {
            "sender": message.sender,
            "room": message.room,
            "body": message.body,
            "created_at": message.created_at,
        }
        self._broadcast_to_room(message.room, "message", **payload)

    def broadcast_file(
        self,
        sender: str,
        room: str,
        filename: str,
        kind: str,
        size: int,
        data: str,
        created_at: str,
    ) -> None:
        self._broadcast_to_room(
            room,
            "file",
            sender=sender,
            room=room,
            filename=filename,
            kind=kind,
            size=size,
            data=data,
            created_at=created_at,
        )

    def broadcast_system(self, text: str, room: str) -> None:
        self._broadcast_to_room(room, "system", room=room, message=text, created_at=now_iso())

    def broadcast_rooms(self) -> None:
        rooms = self.database.list_rooms()
        with self.clients_lock:
            clients = list(self.clients)

        for client in clients:
            try:
                client.send("rooms", rooms=rooms, current=client.room)
            except OSError:
                client.running = False

    def online_clients(self) -> list[dict[str, str]]:
        with self.clients_lock:
            return [
                ClientInfo(
                    username=client.username or "anonymous",
                    room=client.room,
                    address=client.address,
                ).__dict__
                for client in self.clients
                if client.username
            ]

    def _broadcast_to_room(self, target_room: str, packet_type: str, **fields: object) -> None:
        with self.clients_lock:
            clients = [client for client in self.clients if client.room == target_room]

        for client in clients:
            try:
                client.send(packet_type, **fields)
            except OSError:
                client.running = False

    def log(self, message: str) -> None:
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        line = f"[{now_iso()}] {message}"
        print(line)
        with LOG_PATH.open("a", encoding="utf-8") as log_file:
            log_file.write(line + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="SecureChat threaded TLS server")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    SecureChatServer(host=args.host, port=args.port).start()

