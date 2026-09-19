import argparse
import base64
import mimetypes
import queue
import socket
import ssl
import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, scrolledtext, ttk

from secure_chat.config import DEFAULT_HOST, DEFAULT_PORT, DOWNLOAD_DIR, MAX_FILE_SIZE
from secure_chat.protocol import ChatProtocol, ProtocolError
from secure_chat.security import InputValidator, TLSContextFactory, ValidationError


class ChatClientConnection:
    def __init__(self, host: str, port: int, verify_certificate: bool = False) -> None:
        self.host = host
        self.port = port
        self.verify_certificate = verify_certificate
        self.socket: ssl.SSLSocket | None = None
        self.incoming: "queue.Queue[dict[str, object]]" = queue.Queue()
        self.running = False

    def connect(self) -> None:
        raw_socket = socket.create_connection((self.host, self.port), timeout=10)
        context = TLSContextFactory.client_context(self.verify_certificate)
        self.socket = context.wrap_socket(raw_socket, server_hostname=self.host)
        self.socket.settimeout(None)
        self.running = True
        threading.Thread(target=self._listen, daemon=True).start()

    def send(self, packet_type: str, **fields: object) -> None:
        if self.socket is None:
            raise ConnectionError("Not connected")
        ChatProtocol.send(self.socket, packet_type, **fields)

    def close(self) -> None:
        self.running = False
        if self.socket is not None:
            try:
                self.send("logout")
                self.socket.close()
            except OSError:
                pass

    def _listen(self) -> None:
        assert self.socket is not None
        while self.running:
            try:
                packet = ChatProtocol.receive(self.socket)
                self.incoming.put(packet)
            except (ConnectionError, OSError, ProtocolError) as exc:
                self.incoming.put({"type": "connection_closed", "message": str(exc)})
                self.running = False


