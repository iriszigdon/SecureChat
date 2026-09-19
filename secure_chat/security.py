# Remark: imports a module or object needed by this file.
import hmac
# Remark: imports a module or object needed by this file.
import os
# Remark: imports a module or object needed by this file.
import re
# Remark: imports a module or object needed by this file.
import ssl
# Remark: imports a module or object needed by this file.
from datetime import datetime, timedelta, timezone
# Remark: imports a module or object needed by this file.
from hashlib import pbkdf2_hmac

# Remark: imports a module or object needed by this file.
from secure_chat.config import (
    # Remark: runs this instruction as part of the program logic.
    CERT_DIR,
    # Remark: runs this instruction as part of the program logic.
    CERT_PATH,
    # Remark: runs this instruction as part of the program logic.
    KEY_PATH,
    # Remark: runs this instruction as part of the program logic.
    MAX_MESSAGE_LENGTH,
    # Remark: runs this instruction as part of the program logic.
    MAX_PASSWORD_LENGTH,
    # Remark: runs this instruction as part of the program logic.
    MAX_ROOM_LENGTH,
    # Remark: runs this instruction as part of the program logic.
    MAX_USERNAME_LENGTH,
    # Remark: runs this instruction as part of the program logic.
    MAX_FILENAME_LENGTH,
    # Remark: runs this instruction as part of the program logic.
    PBKDF2_ITERATIONS,
# Remark: closes a multi-line expression.
)


# Remark: defines a class for object-oriented structure.
class ValidationError(ValueError):
    # Remark: runs this instruction as part of the program logic.
    """Raised when user-controlled input is not allowed."""


# Remark: defines a class for object-oriented structure.
class PasswordHasher:
    # Remark: applies a decorator to the next function or method.
    @staticmethod
    # Remark: defines a function or method.
    def hash_password(password: str) -> str:
        # Remark: creates or updates a program value.
        salt = os.urandom(16)
        # Remark: starts a multi-line expression.
        digest = pbkdf2_hmac(
            # Remark: runs this instruction as part of the program logic.
            "sha256",
            # Remark: runs this instruction as part of the program logic.
            password.encode("utf-8"),
            # Remark: runs this instruction as part of the program logic.
            salt,
            # Remark: runs this instruction as part of the program logic.
            PBKDF2_ITERATIONS,
        # Remark: closes a multi-line expression.
        )
        # Remark: returns a value to the caller.
        return f"{PBKDF2_ITERATIONS}${salt.hex()}${digest.hex()}"

    # Remark: applies a decorator to the next function or method.
    @staticmethod
    # Remark: defines a function or method.
    def verify_password(password: str, stored_hash: str) -> bool:
        # Remark: starts protected code that may raise an error.
        try:
            # Remark: creates or updates a program value.
            iterations_text, salt_hex, digest_hex = stored_hash.split("$")
            # Remark: creates or updates a program value.
            iterations = int(iterations_text)
            # Remark: creates or updates a program value.
            salt = bytes.fromhex(salt_hex)
            # Remark: creates or updates a program value.
            expected_digest = bytes.fromhex(digest_hex)
        # Remark: handles an expected error safely.
        except (ValueError, TypeError):
            # Remark: returns a value to the caller.
            return False

        # Remark: starts a multi-line expression.
        actual_digest = pbkdf2_hmac(
            # Remark: runs this instruction as part of the program logic.
            "sha256",
            # Remark: runs this instruction as part of the program logic.
            password.encode("utf-8"),
            # Remark: runs this instruction as part of the program logic.
            salt,
            # Remark: runs this instruction as part of the program logic.
            iterations,
        # Remark: closes a multi-line expression.
        )
        # Remark: returns a value to the caller.
        return hmac.compare_digest(actual_digest, expected_digest)


