from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
CERT_DIR = PROJECT_ROOT / "certs"
DOWNLOAD_DIR = PROJECT_ROOT / "downloads"
UPLOAD_DIR = DATA_DIR / "uploads"

DATABASE_PATH = DATA_DIR / "secure_chat.db"
LOG_PATH = DATA_DIR / "server.log"
CERT_PATH = CERT_DIR / "server.crt"
KEY_PATH = CERT_DIR / "server.key"

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 5050

# Media is sent as base64 inside JSON, so packets must be larger than plain text messages.
MAX_PACKET_SIZE = 25 * 1024 * 1024
MAX_FILE_SIZE = 15 * 1024 * 1024
MAX_USERNAME_LENGTH = 20
MAX_PASSWORD_LENGTH = 128
MAX_ROOM_LENGTH = 30
MAX_MESSAGE_LENGTH = 1000
MAX_FILENAME_LENGTH = 120

PBKDF2_ITERATIONS = 250_000

