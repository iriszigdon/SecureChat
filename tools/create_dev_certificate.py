# Remark: imports a module or object needed by this file.
from pathlib import Path
# Remark: imports a module or object needed by this file.
from datetime import datetime, timedelta, timezone

# Remark: imports a module or object needed by this file.
from cryptography import x509
# Remark: imports a module or object needed by this file.
from cryptography.hazmat.primitives import hashes, serialization
# Remark: imports a module or object needed by this file.
from cryptography.hazmat.primitives.asymmetric import rsa
# Remark: imports a module or object needed by this file.
from cryptography.x509.oid import NameOID


# Remark: creates or updates a program value.
ROOT = Path(__file__).resolve().parent.parent
# Remark: creates or updates a program value.
CERT_DIR = ROOT / "certs"
# Remark: creates or updates a program value.
CERT_PATH = CERT_DIR / "server.crt"
# Remark: creates or updates a program value.
KEY_PATH = CERT_DIR / "server.key"


# Remark: defines a function or method.
def main() -> None:
    # Remark: creates or updates a program value.
    CERT_DIR.mkdir(parents=True, exist_ok=True)

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

    # Remark: runs this instruction as part of the program logic.
    print(f"Created {CERT_PATH}")
    # Remark: runs this instruction as part of the program logic.
    print(f"Created {KEY_PATH}")


# Remark: checks a condition before continuing.
if __name__ == "__main__":
    # Remark: runs this instruction as part of the program logic.
    main()