# Remark: defines a class for object-oriented structure.
class InputValidator:
    # Remark: creates or updates a program value.
    USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_]{3,20}$")
    # Remark: creates or updates a program value.
    ROOM_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,30}$")

    # Remark: applies a decorator to the next function or method.
    @classmethod
    # Remark: defines a function or method.
    def username(cls, value: str) -> str:
        # Remark: creates or updates a program value.
        value = value.strip()
        # Remark: checks a condition before continuing.
        if len(value) > MAX_USERNAME_LENGTH or not cls.USERNAME_PATTERN.fullmatch(value):
            # Remark: raises an error for invalid behavior.
            raise ValidationError("Username must be 3-20 letters, numbers, or underscores")
        # Remark: returns a value to the caller.
        return value

    # Remark: applies a decorator to the next function or method.
    @classmethod
    # Remark: defines a function or method.
    def password(cls, value: str) -> str:
        # Remark: checks a condition before continuing.
        if not 6 <= len(value) <= MAX_PASSWORD_LENGTH:
            # Remark: raises an error for invalid behavior.
            raise ValidationError("Password must be 6-128 characters")
        # Remark: returns a value to the caller.
        return value

    # Remark: applies a decorator to the next function or method.
    @classmethod
    # Remark: defines a function or method.
    def room(cls, value: str) -> str:
        # Remark: creates or updates a program value.
        value = value.strip() or "general"
        # Remark: checks a condition before continuing.
        if len(value) > MAX_ROOM_LENGTH or not cls.ROOM_PATTERN.fullmatch(value):
            # Remark: raises an error for invalid behavior.
            raise ValidationError("Room must contain only letters, numbers, _ or -")
        # Remark: returns a value to the caller.
        return value

    # Remark: applies a decorator to the next function or method.
    @classmethod
    # Remark: defines a function or method.
    def message(cls, value: str) -> str:
        # Remark: creates or updates a program value.
        value = value.strip()
        # Remark: checks a condition before continuing.
        if not value:
            # Remark: raises an error for invalid behavior.
            raise ValidationError("Message cannot be empty")
        # Remark: checks a condition before continuing.
        if len(value) > MAX_MESSAGE_LENGTH:
            # Remark: raises an error for invalid behavior.
            raise ValidationError(f"Message cannot be longer than {MAX_MESSAGE_LENGTH} characters")
        # Remark: returns a value to the caller.
        return value

    # Remark: applies a decorator to the next function or method.
    @classmethod
    # Remark: defines a function or method.
    def filename(cls, value: str) -> str:
        # Remark: places a widget in the graphical interface.
        value = value.strip().replace("\\", "_").replace("/", "_")
        # Remark: checks a condition before continuing.
        if not value or value in {".", ".."}:
            # Remark: raises an error for invalid behavior.
            raise ValidationError("Filename is not valid")
        # Remark: checks a condition before continuing.
        if len(value) > MAX_FILENAME_LENGTH:
            # Remark: raises an error for invalid behavior.
            raise ValidationError(f"Filename cannot be longer than {MAX_FILENAME_LENGTH} characters")
        # Remark: returns a value to the caller.
        return value


