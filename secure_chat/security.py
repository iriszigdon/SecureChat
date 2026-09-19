import hmac
import os
import re
import ssl
from datetime import datetime, timedelta, timezone
from hashlib import pbkdf2_hmac

from secure_chat.config import (
    CERT_DIR,
    CERT_PATH,
    KEY_PATH,
    MAX_MESSAGE_LENGTH,
    MAX_PASSWORD_LENGTH,
    MAX_ROOM_LENGTH,
    MAX_USERNAME_LENGTH,
    MAX_FILENAME_LENGTH,
    PBKDF2_ITERATIONS,
)


class ValidationError(ValueError):
    """Raised when user-controlled input is not allowed."""


class PasswordHasher:
    @staticmethod
    def hash_password(password: str) -> str:
        salt = os.urandom(16)
        digest = pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            PBKDF2_ITERATIONS,
        )
        return f"{PBKDF2_ITERATIONS}${salt.hex()}${digest.hex()}"

    @staticmethod
    def verify_password(password: str, stored_hash: str) -> bool:
        try:
            iterations_text, salt_hex, digest_hex = stored_hash.split("$")
            iterations = int(iterations_text)
            salt = bytes.fromhex(salt_hex)
            expected_digest = bytes.fromhex(digest_hex)
        except (ValueError, TypeError):
            return False

        actual_digest = pbkdf2_hmac(
            "sha256",
            password.encode("utf-8"),
            salt,
            iterations,
        )
        return hmac.compare_digest(actual_digest, expected_digest)


class InputValidator:
    USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_]{3,20}$")
    ROOM_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,30}$")

    @classmethod
    def username(cls, value: str) -> str:
        value = value.strip()
        if len(value) > MAX_USERNAME_LENGTH or not cls.USERNAME_PATTERN.fullmatch(value):
            raise ValidationError("Username must be 3-20 letters, numbers, or underscores")
        return value

    @classmethod
    def password(cls, value: str) -> str:
        if not 6 <= len(value) <= MAX_PASSWORD_LENGTH:
            raise ValidationError("Password must be 6-128 characters")
        return value

    @classmethod
    def room(cls, value: str) -> str:
        value = value.strip() or "general"
        if len(value) > MAX_ROOM_LENGTH or not cls.ROOM_PATTERN.fullmatch(value):
            raise ValidationError("Room must contain only letters, numbers, _ or -")
        return value

    @classmethod
    def message(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValidationError("Message cannot be empty")
        if len(value) > MAX_MESSAGE_LENGTH:
            raise ValidationError(f"Message cannot be longer than {MAX_MESSAGE_LENGTH} characters")
        return value

    @classmethod
    def filename(cls, value: str) -> str:
        value = value.strip().replace("\\", "_").replace("/", "_")
        if not value or value in {".", ".."}:
            raise ValidationError("Filename is not valid")
        if len(value) > MAX_FILENAME_LENGTH:
            raise ValidationError(f"Filename cannot be longer than {MAX_FILENAME_LENGTH} characters")
        return value


class TLSContextFactory:
    @staticmethod
    def server_context() -> ssl.SSLContext:
        TLSContextFactory.ensure_development_certificate()
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        context.load_cert_chain(certfile=CERT_PATH, keyfile=KEY_PATH)
        return context

    @staticmethod
    def client_context(verify_certificate: bool = False) -> ssl.SSLContext:
        if verify_certificate:
            context = ssl.create_default_context(cafile=str(CERT_PATH))
            context.check_hostname = False
            return context

        # Local classroom/demo mode: traffic is encrypted, but the self-signed
        # certificate is not authenticated by a public certificate authority.
        context = ssl._create_unverified_context()
        context.minimum_version = ssl.TLSVersion.TLSv1_2
        return context

    @staticmethod
    def ensure_development_certificate() -> None:
        if (
            CERT_PATH.exists()
            and CERT_PATH.stat().st_size > 0
            and KEY_PATH.exists()
            and KEY_PATH.stat().st_size > 0
        ):
            return

        CERT_DIR.mkdir(parents=True, exist_ok=True)
        try:
            from cryptography import x509
            from cryptography.hazmat.primitives import hashes, serialization
            from cryptography.hazmat.primitives.asymmetric import rsa
            from cryptography.x509.oid import NameOID
        except ImportError as exc:
            raise RuntimeError(
                "Missing TLS certificate. Install dependencies with: pip install -r requirements.txt"
            ) from exc

        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        subject = issuer = x509.Name(
            [x509.NameAttribute(NameOID.COMMON_NAME, "SecureChatLocal")]
        )
        certificate = (
            x509.CertificateBuilder()
            .subject_name(subject)
            .issuer_name(issuer)
            .public_key(private_key.public_key())
            .serial_number(x509.random_serial_number())
            .not_valid_before(datetime.now(timezone.utc) - timedelta(days=1))
            .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))
            .sign(private_key, hashes.SHA256())
        )

        KEY_PATH.write_bytes(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )
        CERT_PATH.write_bytes(certificate.public_bytes(serialization.Encoding.PEM))

