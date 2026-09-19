# Remark: imports a module or object needed by this file.
import argparse
# Remark: imports a module or object needed by this file.
import base64
# Remark: imports a module or object needed by this file.
import mimetypes
# Remark: imports a module or object needed by this file.
import os
# Remark: imports a module or object needed by this file.
import queue
# Remark: imports a module or object needed by this file.
import socket
# Remark: imports a module or object needed by this file.
import ssl
# Remark: imports a module or object needed by this file.
import subprocess
# Remark: imports a module or object needed by this file.
import sys
# Remark: imports a module or object needed by this file.
import threading
# Remark: imports a module or object needed by this file.
import tkinter as tk
# Remark: imports a module or object needed by this file.
from pathlib import Path
# Remark: imports a module or object needed by this file.
from tkinter import filedialog, messagebox, scrolledtext, ttk

# Remark: imports a module or object needed by this file.
from PIL import Image, ImageTk

# Remark: imports a module or object needed by this file.
from secure_chat.config import DEFAULT_HOST, DEFAULT_PORT, DOWNLOAD_DIR, MAX_FILE_SIZE
# Remark: imports a module or object needed by this file.
from secure_chat.protocol import ChatProtocol, ProtocolError
# Remark: imports a module or object needed by this file.
from secure_chat.security import InputValidator, TLSContextFactory, ValidationError


# Remark: defines a class for object-oriented structure.
class ChatClientConnection:
    # Remark: defines a function or method.
    def __init__(self, host: str, port: int, verify_certificate: bool = False) -> None:
        # Remark: creates or updates a program value.
        self.host = host
        # Remark: creates or updates a program value.
        self.port = port
        # Remark: creates or updates a program value.
        self.verify_certificate = verify_certificate
        # Remark: creates or updates a program value.
        self.socket: ssl.SSLSocket | None = None
        # Remark: creates or updates a program value.
        self.incoming: "queue.Queue[dict[str, object]]" = queue.Queue()
        # Remark: creates or updates a program value.
        self.running = False

    # Remark: defines a function or method.
    def connect(self) -> None:
        # Remark: creates or updates a program value.
        raw_socket = socket.create_connection((self.host, self.port), timeout=10)
        # Remark: creates or updates a program value.
        context = TLSContextFactory.client_context(self.verify_certificate)
        # Remark: creates or updates a program value.
        self.socket = context.wrap_socket(raw_socket, server_hostname=self.host)
        # Remark: runs this instruction as part of the program logic.
        self.socket.settimeout(None)
        # Remark: creates or updates a program value.
        self.running = True
        # Remark: creates or updates a program value.
        threading.Thread(target=self._listen, daemon=True).start()

    # Remark: defines a function or method.
    def send(self, packet_type: str, **fields: object) -> None:
        # Remark: checks a condition before continuing.
        if self.socket is None:
            # Remark: raises an error for invalid behavior.
            raise ConnectionError("Not connected")
        # Remark: sends data or connects a GUI action.
        ChatProtocol.send(self.socket, packet_type, **fields)

    # Remark: defines a function or method.
    def close(self) -> None:
        # Remark: creates or updates a program value.
        self.running = False
        # Remark: checks a condition before continuing.
        if self.socket is not None:
            # Remark: starts protected code that may raise an error.
            try:
                # Remark: sends data or connects a GUI action.
                self.send("logout")
                # Remark: runs this instruction as part of the program logic.
                self.socket.close()
            # Remark: handles an expected error safely.
            except OSError:
                # Remark: runs this instruction as part of the program logic.
                pass

    # Remark: defines a function or method.
    def _listen(self) -> None:
        # Remark: checks an assumption that should be true.
        assert self.socket is not None
        # Remark: starts a loop that continues while a condition is true.
        while self.running:
            # Remark: starts protected code that may raise an error.
            try:
                # Remark: receives data from the network.
                packet = ChatProtocol.receive(self.socket)
                # Remark: runs this instruction as part of the program logic.
                self.incoming.put(packet)
            # Remark: handles an expected error safely.
            except (ConnectionError, OSError, ProtocolError) as exc:
                # Remark: runs this instruction as part of the program logic.
                self.incoming.put({"type": "connection_closed", "message": str(exc)})
                # Remark: creates or updates a program value.
                self.running = False


