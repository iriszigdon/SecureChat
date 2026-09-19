# Remark: imports a module or object needed by this file.
import argparse
# Remark: imports a module or object needed by this file.
import base64
# Remark: imports a module or object needed by this file.
import socket
# Remark: imports a module or object needed by this file.
import threading
# Remark: imports a module or object needed by this file.
import uuid
# Remark: imports a module or object needed by this file.
from typing import Optional

# Remark: imports a module or object needed by this file.
from secure_chat.config import DEFAULT_HOST, DEFAULT_PORT, LOG_PATH, MAX_FILE_SIZE, UPLOAD_DIR
# Remark: imports a module or object needed by this file.
from secure_chat.models import ChatMessage, ClientInfo, now_iso
# Remark: imports a module or object needed by this file.
from secure_chat.protocol import ChatProtocol, ProtocolError
# Remark: imports a module or object needed by this file.
from secure_chat.security import InputValidator, TLSContextFactory, ValidationError
# Remark: imports a module or object needed by this file.
from secure_chat.storage import ChatDatabase


# Remark: defines a class for object-oriented structure.
class ClientHandler(threading.Thread):
    # Remark: defines a function or method.
    def __init__(
        # Remark: runs this instruction as part of the program logic.
        self,
        # Remark: runs this instruction as part of the program logic.
        server: "SecureChatServer",
        # Remark: runs this instruction as part of the program logic.
        connection: socket.socket,
        # Remark: runs this instruction as part of the program logic.
        address: tuple[str, int],
    # Remark: closes a multi-line expression.
    ) -> None:
        # Remark: creates or updates a program value.
        super().__init__(daemon=True)
        # Remark: creates or updates a program value.
        self.server = server
        # Remark: creates or updates a program value.
        self.connection = connection
        # Remark: creates or updates a program value.
        self.address = f"{address[0]}:{address[1]}"
        # Remark: creates or updates a program value.
        self.username: Optional[str] = None
        # Remark: creates or updates a program value.
        self.room = "general"
        # Remark: creates or updates a program value.
        self.running = True

    # Remark: defines a function or method.
    def run(self) -> None:
        # Remark: starts protected code that may raise an error.
        try:
            # Remark: sends data or connects a GUI action.
            ChatProtocol.send(self.connection, "welcome", message="Connected to SecureChat")
            # Remark: starts a loop that continues while a condition is true.
            while self.running:
                # Remark: receives data from the network.
                packet = ChatProtocol.receive(self.connection)
                # Remark: runs this instruction as part of the program logic.
                self._handle_packet(packet)
        # Remark: handles an expected error safely.
        except (ConnectionError, OSError, ProtocolError, ValidationError) as exc:
            # Remark: runs this instruction as part of the program logic.
            self.server.log(f"Client {self.address} disconnected: {exc}")
        # Remark: runs cleanup code after protected code finishes.
        finally:
            # Remark: creates or updates a program value.
            self.running = False
            # Remark: runs this instruction as part of the program logic.
            self.server.remove_client(self)
            # Remark: runs this instruction as part of the program logic.
            self._safe_close()

    # Remark: defines a function or method.
    def send(self, packet_type: str, **fields: object) -> None:
        # Remark: sends data or connects a GUI action.
        ChatProtocol.send(self.connection, packet_type, **fields)

    # Remark: defines a function or method.
    def _handle_packet(self, packet: dict[str, object]) -> None:
        # Remark: creates or updates a program value.
        packet_type = packet["type"]

        # Remark: starts protected code that may raise an error.
        try:
            # Remark: checks a condition before continuing.
            if packet_type == "register":
                # Remark: runs this instruction as part of the program logic.
                self._register(packet)
            # Remark: checks another possible condition.
            elif packet_type == "login":
                # Remark: runs this instruction as part of the program logic.
                self._login(packet)
            # Remark: checks another possible condition.
            elif packet_type == "join":
                # Remark: runs this instruction as part of the program logic.
                self._require_login()
                # Remark: runs this instruction as part of the program logic.
                self._join(packet)
            # Remark: checks another possible condition.
            elif packet_type == "create_room":
                # Remark: runs this instruction as part of the program logic.
                self._require_login()
                # Remark: runs this instruction as part of the program logic.
                self._create_room(packet)
            # Remark: checks another possible condition.
            elif packet_type == "rooms":
                # Remark: runs this instruction as part of the program logic.
                self._require_login()
                # Remark: runs this instruction as part of the program logic.
                self._rooms()
            # Remark: checks another possible condition.
            elif packet_type == "message":
                # Remark: runs this instruction as part of the program logic.
                self._require_login()
                # Remark: runs this instruction as part of the program logic.
                self._message(packet)
            # Remark: checks another possible condition.
            elif packet_type == "file":
                # Remark: runs this instruction as part of the program logic.
                self._require_login()
                # Remark: runs this instruction as part of the program logic.
                self._file(packet)
            # Remark: checks another possible condition.
            elif packet_type == "users":
                # Remark: runs this instruction as part of the program logic.
                self._require_login()
                # Remark: runs this instruction as part of the program logic.
                self._users()
            # Remark: checks another possible condition.
            elif packet_type == "history":
                # Remark: runs this instruction as part of the program logic.
                self._require_login()
                # Remark: runs this instruction as part of the program logic.
                self._history()
            # Remark: checks another possible condition.
            elif packet_type == "logout":
                # Remark: creates or updates a program value.
                self.running = False
            # Remark: handles the case where previous conditions were false.
            else:
                # Remark: raises an error for invalid behavior.
                raise ProtocolError(f"Unknown packet type: {packet_type}")
        # Remark: handles an expected error safely.
        except ValidationError as exc:
            # Remark: sends data or connects a GUI action.
            self.send("error", action=packet_type, message=str(exc))

    # Remark: defines a function or method.
    def _register(self, packet: dict[str, object]) -> None:
        # Remark: creates or updates a program value.
        username = InputValidator.username(str(packet.get("username", "")))
        # Remark: creates or updates a program value.
        password = InputValidator.password(str(packet.get("password", "")))
        # Remark: creates or updates a program value.
        created = self.server.database.create_user(username, password)

        # Remark: checks a condition before continuing.
        if not created:
            # Remark: sends data or connects a GUI action.
            self.send("error", action="register", message="Username already exists")
            # Remark: returns a value to the caller.
            return

        # Remark: sends data or connects a GUI action.
        self.send("ok", action="register", message="Registration successful")

    # Remark: defines a function or method.
    def _login(self, packet: dict[str, object]) -> None:
        # Remark: creates or updates a program value.
        username = InputValidator.username(str(packet.get("username", "")))
        # Remark: creates or updates a program value.
        password = InputValidator.password(str(packet.get("password", "")))

        # Remark: checks a condition before continuing.
        if not self.server.database.authenticate(username, password):
            # Remark: runs this instruction as part of the program logic.
            self.server.database.log_event("login_failed", f"Failed login for {username}")
            # Remark: sends data or connects a GUI action.
            self.send("error", action="login", message="Invalid username or password")
            # Remark: returns a value to the caller.
            return

        # Remark: creates or updates a program value.
        self.username = username
        # Remark: runs this instruction as part of the program logic.
        self.server.add_client(self)
        # Remark: sends data or connects a GUI action.
        self.send("ok", action="login", message=f"Logged in as {username}")
        # Remark: runs this instruction as part of the program logic.
        self._rooms()
        # Remark: runs this instruction as part of the program logic.
        self._history()
        # Remark: runs this instruction as part of the program logic.
        self.server.broadcast_system(f"{username} joined {self.room}", self.room)

    # Remark: defines a function or method.
    def _join(self, packet: dict[str, object]) -> None:
        # Remark: creates or updates a program value.
        old_room = self.room
        # Remark: creates or updates a program value.
        requested_room = InputValidator.room(str(packet.get("room", "general")))
        # Remark: checks a condition before continuing.
        if not self.server.database.room_exists(requested_room):
            # Remark: sends data or connects a GUI action.
            self.send("error", action="join", message="Room does not exist. Create it first.")
            # Remark: returns a value to the caller.
            return

        # Remark: creates or updates a program value.
        self.room = requested_room
        # Remark: sends data or connects a GUI action.
        self.send("ok", action="join", room=self.room, message=f"Joined room {self.room}")
        # Remark: runs this instruction as part of the program logic.
        self._rooms()
        # Remark: runs this instruction as part of the program logic.
        self._history()
        # Remark: runs this instruction as part of the program logic.
        self.server.broadcast_system(f"{self.username} left {old_room}", old_room)
        # Remark: runs this instruction as part of the program logic.
        self.server.broadcast_system(f"{self.username} joined {self.room}", self.room)

    # Remark: defines a function or method.
    def _create_room(self, packet: dict[str, object]) -> None:
        # Remark: checks an assumption that should be true.
        assert self.username is not None
        # Remark: creates or updates a program value.
        room = InputValidator.room(str(packet.get("room", "")))
        # Remark: creates or updates a program value.
        created = self.server.database.create_room(room, self.username)

        # Remark: checks a condition before continuing.
        if not created:
            # Remark: sends data or connects a GUI action.
            self.send("error", action="create_room", message="Room already exists")
            # Remark: returns a value to the caller.
            return

        # Remark: sends data or connects a GUI action.
        self.send("ok", action="create_room", room=room, message=f"Room {room} created")
        # Remark: runs this instruction as part of the program logic.
        self.server.broadcast_rooms()

    # Remark: defines a function or method.
    def _message(self, packet: dict[str, object]) -> None:
        # Remark: creates or updates a program value.
        body = InputValidator.message(str(packet.get("body", "")))
        # Remark: checks an assumption that should be true.
        assert self.username is not None

        # Remark: starts a multi-line expression.
        message = ChatMessage(
            # Remark: creates or updates a program value.
            sender=self.username,
            # Remark: creates or updates a program value.
            room=self.room,
            # Remark: creates or updates a program value.
            body=body,
            # Remark: creates or updates a program value.
            created_at=now_iso(),
        # Remark: closes a multi-line expression.
        )
        # Remark: runs this instruction as part of the program logic.
        self.server.database.save_message(message)
        # Remark: runs this instruction as part of the program logic.
        self.server.broadcast_chat(message)

    # Remark: defines a function or method.
    def _file(self, packet: dict[str, object]) -> None:
        # Remark: checks an assumption that should be true.
        assert self.username is not None

        # Remark: creates or updates a program value.
        filename = InputValidator.filename(str(packet.get("filename", "")))
        # Remark: creates or updates a program value.
        kind = str(packet.get("kind", "file"))
        # Remark: creates or updates a program value.
        encoded_data = str(packet.get("data", ""))

        # Remark: starts protected code that may raise an error.
        try:
            # Remark: creates or updates a program value.
            file_data = base64.b64decode(encoded_data.encode("ascii"), validate=True)
        # Remark: handles an expected error safely.
        except Exception as exc:
            # Remark: raises an error for invalid behavior.
            raise ValidationError("File data is not valid base64") from exc

        # Remark: checks a condition before continuing.
        if len(file_data) > MAX_FILE_SIZE:
            # Remark: raises an error for invalid behavior.
            raise ValidationError(f"File is too large. Maximum size is {MAX_FILE_SIZE // (1024 * 1024)} MB")

        # Remark: creates or updates a program value.
        room_upload_dir = UPLOAD_DIR / self.room
        # Remark: creates or updates a program value.
        room_upload_dir.mkdir(parents=True, exist_ok=True)
        # Remark: creates or updates a program value.
        stored_filename = f"{uuid.uuid4().hex}_{filename}"
        # Remark: runs this instruction as part of the program logic.
        (room_upload_dir / stored_filename).write_bytes(file_data)

        # Remark: creates or updates a program value.
        created_at = now_iso()
        # Remark: starts a multi-line expression.
        message = ChatMessage(
            # Remark: creates or updates a program value.
            sender=self.username,
            # Remark: creates or updates a program value.
            room=self.room,
            # Remark: creates or updates a program value.
            body=f"[{kind}] {filename}",
            # Remark: creates or updates a program value.
            created_at=created_at,
        # Remark: closes a multi-line expression.
        )
        # Remark: runs this instruction as part of the program logic.
        self.server.database.save_message(message)
        # Remark: starts a multi-line expression.
        self.server.broadcast_file(
            # Remark: creates or updates a program value.
            sender=self.username,
            # Remark: creates or updates a program value.
            room=self.room,
            # Remark: creates or updates a program value.
            filename=filename,
            # Remark: creates or updates a program value.
            kind=kind,
            # Remark: creates or updates a program value.
            size=len(file_data),
            # Remark: creates or updates a program value.
            data=encoded_data,
            # Remark: creates or updates a program value.
            created_at=created_at,
        # Remark: closes a multi-line expression.
        )

    # Remark: defines a function or method.
    def _users(self) -> None:
        # Remark: creates or updates a program value.
        users = [user.username for user in self.server.database.list_users()]
        # Remark: creates or updates a program value.
        online = self.server.online_clients()
        # Remark: sends data or connects a GUI action.
        self.send("users", registered=users, online=online)

    # Remark: defines a function or method.
    def _rooms(self) -> None:
        # Remark: sends data or connects a GUI action.
        self.send("rooms", rooms=self.server.database.list_rooms(), current=self.room)

    # Remark: defines a function or method.
    def _history(self) -> None:
        # Remark: starts a multi-line expression.
        messages = [
            # Remark: starts a multi-line expression.
            {
                # Remark: runs this instruction as part of the program logic.
                "sender": message.sender,
                # Remark: runs this instruction as part of the program logic.
                "room": message.room,
                # Remark: runs this instruction as part of the program logic.
                "body": message.body,
                # Remark: runs this instruction as part of the program logic.
                "created_at": message.created_at,
            # Remark: closes a multi-line expression.
            }
            # Remark: starts a loop over multiple values.
            for message in self.server.database.recent_messages(self.room)
        # Remark: closes a multi-line expression.
        ]
        # Remark: sends data or connects a GUI action.
        self.send("history", room=self.room, messages=messages)

    # Remark: defines a function or method.
    def _require_login(self) -> None:
        # Remark: checks a condition before continuing.
        if self.username is None:
            # Remark: raises an error for invalid behavior.
            raise ProtocolError("Login required")

    # Remark: defines a function or method.
    def _safe_close(self) -> None:
        # Remark: starts protected code that may raise an error.
        try:
            # Remark: runs this instruction as part of the program logic.
            self.connection.close()
        # Remark: handles an expected error safely.
        except OSError:
            # Remark: runs this instruction as part of the program logic.
            pass