class SecureChatApp(tk.Tk):
    def __init__(self, connection: ChatClientConnection) -> None:
        super().__init__()
        self.connection = connection
        self.title("SecureChat - Encrypted Multi-User Chat")
        self.geometry("980x640")
        self.minsize(900, 580)
        self.resizable(True, True)
        self.configure(bg="#111827")
        self.logged_in = False
        self.current_room = "general"
        self.current_screen = "auth"

        self._build_ui()
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        self.after(100, self._poll_incoming)

    def _build_ui(self) -> None:
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()
        self.room_var = tk.StringVar(value="general")
        self.new_room_var = tk.StringVar()
        self.message_var = tk.StringVar()
        self.auth_status_var = tk.StringVar(value="Connected. Register or login to continue.")
        self.chat_status_var = tk.StringVar(value="")
        self.login_badge_var = tk.StringVar(value="")

        self._build_auth_screen()
        self._build_chat_screen()
        self._show_auth_screen()

    def _build_auth_screen(self) -> None:
        self.auth_frame = tk.Frame(self, bg="#111827")

        card = tk.Frame(self.auth_frame, bg="#f8fafc", padx=34, pady=30)
        card.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        tk.Label(
            card,
            text="SecureChat",
            bg="#f8fafc",
            fg="#2563eb",
            font=("Segoe UI", 30, "bold"),
        ).grid(row=0, column=0, columnspan=2, pady=(0, 6))
        tk.Label(
            card,
            text="Encrypted multi-user chat",
            bg="#f8fafc",
            fg="#475569",
            font=("Segoe UI", 12),
        ).grid(row=1, column=0, columnspan=2, pady=(0, 24))

        tk.Label(card, text="Username", bg="#f8fafc", fg="#0f172a", font=("Segoe UI", 11, "bold")).grid(
            row=2, column=0, sticky="w"
        )
        tk.Entry(
            card,
            textvariable=self.username_var,
            width=30,
            font=("Segoe UI", 12),
            bg="#e0f2fe",
            fg="#0f172a",
            relief=tk.FLAT,
        ).grid(row=3, column=0, columnspan=2, sticky="ew", pady=(4, 14), ipady=8)

        tk.Label(card, text="Password", bg="#f8fafc", fg="#0f172a", font=("Segoe UI", 11, "bold")).grid(
            row=4, column=0, sticky="w"
        )
        password_entry = tk.Entry(
            card,
            textvariable=self.password_var,
            show="*",
            width=30,
            font=("Segoe UI", 12),
            bg="#fef3c7",
            fg="#0f172a",
            relief=tk.FLAT,
        )
        password_entry.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(4, 18), ipady=8)
        password_entry.bind("<Return>", lambda _event: self._login())

        tk.Button(
            card,
            text="Register",
            command=self._register_user,
            bg="#22c55e",
            fg="white",
            activebackground="#16a34a",
            font=("Segoe UI", 11, "bold"),
            relief=tk.FLAT,
            padx=16,
            pady=8,
        ).grid(row=6, column=0, sticky="ew", padx=(0, 8))
        tk.Button(
            card,
            text="Login",
            command=self._login,
            bg="#3b82f6",
            fg="white",
            activebackground="#2563eb",
            font=("Segoe UI", 11, "bold"),
            relief=tk.FLAT,
            padx=16,
            pady=8,
        ).grid(row=6, column=1, sticky="ew", padx=(8, 0))

        self.auth_status_label = tk.Label(
            card,
            textvariable=self.auth_status_var,
            bg="#dbeafe",
            fg="#2563eb",
            wraplength=360,
            font=("Segoe UI", 12, "bold"),
            padx=10,
            pady=8,
        )
        self.auth_status_label.grid(row=7, column=0, columnspan=2, pady=(18, 0))

    def _build_chat_screen(self) -> None:
        self.chat_frame = tk.Frame(self, bg="#dbeafe")
        self.chat_frame.columnconfigure(1, weight=1)
        self.chat_frame.rowconfigure(1, weight=1)

        header = tk.Frame(self.chat_frame, bg="#1d4ed8", padx=14, pady=12)
        header.grid(row=0, column=0, columnspan=3, sticky="ew")
        header.columnconfigure(1, weight=1)

        tk.Label(
            header,
            text="SecureChat",
            bg="#1d4ed8",
            fg="white",
            font=("Segoe UI", 20, "bold"),
        ).grid(row=0, column=0, sticky="w")
        tk.Label(
            header,
            textvariable=self.login_badge_var,
            bg="#1d4ed8",
            fg="#bbf7d0",
            font=("Segoe UI", 12, "bold"),
        ).grid(row=0, column=1, sticky="e")

        rooms_panel = tk.Frame(self.chat_frame, bg="#eff6ff", padx=10, pady=10)
        rooms_panel.grid(row=1, column=0, sticky="nsw", padx=(10, 5), pady=10)
        rooms_panel.rowconfigure(1, weight=1)

        tk.Label(rooms_panel, text="Rooms", bg="#eff6ff", fg="#1e3a8a", font=("Segoe UI", 14, "bold")).grid(
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 8)
        )
        self.rooms_box = tk.Listbox(
            rooms_panel,
            width=22,
            height=18,
            bg="#ffffff",
            fg="#0f172a",
            selectbackground="#3b82f6",
            relief=tk.FLAT,
            font=("Segoe UI", 10),
        )
        self.rooms_box.grid(row=1, column=0, columnspan=2, sticky="nsew")
        self.rooms_box.bind("<<ListboxSelect>>", self._on_room_select)

        tk.Button(
            rooms_panel,
            text="Join Selected",
            command=self._join_room,
            bg="#8b5cf6",
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 10, "bold"),
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(8, 12))

        tk.Entry(
            rooms_panel,
            textvariable=self.new_room_var,
            bg="#fef3c7",
            relief=tk.FLAT,
            font=("Segoe UI", 10),
        ).grid(row=3, column=0, columnspan=2, sticky="ew", ipady=6)
        tk.Button(
            rooms_panel,
            text="Create Room",
            command=self._create_room,
            bg="#f97316",
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 10, "bold"),
        ).grid(row=4, column=0, columnspan=2, sticky="ew", pady=(8, 8))
        tk.Button(
            rooms_panel,
            text="Refresh Rooms",
            command=self._request_rooms,
            bg="#06b6d4",
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 10, "bold"),
        ).grid(row=5, column=0, columnspan=2, sticky="ew")

        chat_panel = tk.Frame(self.chat_frame, bg="#dbeafe", padx=5, pady=10)
        chat_panel.grid(row=1, column=1, sticky="nsew", pady=10)
        chat_panel.rowconfigure(1, weight=1)
        chat_panel.columnconfigure(0, weight=1)

        self.room_title_var = tk.StringVar(value="Room: general")
        tk.Label(
            chat_panel,
            textvariable=self.room_title_var,
            bg="#dbeafe",
            fg="#1e3a8a",
            font=("Segoe UI", 14, "bold"),
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        self.chat_box = scrolledtext.ScrolledText(
            chat_panel,
            state=tk.DISABLED,
            wrap=tk.WORD,
            bg="#ffffff",
            fg="#0f172a",
            insertbackground="#0f172a",
            relief=tk.FLAT,
            font=("Consolas", 10),
        )
        self.chat_box.grid(row=1, column=0, sticky="nsew")

        send_frame = tk.Frame(chat_panel, bg="#dbeafe")
        send_frame.grid(row=2, column=0, sticky="ew", pady=(10, 0))
        send_frame.columnconfigure(0, weight=1)
        message_entry = tk.Entry(send_frame, textvariable=self.message_var, bg="#ffffff", relief=tk.FLAT, font=("Segoe UI", 11))
        message_entry.grid(row=0, column=0, sticky="ew", ipady=8, padx=(0, 8))
        message_entry.bind("<Return>", lambda _event: self._send_message())
        tk.Button(
            send_frame,
            text="Send",
            command=self._send_message,
            bg="#22c55e",
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 11, "bold"),
            padx=20,
        ).grid(row=0, column=1)

        media_frame = tk.Frame(chat_panel, bg="#dbeafe")
        media_frame.grid(row=3, column=0, sticky="ew", pady=(8, 0))
        for emoji in ["😀", "😂", "❤️", "👍", "🔥", "🎉"]:
            tk.Button(
                media_frame,
                text=emoji,
                command=lambda value=emoji: self._insert_emoji(value),
                bg="#fef3c7",
                relief=tk.FLAT,
                font=("Segoe UI Emoji", 12),
                width=3,
            ).pack(side=tk.LEFT, padx=(0, 5))

        tk.Button(
            media_frame,
            text="Send File",
            command=lambda: self._send_file("file"),
            bg="#64748b",
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 10, "bold"),
            padx=10,
        ).pack(side=tk.LEFT, padx=(12, 5))
        tk.Button(
            media_frame,
            text="Send Image",
            command=lambda: self._send_file("image"),
            bg="#ec4899",
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 10, "bold"),
            padx=10,
        ).pack(side=tk.LEFT, padx=5)
        tk.Button(
            media_frame,
            text="Send Video",
            command=lambda: self._send_file("video"),
            bg="#7c3aed",
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 10, "bold"),
            padx=10,
        ).pack(side=tk.LEFT, padx=5)

        users_panel = tk.Frame(self.chat_frame, bg="#ecfdf5", padx=10, pady=10)
        users_panel.grid(row=1, column=2, sticky="nse", padx=(5, 10), pady=10)
        users_panel.rowconfigure(1, weight=1)
        tk.Label(users_panel, text="Online Users", bg="#ecfdf5", fg="#166534", font=("Segoe UI", 14, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 8)
        )
        self.users_box = tk.Listbox(
            users_panel,
            width=24,
            height=18,
            bg="#ffffff",
            fg="#0f172a",
            selectbackground="#22c55e",
            relief=tk.FLAT,
            font=("Segoe UI", 10),
        )
        self.users_box.grid(row=1, column=0, sticky="nsew")
        tk.Button(
            users_panel,
            text="Refresh Users",
            command=self._request_users,
            bg="#16a34a",
            fg="white",
            relief=tk.FLAT,
            font=("Segoe UI", 10, "bold"),
        ).grid(row=2, column=0, sticky="ew", pady=(8, 0))

        self.chat_status_label = tk.Label(
            self.chat_frame,
            textvariable=self.chat_status_var,
            bg="#dbeafe",
            fg="#1d4ed8",
            font=("Segoe UI", 10, "bold"),
        )
        self.chat_status_label.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=(0, 8))

    def _show_auth_screen(self) -> None:
        self.current_screen = "auth"
        self.chat_frame.pack_forget()
        self.auth_frame.pack(fill=tk.BOTH, expand=True)

    def _show_chat_screen(self) -> None:
        self.current_screen = "chat"
        self.auth_frame.pack_forget()
        self.chat_frame.pack(fill=tk.BOTH, expand=True)

    def _register_user(self) -> None:
        self._send_auth_packet("register")

    def _login(self) -> None:
        self._send_auth_packet("login")

    def _send_auth_packet(self, packet_type: str) -> None:
        try:
            username = InputValidator.username(self.username_var.get())
            password = InputValidator.password(self.password_var.get())
            self.connection.send(
                packet_type,
                username=username,
                password=password,
            )
        except ValidationError as exc:
            self._set_auth_status(str(exc), ok=False)
            messagebox.showerror("Invalid details", str(exc))
        except Exception as exc:
            self._set_auth_status(f"Connection error: {exc}", ok=False)

    def _join_room(self) -> None:
        if not self.logged_in:
            self._set_chat_status("Please login first.", ok=False)
            return
        room = self.room_var.get().strip()
        if not room:
            self._set_chat_status("Choose a room first.", ok=False)
            return
        self.connection.send("join", room=room)

    def _create_room(self) -> None:
        if not self.logged_in:
            self._set_chat_status("Please login first.", ok=False)
            return
        room = self.new_room_var.get().strip()
        if not room:
            self._set_chat_status("Write a room name to create.", ok=False)
            return
        self.connection.send("create_room", room=room)

    def _request_users(self) -> None:
        if self.logged_in:
            self.connection.send("users")

    def _request_rooms(self) -> None:
        if self.logged_in:
            self.connection.send("rooms")

    def _send_message(self) -> None:
        if not self.logged_in:
            self._set_chat_status("Please login first.", ok=False)
            return

        body = self.message_var.get()
        if not body.strip():
            return

        try:
            self.connection.send("message", body=body)
            self.message_var.set("")
        except Exception as exc:
            self._set_chat_status(f"Send failed: {exc}", ok=False)

    def _insert_emoji(self, emoji: str) -> None:
        self.message_var.set(self.message_var.get() + emoji)

    def _send_file(self, kind: str) -> None:
        if not self.logged_in:
            self._set_chat_status("Please login first.", ok=False)
            return

        filters = {
            "file": [("All files", "*.*")],
            "image": [("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"), ("All files", "*.*")],
            "video": [("Video files", "*.mp4 *.mov *.avi *.mkv *.webm"), ("All files", "*.*")],
        }
        selected_path = filedialog.askopenfilename(filetypes=filters.get(kind, filters["file"]))
        if not selected_path:
            return

        path = Path(selected_path)
        if path.stat().st_size > MAX_FILE_SIZE:
            self._set_chat_status(
                f"File is too large. Maximum size is {MAX_FILE_SIZE // (1024 * 1024)} MB.",
                ok=False,
            )
            return

        try:
            filename = InputValidator.filename(path.name)
            encoded_data = base64.b64encode(path.read_bytes()).decode("ascii")
            mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            self.connection.send(
                "file",
                filename=filename,
                kind=kind,
                mime_type=mime_type,
                data=encoded_data,
            )
            self._set_chat_status(f"Sending {kind}: {filename}", ok=True)
        except Exception as exc:
            self._set_chat_status(f"Could not send {kind}: {exc}", ok=False)

    def _poll_incoming(self) -> None:
        while not self.connection.incoming.empty():
            packet = self.connection.incoming.get_nowait()
            self._handle_packet(packet)
        self.after(100, self._poll_incoming)

    def _handle_packet(self, packet: dict[str, object]) -> None:
        packet_type = packet.get("type")

        if packet_type == "welcome":
            self._set_auth_status(str(packet.get("message", "Connected")), ok=True)
        elif packet_type == "ok":
            self._handle_ok(packet)
        elif packet_type == "error":
            self._handle_error(packet)
        elif packet_type == "history":
            self._show_history(packet)
        elif packet_type == "message":
            self._append_chat(
                f"[{packet.get('created_at')}] {packet.get('sender')}: {packet.get('body')}"
            )
        elif packet_type == "file":
            self._handle_file_packet(packet)
        elif packet_type == "system":
            self._append_chat(f"* {packet.get('message')}")
        elif packet_type == "users":
            self._show_users(packet)
        elif packet_type == "rooms":
            self._show_rooms(packet)
        elif packet_type == "connection_closed":
            message = f"Disconnected: {packet.get('message')}"
            if self.current_screen == "auth":
                self._set_auth_status(message, ok=False)
            else:
                self._set_chat_status(message, ok=False)

    def _handle_ok(self, packet: dict[str, object]) -> None:
        action = packet.get("action")
        message = str(packet.get("message", "OK"))
        if action == "login":
            self.logged_in = True
            self.login_badge_var.set(f"Logged in as {self.username_var.get().strip()}")
            self._show_chat_screen()
            self._set_chat_status(message, ok=True)
            messagebox.showinfo("Login OK", message)
            self._request_rooms()
            self._request_users()
        elif action == "register":
            self._set_auth_status(f"{message}. Logging in...", ok=True)
            messagebox.showinfo("Register OK", f"{message}. You will be logged in now.")
            self.connection.send(
                "login",
                username=self.username_var.get(),
                password=self.password_var.get(),
            )
        elif action == "create_room":
            room = str(packet.get("room", "general"))
            self.new_room_var.set("")
            self.room_var.set(room)
            self._set_chat_status(message, ok=True)
            self.connection.send("join", room=room)
        elif action == "join":
            self.current_room = str(packet.get("room", "general"))
            self.room_var.set(self.current_room)
            self.room_title_var.set(f"Room: {self.current_room}")
            self._clear_chat()
            self._set_chat_status(message, ok=True)
            self._request_rooms()
            self._request_users()

    def _handle_error(self, packet: dict[str, object]) -> None:
        action = packet.get("action")
        message = str(packet.get("message", "Unknown error"))

        if action == "register" and "already exists" in message.lower():
            self._set_auth_status("Username already exists. Trying to login...", ok=True)
            self.connection.send(
                "login",
                username=self.username_var.get(),
                password=self.password_var.get(),
            )
            return

        if action in {"register", "login"} or self.current_screen == "auth":
            self._set_auth_status(message, ok=False)
            messagebox.showerror("Login/Register failed", message)
            return

        self._set_chat_status(message, ok=False)
        messagebox.showerror("Action failed", message)

    def _show_history(self, packet: dict[str, object]) -> None:
        room = packet.get("room", "general")
        self.current_room = str(room)
        self.room_var.set(self.current_room)
        self.room_title_var.set(f"Room: {self.current_room}")
        self.chat_box.configure(state=tk.NORMAL)
        self.chat_box.delete("1.0", tk.END)
        self.chat_box.insert(tk.END, f"--- History for room {self.current_room} ---\n")
        for message in packet.get("messages", []):
            if isinstance(message, dict):
                self.chat_box.insert(
                    tk.END,
                    f"[{message.get('created_at')}] {message.get('sender')}: {message.get('body')}\n",
                )
        self.chat_box.configure(state=tk.DISABLED)
        self.chat_box.see(tk.END)

    def _show_users(self, packet: dict[str, object]) -> None:
        self.users_box.delete(0, tk.END)
        online = packet.get("online", [])
        if isinstance(online, list):
            for user in online:
                if isinstance(user, dict):
                    self.users_box.insert(tk.END, f"{user.get('username')} @ {user.get('room')}")

    def _show_rooms(self, packet: dict[str, object]) -> None:
        rooms = packet.get("rooms", [])
        current = str(packet.get("current", self.current_room))
        self.rooms_box.delete(0, tk.END)

        if isinstance(rooms, list):
            for index, room in enumerate(rooms):
                room_name = str(room)
                self.rooms_box.insert(tk.END, room_name)
                if room_name == current:
                    self.rooms_box.selection_clear(0, tk.END)
                    self.rooms_box.selection_set(index)
                    self.rooms_box.see(index)
                    self.room_var.set(room_name)

    def _on_room_select(self, _event: tk.Event) -> None:
        selection = self.rooms_box.curselection()
        if selection:
            self.room_var.set(self.rooms_box.get(selection[0]))

    def _handle_file_packet(self, packet: dict[str, object]) -> None:
        try:
            filename = InputValidator.filename(str(packet.get("filename", "download.bin")))
            kind = str(packet.get("kind", "file"))
            sender = str(packet.get("sender", "unknown"))
            created_at = str(packet.get("created_at", ""))
            encoded_data = str(packet.get("data", ""))
            file_data = base64.b64decode(encoded_data.encode("ascii"), validate=True)
        except Exception as exc:
            self._set_chat_status(f"Received invalid file packet: {exc}", ok=False)
            return

        DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
        save_path = self._unique_download_path(filename)
        save_path.write_bytes(file_data)
        self._append_chat(
            f"[{created_at}] {sender} sent {kind}: {filename} "
            f"(saved to {save_path})"
        )

    def _unique_download_path(self, filename: str) -> Path:
        path = DOWNLOAD_DIR / filename
        if not path.exists():
            return path

        stem = path.stem
        suffix = path.suffix
        counter = 1
        while True:
            candidate = DOWNLOAD_DIR / f"{stem}_{counter}{suffix}"
            if not candidate.exists():
                return candidate
            counter += 1

    def _append_chat(self, text: str) -> None:
        self.chat_box.configure(state=tk.NORMAL)
        self.chat_box.insert(tk.END, text + "\n")
        self.chat_box.configure(state=tk.DISABLED)
        self.chat_box.see(tk.END)

    def _clear_chat(self) -> None:
        self.chat_box.configure(state=tk.NORMAL)
        self.chat_box.delete("1.0", tk.END)
        self.chat_box.configure(state=tk.DISABLED)

    def _set_auth_status(self, message: str, ok: bool) -> None:
        self.auth_status_var.set(message)
        self.auth_status_label.configure(
            bg="#dcfce7" if ok else "#fee2e2",
            fg="#166534" if ok else "#991b1b",
        )

    def _set_chat_status(self, message: str, ok: bool) -> None:
        self.chat_status_var.set(message)
        self.chat_status_label.configure(fg="#16a34a" if ok else "#dc2626")

    def _on_close(self) -> None:
        self.connection.close()
        self.destroy()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="SecureChat Tkinter client")
    parser.add_argument("--host", default=DEFAULT_HOST)
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    parser.add_argument("--verify-cert", action="store_true")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    client_connection = ChatClientConnection(
        host=args.host,
        port=args.port,
        verify_certificate=args.verify_cert,
    )
    client_connection.connect()
    app = SecureChatApp(client_connection)
    app.mainloop()

