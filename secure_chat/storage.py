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
            # Remark: runs this instruction as part of the program logic.
            self._add_column_if_missing(connection, "users", "is_admin", "INTEGER NOT NULL DEFAULT 0")
            # Remark: runs this instruction as part of the program logic.
            self._add_column_if_missing(connection, "users", "profile_status", "TEXT NOT NULL DEFAULT ''")
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
            # Remark: runs this instruction as part of the program logic.
            self._add_column_if_missing(connection, "messages", "edited_at", "TEXT")
            # Remark: runs this instruction as part of the program logic.
            self._add_column_if_missing(connection, "messages", "deleted", "INTEGER NOT NULL DEFAULT 0")
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
            # Remark: runs this instruction as part of the program logic.
            self._add_column_if_missing(connection, "rooms", "password_hash", "TEXT")
            # Remark: runs this instruction as part of the program logic.
            self._add_column_if_missing(connection, "rooms", "owner", "TEXT")
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: runs this instruction as part of the program logic.
                """
                CREATE TABLE IF NOT EXISTS friends (
                    requester TEXT NOT NULL,
                    receiver TEXT NOT NULL,
                    status TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    PRIMARY KEY(requester, receiver)
                )
                """
            # Remark: closes a multi-line expression.
            )
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: runs this instruction as part of the program logic.
                """
                CREATE TABLE IF NOT EXISTS downloads (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL,
                    filename TEXT NOT NULL,
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
    def _add_column_if_missing(self, connection: sqlite3.Connection, table: str, column: str, definition: str) -> None:
        # Remark: creates or updates a program value.
        columns = [row["name"] for row in connection.execute(f"PRAGMA table_info({table})").fetchall()]
        # Remark: checks a condition before continuing.
        if column not in columns:
            # Remark: runs this instruction as part of the program logic.
            connection.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")

    # Remark: defines a function or method.
    def create_user(self, username: str, password: str) -> bool:
        # Remark: creates or updates a program value.
        password_hash = PasswordHasher.hash_password(password)
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: creates or updates a program value.
            user_count = connection.execute("SELECT COUNT(*) AS count FROM users").fetchone()["count"]
            # Remark: creates or updates a program value.
            is_admin = 1 if user_count == 0 or username.lower() == "admin" else 0
            # Remark: starts protected code that may raise an error.
            try:
                # Remark: starts a multi-line expression.
                connection.execute(
                    # Remark: runs this instruction as part of the program logic.
                    "INSERT INTO users(username, password_hash, created_at, is_admin) VALUES (?, ?, ?, ?)",
                    # Remark: runs this instruction as part of the program logic.
                    (username, password_hash, now_iso(), is_admin),
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
    def save_message(self, message: ChatMessage) -> int:
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
            cursor = connection.execute(
                # Remark: runs this instruction as part of the program logic.
                "INSERT INTO messages(sender, room, body, created_at) VALUES (?, ?, ?, ?)",
                # Remark: runs this instruction as part of the program logic.
                (message.sender, message.room, message.body, message.created_at),
            # Remark: closes a multi-line expression.
            )
            # Remark: returns a value to the caller.
            return int(cursor.lastrowid)

    # Remark: defines a function or method.
    def create_room(self, room: str, created_by: str, password: str = "") -> bool:
        # Remark: creates or updates a program value.
        password_hash = PasswordHasher.hash_password(password) if password else None
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts protected code that may raise an error.
            try:
                # Remark: starts a multi-line expression.
                connection.execute(
                    # Remark: runs this instruction as part of the program logic.
                    "INSERT INTO rooms(name, created_by, created_at, owner, password_hash) VALUES (?, ?, ?, ?, ?)",
                    # Remark: runs this instruction as part of the program logic.
                    (room, created_by, now_iso(), created_by, password_hash),
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
    def can_join_room(self, room: str, password: str = "") -> bool:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            row = connection.execute(
                # Remark: creates or updates a program value.
                "SELECT password_hash FROM rooms WHERE name = ?",
                # Remark: runs this instruction as part of the program logic.
                (room,),
            # Remark: closes a multi-line expression.
            ).fetchone()
        # Remark: checks a condition before continuing.
        if row is None:
            # Remark: returns a value to the caller.
            return False
        # Remark: checks a condition before continuing.
        if not row["password_hash"]:
            # Remark: returns a value to the caller.
            return True
        # Remark: returns a value to the caller.
        return PasswordHasher.verify_password(password, row["password_hash"])

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
                WHERE room = ? AND deleted = 0
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
    def is_admin(self, username: str) -> bool:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            row = connection.execute(
                # Remark: creates or updates a program value.
                "SELECT is_admin FROM users WHERE username = ?",
                # Remark: runs this instruction as part of the program logic.
                (username,),
            # Remark: closes a multi-line expression.
            ).fetchone()
        # Remark: returns a value to the caller.
        return bool(row and row["is_admin"])

    # Remark: defines a function or method.
    def update_profile(self, username: str, status: str) -> None:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: creates or updates a program value.
                "UPDATE users SET profile_status = ? WHERE username = ?",
                # Remark: runs this instruction as part of the program logic.
                (status, username),
            # Remark: closes a multi-line expression.
            )

    # Remark: defines a function or method.
    def get_profile(self, username: str) -> str:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            row = connection.execute(
                # Remark: creates or updates a program value.
                "SELECT profile_status FROM users WHERE username = ?",
                # Remark: runs this instruction as part of the program logic.
                (username,),
            # Remark: closes a multi-line expression.
            ).fetchone()
        # Remark: returns a value to the caller.
        return row["profile_status"] if row else "User not found"

    # Remark: defines a function or method.
    def search_messages(self, room: str, term: str, limit: int = 20) -> list[str]:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            rows = connection.execute(
                # Remark: runs this instruction as part of the program logic.
                """
                SELECT id, sender, body, created_at
                FROM messages
                WHERE room = ? AND body LIKE ? AND deleted = 0
                ORDER BY id DESC
                LIMIT ?
                """,
                # Remark: runs this instruction as part of the program logic.
                (room, f"%{term}%", limit),
            # Remark: closes a multi-line expression.
            ).fetchall()
        # Remark: returns a value to the caller.
        return [f"#{row['id']} [{row['created_at']}] {row['sender']}: {row['body']}" for row in rows]

    # Remark: defines a function or method.
    def image_gallery(self, room: str, limit: int = 20) -> list[str]:
        # Remark: returns a value to the caller.
        return self.search_messages(room, "[image]", limit)

    # Remark: defines a function or method.
    def edit_message(self, message_id: int, username: str, body: str, is_admin: bool) -> bool:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: creates or updates a program value.
            row = connection.execute("SELECT sender FROM messages WHERE id = ?", (message_id,)).fetchone()
            # Remark: checks a condition before continuing.
            if row is None or (row["sender"] != username and not is_admin):
                # Remark: returns a value to the caller.
                return False
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: creates or updates a program value.
                "UPDATE messages SET body = ?, edited_at = ? WHERE id = ?",
                # Remark: runs this instruction as part of the program logic.
                (body, now_iso(), message_id),
            # Remark: closes a multi-line expression.
            )
        # Remark: returns a value to the caller.
        return True

    # Remark: defines a function or method.
    def delete_message(self, message_id: int, username: str, is_admin: bool) -> bool:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: creates or updates a program value.
            row = connection.execute("SELECT sender FROM messages WHERE id = ?", (message_id,)).fetchone()
            # Remark: checks a condition before continuing.
            if row is None or (row["sender"] != username and not is_admin):
                # Remark: returns a value to the caller.
                return False
            # Remark: creates or updates a program value.
            connection.execute("UPDATE messages SET deleted = 1 WHERE id = ?", (message_id,))
        # Remark: returns a value to the caller.
        return True

    # Remark: defines a function or method.
    def send_friend_request(self, requester: str, receiver: str) -> bool:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts protected code that may raise an error.
            try:
                # Remark: starts a multi-line expression.
                connection.execute(
                    # Remark: runs this instruction as part of the program logic.
                    "INSERT INTO friends(requester, receiver, status, created_at) VALUES (?, ?, ?, ?)",
                    # Remark: runs this instruction as part of the program logic.
                    (requester, receiver, "pending", now_iso()),
                # Remark: closes a multi-line expression.
                )
            # Remark: handles an expected error safely.
            except sqlite3.IntegrityError:
                # Remark: returns a value to the caller.
                return False
        # Remark: returns a value to the caller.
        return True

    # Remark: defines a function or method.
    def accept_friend_request(self, requester: str, receiver: str) -> bool:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            cursor = connection.execute(
                # Remark: creates or updates a program value.
                "UPDATE friends SET status = 'accepted' WHERE requester = ? AND receiver = ?",
                # Remark: runs this instruction as part of the program logic.
                (requester, receiver),
            # Remark: closes a multi-line expression.
            )
        # Remark: returns a value to the caller.
        return cursor.rowcount > 0

    # Remark: defines a function or method.
    def list_friends(self, username: str) -> list[str]:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            rows = connection.execute(
                # Remark: runs this instruction as part of the program logic.
                """
                SELECT requester, receiver
                FROM friends
                WHERE status = 'accepted' AND (requester = ? OR receiver = ?)
                """,
                # Remark: runs this instruction as part of the program logic.
                (username, username),
            # Remark: closes a multi-line expression.
            ).fetchall()
        # Remark: returns a value to the caller.
        return [row["receiver"] if row["requester"] == username else row["requester"] for row in rows]

    # Remark: defines a function or method.
    def record_download(self, username: str, filename: str) -> None:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            connection.execute(
                # Remark: runs this instruction as part of the program logic.
                "INSERT INTO downloads(username, filename, created_at) VALUES (?, ?, ?)",
                # Remark: runs this instruction as part of the program logic.
                (username, filename, now_iso()),
            # Remark: closes a multi-line expression.
            )

    # Remark: defines a function or method.
    def audit_events(self, limit: int = 20) -> list[str]:
        # Remark: uses a managed resource safely.
        with self._lock, self._connect() as connection:
            # Remark: starts a multi-line expression.
            rows = connection.execute(
                # Remark: runs this instruction as part of the program logic.
                "SELECT event_type, details, created_at FROM audit_log ORDER BY id DESC LIMIT ?",
                # Remark: runs this instruction as part of the program logic.
                (limit,),
            # Remark: closes a multi-line expression.
            ).fetchall()
        # Remark: returns a value to the caller.
        return [f"[{row['created_at']}] {row['event_type']}: {row['details']}" for row in rows]

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