# Remark: defines a class for object-oriented structure.
class SecureChatApp(tk.Tk):
    # Remark: defines a function or method.
    def __init__(self, connection: ChatClientConnection) -> None:
        # Remark: runs this instruction as part of the program logic.
        super().__init__()
        # Remark: creates or updates a program value.
        self.connection = connection
        # Remark: runs this instruction as part of the program logic.
        self.title("SecureChat - Encrypted Multi-User Chat")
        # Remark: runs this instruction as part of the program logic.
        self.geometry("980x640")
        # Remark: runs this instruction as part of the program logic.
        self.minsize(900, 580)
        # Remark: runs this instruction as part of the program logic.
        self.resizable(True, True)
        # Remark: creates or updates a program value.
        self.configure(bg="#111827")
        # Remark: creates or updates a program value.
        self.logged_in = False
        # Remark: creates or updates a program value.
        self.current_room = "general"
        # Remark: creates or updates a program value.
        self.current_screen = "auth"
        # Remark: creates or updates a program value.
        self.chat_images: list[ImageTk.PhotoImage] = []
        # Remark: creates or updates a program value.
        self.chat_links: dict[str, Path] = {}

        # Remark: runs this instruction as part of the program logic.
        self._build_ui()
        # Remark: runs this instruction as part of the program logic.
        self.protocol("WM_DELETE_WINDOW", self._on_close)
        # Remark: runs this instruction as part of the program logic.
        self.after(100, self._poll_incoming)

    # Remark: defines a function or method.
    def _build_ui(self) -> None:
        # Remark: creates or updates a program value.
        self.username_var = tk.StringVar()
        # Remark: creates or updates a program value.
        self.password_var = tk.StringVar()
        # Remark: creates or updates a program value.
        self.room_var = tk.StringVar(value="general")
        # Remark: creates or updates a program value.
        self.new_room_var = tk.StringVar()
        # Remark: creates or updates a program value.
        self.message_var = tk.StringVar()
        # Remark: creates or updates a program value.
        self.auth_status_var = tk.StringVar(value="Connected. Register or login to continue.")
        # Remark: creates or updates a program value.
        self.chat_status_var = tk.StringVar(value="")
        # Remark: creates or updates a program value.
        self.login_badge_var = tk.StringVar(value="")

        # Remark: runs this instruction as part of the program logic.
        self._build_auth_screen()
        # Remark: runs this instruction as part of the program logic.
        self._build_chat_screen()
        # Remark: runs this instruction as part of the program logic.
        self._show_auth_screen()

    # Remark: defines a function or method.
    def _build_auth_screen(self) -> None:
        # Remark: creates or updates a program value.
        self.auth_frame = tk.Frame(self, bg="#111827")

        # Remark: creates or updates a program value.
        card = tk.Frame(self.auth_frame, bg="#f8fafc", padx=34, pady=30)
        # Remark: places a widget in the graphical interface.
        card.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Remark: starts a multi-line expression.
        tk.Label(
            # Remark: runs this instruction as part of the program logic.
            card,
            # Remark: creates or updates a program value.
            text="SecureChat",
            # Remark: creates or updates a program value.
            bg="#f8fafc",
            # Remark: creates or updates a program value.
            fg="#2563eb",
            # Remark: creates or updates a program value.
            font=("Segoe UI", 30, "bold"),
        # Remark: closes a multi-line expression.
        ).grid(row=0, column=0, columnspan=2, pady=(0, 6))
        # Remark: starts a multi-line expression.
        tk.Label(
            # Remark: runs this instruction as part of the program logic.
            card,
            # Remark: creates or updates a program value.
            text="Encrypted multi-user chat",
            # Remark: creates or updates a program value.
            bg="#f8fafc",
            # Remark: creates or updates a program value.
            fg="#475569",
            # Remark: creates or updates a program value.
            font=("Segoe UI", 12),
        # Remark: closes a multi-line expression.
        ).grid(row=1, column=0, columnspan=2, pady=(0, 24))

        # Remark: starts a multi-line expression.
        tk.Label(card, text="Username", bg="#f8fafc", fg="#0f172a", font=("Segoe UI", 11, "bold")).grid(
            # Remark: creates or updates a program value.
            row=2, column=0, sticky="w"
        # Remark: closes a multi-line expression.
        )
        # Remark: starts a multi-line expression.
        tk.Entry(
            # Remark: runs this instruction as part of the program logic.
            card,
            # Remark: creates or updates a program value.
            textvariable=self.username_var,
            # Remark: creates or updates a program value.
            width=30,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 12),
            # Remark: creates or updates a program value.
            bg="#e0f2fe",
            # Remark: creates or updates a program value.
            fg="#0f172a",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
        # Remark: closes a multi-line expression.
        ).grid(row=3, column=0, columnspan=2, sticky="ew", pady=(4, 14), ipady=8)

        # Remark: starts a multi-line expression.
        tk.Label(card, text="Password", bg="#f8fafc", fg="#0f172a", font=("Segoe UI", 11, "bold")).grid(
            # Remark: creates or updates a program value.
            row=4, column=0, sticky="w"
        # Remark: closes a multi-line expression.
        )
        # Remark: starts a multi-line expression.
        password_entry = tk.Entry(
            # Remark: runs this instruction as part of the program logic.
            card,
            # Remark: creates or updates a program value.
            textvariable=self.password_var,
            # Remark: creates or updates a program value.
            show="*",
            # Remark: creates or updates a program value.
            width=30,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 12),
            # Remark: creates or updates a program value.
            bg="#fef3c7",
            # Remark: creates or updates a program value.
            fg="#0f172a",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
        # Remark: closes a multi-line expression.
        )
        # Remark: places a widget in the graphical interface.
        password_entry.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(4, 18), ipady=8)
        # Remark: runs this instruction as part of the program logic.
        password_entry.bind("<Return>", lambda _event: self._login())

        # Remark: starts a multi-line expression.
        tk.Button(
            # Remark: runs this instruction as part of the program logic.
            card,
            # Remark: creates or updates a program value.
            text="Register",
            # Remark: creates or updates a program value.
            command=self._register_user,
            # Remark: creates or updates a program value.
            bg="#22c55e",
            # Remark: creates or updates a program value.
            fg="white",
            # Remark: creates or updates a program value.
            activebackground="#16a34a",
            # Remark: creates or updates a program value.
            font=("Segoe UI", 11, "bold"),
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            padx=16,
            # Remark: creates or updates a program value.
            pady=8,
        # Remark: closes a multi-line expression.
        ).grid(row=6, column=0, sticky="ew", padx=(0, 8))
        # Remark: starts a multi-line expression.
        tk.Button(
            # Remark: runs this instruction as part of the program logic.
            card,
            # Remark: creates or updates a program value.
            text="Login",
            # Remark: creates or updates a program value.
            command=self._login,
            # Remark: creates or updates a program value.
            bg="#3b82f6",
            # Remark: creates or updates a program value.
            fg="white",
            # Remark: creates or updates a program value.
            activebackground="#2563eb",
            # Remark: creates or updates a program value.
            font=("Segoe UI", 11, "bold"),
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            padx=16,
            # Remark: creates or updates a program value.
            pady=8,
        # Remark: closes a multi-line expression.
        ).grid(row=6, column=1, sticky="ew", padx=(8, 0))

        # Remark: starts a multi-line expression.
        self.auth_status_label = tk.Label(
            # Remark: runs this instruction as part of the program logic.
            card,
            # Remark: creates or updates a program value.
            textvariable=self.auth_status_var,
            # Remark: creates or updates a program value.
            bg="#dbeafe",
            # Remark: creates or updates a program value.
            fg="#2563eb",
            # Remark: creates or updates a program value.
            wraplength=360,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 12, "bold"),
            # Remark: creates or updates a program value.
            padx=10,
            # Remark: creates or updates a program value.
            pady=8,
        # Remark: closes a multi-line expression.
        )
        # Remark: places a widget in the graphical interface.
        self.auth_status_label.grid(row=7, column=0, columnspan=2, pady=(18, 0))

    # Remark: defines a function or method.
    def _build_chat_screen(self) -> None:
        # Remark: creates or updates a program value.
        self.chat_frame = tk.Frame(self, bg="#dbeafe")
        # Remark: creates or updates a program value.
        self.chat_frame.columnconfigure(1, weight=1)
        # Remark: creates or updates a program value.
        self.chat_frame.rowconfigure(1, weight=1)

        # Remark: creates or updates a program value.
        header = tk.Frame(self.chat_frame, bg="#1d4ed8", padx=14, pady=12)
        # Remark: places a widget in the graphical interface.
        header.grid(row=0, column=0, columnspan=3, sticky="ew")
        # Remark: creates or updates a program value.
        header.columnconfigure(1, weight=1)

        # Remark: starts a multi-line expression.
        tk.Label(
            # Remark: runs this instruction as part of the program logic.
            header,
            # Remark: creates or updates a program value.
            text="SecureChat",
            # Remark: creates or updates a program value.
            bg="#1d4ed8",
            # Remark: creates or updates a program value.
            fg="white",
            # Remark: creates or updates a program value.
            font=("Segoe UI", 20, "bold"),
        # Remark: closes a multi-line expression.
        ).grid(row=0, column=0, sticky="w")
        # Remark: starts a multi-line expression.
        tk.Label(
            # Remark: runs this instruction as part of the program logic.
            header,
            # Remark: creates or updates a program value.
            textvariable=self.login_badge_var,
            # Remark: creates or updates a program value.
            bg="#1d4ed8",
            # Remark: creates or updates a program value.
            fg="#bbf7d0",
            # Remark: creates or updates a program value.
            font=("Segoe UI", 12, "bold"),
        # Remark: closes a multi-line expression.
        ).grid(row=0, column=1, sticky="e")

        # Remark: creates or updates a program value.
        rooms_panel = tk.Frame(self.chat_frame, bg="#eff6ff", padx=10, pady=10)
        # Remark: places a widget in the graphical interface.
        rooms_panel.grid(row=1, column=0, sticky="nsw", padx=(10, 5), pady=10)
        # Remark: creates or updates a program value.
        rooms_panel.rowconfigure(1, weight=1)

        # Remark: starts a multi-line expression.
        tk.Label(rooms_panel, text="Rooms", bg="#eff6ff", fg="#1e3a8a", font=("Segoe UI", 14, "bold")).grid(
            # Remark: creates or updates a program value.
            row=0, column=0, columnspan=2, sticky="w", pady=(0, 8)
        # Remark: closes a multi-line expression.
        )
        # Remark: starts a multi-line expression.
        self.rooms_box = tk.Listbox(
            # Remark: runs this instruction as part of the program logic.
            rooms_panel,
            # Remark: creates or updates a program value.
            width=22,
            # Remark: creates or updates a program value.
            height=18,
            # Remark: creates or updates a program value.
            bg="#ffffff",
            # Remark: creates or updates a program value.
            fg="#0f172a",
            # Remark: creates or updates a program value.
            selectbackground="#3b82f6",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 10),
        # Remark: closes a multi-line expression.
        )
        # Remark: places a widget in the graphical interface.
        self.rooms_box.grid(row=1, column=0, columnspan=2, sticky="nsew")
        # Remark: runs this instruction as part of the program logic.
        self.rooms_box.bind("<<ListboxSelect>>", self._on_room_select)

        # Remark: starts a multi-line expression.
        tk.Button(
            # Remark: runs this instruction as part of the program logic.
            rooms_panel,
            # Remark: creates or updates a program value.
            text="Join Selected",
            # Remark: creates or updates a program value.
            command=self._join_room,
            # Remark: creates or updates a program value.
            bg="#8b5cf6",
            # Remark: creates or updates a program value.
            fg="white",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 10, "bold"),
        # Remark: closes a multi-line expression.
        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(8, 12))

        # Remark: starts a multi-line expression.
        tk.Entry(
            # Remark: runs this instruction as part of the program logic.
            rooms_panel,
            # Remark: creates or updates a program value.
            textvariable=self.new_room_var,
            # Remark: creates or updates a program value.
            bg="#fef3c7",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 10),
        # Remark: closes a multi-line expression.
        ).grid(row=3, column=0, columnspan=2, sticky="ew", ipady=6)
        # Remark: starts a multi-line expression.
        tk.Button(
            # Remark: runs this instruction as part of the program logic.
            rooms_panel,
            # Remark: creates or updates a program value.
            text="Create Room",
            # Remark: creates or updates a program value.
            command=self._create_room,
            # Remark: creates or updates a program value.
            bg="#f97316",
            # Remark: creates or updates a program value.
            fg="white",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 10, "bold"),
        # Remark: closes a multi-line expression.
        ).grid(row=4, column=0, columnspan=2, sticky="ew", pady=(8, 8))
        # Remark: starts a multi-line expression.
        tk.Button(
            # Remark: runs this instruction as part of the program logic.
            rooms_panel,
            # Remark: creates or updates a program value.
            text="Refresh Rooms",
            # Remark: creates or updates a program value.
            command=self._request_rooms,
            # Remark: creates or updates a program value.
            bg="#06b6d4",
            # Remark: creates or updates a program value.
            fg="white",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 10, "bold"),
        # Remark: closes a multi-line expression.
        ).grid(row=5, column=0, columnspan=2, sticky="ew")

        # Remark: creates or updates a program value.
        chat_panel = tk.Frame(self.chat_frame, bg="#dbeafe", padx=5, pady=10)
        # Remark: places a widget in the graphical interface.
        chat_panel.grid(row=1, column=1, sticky="nsew", pady=10)
        # Remark: creates or updates a program value.
        chat_panel.rowconfigure(1, weight=1)
        # Remark: creates or updates a program value.
        chat_panel.columnconfigure(0, weight=1)

        # Remark: creates or updates a program value.
        self.room_title_var = tk.StringVar(value="Room: general")
        # Remark: starts a multi-line expression.
        tk.Label(
            # Remark: runs this instruction as part of the program logic.
            chat_panel,
            # Remark: creates or updates a program value.
            textvariable=self.room_title_var,
            # Remark: creates or updates a program value.
            bg="#dbeafe",
            # Remark: creates or updates a program value.
            fg="#1e3a8a",
            # Remark: creates or updates a program value.
            font=("Segoe UI", 14, "bold"),
        # Remark: closes a multi-line expression.
        ).grid(row=0, column=0, sticky="w", pady=(0, 8))

        # Remark: starts a multi-line expression.
        self.chat_box = scrolledtext.ScrolledText(
            # Remark: runs this instruction as part of the program logic.
            chat_panel,
            # Remark: creates or updates a program value.
            state=tk.DISABLED,
            # Remark: creates or updates a program value.
            wrap=tk.WORD,
            # Remark: creates or updates a program value.
            bg="#ffffff",
            # Remark: creates or updates a program value.
            fg="#0f172a",
            # Remark: creates or updates a program value.
            insertbackground="#0f172a",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            font=("Consolas", 10),
        # Remark: closes a multi-line expression.
        )
        # Remark: places a widget in the graphical interface.
        self.chat_box.grid(row=1, column=0, sticky="nsew")

        # Remark: creates or updates a program value.
        send_frame = tk.Frame(chat_panel, bg="#dbeafe")
        # Remark: places a widget in the graphical interface.
        send_frame.grid(row=2, column=0, sticky="ew", pady=(10, 0))
        # Remark: creates or updates a program value.
        send_frame.columnconfigure(0, weight=1)
        # Remark: creates or updates a program value.
        message_entry = tk.Entry(send_frame, textvariable=self.message_var, bg="#ffffff", relief=tk.FLAT, font=("Segoe UI", 11))
        # Remark: places a widget in the graphical interface.
        message_entry.grid(row=0, column=0, sticky="ew", ipady=8, padx=(0, 8))
        # Remark: runs this instruction as part of the program logic.
        message_entry.bind("<Return>", lambda _event: self._send_message())
        # Remark: starts a multi-line expression.
        tk.Button(
            # Remark: runs this instruction as part of the program logic.
            send_frame,
            # Remark: creates or updates a program value.
            text="Send",
            # Remark: creates or updates a program value.
            command=self._send_message,
            # Remark: creates or updates a program value.
            bg="#22c55e",
            # Remark: creates or updates a program value.
            fg="white",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 11, "bold"),
            # Remark: creates or updates a program value.
            padx=20,
        # Remark: closes a multi-line expression.
        ).grid(row=0, column=1)

        # Remark: creates or updates a program value.
        media_frame = tk.Frame(chat_panel, bg="#dbeafe")
        # Remark: places a widget in the graphical interface.
        media_frame.grid(row=3, column=0, sticky="ew", pady=(8, 0))
        # Remark: starts a loop over multiple values.
        for emoji in ["😀", "😂", "❤️", "👍", "🔥", "🎉"]:
            # Remark: starts a multi-line expression.
            tk.Button(
                # Remark: runs this instruction as part of the program logic.
                media_frame,
                # Remark: creates or updates a program value.
                text=emoji,
                # Remark: creates or updates a program value.
                command=lambda value=emoji: self._insert_emoji(value),
                # Remark: creates or updates a program value.
                bg="#fef3c7",
                # Remark: creates or updates a program value.
                relief=tk.FLAT,
                # Remark: creates or updates a program value.
                font=("Segoe UI Emoji", 12),
                # Remark: creates or updates a program value.
                width=3,
            # Remark: closes a multi-line expression.
            ).pack(side=tk.LEFT, padx=(0, 5))

        # Remark: starts a multi-line expression.
        tk.Button(
            # Remark: runs this instruction as part of the program logic.
            media_frame,
            # Remark: creates or updates a program value.
            text="Send File",
            # Remark: creates or updates a program value.
            command=lambda: self._send_file("file"),
            # Remark: creates or updates a program value.
            bg="#64748b",
            # Remark: creates or updates a program value.
            fg="white",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 10, "bold"),
            # Remark: creates or updates a program value.
            padx=10,
        # Remark: closes a multi-line expression.
        ).pack(side=tk.LEFT, padx=(12, 5))
        # Remark: starts a multi-line expression.
        tk.Button(
            # Remark: runs this instruction as part of the program logic.
            media_frame,
            # Remark: creates or updates a program value.
            text="Send Image",
            # Remark: creates or updates a program value.
            command=lambda: self._send_file("image"),
            # Remark: creates or updates a program value.
            bg="#ec4899",
            # Remark: creates or updates a program value.
            fg="white",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 10, "bold"),
            # Remark: creates or updates a program value.
            padx=10,
        # Remark: closes a multi-line expression.
        ).pack(side=tk.LEFT, padx=5)
        # Remark: starts a multi-line expression.
        tk.Button(
            # Remark: runs this instruction as part of the program logic.
            media_frame,
            # Remark: creates or updates a program value.
            text="Send Video",
            # Remark: creates or updates a program value.
            command=lambda: self._send_file("video"),
            # Remark: creates or updates a program value.
            bg="#7c3aed",
            # Remark: creates or updates a program value.
            fg="white",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 10, "bold"),
            # Remark: creates or updates a program value.
            padx=10,
        # Remark: closes a multi-line expression.
        ).pack(side=tk.LEFT, padx=5)

        # Remark: creates or updates a program value.
        users_panel = tk.Frame(self.chat_frame, bg="#ecfdf5", padx=10, pady=10)
        # Remark: places a widget in the graphical interface.
        users_panel.grid(row=1, column=2, sticky="nse", padx=(5, 10), pady=10)
        # Remark: creates or updates a program value.
        users_panel.rowconfigure(1, weight=1)
        # Remark: starts a multi-line expression.
        tk.Label(users_panel, text="Online Users", bg="#ecfdf5", fg="#166534", font=("Segoe UI", 14, "bold")).grid(
            # Remark: creates or updates a program value.
            row=0, column=0, sticky="w", pady=(0, 8)
        # Remark: closes a multi-line expression.
        )
        # Remark: starts a multi-line expression.
        self.users_box = tk.Listbox(
            # Remark: runs this instruction as part of the program logic.
            users_panel,
            # Remark: creates or updates a program value.
            width=24,
            # Remark: creates or updates a program value.
            height=18,
            # Remark: creates or updates a program value.
            bg="#ffffff",
            # Remark: creates or updates a program value.
            fg="#0f172a",
            # Remark: creates or updates a program value.
            selectbackground="#22c55e",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 10),
        # Remark: closes a multi-line expression.
        )
        # Remark: places a widget in the graphical interface.
        self.users_box.grid(row=1, column=0, sticky="nsew")
        # Remark: starts a multi-line expression.
        tk.Button(
            # Remark: runs this instruction as part of the program logic.
            users_panel,
            # Remark: creates or updates a program value.
            text="Refresh Users",
            # Remark: creates or updates a program value.
            command=self._request_users,
            # Remark: creates or updates a program value.
            bg="#16a34a",
            # Remark: creates or updates a program value.
            fg="white",
            # Remark: creates or updates a program value.
            relief=tk.FLAT,
            # Remark: creates or updates a program value.
            font=("Segoe UI", 10, "bold"),
        # Remark: closes a multi-line expression.
        ).grid(row=2, column=0, sticky="ew", pady=(8, 0))

        # Remark: starts a multi-line expression.
        self.chat_status_label = tk.Label(
            # Remark: runs this instruction as part of the program logic.
            self.chat_frame,
            # Remark: creates or updates a program value.
            textvariable=self.chat_status_var,
            # Remark: creates or updates a program value.
            bg="#dbeafe",
            # Remark: creates or updates a program value.
            fg="#1d4ed8",
            # Remark: creates or updates a program value.
            font=("Segoe UI", 10, "bold"),
        # Remark: closes a multi-line expression.
        )
        # Remark: places a widget in the graphical interface.
        self.chat_status_label.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=(0, 8))

    # Remark: defines a function or method.
    def _show_auth_screen(self) -> None:
        # Remark: creates or updates a program value.
        self.current_screen = "auth"
        # Remark: runs this instruction as part of the program logic.
        self.chat_frame.pack_forget()
        # Remark: places a widget in the graphical interface.
        self.auth_frame.pack(fill=tk.BOTH, expand=True)

    # Remark: defines a function or method.
    def _show_chat_screen(self) -> None:
        # Remark: creates or updates a program value.
        self.current_screen = "chat"
        # Remark: runs this instruction as part of the program logic.
        self.auth_frame.pack_forget()
        # Remark: places a widget in the graphical interface.
        self.chat_frame.pack(fill=tk.BOTH, expand=True)

    # Remark: defines a function or method.
    def _register_user(self) -> None:
        # Remark: runs this instruction as part of the program logic.
        self._send_auth_packet("register")

    # Remark: defines a function or method.
    def _login(self) -> None:
        # Remark: runs this instruction as part of the program logic.
        self._send_auth_packet("login")

    # Remark: defines a function or method.
    def _send_auth_packet(self, packet_type: str) -> None:
        # Remark: starts protected code that may raise an error.
        try:
            # Remark: creates or updates a program value.
            username = InputValidator.username(self.username_var.get())
            # Remark: creates or updates a program value.
            password = InputValidator.password(self.password_var.get())
            # Remark: starts a multi-line expression.
            self.connection.send(
                # Remark: runs this instruction as part of the program logic.
                packet_type,
                # Remark: creates or updates a program value.
                username=username,
                # Remark: creates or updates a program value.
                password=password,
            # Remark: closes a multi-line expression.
            )
        # Remark: handles an expected error safely.
        except ValidationError as exc:
            # Remark: creates or updates a program value.
            self._set_auth_status(str(exc), ok=False)
            # Remark: runs this instruction as part of the program logic.
            messagebox.showerror("Invalid details", str(exc))
        # Remark: handles an expected error safely.
        except Exception as exc:
            # Remark: creates or updates a program value.
            self._set_auth_status(f"Connection error: {exc}", ok=False)

    # Remark: defines a function or method.
    def _join_room(self) -> None:
        # Remark: checks a condition before continuing.
        if not self.logged_in:
            # Remark: creates or updates a program value.
            self._set_chat_status("Please login first.", ok=False)
            # Remark: returns a value to the caller.
            return
        # Remark: creates or updates a program value.
        room = self.room_var.get().strip()
        # Remark: checks a condition before continuing.
        if not room:
            # Remark: creates or updates a program value.
            self._set_chat_status("Choose a room first.", ok=False)
            # Remark: returns a value to the caller.
            return
        # Remark: sends data or connects a GUI action.
        self.connection.send("join", room=room)

    # Remark: defines a function or method.
    def _create_room(self) -> None:
        # Remark: checks a condition before continuing.
        if not self.logged_in:
            # Remark: creates or updates a program value.
            self._set_chat_status("Please login first.", ok=False)
            # Remark: returns a value to the caller.
            return
        # Remark: creates or updates a program value.
        room = self.new_room_var.get().strip()
        # Remark: checks a condition before continuing.
        if not room:
            # Remark: creates or updates a program value.
            self._set_chat_status("Write a room name to create.", ok=False)
            # Remark: returns a value to the caller.
            return
        # Remark: sends data or connects a GUI action.
        self.connection.send("create_room", room=room)

    # Remark: defines a function or method.
    def _request_users(self) -> None:
        # Remark: checks a condition before continuing.
        if self.logged_in:
            # Remark: sends data or connects a GUI action.
            self.connection.send("users")

    # Remark: defines a function or method.
    def _request_rooms(self) -> None:
        # Remark: checks a condition before continuing.
        if self.logged_in:
            # Remark: sends data or connects a GUI action.
            self.connection.send("rooms")

    # Remark: defines a function or method.
    def _send_message(self) -> None:
        # Remark: checks a condition before continuing.
        if not self.logged_in:
            # Remark: creates or updates a program value.
            self._set_chat_status("Please login first.", ok=False)
            # Remark: returns a value to the caller.
            return

        # Remark: creates or updates a program value.
        body = self.message_var.get()
        # Remark: checks a condition before continuing.
        if not body.strip():
            # Remark: returns a value to the caller.
            return

        # Remark: starts protected code that may raise an error.
        try:
            # Remark: sends data or connects a GUI action.
            self.connection.send("message", body=body)
            # Remark: runs this instruction as part of the program logic.
            self.message_var.set("")
        # Remark: handles an expected error safely.
        except Exception as exc:
            # Remark: creates or updates a program value.
            self._set_chat_status(f"Send failed: {exc}", ok=False)

    # Remark: defines a function or method.
    def _insert_emoji(self, emoji: str) -> None:
        # Remark: runs this instruction as part of the program logic.
        self.message_var.set(self.message_var.get() + emoji)

    # Remark: defines a function or method.
    def _send_file(self, kind: str) -> None:
        # Remark: checks a condition before continuing.
        if not self.logged_in:
            # Remark: creates or updates a program value.
            self._set_chat_status("Please login first.", ok=False)
            # Remark: returns a value to the caller.
            return

        # Remark: starts a multi-line expression.
        filters = {
            # Remark: runs this instruction as part of the program logic.
            "file": [("All files", "*.*")],
            # Remark: runs this instruction as part of the program logic.
            "image": [("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"), ("All files", "*.*")],
            # Remark: runs this instruction as part of the program logic.
            "video": [("Video files", "*.mp4 *.mov *.avi *.mkv *.webm"), ("All files", "*.*")],
        # Remark: closes a multi-line expression.
        }
        # Remark: creates or updates a program value.
        selected_path = filedialog.askopenfilename(filetypes=filters.get(kind, filters["file"]))
        # Remark: checks a condition before continuing.
        if not selected_path:
            # Remark: returns a value to the caller.
            return

        # Remark: creates or updates a program value.
        path = Path(selected_path)
        # Remark: checks a condition before continuing.
        if path.stat().st_size > MAX_FILE_SIZE:
            # Remark: starts a multi-line expression.
            self._set_chat_status(
                # Remark: runs this instruction as part of the program logic.
                f"File is too large. Maximum size is {MAX_FILE_SIZE // (1024 * 1024)} MB.",
                # Remark: creates or updates a program value.
                ok=False,
            # Remark: closes a multi-line expression.
            )
            # Remark: returns a value to the caller.
            return

        # Remark: starts protected code that may raise an error.
        try:
            # Remark: creates or updates a program value.
            filename = InputValidator.filename(path.name)
            # Remark: creates or updates a program value.
            encoded_data = base64.b64encode(path.read_bytes()).decode("ascii")
            # Remark: creates or updates a program value.
            mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
            # Remark: starts a multi-line expression.
            self.connection.send(
                # Remark: runs this instruction as part of the program logic.
                "file",
                # Remark: creates or updates a program value.
                filename=filename,
                # Remark: creates or updates a program value.
                kind=kind,
                # Remark: creates or updates a program value.
                mime_type=mime_type,
                # Remark: creates or updates a program value.
                data=encoded_data,
            # Remark: closes a multi-line expression.
            )
            # Remark: creates or updates a program value.
            self._set_chat_status(f"Sending {kind}: {filename}", ok=True)
        # Remark: handles an expected error safely.
        except Exception as exc:
            # Remark: creates or updates a program value.
            self._set_chat_status(f"Could not send {kind}: {exc}", ok=False)

    # Remark: defines a function or method.
    def _poll_incoming(self) -> None:
        # Remark: starts a loop that continues while a condition is true.
        while not self.connection.incoming.empty():
            # Remark: creates or updates a program value.
            packet = self.connection.incoming.get_nowait()
            # Remark: runs this instruction as part of the program logic.
            self._handle_packet(packet)
        # Remark: runs this instruction as part of the program logic.
        self.after(100, self._poll_incoming)

    # Remark: defines a function or method.
    def _handle_packet(self, packet: dict[str, object]) -> None:
        # Remark: creates or updates a program value.
        packet_type = packet.get("type")

        # Remark: checks a condition before continuing.
        if packet_type == "welcome":
            # Remark: creates or updates a program value.
            self._set_auth_status(str(packet.get("message", "Connected")), ok=True)
        # Remark: checks another possible condition.
        elif packet_type == "ok":
            # Remark: runs this instruction as part of the program logic.
            self._handle_ok(packet)
        # Remark: checks another possible condition.
        elif packet_type == "error":
            # Remark: runs this instruction as part of the program logic.
            self._handle_error(packet)
        # Remark: checks another possible condition.
        elif packet_type == "history":
            # Remark: runs this instruction as part of the program logic.
            self._show_history(packet)
        # Remark: checks another possible condition.
        elif packet_type == "message":
            # Remark: starts a multi-line expression.
            self._append_chat(
                # Remark: runs this instruction as part of the program logic.
                f"[{packet.get('created_at')}] {packet.get('sender')}: {packet.get('body')}"
            # Remark: closes a multi-line expression.
            )
        # Remark: checks another possible condition.
        elif packet_type == "file":
            # Remark: runs this instruction as part of the program logic.
            self._handle_file_packet(packet)
        # Remark: checks another possible condition.
        elif packet_type == "system":
            # Remark: runs this instruction as part of the program logic.
            self._append_chat(f"* {packet.get('message')}")
        # Remark: checks another possible condition.
        elif packet_type == "users":
            # Remark: runs this instruction as part of the program logic.
            self._show_users(packet)
        # Remark: checks another possible condition.
        elif packet_type == "rooms":
            # Remark: runs this instruction as part of the program logic.
            self._show_rooms(packet)
        # Remark: checks another possible condition.
        elif packet_type == "connection_closed":
            # Remark: creates or updates a program value.
            message = f"Disconnected: {packet.get('message')}"
            # Remark: checks a condition before continuing.
            if self.current_screen == "auth":
                # Remark: creates or updates a program value.
                self._set_auth_status(message, ok=False)
            # Remark: handles the case where previous conditions were false.
            else:
                # Remark: creates or updates a program value.
                self._set_chat_status(message, ok=False)

    # Remark: defines a function or method.
    def _handle_ok(self, packet: dict[str, object]) -> None:
        # Remark: creates or updates a program value.
        action = packet.get("action")
        # Remark: creates or updates a program value.
        message = str(packet.get("message", "OK"))
        # Remark: checks a condition before continuing.
        if action == "login":
            # Remark: creates or updates a program value.
            self.logged_in = True
            # Remark: runs this instruction as part of the program logic.
            self.login_badge_var.set(f"Logged in as {self.username_var.get().strip()}")
            # Remark: runs this instruction as part of the program logic.
            self._show_chat_screen()
            # Remark: creates or updates a program value.
            self._set_chat_status(message, ok=True)
            # Remark: runs this instruction as part of the program logic.
            messagebox.showinfo("Login OK", message)
            # Remark: runs this instruction as part of the program logic.
            self._request_rooms()
            # Remark: runs this instruction as part of the program logic.
            self._request_users()
        # Remark: checks another possible condition.
        elif action == "register":
            # Remark: creates or updates a program value.
            self._set_auth_status(f"{message}. Logging in...", ok=True)
            # Remark: runs this instruction as part of the program logic.
            messagebox.showinfo("Register OK", f"{message}. You will be logged in now.")
            # Remark: starts a multi-line expression.
            self.connection.send(
                # Remark: runs this instruction as part of the program logic.
                "login",
                # Remark: creates or updates a program value.
                username=self.username_var.get(),
                # Remark: creates or updates a program value.
                password=self.password_var.get(),
            # Remark: closes a multi-line expression.
            )
        # Remark: checks another possible condition.
        elif action == "create_room":
            # Remark: creates or updates a program value.
            room = str(packet.get("room", "general"))
            # Remark: runs this instruction as part of the program logic.
            self.new_room_var.set("")
            # Remark: runs this instruction as part of the program logic.
            self.room_var.set(room)
            # Remark: creates or updates a program value.
            self._set_chat_status(message, ok=True)
            # Remark: sends data or connects a GUI action.
            self.connection.send("join", room=room)
        # Remark: checks another possible condition.
        elif action == "join":
            # Remark: creates or updates a program value.
            self.current_room = str(packet.get("room", "general"))
            # Remark: runs this instruction as part of the program logic.
            self.room_var.set(self.current_room)
            # Remark: runs this instruction as part of the program logic.
            self.room_title_var.set(f"Room: {self.current_room}")
            # Remark: runs this instruction as part of the program logic.
            self._clear_chat()
            # Remark: creates or updates a program value.
            self._set_chat_status(message, ok=True)
            # Remark: runs this instruction as part of the program logic.
            self._request_rooms()
            # Remark: runs this instruction as part of the program logic.
            self._request_users()

    # Remark: defines a function or method.
    def _handle_error(self, packet: dict[str, object]) -> None:
        # Remark: creates or updates a program value.
        action = packet.get("action")
        # Remark: creates or updates a program value.
        message = str(packet.get("message", "Unknown error"))

        # Remark: checks a condition before continuing.
        if action == "register" and "already exists" in message.lower():
            # Remark: creates or updates a program value.
            self._set_auth_status("Username already exists. Trying to login...", ok=True)
            # Remark: starts a multi-line expression.
            self.connection.send(
                # Remark: runs this instruction as part of the program logic.
                "login",
                # Remark: creates or updates a program value.
                username=self.username_var.get(),
                # Remark: creates or updates a program value.
                password=self.password_var.get(),
            # Remark: closes a multi-line expression.
            )
            # Remark: returns a value to the caller.
            return

        # Remark: checks a condition before continuing.
        if action in {"register", "login"} or self.current_screen == "auth":
            # Remark: creates or updates a program value.
            self._set_auth_status(message, ok=False)
            # Remark: runs this instruction as part of the program logic.
            messagebox.showerror("Login/Register failed", message)
            # Remark: returns a value to the caller.
            return

        # Remark: creates or updates a program value.
        self._set_chat_status(message, ok=False)
        # Remark: runs this instruction as part of the program logic.
        messagebox.showerror("Action failed", message)

    # Remark: defines a function or method.
    def _show_history(self, packet: dict[str, object]) -> None:
        # Remark: creates or updates a program value.
        room = packet.get("room", "general")
        # Remark: creates or updates a program value.
        self.current_room = str(room)
        # Remark: runs this instruction as part of the program logic.
        self.room_var.set(self.current_room)
        # Remark: runs this instruction as part of the program logic.
        self.room_title_var.set(f"Room: {self.current_room}")
        # Remark: creates or updates a program value.
        self.chat_box.configure(state=tk.NORMAL)
        # Remark: runs this instruction as part of the program logic.
        self.chat_box.delete("1.0", tk.END)
        # Remark: runs this instruction as part of the program logic.
        self.chat_box.insert(tk.END, f"--- History for room {self.current_room} ---\n")
        # Remark: starts a loop over multiple values.
        for message in packet.get("messages", []):
            # Remark: checks a condition before continuing.
            if isinstance(message, dict):
                # Remark: starts a multi-line expression.
                self.chat_box.insert(
                    # Remark: runs this instruction as part of the program logic.
                    tk.END,
                    # Remark: runs this instruction as part of the program logic.
                    f"[{message.get('created_at')}] {message.get('sender')}: {message.get('body')}\n",
                # Remark: closes a multi-line expression.
                )
        # Remark: creates or updates a program value.
        self.chat_box.configure(state=tk.DISABLED)
        # Remark: runs this instruction as part of the program logic.
        self.chat_box.see(tk.END)

    # Remark: defines a function or method.
    def _show_users(self, packet: dict[str, object]) -> None:
        # Remark: runs this instruction as part of the program logic.
        self.users_box.delete(0, tk.END)
        # Remark: creates or updates a program value.
        online = packet.get("online", [])
        # Remark: checks a condition before continuing.
        if isinstance(online, list):
            # Remark: starts a loop over multiple values.
            for user in online:
                # Remark: checks a condition before continuing.
                if isinstance(user, dict):
                    # Remark: runs this instruction as part of the program logic.
                    self.users_box.insert(tk.END, f"{user.get('username')} @ {user.get('room')}")

    # Remark: defines a function or method.
    def _show_rooms(self, packet: dict[str, object]) -> None:
        # Remark: creates or updates a program value.
        rooms = packet.get("rooms", [])
        # Remark: creates or updates a program value.
        current = str(packet.get("current", self.current_room))
        # Remark: runs this instruction as part of the program logic.
        self.rooms_box.delete(0, tk.END)

        # Remark: checks a condition before continuing.
        if isinstance(rooms, list):
            # Remark: starts a loop over multiple values.
            for index, room in enumerate(rooms):
                # Remark: creates or updates a program value.
                room_name = str(room)
                # Remark: runs this instruction as part of the program logic.
                self.rooms_box.insert(tk.END, room_name)
                # Remark: checks a condition before continuing.
                if room_name == current:
                    # Remark: runs this instruction as part of the program logic.
                    self.rooms_box.selection_clear(0, tk.END)
                    # Remark: runs this instruction as part of the program logic.
                    self.rooms_box.selection_set(index)
                    # Remark: runs this instruction as part of the program logic.
                    self.rooms_box.see(index)
                    # Remark: runs this instruction as part of the program logic.
                    self.room_var.set(room_name)

    # Remark: defines a function or method.
    def _on_room_select(self, _event: tk.Event) -> None:
        # Remark: creates or updates a program value.
        selection = self.rooms_box.curselection()
        # Remark: checks a condition before continuing.
        if selection:
            # Remark: runs this instruction as part of the program logic.
            self.room_var.set(self.rooms_box.get(selection[0]))

    # Remark: defines a function or method.
    def _handle_file_packet(self, packet: dict[str, object]) -> None:
        # Remark: starts protected code that may raise an error.
        try:
            # Remark: creates or updates a program value.
            filename = InputValidator.filename(str(packet.get("filename", "download.bin")))
            # Remark: creates or updates a program value.
            kind = str(packet.get("kind", "file"))
            # Remark: creates or updates a program value.
            sender = str(packet.get("sender", "unknown"))
            # Remark: creates or updates a program value.
            created_at = str(packet.get("created_at", ""))
            # Remark: creates or updates a program value.
            encoded_data = str(packet.get("data", ""))
            # Remark: creates or updates a program value.
            file_data = base64.b64decode(encoded_data.encode("ascii"), validate=True)
        # Remark: handles an expected error safely.
        except Exception as exc:
            # Remark: creates or updates a program value.
            self._set_chat_status(f"Received invalid file packet: {exc}", ok=False)
            # Remark: returns a value to the caller.
            return

        # Remark: creates or updates a program value.
        DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
        # Remark: creates or updates a program value.
        save_path = self._unique_download_path(filename)
        # Remark: runs this instruction as part of the program logic.
        save_path.write_bytes(file_data)

        # Remark: checks a condition before continuing.
        if kind == "image":
            # Remark: runs this instruction as part of the program logic.
            self._append_image_preview(created_at, sender, filename, save_path)
        # Remark: handles the case where previous conditions were false.
        else:
            # Remark: runs this instruction as part of the program logic.
            self._append_clickable_file(created_at, sender, kind, filename, save_path)

    # Remark: defines a function or method.
    def _unique_download_path(self, filename: str) -> Path:
        # Remark: creates or updates a program value.
        path = DOWNLOAD_DIR / filename
        # Remark: checks a condition before continuing.
        if not path.exists():
            # Remark: returns a value to the caller.
            return path

        # Remark: creates or updates a program value.
        stem = path.stem
        # Remark: creates or updates a program value.
        suffix = path.suffix
        # Remark: creates or updates a program value.
        counter = 1
        # Remark: starts a loop that continues while a condition is true.
        while True:
            # Remark: creates or updates a program value.
            candidate = DOWNLOAD_DIR / f"{stem}_{counter}{suffix}"
            # Remark: checks a condition before continuing.
            if not candidate.exists():
                # Remark: returns a value to the caller.
                return candidate
            # Remark: creates or updates a program value.
            counter += 1

    # Remark: defines a function or method.
    def _append_image_preview(
        # Remark: runs this instruction as part of the program logic.
        self,
        # Remark: runs this instruction as part of the program logic.
        created_at: str,
        # Remark: runs this instruction as part of the program logic.
        sender: str,
        # Remark: runs this instruction as part of the program logic.
        filename: str,
        # Remark: runs this instruction as part of the program logic.
        save_path: Path,
    # Remark: closes a multi-line expression.
    ) -> None:
        # Remark: runs this instruction as part of the program logic.
        self._append_clickable_file(created_at, sender, "image", filename, save_path)

        # Remark: starts protected code that may raise an error.
        try:
            # Remark: creates or updates a program value.
            image = Image.open(save_path)
            # Remark: runs this instruction as part of the program logic.
            image.thumbnail((320, 220))
            # Remark: creates or updates a program value.
            preview = ImageTk.PhotoImage(image)
        # Remark: handles an expected error safely.
        except Exception as exc:
            # Remark: runs this instruction as part of the program logic.
            self._append_chat(f"Could not show image preview: {exc}")
            # Remark: returns a value to the caller.
            return

        # Remark: runs this instruction as part of the program logic.
        self.chat_images.append(preview)
        # Remark: creates or updates a program value.
        self.chat_box.configure(state=tk.NORMAL)
        # Remark: creates or updates a program value.
        self.chat_box.image_create(tk.END, image=preview)
        # Remark: runs this instruction as part of the program logic.
        self.chat_box.insert(tk.END, "\n")
        # Remark: creates or updates a program value.
        self.chat_box.configure(state=tk.DISABLED)
        # Remark: runs this instruction as part of the program logic.
        self.chat_box.see(tk.END)

    # Remark: defines a function or method.
    def _append_clickable_file(
        # Remark: runs this instruction as part of the program logic.
        self,
        # Remark: runs this instruction as part of the program logic.
        created_at: str,
        # Remark: runs this instruction as part of the program logic.
        sender: str,
        # Remark: runs this instruction as part of the program logic.
        kind: str,
        # Remark: runs this instruction as part of the program logic.
        filename: str,
        # Remark: runs this instruction as part of the program logic.
        save_path: Path,
    # Remark: closes a multi-line expression.
    ) -> None:
        # Remark: creates or updates a program value.
        link_tag = f"link_{len(self.chat_links)}"
        # Remark: creates or updates a program value.
        self.chat_links[link_tag] = save_path

        # Remark: creates or updates a program value.
        self.chat_box.configure(state=tk.NORMAL)
        # Remark: runs this instruction as part of the program logic.
        self.chat_box.insert(tk.END, f"[{created_at}] {sender} sent {kind}: ")
        # Remark: runs this instruction as part of the program logic.
        self.chat_box.insert(tk.END, filename, (link_tag,))
        # Remark: runs this instruction as part of the program logic.
        self.chat_box.insert(tk.END, " (click to open)\n")
        # Remark: creates or updates a program value.
        self.chat_box.tag_configure(link_tag, foreground="#2563eb", underline=True)
        # Remark: creates or updates a program value.
        self.chat_box.tag_bind(link_tag, "<Button-1>", lambda _event, tag=link_tag: self._open_chat_link(tag))
        # Remark: creates or updates a program value.
        self.chat_box.tag_bind(link_tag, "<Enter>", lambda _event: self.chat_box.configure(cursor="hand2"))
        # Remark: creates or updates a program value.
        self.chat_box.tag_bind(link_tag, "<Leave>", lambda _event: self.chat_box.configure(cursor=""))
        # Remark: creates or updates a program value.
        self.chat_box.configure(state=tk.DISABLED)
        # Remark: runs this instruction as part of the program logic.
        self.chat_box.see(tk.END)

    # Remark: defines a function or method.
    def _open_chat_link(self, link_tag: str) -> None:
        # Remark: creates or updates a program value.
        path = self.chat_links.get(link_tag)
        # Remark: checks a condition before continuing.
        if path is None:
            # Remark: returns a value to the caller.
            return

        # Remark: starts protected code that may raise an error.
        try:
            # Remark: checks a condition before continuing.
            if os.name == "nt":
                # Remark: runs this instruction as part of the program logic.
                os.startfile(path)
            # Remark: checks another possible condition.
            elif sys.platform == "darwin":
                # Remark: runs this instruction as part of the program logic.
                subprocess.Popen(["open", str(path)])
            # Remark: handles the case where previous conditions were false.
            else:
                # Remark: runs this instruction as part of the program logic.
                subprocess.Popen(["xdg-open", str(path)])
        # Remark: handles an expected error safely.
        except Exception as exc:
            # Remark: creates or updates a program value.
            self._set_chat_status(f"Could not open file: {exc}", ok=False)

    # Remark: defines a function or method.
    def _append_chat(self, text: str) -> None:
        # Remark: creates or updates a program value.
        self.chat_box.configure(state=tk.NORMAL)
        # Remark: runs this instruction as part of the program logic.
        self.chat_box.insert(tk.END, text + "\n")
        # Remark: creates or updates a program value.
        self.chat_box.configure(state=tk.DISABLED)
        # Remark: runs this instruction as part of the program logic.
        self.chat_box.see(tk.END)

    # Remark: defines a function or method.
    def _clear_chat(self) -> None:
        # Remark: creates or updates a program value.
        self.chat_box.configure(state=tk.NORMAL)
        # Remark: runs this instruction as part of the program logic.
        self.chat_box.delete("1.0", tk.END)
        # Remark: creates or updates a program value.
        self.chat_box.configure(state=tk.DISABLED)

    # Remark: defines a function or method.
    def _set_auth_status(self, message: str, ok: bool) -> None:
        # Remark: runs this instruction as part of the program logic.
        self.auth_status_var.set(message)
        # Remark: starts a multi-line expression.
        self.auth_status_label.configure(
            # Remark: creates or updates a program value.
            bg="#dcfce7" if ok else "#fee2e2",
            # Remark: creates or updates a program value.
            fg="#166534" if ok else "#991b1b",
        # Remark: closes a multi-line expression.
        )

    # Remark: defines a function or method.
    def _set_chat_status(self, message: str, ok: bool) -> None:
        # Remark: runs this instruction as part of the program logic.
        self.chat_status_var.set(message)
        # Remark: creates or updates a program value.
        self.chat_status_label.configure(fg="#16a34a" if ok else "#dc2626")

    # Remark: defines a function or method.
    def _on_close(self) -> None:
        # Remark: runs this instruction as part of the program logic.
        self.connection.close()
        # Remark: runs this instruction as part of the program logic.
        self.destroy()


