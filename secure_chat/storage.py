import sqlite3
import threading
from pathlib import Path

from secure_chat.config import DATABASE_PATH, DATA_DIR
from secure_chat.models import ChatMessage, User, now_iso
from secure_chat.security import PasswordHasher


class ChatDatabase:
    def __init__(self, path: Path = DATABASE_PATH) -> None:
        self.path = path
        self._lock = threading.Lock()
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        self._initialize()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.path, check_same_thread=False)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    password_hash TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            connection.execute(
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
            )
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS rooms (
                    name TEXT PRIMARY KEY,
                    created_by TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            connection.execute(
                """
                CREATE TABLE IF NOT EXISTS audit_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    event_type TEXT NOT NULL,
                    details TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
                """
            )
            connection.execute(
                "INSERT OR IGNORE INTO rooms(name, created_by, created_at) VALUES (?, ?, ?)",
                ("general", "system", now_iso()),
            )

    def create_user(self, username: str, password: str) -> bool:
        password_hash = PasswordHasher.hash_password(password)
        with self._lock, self._connect() as connection:
            try:
                connection.execute(
                    "INSERT INTO users(username, password_hash, created_at) VALUES (?, ?, ?)",
                    (username, password_hash, now_iso()),
                )
            except sqlite3.IntegrityError:
                return False
        self.log_event("register", f"User registered: {username}")
        return True

    def authenticate(self, username: str, password: str) -> bool:
        with self._lock, self._connect() as connection:
            row = connection.execute(
                "SELECT password_hash FROM users WHERE username = ?",
                (username,),
            ).fetchone()

        if row is None:
            return False

        return PasswordHasher.verify_password(password, row["password_hash"])

    def save_message(self, message: ChatMessage) -> None:
        with self._lock, self._connect() as connection:
            connection.execute(
                "INSERT OR IGNORE INTO rooms(name, created_by, created_at) VALUES (?, ?, ?)",
                (message.room, message.sender, now_iso()),
            )
            connection.execute(
                "INSERT INTO messages(sender, room, body, created_at) VALUES (?, ?, ?, ?)",
                (message.sender, message.room, message.body, message.created_at),
            )

    def create_room(self, room: str, created_by: str) -> bool:
        with self._lock, self._connect() as connection:
            try:
                connection.execute(
                    "INSERT INTO rooms(name, created_by, created_at) VALUES (?, ?, ?)",
                    (room, created_by, now_iso()),
                )
            except sqlite3.IntegrityError:
                return False
        self.log_event("room_created", f"{created_by} created room {room}")
        return True

    def room_exists(self, room: str) -> bool:
        with self._lock, self._connect() as connection:
            row = connection.execute(
                "SELECT 1 FROM rooms WHERE name = ?",
                (room,),
            ).fetchone()
        return row is not None

    def list_rooms(self) -> list[str]:
        with self._lock, self._connect() as connection:
            rows = connection.execute("SELECT name FROM rooms ORDER BY name").fetchall()
        return [row["name"] for row in rows]

    def recent_messages(self, room: str, limit: int = 50) -> list[ChatMessage]:
        with self._lock, self._connect() as connection:
            rows = connection.execute(
                """
                SELECT sender, room, body, created_at
                FROM messages
                WHERE room = ?
                ORDER BY id DESC
                LIMIT ?
                """,
                (room, limit),
            ).fetchall()

        return [
            ChatMessage(
                sender=row["sender"],
                room=row["room"],
                body=row["body"],
                created_at=row["created_at"],
            )
            for row in reversed(rows)
        ]

    def list_users(self) -> list[User]:
        with self._lock, self._connect() as connection:
            rows = connection.execute(
                "SELECT username, created_at FROM users ORDER BY username"
            ).fetchall()

        return [User(username=row["username"], created_at=row["created_at"]) for row in rows]

    def log_event(self, event_type: str, details: str) -> None:
        with self._lock, self._connect() as connection:
            connection.execute(
                "INSERT INTO audit_log(event_type, details, created_at) VALUES (?, ?, ?)",
                (event_type, details, now_iso()),
            )

