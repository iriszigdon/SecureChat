# Remark: imports a module or object needed by this file.
from dataclasses import dataclass
# Remark: imports a module or object needed by this file.
from datetime import datetime


# Remark: applies a decorator to the next function or method.
@dataclass(frozen=True)
# Remark: defines a class for object-oriented structure.
class User:
    # Remark: runs this instruction as part of the program logic.
    username: str
    # Remark: runs this instruction as part of the program logic.
    created_at: str


# Remark: applies a decorator to the next function or method.
@dataclass(frozen=True)
# Remark: defines a class for object-oriented structure.
class ChatMessage:
    # Remark: runs this instruction as part of the program logic.
    sender: str
    # Remark: runs this instruction as part of the program logic.
    room: str
    # Remark: runs this instruction as part of the program logic.
    body: str
    # Remark: runs this instruction as part of the program logic.
    created_at: str


# Remark: applies a decorator to the next function or method.
@dataclass(frozen=True)
# Remark: defines a class for object-oriented structure.
class ClientInfo:
    # Remark: runs this instruction as part of the program logic.
    username: str
    # Remark: runs this instruction as part of the program logic.
    room: str
    # Remark: runs this instruction as part of the program logic.
    address: str


# Remark: applies a decorator to the next function or method.
@dataclass(frozen=True)
# Remark: defines a class for object-oriented structure.
class ServerEvent:
    # Remark: runs this instruction as part of the program logic.
    event_type: str
    # Remark: runs this instruction as part of the program logic.
    message: str
    # Remark: runs this instruction as part of the program logic.
    created_at: str


# Remark: defines a function or method.
def now_iso() -> str:
    # Remark: returns a value to the caller.
    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