# Remark: defines a function or method.
def parse_args() -> argparse.Namespace:
    # Remark: creates or updates a program value.
    parser = argparse.ArgumentParser(description="SecureChat Tkinter client")
    # Remark: creates or updates a program value.
    parser.add_argument("--host", default=DEFAULT_HOST)
    # Remark: creates or updates a program value.
    parser.add_argument("--port", type=int, default=DEFAULT_PORT)
    # Remark: creates or updates a program value.
    parser.add_argument("--verify-cert", action="store_true")
    # Remark: returns a value to the caller.
    return parser.parse_args()


# Remark: checks a condition before continuing.
if __name__ == "__main__":
    # Remark: creates or updates a program value.
    args = parse_args()
    # Remark: starts a multi-line expression.
    client_connection = ChatClientConnection(
        # Remark: creates or updates a program value.
        host=args.host,
        # Remark: creates or updates a program value.
        port=args.port,
        # Remark: creates or updates a program value.
        verify_certificate=args.verify_cert,
    # Remark: closes a multi-line expression.
    )
    # Remark: runs this instruction as part of the program logic.
    client_connection.connect()
    # Remark: creates or updates a program value.
    app = SecureChatApp(client_connection)
    # Remark: runs this instruction as part of the program logic.
    app.mainloop()

