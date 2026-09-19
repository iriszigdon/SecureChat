# Remark: imports a module or object needed by this file.
import json
# Remark: imports a module or object needed by this file.
import socket
# Remark: imports a module or object needed by this file.
import struct
# Remark: imports a module or object needed by this file.
from typing import Any

# Remark: imports a module or object needed by this file.
from secure_chat.config import MAX_PACKET_SIZE


# Remark: defines a class for object-oriented structure.
class ProtocolError(Exception):
    # Remark: runs this instruction as part of the program logic.
    """Raised when a peer sends an invalid protocol packet."""


# Remark: defines a class for object-oriented structure.
class ChatProtocol:
    # Remark: runs this instruction as part of the program logic.
    """
    Custom length-prefixed JSON protocol.

    Packet layout:
    - 4 bytes unsigned big-endian payload length
    - UTF-8 JSON payload
    """

    # Remark: creates or updates a program value.
    HEADER_SIZE = 4

    # Remark: applies a decorator to the next function or method.
    @staticmethod
    # Remark: defines a function or method.
    def send(sock: socket.socket, packet_type: str, **fields: Any) -> None:
        # Remark: creates or updates a program value.
        packet = {"type": packet_type, **fields}
        # Remark: creates or updates a program value.
        raw = json.dumps(packet, ensure_ascii=False).encode("utf-8")
        # Remark: checks a condition before continuing.
        if len(raw) > MAX_PACKET_SIZE:
            # Remark: raises an error for invalid behavior.
            raise ProtocolError("Packet is too large")

        # Remark: places a widget in the graphical interface.
        header = struct.pack("!I", len(raw))
        # Remark: runs this instruction as part of the program logic.
        sock.sendall(header + raw)

    # Remark: applies a decorator to the next function or method.
    @staticmethod
    # Remark: defines a function or method.
    def receive(sock: socket.socket) -> dict[str, Any]:
        # Remark: creates or updates a program value.
        header = ChatProtocol._receive_exact(sock, ChatProtocol.HEADER_SIZE)
        # Remark: checks a condition before continuing.
        if not header:
            # Remark: raises an error for invalid behavior.
            raise ConnectionError("Peer disconnected")

        # Remark: places a widget in the graphical interface.
        (payload_size,) = struct.unpack("!I", header)
        # Remark: checks a condition before continuing.
        if payload_size <= 0 or payload_size > MAX_PACKET_SIZE:
            # Remark: raises an error for invalid behavior.
            raise ProtocolError("Invalid packet size")

        # Remark: creates or updates a program value.
        payload = ChatProtocol._receive_exact(sock, payload_size)
        # Remark: starts protected code that may raise an error.
        try:
            # Remark: creates or updates a program value.
            packet = json.loads(payload.decode("utf-8"))
        # Remark: handles an expected error safely.
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            # Remark: raises an error for invalid behavior.
            raise ProtocolError("Packet is not valid UTF-8 JSON") from exc

        # Remark: checks a condition before continuing.
        if not isinstance(packet, dict) or not isinstance(packet.get("type"), str):
            # Remark: raises an error for invalid behavior.
            raise ProtocolError("Packet must contain a string type")

        # Remark: returns a value to the caller.
        return packet

    # Remark: applies a decorator to the next function or method.
    @staticmethod
    # Remark: defines a function or method.
    def _receive_exact(sock: socket.socket, size: int) -> bytes:
        # Remark: creates or updates a program value.
        chunks: list[bytes] = []
        # Remark: creates or updates a program value.
        remaining = size

        # Remark: starts a loop that continues while a condition is true.
        while remaining > 0:
            # Remark: receives data from the network.
            chunk = sock.recv(remaining)
            # Remark: checks a condition before continuing.
            if not chunk:
                # Remark: raises an error for invalid behavior.
                raise ConnectionError("Peer disconnected")
            # Remark: runs this instruction as part of the program logic.
            chunks.append(chunk)
            # Remark: creates or updates a program value.
            remaining -= len(chunk)

        # Remark: returns a value to the caller.
        return b"".join(chunks)

