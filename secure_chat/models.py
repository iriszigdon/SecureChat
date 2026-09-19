from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class User:
    username: str
    created_at: str


@dataclass(frozen=True)
class ChatMessage:
    sender: str
    room: str
    body: str
    created_at: str


@dataclass(frozen=True)
class ClientInfo:
    username: str
    room: str
    address: str


@dataclass(frozen=True)
class ServerEvent:
    event_type: str
    message: str
    created_at: str


def now_iso() -> str:
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

