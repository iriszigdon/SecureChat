# SecureChat

SecureChat is an encrypted multi-user chat system for a 5-unit cyber/networking bagrut project.

It includes:

- A threaded TCP socket server.
- Multiple clients connected at the same time.
- A custom length-prefixed JSON protocol.
- TLS encryption for all network traffic.
- User registration and login.
- Salted password hashing with PBKDF2.
- Chat rooms and message history.
- Emoji messages.
- File, image, and video sending.
- SQLite file-based storage.
- A Tkinter graphical client.
- Audit logs for important server events.

## Run

Use Python 3.10 or newer.

Install dependencies:

```powershell
pip install -r requirements.txt
```

Start the server:

```powershell
python -m secure_chat.server
```

Start a client in another terminal:

```powershell
python -m secure_chat.client_gui
```

Open more client windows to demonstrate a multi-client server.

The server automatically creates a local self-signed TLS certificate on first run. You can also create it manually:

```powershell
python tools/create_dev_certificate.py
```

## Demo Flow

1. Start the server.
2. Open two or more clients.
3. Register different users.
4. Login from each client.
5. Join the same room, for example `general`.
6. Send messages and show that they arrive in real time.
7. Use the emoji buttons to add emojis to messages.
8. Use **Send File**, **Send Image**, or **Send Video** to transfer media.
9. Close one client and show that the server stays alive.
10. Restart a client and show that message history is loaded from SQLite.

Received media files are saved automatically in the `downloads` folder.
The server also saves uploaded media in `data/uploads`.

## Security Notes

This project is defensive. It does not implement attacks.

Implemented protections:

- TLS encrypts traffic between client and server.
- Passwords are never stored as plain text.
- Password hashes use PBKDF2 with a random salt.
- The protocol rejects oversized packets.
- File names are sanitized before saving.
- File size is limited before transfer.
- Usernames, room names, and message lengths are validated.
- SQLite queries use parameters to avoid SQL injection.
- Each client runs in its own thread, so one client cannot block all others.
- Client disconnects are handled with exceptions so the server does not crash.

For a real production system, use a certificate from a trusted certificate authority and enable certificate verification on the client.