# Remark: defines a class for object-oriented structure.
class SecureChatServer:
    # Remark: defines a function or method.
    def __init__(self, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> None:
        # Remark: creates or updates a program value.
        self.host = host
        # Remark: creates or updates a program value.
        self.port = port
        # Remark: creates or updates a program value.
        self.database = ChatDatabase()
        # Remark: creates or updates a program value.
        self.clients: set[ClientHandler] = set()
        # Remark: creates or updates a program value.
        self.clients_lock = threading.Lock()
        # Remark: creates or updates a program value.
        self.running = False

    # Remark: defines a function or method.
    def start(self) -> None:
        # Remark: creates or updates a program value.
        context = TLSContextFactory.server_context()
        # Remark: creates or updates a program value.
        self.running = True

        # Remark: uses a managed resource safely.
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            # Remark: runs this instruction as part of the program logic.
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # Remark: runs this instruction as part of the program logic.
            server_socket.bind((self.host, self.port))
            # Remark: runs this instruction as part of the program logic.
            server_socket.listen()
            # Remark: runs this instruction as part of the program logic.
            self.log(f"Server listening on {self.host}:{self.port}")

            # Remark: starts a loop that continues while a condition is true.
            while self.running:
                # Remark: creates or updates a program value.
                raw_connection, address = server_socket.accept()
                # Remark: starts protected code that may raise an error.
                try:
                    # Remark: creates or updates a program value.
                    tls_connection = context.wrap_socket(raw_connection, server_side=True)
                # Remark: handles an expected error safely.
                except OSError as exc:
                    # Remark: runs this instruction as part of the program logic.
                    self.log(f"TLS handshake failed from {address}: {exc}")
                    # Remark: runs this instruction as part of the program logic.
                    raw_connection.close()
                    # Remark: runs this instruction as part of the program logic.
                    continue

                # Remark: runs this instruction as part of the program logic.
                ClientHandler(self, tls_connection, address).start()

    # Remark: defines a function or method.
    def add_client(self, client: ClientHandler) -> None:
        # Remark: uses a managed resource safely.
        with self.clients_lock:
            # Remark: runs this instruction as part of the program logic.
            self.clients.add(client)
        # Remark: runs this instruction as part of the program logic.
        self.database.log_event("login", f"{client.username} logged in from {client.address}")

    # Remark: defines a function or method.
    def remove_client(self, client: ClientHandler) -> None:
        # Remark: creates or updates a program value.
        removed = False
        # Remark: uses a managed resource safely.
        with self.clients_lock:
            # Remark: checks a condition before continuing.
            if client in self.clients:
                # Remark: runs this instruction as part of the program logic.
                self.clients.remove(client)
                # Remark: creates or updates a program value.
                removed = True

        # Remark: checks a condition before continuing.
        if removed and client.username:
            # Remark: runs this instruction as part of the program logic.
            self.broadcast_system(f"{client.username} disconnected", client.room)
            # Remark: runs this instruction as part of the program logic.
            self.database.log_event("disconnect", f"{client.username} disconnected")

    # Remark: defines a function or method.
    def broadcast_chat(self, message: ChatMessage) -> None:
        # Remark: starts a multi-line expression.
        payload = {
            # Remark: runs this instruction as part of the program logic.
            "sender": message.sender,
            # Remark: runs this instruction as part of the program logic.
            "room": message.room,
            # Remark: runs this instruction as part of the program logic.
            "body": message.body,
            # Remark: runs this instruction as part of the program logic.
            "created_at": message.created_at,
        # Remark: closes a multi-line expression.
        }
        # Remark: runs this instruction as part of the program logic.
        self._broadcast_to_room(message.room, "message", **payload)

    # Remark: defines a function or method.
    def broadcast_file(
        # Remark: runs this instruction as part of the program logic.
        self,
        # Remark: runs this instruction as part of the program logic.
        sender: str,
        # Remark: runs this instruction as part of the program logic.
        room: str,
        # Remark: runs this instruction as part of the program logic.
        filename: str,
        # Remark: runs this instruction as part of the program logic.
        kind: str,
        # Remark: runs this instruction as part of the program logic.
        size: int,
        # Remark: runs this instruction as part of the program logic.
        data: str,
        # Remark: runs this instruction as part of the program logic.
        created_at: str,
    # Remark: closes a multi-line expression.
    ) -> None:
        # Remark: starts a multi-line expression.
        self._broadcast_to_room(
            # Remark: runs this instruction as part of the program logic.
            room,
            # Remark: runs this instruction as part of the program logic.
            "file",
            # Remark: creates or updates a program value.
            sender=sender,
            # Remark: creates or updates a program value.
            room=room,
            # Remark: creates or updates a program value.
            filename=filename,
            # Remark: creates or updates a program value.
            kind=kind,
            # Remark: creates or updates a program value.
            size=size,
            # Remark: creates or updates a program value.
            data=data,
            # Remark: creates or updates a program value.
            created_at=created_at,
        # Remark: closes a multi-line expression.
        )

    # Remark: defines a function or method.
    def broadcast_system(self, text: str, room: str) -> None:
        # Remark: creates or updates a program value.
        self._broadcast_to_room(room, "system", room=room, message=text, created_at=now_iso())

    # Remark: defines a function or method.
    def broadcast_rooms(self) -> None:
        # Remark: creates or updates a program value.
        rooms = self.database.list_rooms()
        # Remark: uses a managed resource safely.
        with self.clients_lock:
            # Remark: creates or updates a program value.
            clients = list(self.clients)

        # Remark: starts a loop over multiple values.
        for client in clients:
            # Remark: starts protected code that may raise an error.
            try:
                # Remark: sends data or connects a GUI action.
                client.send("rooms", rooms=rooms, current=client.room)
            # Remark: handles an expected error safely.
            except OSError:
                # Remark: creates or updates a program value.
                client.running = False

    # Remark: defines a function or method.
    def online_clients(self) -> list[dict[str, str]]:
        # Remark: uses a managed resource safely.
        with self.clients_lock:
            # Remark: returns a value to the caller.
            return [
                # Remark: starts a multi-line expression.
                ClientInfo(
                    # Remark: creates or updates a program value.
                    username=client.username or "anonymous",
                    # Remark: creates or updates a program value.
                    room=client.room,
                    # Remark: creates or updates a program value.
                    address=client.address,
                # Remark: closes a multi-line expression.
                ).__dict__
                # Remark: starts a loop over multiple values.
                for client in self.clients
                # Remark: checks a condition before continuing.
                if client.username
            # Remark: closes a multi-line expression.
            ]

    # Remark: defines a function or method.
    def _broadcast_to_room(self, target_room: str, packet_type: str, **fields: object) -> None:
        # Remark: uses a managed resource safely.
        with self.clients_lock:
            # Remark: creates or updates a program value.
            clients = [client for client in self.clients if client.room == target_room]

        # Remark: starts a loop over multiple values.
        for client in clients:
            # Remark: starts protected code that may raise an error.
            try:
                # Remark: sends data or connects a GUI action.
                client.send(packet_type, **fields)
            # Remark: handles an expected error safely.
            except OSError:
                # Remark: creates or updates a program value.
                client.running = False

    # Remark: defines a function or method.
    def log(self, message: str) -> None:
        # Remark: creates or updates a program value.
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        # Remark: creates or updates a program value.
        line = f"[{now_iso()}] {message}"
        # Remark: runs this instruction as part of the program logic.
        print(line)
        # Remark: uses a managed resource safely.
        with LOG_PATH.open("a", encoding="utf-8") as log_file:
            # Remark: runs this instruction as part of the program logic.
            log_file.write(line + "\n")


# Remark: defines a function or method.
def parse_args() -> argparse.Namespace:
    # Remark: creates or updates a program value.
    parser = argparse.ArgumentParser(description="SecureChat threaded TLS server")
    # Remark: creates or updates a program value.
    parser.add_argument("--host", default=DEFAULT_HOST)
    # Remark: creates or updates a program value.
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    # Remark: returns a value to the caller.
    return parser.parse_args()


# Remark: checks a condition before continuing.
if __name__ == "__main__":
    # Remark: creates or updates a program value.
    args = parse_args()
    # Remark: creates or updates a program value.
    SecureChatServer(host=args.host, port=args.port).start()

