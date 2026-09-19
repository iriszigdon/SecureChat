# Remark: imports a module or object needed by this file.
import sqlite3
# Remark: imports a module or object needed by this file.
import threading
# Remark: imports a module or object needed by this file.
from pathlib import Path

# Remark: imports a module or object needed by this file.
from secure_chat.config import DATABASE_PATH, DATA_DIR
# Remark: imports a module or object needed by this file.
from secure_chat.models import ChatMessage, User, now_iso
# Remark: imports a module or object needed by this file.
from secure_chat.security import PasswordHasher


# Remark: defines a class for object-oriented structure.
class ChatDatabase:
    # Remark: defines a function or method.
    def __init__(self, path: Path = DATABASE_PATH) -> None:
        # Remark: creates or updates a program value.
        self.path = path
        # Remark: creates or updates a program value.
        self._lock = threading.Lock()
        # Remark: creates or updates a program value.
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        # Remark: runs this instruction as part of the program logic.
        self._initialize()

    # Remark: defines a function or method.
    def _connect(self) -> sqlite3.Connection:
        # Remark: creates or updates a program value.
        connection = sqlite3.connect(self.path, check_same_thread=False)
        # Remark: creates or updates a program value.
        connection.row_factory = sqlite3.Row
        # Remark: returns a value to the caller.
        return connection

    # Remark: defines a function or method.
    def _initialize(self) -> None:
        # Remark: uses a managed resource safely.
        with self._connect() as connection:
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: runs this instruction as part of the program logic.
                """
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password_hash TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            # Remark: closes a multi-line expression.
            )
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: runs this instruction as part of the program logic.
                """
                CREATE TABLE IF NOT EXISTS messages (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    sender TEXT NOT NULL,
                    room TEXT NOT NULL,
                    body TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    FOREIGN KEY(sender) REFERENCES users(username)
                )
                """
            # Remark: closes a multi-line expression.
            )
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: runs this instruction as part of the program logic.
                """
                CREATE TABLE IF NOT EXISTS rooms (
                    name TEXT PRIMARY KEY,
                    created_by TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            # Remark: closes a multi-line expression.
            )
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: runs this instruction as part of the program logic.
                """
                CREATE TABLE IF NOT EXISTS audit_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_type TEXT NOT NULL,
                    details TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            # Remark: closes a multi-line expression.
            )
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: runs this instruction as part of the program logic.
                "INSERT OR IGNORE INTO rooms(name, created_by, created_at) VALUES (?, ?, ?)",
                # Remark: runs this instruction as part of the program logic.
                ("general", "system", now_iso()),
            # Remark: closes a multi-line expression.
            )

    # Remark: defines a function or method.
    def create_user(self, username: str, password: str) -> bool:
        # Remark: creates or updates a program value.
        password_hash = PasswordHasher.hash_password(password)
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts protected code that may raise an error.
            try:
                # Remark: starts a multi-line expression.
                connection.execute(
                    # Remark: runs this instruction as part of the program logic.
                    "INSERT INTO users(username, password_hash, created_at) VALUES (?, ?, ?)",
                    # Remark: runs this instruction as part of the program logic.
                    (username, password_hash, now_iso()),
                # Remark: closes a multi-line expression.
                )
            # Remark: handles an expected error safely.
            except sqlite3.IntegrityError:
                # Remark: returns a value to the caller.
                return False
        # Remark: runs this instruction as part of the program logic.
        self.log_event("register", f"User registered: {username}")
        # Remark: returns a value to the caller.
        return True

    # Remark: defines a function or method.
    def authenticate(self, username: str, password: str) -> bool:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            row = connection.execute(
                # Remark: creates or updates a program value.
                "SELECT password_hash FROM users WHERE username = ?",
                # Remark: runs this instruction as part of the program logic.
                (username,),
            # Remark: closes a multi-line expression.
            ).fetchone()

        # Remark: checks a condition before continuing.
        if row is None:
            # Remark: returns a value to the caller.
            return False

        # Remark: returns a value to the caller.
        return PasswordHasher.verify_password(password, row["password_hash"])

    # Remark: defines a function or method.
    def save_message(self, message: ChatMessage) -> None:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: runs this instruction as part of the program logic.
                "INSERT OR IGNORE INTO rooms(name, created_by, created_at) VALUES (?, ?, ?)",
                # Remark: runs this instruction as part of the program logic.
                (message.room, message.sender, now_iso()),
            # Remark: closes a multi-line expression.
            )
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: runs this instruction as part of the program logic.
                "INSERT INTO messages(sender, room, body, created_at) VALUES (?, ?, ?, ?)",
                # Remark: runs this instruction as part of the program logic.
                (message.sender, message.room, message.body, message.created_at),
            # Remark: closes a multi-line expression.
            )

    # Remark: defines a function or method.
    def create_room(self, room: str, created_by: str) -> bool:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts protected code that may raise an error.
            try:
                # Remark: starts a multi-line expression.
                connection.execute(
                    # Remark: runs this instruction as part of the program logic.
                    "INSERT INTO rooms(name, created_by, created_at) VALUES (?, ?, ?)",
                    # Remark: runs this instruction as part of the program logic.
                    (room, created_by, now_iso()),
                # Remark: closes a multi-line expression.
                )
            # Remark: handles an expected error safely.
            except sqlite3.IntegrityError:
                # Remark: returns a value to the caller.
                return False
        # Remark: runs this instruction as part of the program logic.
        self.log_event("room_created", f"{created_by} created room {room}")
        # Remark: returns a value to the caller.
        return True

    # Remark: defines a function or method.
    def room_exists(self, room: str) -> bool:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            row = connection.execute(
                # Remark: creates or updates a program value.
                "SELECT 1 FROM rooms WHERE name = ?",
                # Remark: runs this instruction as part of the program logic.
                (room,),
            # Remark: closes a multi-line expression.
            ).fetchone()
        # Remark: returns a value to the caller.
        return row is not None

    # Remark: defines a function or method.
    def list_rooms(self) -> list[str]:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: creates or updates a program value.
            rows = connection.execute("SELECT name FROM rooms ORDER BY name").fetchall()
        # Remark: returns a value to the caller.
        return [row["name"] for row in rows]

    # Remark: defines a function or method.
    def recent_messages(self, room: str, limit: int = 50) -> list[ChatMessage]:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            rows = connection.execute(
                # Remark: runs this instruction as part of the program logic.
                """
                SELECT sender, room, body, created_at
                FROM messages
                WHERE room = ?
                ORDER BY id DESC
                LIMIT ?
                """,
                # Remark: runs this instruction as part of the program logic.
                (room, limit),
            # Remark: closes a multi-line expression.
            ).fetchall()

        # Remark: returns a value to the caller.
        return [
            # Remark: starts a multi-line expression.
            ChatMessage(
                # Remark: creates or updates a program value.
                sender=row["sender"],
                # Remark: creates or updates a program value.
                room=row["room"],
                # Remark: creates or updates a program value.
                body=row["body"],
                # Remark: creates or updates a program value.
                created_at=row["created_at"],
            # Remark: closes a multi-line expression.
            )
            # Remark: starts a loop over multiple values.
            for row in reversed(rows)
        # Remark: closes a multi-line expression.
        ]

    # Remark: defines a function or method.
    def list_users(self) -> list[User]:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            rows = connection.execute(
                # Remark: runs this instruction as part of the program logic.
                "SELECT username, created_at FROM users ORDER BY username"
            # Remark: closes a multi-line expression.
            ).fetchall()

        # Remark: returns a value to the caller.
        return [User(username=row["username"], created_at=row["created_at"]) for row in rows]

    # Remark: defines a function or method.
    def log_event(self, event_type: str, details: str) -> None:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: runs this instruction as part of the program logic.
                "INSERT INTO audit_log(event_type, details, created_at) VALUES (?, ?, ?)",
                # Remark: runs this instruction as part of the program logic.
                (event_type, details, now_iso()),
            # Remark: closes a multi-line expression.
            )

