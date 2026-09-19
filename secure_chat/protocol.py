import json
import socket
import struct
from typing import Any

from secure_chat.config import MAX_PACKET_SIZE


class ProtocolError(Exception):
    """Raised when a peer sends an invalid protocol packet."""


class ChatProtocol:
    """
    Custom length-prefixed JSON protocol.

    Packet layout:
    - 4 bytes unsigned big-endian payload length
    - UTF-8 JSON payload
    """

    HEADER_SIZE = 4

    @staticmethod
    def send(sock: socket.socket, packet_type: str, **fields: Any) -> None:
        packet = {"type": packet_type, **fields}
        raw = json.dumps(packet, ensure_ascii=False).encode("utf-8")
        if len(raw) > MAX_PACKET_SIZE:
            raise ProtocolError("Packet is too large")

        header = struct.pack("!I", len(raw))
        sock.sendall(header + raw)

    @staticmethod
    def receive(sock: socket.socket) -> dict[str, Any]:
        header = ChatProtocol._receive_exact(sock, ChatProtocol.HEADER_SIZE)
        if not header:
            raise ConnectionError("Peer disconnected")

        (payload_size,) = struct.unpack("!I", header)
        if payload_size <= 0 or payload_size > MAX_PACKET_SIZE:
            raise ProtocolError("Invalid packet size")

        payload = ChatProtocol._receive_exact(sock, payload_size)
        try:
            packet = json.loads(payload.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ProtocolError("Packet is not valid UTF-8 JSON") from exc

        if not isinstance(packet, dict) or not isinstance(packet.get("type"), str):
            raise ProtocolError("Packet must contain a string type")

        return packet

    @staticmethod
    def _receive_exact(sock: socket.socket, size: int) -> bytes:
        chunks: list[bytes] = []
        remaining = size

        while remaining > 0:
            chunk = sock.recv(remaining)
            if not chunk:
                raise ConnectionError("Peer disconnected")
            chunks.append(chunk)
            remaining -= len(chunk)

        return b"".join(chunks)

