# Remark: imports a module or object needed by this file.
from pathlib import Path


# Remark: creates or updates a program value.
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# Remark: creates or updates a program value.
DATA_DIR = PROJECT_ROOT / "data"
# Remark: creates or updates a program value.
CERT_DIR = PROJECT_ROOT / "certs"
# Remark: creates or updates a program value.
DOWNLOAD_DIR = PROJECT_ROOT / "downloads"
# Remark: creates or updates a program value.
UPLOAD_DIR = DATA_DIR / "uploads"

# Remark: creates or updates a program value.
DATABASE_PATH = DATA_DIR / "secure_chat.db"
# Remark: creates or updates a program value.
LOG_PATH = DATA_DIR / "server.log"
# Remark: creates or updates a program value.
CERT_PATH = CERT_DIR / "server.crt"
# Remark: creates or updates a program value.
KEY_PATH = CERT_DIR / "server.key"

# Remark: creates or updates a program value.
DEFAULT_HOST = "127.0.0.1"
# Remark: creates or updates a program value.
DEFAULT_PORT = 5050

# Media is sent as base64 inside JSON, so packets must be larger than plain text messages.
# Remark: creates or updates a program value.
MAX_PACKET_SIZE = 25 * 1024 * 1024
# Remark: creates or updates a program value.
MAX_FILE_SIZE = 15 * 1024 * 1024
# Remark: creates or updates a program value.
MAX_USERNAME_LENGTH = 20
# Remark: creates or updates a program value.
MAX_PASSWORD_LENGTH = 128
# Remark: creates or updates a program value.
MAX_ROOM_LENGTH = 30
# Remark: creates or updates a program value.
MAX_MESSAGE_LENGTH = 1000
# Remark: creates or updates a program value.
MAX_FILENAME_LENGTH = 120

# Remark: creates or updates a program value.
PBKDF2_ITERATIONS = 250_000

