# SecureChat Requirement Mapping

This file maps the project to the 5-unit cyber/networking bagrut requirements in `cyberProject-5.pdf`.

## Mandatory Requirements

1. Object-oriented programming  
   The project contains multiple classes, including:
   - `ChatProtocol`
   - `PasswordHasher`
   - `InputValidator`
   - `TLSContextFactory`
   - `ChatDatabase`
   - `ClientHandler`
   - `SecureChatServer`
   - `ChatClientConnection`
   - `SecureChatApp`

2. Communication  
   The project uses TCP sockets.  
   The server supports multiple clients at the same time.  
   The custom protocol is a 4-byte length header followed by a JSON payload.

3. Operating system  
   The server uses threads for client handling.  
   The project uses the file system through SQLite database files, log files, and TLS certificate files.

4. Security  
   Network traffic is encrypted with TLS.  
   Passwords are stored as salted PBKDF2 hashes.  
   Input validation, maximum packet sizes, parameterized SQL, and exception handling reduce common vulnerabilities.

5. User interface  
   The client has an interactive Tkinter GUI with registration, login, room joining, message sending, chat history, and online user display.

## Suggested Architecture Diagram

```text
+------------------+        TLS TCP socket         +----------------------+
| Tkinter Client 1  | <---------------------------> |                      |
+------------------+                               |                      |
                                                   |  SecureChat Server   |
+------------------+        TLS TCP socket         |                      |
| Tkinter Client 2  | <---------------------------> |                      |
+------------------+                               +----------+-----------+
                                                              |
                                                              |
                                                       +------v------+
                                                       | SQLite DB   |
                                                       | Log file    |
                                                       +-------------+
```

## Protocol Examples

Register:

```json
{
  "type": "register",
  "username": "alice",
  "password": "secret123"
}
```

Login:

```json
{
  "type": "login",
  "username": "alice",
  "password": "secret123"
}
```

Chat message:

```json
{
  "type": "message",
  "body": "Hello everyone"
}
```

Server message:

```json
{
  "type": "message",
  "sender": "alice",
  "room": "general",
  "body": "Hello everyone",
  "created_at": "2026-09-20T10:00:00Z"
}
```

## Central Algorithms To Explain

- Length-prefixed packet sending and receiving.
- Thread-per-client server model.
- Broadcast to all clients in the same room.
- Password hashing and verification.
- Message history storage and retrieval.
- Validation before processing user input.

## Weaknesses and Mitigations

- Man-in-the-middle risk: traffic is encrypted with TLS. For production, verify a trusted certificate.
- SQL injection: all database commands use SQL parameters.
- Server crash from malformed packets: invalid packets raise controlled exceptions and disconnect only that client.
- Oversized packet attack: packets are limited by `MAX_PACKET_SIZE`.
- Weak password storage: passwords are stored as salted PBKDF2 hashes, not plain text.
- Client disconnect: handled with `try/except` so other clients continue working.