# Remark: defines a class for object-oriented structure.
class TLSContextFactory:
    # Remark: applies a decorator to the next function or method.
    @staticmethod
    # Remark: defines a function or method.
    def server_context() -> ssl.SSLContext:
        # Remark: runs this instruction as part of the program logic.
        TLSContextFactory.ensure_development_certificate()
        # Remark: creates or updates a program value.
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        # Remark: creates or updates a program value.
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        # Remark: creates or updates a program value.
        context.load_cert_chain(certfile=CERT_PATH, keyfile=KEY_PATH)
        # Remark: returns a value to the caller.
        return context

    # Remark: applies a decorator to the next function or method.
    @staticmethod
    # Remark: defines a function or method.
    def client_context(verify_certificate: bool = False) -> ssl.SSLContext:
        # Remark: checks a condition before continuing.
        if verify_certificate:
            # Remark: creates or updates a program value.
            context = ssl.create_default_context(cafile=str(CERT_PATH))
            # Remark: creates or updates a program value.
            context.check_hostname = False
            # Remark: returns a value to the caller.
            return context

        # Local classroom/demo mode: traffic is encrypted, but the self-signed
        # certificate is not authenticated by a public certificate authority.
        # Remark: creates or updates a program value.
        context = ssl._create_unverified_context()
        # Remark: creates or updates a program value.
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        # Remark: returns a value to the caller.
        return context

    # Remark: applies a decorator to the next function or method.
    @staticmethod
    # Remark: defines a function or method.
    def ensure_development_certificate() -> None:
        # Remark: checks a condition before continuing.
        if (
            # Remark: runs this instruction as part of the program logic.
            CERT_PATH.exists()
            # Remark: runs this instruction as part of the program logic.
            and CERT_PATH.stat().st_size > 0
            # Remark: runs this instruction as part of the program logic.
            and KEY_PATH.exists()
            # Remark: runs this instruction as part of the program logic.
            and KEY_PATH.stat().st_size > 0
        # Remark: closes a multi-line expression.
        ):
            # Remark: returns a value to the caller.
            return

        # Remark: creates or updates a program value.
        CERT_DIR.mkdir(parents=True, exist_ok=True)
        # Remark: starts protected code that may raise an error.
        try:
            # Remark: imports a module or object needed by this file.
            from cryptography import x509
            # Remark: imports a module or object needed by this file.
            from cryptography.hazmat.primitives import hashes, serialization
            # Remark: imports a module or object needed by this file.
            from cryptography.hazmat.primitives.asymmetric import rsa
            # Remark: imports a module or object needed by this file.
            from cryptography.x509.oid import NameOID
        # Remark: handles an expected error safely.
        except ImportError as exc:
            # Remark: raises an error for invalid behavior.
            raise RuntimeError(
                # Remark: runs this instruction as part of the program logic.
                "Missing TLS certificate. Install dependencies with: pip install -r requirements.txt"
            # Remark: closes a multi-line expression.
            ) from exc

        # Remark: creates or updates a program value.
        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        # Remark: starts a multi-line expression.
        subject = issuer = x509.Name(
            # Remark: runs this instruction as part of the program logic.
            [x509.NameAttribute(NameOID.COMMON_NAME, "SecureChatLocal")]
        # Remark: closes a multi-line expression.
        )
        # Remark: starts a multi-line expression.
        certificate = (
            # Remark: runs this instruction as part of the program logic.
            x509.CertificateBuilder()
            # Remark: runs this instruction as part of the program logic.
            .subject_name(subject)
            # Remark: runs this instruction as part of the program logic.
            .issuer_name(issuer)
            # Remark: runs this instruction as part of the program logic.
            .public_key(private_key.public_key())
            # Remark: runs this instruction as part of the program logic.
            .serial_number(x509.random_serial_number())
            # Remark: creates or updates a program value.
            .not_valid_before(datetime.now(timezone.utc) - timedelta(days=1))
            # Remark: creates or updates a program value.
            .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))
            # Remark: runs this instruction as part of the program logic.
            .sign(private_key, hashes.SHA256())
        # Remark: closes a multi-line expression.
        )

        # Remark: starts a multi-line expression.
        KEY_PATH.write_bytes(
            # Remark: starts a multi-line expression.
            private_key.private_bytes(
                # Remark: creates or updates a program value.
                encoding=serialization.Encoding.PEM,
                # Remark: creates or updates a program value.
                format=serialization.PrivateFormat.PKCS8,
                # Remark: creates or updates a program value.
                encryption_algorithm=serialization.NoEncryption(),
            # Remark: closes a multi-line expression.
            )
        # Remark: closes a multi-line expression.
        )
        # Remark: runs this instruction as part of the program logic.
        CERT_PATH.write_bytes(certificate.public_bytes(serialization.Encoding.PEM))

