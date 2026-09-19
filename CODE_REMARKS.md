# Code Remarks

Every Python source line is listed with a short remark for school documentation.

## `secure_chat/__init__.py`

- Line 1: `"""Secure multi-user chat project for 5-unit cyber/networking bagrut."""`
  Remark: Documentation string that explains a module, class, or function.
- Line 2: ` `
  Remark: Blank line used to separate logical code sections.

## `secure_chat/client_gui.py`

- Line 1: `import argparse`
  Remark: Imports code that this file needs.
- Line 2: `import base64`
  Remark: Imports code that this file needs.
- Line 3: `import mimetypes`
  Remark: Imports code that this file needs.
- Line 4: `import os`
  Remark: Imports code that this file needs.
- Line 5: `import queue`
  Remark: Imports code that this file needs.
- Line 6: `import socket`
  Remark: Imports code that this file needs.
- Line 7: `import ssl`
  Remark: Imports code that this file needs.
- Line 8: `import subprocess`
  Remark: Imports code that this file needs.
- Line 9: `import sys`
  Remark: Imports code that this file needs.
- Line 10: `import threading`
  Remark: Imports code that this file needs.
- Line 11: `import tkinter as tk`
  Remark: Imports code that this file needs.
- Line 12: `from pathlib import Path`
  Remark: Imports code that this file needs.
- Line 13: `from tkinter import filedialog, messagebox, scrolledtext, ttk`
  Remark: Imports code that this file needs.
- Line 14: ` `
  Remark: Blank line used to separate logical code sections.
- Line 15: `from PIL import Image, ImageTk`
  Remark: Imports code that this file needs.
- Line 16: ` `
  Remark: Blank line used to separate logical code sections.
- Line 17: `from secure_chat.config import DEFAULT_HOST, DEFAULT_PORT, DOWNLOAD_DIR, MAX_FILE_SIZE`
  Remark: Imports code that this file needs.
- Line 18: `from secure_chat.protocol import ChatProtocol, ProtocolError`
  Remark: Imports code that this file needs.
- Line 19: `from secure_chat.security import InputValidator, TLSContextFactory, ValidationError`
  Remark: Imports code that this file needs.
- Line 20: ` `
  Remark: Blank line used to separate logical code sections.
- Line 21: ` `
  Remark: Blank line used to separate logical code sections.
- Line 22: `class ChatClientConnection:`
  Remark: Defines an object-oriented class used by the project.
- Line 23: `    def __init__(self, host: str, port: int, verify_certificate: bool = False) -> None:`
  Remark: Defines a function or method.
- Line 24: `        self.host = host`
  Remark: Creates or updates a value used by the program.
- Line 25: `        self.port = port`
  Remark: Creates or updates a value used by the program.
- Line 26: `        self.verify_certificate = verify_certificate`
  Remark: Creates or updates a value used by the program.
- Line 27: `        self.socket: ssl.SSLSocket | None = None`
  Remark: Creates or updates a value used by the program.
- Line 28: `        self.incoming: "queue.Queue[dict[str, object]]" = queue.Queue()`
  Remark: Creates or updates a value used by the program.
- Line 29: `        self.running = False`
  Remark: Creates or updates a value used by the program.
- Line 30: ` `
  Remark: Blank line used to separate logical code sections.
- Line 31: `    def connect(self) -> None:`
  Remark: Defines a function or method.
- Line 32: `        raw_socket = socket.create_connection((self.host, self.port), timeout=10)`
  Remark: Creates or updates a value used by the program.
- Line 33: `        context = TLSContextFactory.client_context(self.verify_certificate)`
  Remark: Creates or updates a value used by the program.
- Line 34: `        self.socket = context.wrap_socket(raw_socket, server_hostname=self.host)`
  Remark: Creates or updates a value used by the program.
- Line 35: `        self.socket.settimeout(None)`
  Remark: Runs a program instruction for the current feature.
- Line 36: `        self.running = True`
  Remark: Creates or updates a value used by the program.
- Line 37: `        threading.Thread(target=self._listen, daemon=True).start()`
  Remark: Creates or updates a value used by the program.
- Line 38: ` `
  Remark: Blank line used to separate logical code sections.
- Line 39: `    def send(self, packet_type: str, **fields: object) -> None:`
  Remark: Defines a function or method.
- Line 40: `        if self.socket is None:`
  Remark: Checks a condition before choosing what to do.
- Line 41: `            raise ConnectionError("Not connected")`
  Remark: Raises an error when invalid behavior is detected.
- Line 42: `        ChatProtocol.send(self.socket, packet_type, **fields)`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 43: ` `
  Remark: Blank line used to separate logical code sections.
- Line 44: `    def close(self) -> None:`
  Remark: Defines a function or method.
- Line 45: `        self.running = False`
  Remark: Creates or updates a value used by the program.
- Line 46: `        if self.socket is not None:`
  Remark: Checks a condition before choosing what to do.
- Line 47: `            try:`
  Remark: Starts error-handling code.
- Line 48: `                self.send("logout")`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 49: `                self.socket.close()`
  Remark: Runs a program instruction for the current feature.
- Line 50: `            except OSError:`
  Remark: Handles an expected error so the program does not crash.
- Line 51: `                pass`
  Remark: Runs a program instruction for the current feature.
- Line 52: ` `
  Remark: Blank line used to separate logical code sections.
- Line 53: `    def _listen(self) -> None:`
  Remark: Defines a function or method.
- Line 54: `        assert self.socket is not None`
  Remark: Documents and checks an assumption in the code.
- Line 55: `        while self.running:`
  Remark: Repeats code while a condition remains true.
- Line 56: `            try:`
  Remark: Starts error-handling code.
- Line 57: `                packet = ChatProtocol.receive(self.socket)`
  Remark: Receives data from the network connection.
- Line 58: `                self.incoming.put(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 59: `            except (ConnectionError, OSError, ProtocolError) as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 60: `                self.incoming.put({"type": "connection_closed", "message": str(exc)})`
  Remark: Runs a program instruction for the current feature.
- Line 61: `                self.running = False`
  Remark: Creates or updates a value used by the program.
- Line 62: ` `
  Remark: Blank line used to separate logical code sections.
- Line 63: ` `
  Remark: Blank line used to separate logical code sections.
- Line 64: `class SecureChatApp(tk.Tk):`
  Remark: Defines an object-oriented class used by the project.
- Line 65: `    def __init__(self, connection: ChatClientConnection) -> None:`
  Remark: Defines a function or method.
- Line 66: `        super().__init__()`
  Remark: Runs a program instruction for the current feature.
- Line 67: `        self.connection = connection`
  Remark: Creates or updates a value used by the program.
- Line 68: `        self.title("SecureChat - Encrypted Multi-User Chat")`
  Remark: Runs a program instruction for the current feature.
- Line 69: `        self.geometry("980x640")`
  Remark: Runs a program instruction for the current feature.
- Line 70: `        self.minsize(900, 580)`
  Remark: Runs a program instruction for the current feature.
- Line 71: `        self.resizable(True, True)`
  Remark: Runs a program instruction for the current feature.
- Line 72: `        self.configure(bg="#111827")`
  Remark: Creates or updates a value used by the program.
- Line 73: `        self.logged_in = False`
  Remark: Creates or updates a value used by the program.
- Line 74: `        self.current_room = "general"`
  Remark: Creates or updates a value used by the program.
- Line 75: `        self.current_screen = "auth"`
  Remark: Creates or updates a value used by the program.
- Line 76: `        self.chat_images: list[ImageTk.PhotoImage] = []`
  Remark: Creates or updates a value used by the program.
- Line 77: `        self.chat_links: dict[str, Path] = {}`
  Remark: Creates or updates a value used by the program.
- Line 78: ` `
  Remark: Blank line used to separate logical code sections.
- Line 79: `        self._build_ui()`
  Remark: Runs a program instruction for the current feature.
- Line 80: `        self.protocol("WM_DELETE_WINDOW", self._on_close)`
  Remark: Runs a program instruction for the current feature.
- Line 81: `        self.after(100, self._poll_incoming)`
  Remark: Runs a program instruction for the current feature.
- Line 82: ` `
  Remark: Blank line used to separate logical code sections.
- Line 83: `    def _build_ui(self) -> None:`
  Remark: Defines a function or method.
- Line 84: `        self.username_var = tk.StringVar()`
  Remark: Creates or updates a value used by the program.
- Line 85: `        self.password_var = tk.StringVar()`
  Remark: Creates or updates a value used by the program.
- Line 86: `        self.room_var = tk.StringVar(value="general")`
  Remark: Creates or updates a value used by the program.
- Line 87: `        self.new_room_var = tk.StringVar()`
  Remark: Creates or updates a value used by the program.
- Line 88: `        self.message_var = tk.StringVar()`
  Remark: Creates or updates a value used by the program.
- Line 89: `        self.auth_status_var = tk.StringVar(value="Connected. Register or login to continue.")`
  Remark: Creates or updates a value used by the program.
- Line 90: `        self.chat_status_var = tk.StringVar(value="")`
  Remark: Creates or updates a value used by the program.
- Line 91: `        self.login_badge_var = tk.StringVar(value="")`
  Remark: Creates or updates a value used by the program.
- Line 92: ` `
  Remark: Blank line used to separate logical code sections.
- Line 93: `        self._build_auth_screen()`
  Remark: Runs a program instruction for the current feature.
- Line 94: `        self._build_chat_screen()`
  Remark: Runs a program instruction for the current feature.
- Line 95: `        self._show_auth_screen()`
  Remark: Runs a program instruction for the current feature.
- Line 96: ` `
  Remark: Blank line used to separate logical code sections.
- Line 97: `    def _build_auth_screen(self) -> None:`
  Remark: Defines a function or method.
- Line 98: `        self.auth_frame = tk.Frame(self, bg="#111827")`
  Remark: Creates or updates a value used by the program.
- Line 99: ` `
  Remark: Blank line used to separate logical code sections.
- Line 100: `        card = tk.Frame(self.auth_frame, bg="#f8fafc", padx=34, pady=30)`
  Remark: Creates or updates a value used by the program.
- Line 101: `        card.place(relx=0.5, rely=0.5, anchor=tk.CENTER)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 102: ` `
  Remark: Blank line used to separate logical code sections.
- Line 103: `        tk.Label(`
  Remark: Runs a program instruction for the current feature.
- Line 104: `            card,`
  Remark: Runs a program instruction for the current feature.
- Line 105: `            text="SecureChat",`
  Remark: Creates or updates a value used by the program.
- Line 106: `            bg="#f8fafc",`
  Remark: Creates or updates a value used by the program.
- Line 107: `            fg="#2563eb",`
  Remark: Creates or updates a value used by the program.
- Line 108: `            font=("Segoe UI", 30, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 109: `        ).grid(row=0, column=0, columnspan=2, pady=(0, 6))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 110: `        tk.Label(`
  Remark: Runs a program instruction for the current feature.
- Line 111: `            card,`
  Remark: Runs a program instruction for the current feature.
- Line 112: `            text="Encrypted multi-user chat",`
  Remark: Creates or updates a value used by the program.
- Line 113: `            bg="#f8fafc",`
  Remark: Creates or updates a value used by the program.
- Line 114: `            fg="#475569",`
  Remark: Creates or updates a value used by the program.
- Line 115: `            font=("Segoe UI", 12),`
  Remark: Creates or updates a value used by the program.
- Line 116: `        ).grid(row=1, column=0, columnspan=2, pady=(0, 24))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 117: ` `
  Remark: Blank line used to separate logical code sections.
- Line 118: `        tk.Label(card, text="Username", bg="#f8fafc", fg="#0f172a", font=("Segoe UI", 11, "bold")).grid(`
  Remark: Places a visual widget on the Tkinter screen.
- Line 119: `            row=2, column=0, sticky="w"`
  Remark: Creates or updates a value used by the program.
- Line 120: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 121: `        tk.Entry(`
  Remark: Runs a program instruction for the current feature.
- Line 122: `            card,`
  Remark: Runs a program instruction for the current feature.
- Line 123: `            textvariable=self.username_var,`
  Remark: Creates or updates a value used by the program.
- Line 124: `            width=30,`
  Remark: Creates or updates a value used by the program.
- Line 125: `            font=("Segoe UI", 12),`
  Remark: Creates or updates a value used by the program.
- Line 126: `            bg="#e0f2fe",`
  Remark: Creates or updates a value used by the program.
- Line 127: `            fg="#0f172a",`
  Remark: Creates or updates a value used by the program.
- Line 128: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 129: `        ).grid(row=3, column=0, columnspan=2, sticky="ew", pady=(4, 14), ipady=8)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 130: ` `
  Remark: Blank line used to separate logical code sections.
- Line 131: `        tk.Label(card, text="Password", bg="#f8fafc", fg="#0f172a", font=("Segoe UI", 11, "bold")).grid(`
  Remark: Places a visual widget on the Tkinter screen.
- Line 132: `            row=4, column=0, sticky="w"`
  Remark: Creates or updates a value used by the program.
- Line 133: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 134: `        password_entry = tk.Entry(`
  Remark: Creates or updates a value used by the program.
- Line 135: `            card,`
  Remark: Runs a program instruction for the current feature.
- Line 136: `            textvariable=self.password_var,`
  Remark: Creates or updates a value used by the program.
- Line 137: `            show="*",`
  Remark: Creates or updates a value used by the program.
- Line 138: `            width=30,`
  Remark: Creates or updates a value used by the program.
- Line 139: `            font=("Segoe UI", 12),`
  Remark: Creates or updates a value used by the program.
- Line 140: `            bg="#fef3c7",`
  Remark: Creates or updates a value used by the program.
- Line 141: `            fg="#0f172a",`
  Remark: Creates or updates a value used by the program.
- Line 142: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 143: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 144: `        password_entry.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(4, 18), ipady=8)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 145: `        password_entry.bind("<Return>", lambda _event: self._login())`
  Remark: Runs a program instruction for the current feature.
- Line 146: ` `
  Remark: Blank line used to separate logical code sections.
- Line 147: `        tk.Button(`
  Remark: Runs a program instruction for the current feature.
- Line 148: `            card,`
  Remark: Runs a program instruction for the current feature.
- Line 149: `            text="Register",`
  Remark: Creates or updates a value used by the program.
- Line 150: `            command=self._register_user,`
  Remark: Creates or updates a value used by the program.
- Line 151: `            bg="#22c55e",`
  Remark: Creates or updates a value used by the program.
- Line 152: `            fg="white",`
  Remark: Creates or updates a value used by the program.
- Line 153: `            activebackground="#16a34a",`
  Remark: Creates or updates a value used by the program.
- Line 154: `            font=("Segoe UI", 11, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 155: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 156: `            padx=16,`
  Remark: Creates or updates a value used by the program.
- Line 157: `            pady=8,`
  Remark: Creates or updates a value used by the program.
- Line 158: `        ).grid(row=6, column=0, sticky="ew", padx=(0, 8))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 159: `        tk.Button(`
  Remark: Runs a program instruction for the current feature.
- Line 160: `            card,`
  Remark: Runs a program instruction for the current feature.
- Line 161: `            text="Login",`
  Remark: Creates or updates a value used by the program.
- Line 162: `            command=self._login,`
  Remark: Creates or updates a value used by the program.
- Line 163: `            bg="#3b82f6",`
  Remark: Creates or updates a value used by the program.
- Line 164: `            fg="white",`
  Remark: Creates or updates a value used by the program.
- Line 165: `            activebackground="#2563eb",`
  Remark: Creates or updates a value used by the program.
- Line 166: `            font=("Segoe UI", 11, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 167: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 168: `            padx=16,`
  Remark: Creates or updates a value used by the program.
- Line 169: `            pady=8,`
  Remark: Creates or updates a value used by the program.
- Line 170: `        ).grid(row=6, column=1, sticky="ew", padx=(8, 0))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 171: ` `
  Remark: Blank line used to separate logical code sections.
- Line 172: `        self.auth_status_label = tk.Label(`
  Remark: Creates or updates a value used by the program.
- Line 173: `            card,`
  Remark: Runs a program instruction for the current feature.
- Line 174: `            textvariable=self.auth_status_var,`
  Remark: Creates or updates a value used by the program.
- Line 175: `            bg="#dbeafe",`
  Remark: Creates or updates a value used by the program.
- Line 176: `            fg="#2563eb",`
  Remark: Creates or updates a value used by the program.
- Line 177: `            wraplength=360,`
  Remark: Creates or updates a value used by the program.
- Line 178: `            font=("Segoe UI", 12, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 179: `            padx=10,`
  Remark: Creates or updates a value used by the program.
- Line 180: `            pady=8,`
  Remark: Creates or updates a value used by the program.
- Line 181: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 182: `        self.auth_status_label.grid(row=7, column=0, columnspan=2, pady=(18, 0))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 183: ` `
  Remark: Blank line used to separate logical code sections.
- Line 184: `    def _build_chat_screen(self) -> None:`
  Remark: Defines a function or method.
- Line 185: `        self.chat_frame = tk.Frame(self, bg="#dbeafe")`
  Remark: Creates or updates a value used by the program.
- Line 186: `        self.chat_frame.columnconfigure(1, weight=1)`
  Remark: Creates or updates a value used by the program.
- Line 187: `        self.chat_frame.rowconfigure(1, weight=1)`
  Remark: Creates or updates a value used by the program.
- Line 188: ` `
  Remark: Blank line used to separate logical code sections.
- Line 189: `        header = tk.Frame(self.chat_frame, bg="#1d4ed8", padx=14, pady=12)`
  Remark: Creates or updates a value used by the program.
- Line 190: `        header.grid(row=0, column=0, columnspan=3, sticky="ew")`
  Remark: Places a visual widget on the Tkinter screen.
- Line 191: `        header.columnconfigure(1, weight=1)`
  Remark: Creates or updates a value used by the program.
- Line 192: ` `
  Remark: Blank line used to separate logical code sections.
- Line 193: `        tk.Label(`
  Remark: Runs a program instruction for the current feature.
- Line 194: `            header,`
  Remark: Runs a program instruction for the current feature.
- Line 195: `            text="SecureChat",`
  Remark: Creates or updates a value used by the program.
- Line 196: `            bg="#1d4ed8",`
  Remark: Creates or updates a value used by the program.
- Line 197: `            fg="white",`
  Remark: Creates or updates a value used by the program.
- Line 198: `            font=("Segoe UI", 20, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 199: `        ).grid(row=0, column=0, sticky="w")`
  Remark: Places a visual widget on the Tkinter screen.
- Line 200: `        tk.Label(`
  Remark: Runs a program instruction for the current feature.
- Line 201: `            header,`
  Remark: Runs a program instruction for the current feature.
- Line 202: `            textvariable=self.login_badge_var,`
  Remark: Creates or updates a value used by the program.
- Line 203: `            bg="#1d4ed8",`
  Remark: Creates or updates a value used by the program.
- Line 204: `            fg="#bbf7d0",`
  Remark: Creates or updates a value used by the program.
- Line 205: `            font=("Segoe UI", 12, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 206: `        ).grid(row=0, column=1, sticky="e")`
  Remark: Places a visual widget on the Tkinter screen.
- Line 207: ` `
  Remark: Blank line used to separate logical code sections.
- Line 208: `        rooms_panel = tk.Frame(self.chat_frame, bg="#eff6ff", padx=10, pady=10)`
  Remark: Creates or updates a value used by the program.
- Line 209: `        rooms_panel.grid(row=1, column=0, sticky="nsw", padx=(10, 5), pady=10)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 210: `        rooms_panel.rowconfigure(1, weight=1)`
  Remark: Creates or updates a value used by the program.
- Line 211: ` `
  Remark: Blank line used to separate logical code sections.
- Line 212: `        tk.Label(rooms_panel, text="Rooms", bg="#eff6ff", fg="#1e3a8a", font=("Segoe UI", 14, "bold")).grid(`
  Remark: Places a visual widget on the Tkinter screen.
- Line 213: `            row=0, column=0, columnspan=2, sticky="w", pady=(0, 8)`
  Remark: Creates or updates a value used by the program.
- Line 214: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 215: `        self.rooms_box = tk.Listbox(`
  Remark: Creates or updates a value used by the program.
- Line 216: `            rooms_panel,`
  Remark: Runs a program instruction for the current feature.
- Line 217: `            width=22,`
  Remark: Creates or updates a value used by the program.
- Line 218: `            height=18,`
  Remark: Creates or updates a value used by the program.
- Line 219: `            bg="#ffffff",`
  Remark: Creates or updates a value used by the program.
- Line 220: `            fg="#0f172a",`
  Remark: Creates or updates a value used by the program.
- Line 221: `            selectbackground="#3b82f6",`
  Remark: Creates or updates a value used by the program.
- Line 222: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 223: `            font=("Segoe UI", 10),`
  Remark: Creates or updates a value used by the program.
- Line 224: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 225: `        self.rooms_box.grid(row=1, column=0, columnspan=2, sticky="nsew")`
  Remark: Places a visual widget on the Tkinter screen.
- Line 226: `        self.rooms_box.bind("<<ListboxSelect>>", self._on_room_select)`
  Remark: Runs a program instruction for the current feature.
- Line 227: ` `
  Remark: Blank line used to separate logical code sections.
- Line 228: `        tk.Button(`
  Remark: Runs a program instruction for the current feature.
- Line 229: `            rooms_panel,`
  Remark: Runs a program instruction for the current feature.
- Line 230: `            text="Join Selected",`
  Remark: Creates or updates a value used by the program.
- Line 231: `            command=self._join_room,`
  Remark: Creates or updates a value used by the program.
- Line 232: `            bg="#8b5cf6",`
  Remark: Creates or updates a value used by the program.
- Line 233: `            fg="white",`
  Remark: Creates or updates a value used by the program.
- Line 234: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 235: `            font=("Segoe UI", 10, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 236: `        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(8, 12))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 237: ` `
  Remark: Blank line used to separate logical code sections.
- Line 238: `        tk.Entry(`
  Remark: Runs a program instruction for the current feature.
- Line 239: `            rooms_panel,`
  Remark: Runs a program instruction for the current feature.
- Line 240: `            textvariable=self.new_room_var,`
  Remark: Creates or updates a value used by the program.
- Line 241: `            bg="#fef3c7",`
  Remark: Creates or updates a value used by the program.
- Line 242: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 243: `            font=("Segoe UI", 10),`
  Remark: Creates or updates a value used by the program.
- Line 244: `        ).grid(row=3, column=0, columnspan=2, sticky="ew", ipady=6)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 245: `        tk.Button(`
  Remark: Runs a program instruction for the current feature.
- Line 246: `            rooms_panel,`
  Remark: Runs a program instruction for the current feature.
- Line 247: `            text="Create Room",`
  Remark: Creates or updates a value used by the program.
- Line 248: `            command=self._create_room,`
  Remark: Creates or updates a value used by the program.
- Line 249: `            bg="#f97316",`
  Remark: Creates or updates a value used by the program.
- Line 250: `            fg="white",`
  Remark: Creates or updates a value used by the program.
- Line 251: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 252: `            font=("Segoe UI", 10, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 253: `        ).grid(row=4, column=0, columnspan=2, sticky="ew", pady=(8, 8))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 254: `        tk.Button(`
  Remark: Runs a program instruction for the current feature.
- Line 255: `            rooms_panel,`
  Remark: Runs a program instruction for the current feature.
- Line 256: `            text="Refresh Rooms",`
  Remark: Creates or updates a value used by the program.
- Line 257: `            command=self._request_rooms,`
  Remark: Creates or updates a value used by the program.
- Line 258: `            bg="#06b6d4",`
  Remark: Creates or updates a value used by the program.
- Line 259: `            fg="white",`
  Remark: Creates or updates a value used by the program.
- Line 260: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 261: `            font=("Segoe UI", 10, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 262: `        ).grid(row=5, column=0, columnspan=2, sticky="ew")`
  Remark: Places a visual widget on the Tkinter screen.
- Line 263: ` `
  Remark: Blank line used to separate logical code sections.
- Line 264: `        chat_panel = tk.Frame(self.chat_frame, bg="#dbeafe", padx=5, pady=10)`
  Remark: Creates or updates a value used by the program.
- Line 265: `        chat_panel.grid(row=1, column=1, sticky="nsew", pady=10)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 266: `        chat_panel.rowconfigure(1, weight=1)`
  Remark: Creates or updates a value used by the program.
- Line 267: `        chat_panel.columnconfigure(0, weight=1)`
  Remark: Creates or updates a value used by the program.
- Line 268: ` `
  Remark: Blank line used to separate logical code sections.
- Line 269: `        self.room_title_var = tk.StringVar(value="Room: general")`
  Remark: Creates or updates a value used by the program.
- Line 270: `        tk.Label(`
  Remark: Runs a program instruction for the current feature.
- Line 271: `            chat_panel,`
  Remark: Runs a program instruction for the current feature.
- Line 272: `            textvariable=self.room_title_var,`
  Remark: Creates or updates a value used by the program.
- Line 273: `            bg="#dbeafe",`
  Remark: Creates or updates a value used by the program.
- Line 274: `            fg="#1e3a8a",`
  Remark: Creates or updates a value used by the program.
- Line 275: `            font=("Segoe UI", 14, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 276: `        ).grid(row=0, column=0, sticky="w", pady=(0, 8))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 277: ` `
  Remark: Blank line used to separate logical code sections.
- Line 278: `        self.chat_box = scrolledtext.ScrolledText(`
  Remark: Creates or updates a value used by the program.
- Line 279: `            chat_panel,`
  Remark: Runs a program instruction for the current feature.
- Line 280: `            state=tk.DISABLED,`
  Remark: Creates or updates a value used by the program.
- Line 281: `            wrap=tk.WORD,`
  Remark: Creates or updates a value used by the program.
- Line 282: `            bg="#ffffff",`
  Remark: Creates or updates a value used by the program.
- Line 283: `            fg="#0f172a",`
  Remark: Creates or updates a value used by the program.
- Line 284: `            insertbackground="#0f172a",`
  Remark: Creates or updates a value used by the program.
- Line 285: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 286: `            font=("Consolas", 10),`
  Remark: Creates or updates a value used by the program.
- Line 287: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 288: `        self.chat_box.grid(row=1, column=0, sticky="nsew")`
  Remark: Places a visual widget on the Tkinter screen.
- Line 289: ` `
  Remark: Blank line used to separate logical code sections.
- Line 290: `        send_frame = tk.Frame(chat_panel, bg="#dbeafe")`
  Remark: Creates or updates a value used by the program.
- Line 291: `        send_frame.grid(row=2, column=0, sticky="ew", pady=(10, 0))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 292: `        send_frame.columnconfigure(0, weight=1)`
  Remark: Creates or updates a value used by the program.
- Line 293: `        message_entry = tk.Entry(send_frame, textvariable=self.message_var, bg="#ffffff", relief=tk.FLAT, font=("Segoe UI", 11))`
  Remark: Creates or updates a value used by the program.
- Line 294: `        message_entry.grid(row=0, column=0, sticky="ew", ipady=8, padx=(0, 8))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 295: `        message_entry.bind("<Return>", lambda _event: self._send_message())`
  Remark: Runs a program instruction for the current feature.
- Line 296: `        tk.Button(`
  Remark: Runs a program instruction for the current feature.
- Line 297: `            send_frame,`
  Remark: Runs a program instruction for the current feature.
- Line 298: `            text="Send",`
  Remark: Creates or updates a value used by the program.
- Line 299: `            command=self._send_message,`
  Remark: Creates or updates a value used by the program.
- Line 300: `            bg="#22c55e",`
  Remark: Creates or updates a value used by the program.
- Line 301: `            fg="white",`
  Remark: Creates or updates a value used by the program.
- Line 302: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 303: `            font=("Segoe UI", 11, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 304: `            padx=20,`
  Remark: Creates or updates a value used by the program.
- Line 305: `        ).grid(row=0, column=1)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 306: ` `
  Remark: Blank line used to separate logical code sections.
- Line 307: `        media_frame = tk.Frame(chat_panel, bg="#dbeafe")`
  Remark: Creates or updates a value used by the program.
- Line 308: `        media_frame.grid(row=3, column=0, sticky="ew", pady=(8, 0))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 309: `        for emoji in ["😀", "😂", "❤️", "👍", "🔥", "🎉"]:`
  Remark: Loops over multiple values.
- Line 310: `            tk.Button(`
  Remark: Runs a program instruction for the current feature.
- Line 311: `                media_frame,`
  Remark: Runs a program instruction for the current feature.
- Line 312: `                text=emoji,`
  Remark: Creates or updates a value used by the program.
- Line 313: `                command=lambda value=emoji: self._insert_emoji(value),`
  Remark: Creates or updates a value used by the program.
- Line 314: `                bg="#fef3c7",`
  Remark: Creates or updates a value used by the program.
- Line 315: `                relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 316: `                font=("Segoe UI Emoji", 12),`
  Remark: Creates or updates a value used by the program.
- Line 317: `                width=3,`
  Remark: Creates or updates a value used by the program.
- Line 318: `            ).pack(side=tk.LEFT, padx=(0, 5))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 319: ` `
  Remark: Blank line used to separate logical code sections.
- Line 320: `        tk.Button(`
  Remark: Runs a program instruction for the current feature.
- Line 321: `            media_frame,`
  Remark: Runs a program instruction for the current feature.
- Line 322: `            text="Send File",`
  Remark: Creates or updates a value used by the program.
- Line 323: `            command=lambda: self._send_file("file"),`
  Remark: Creates or updates a value used by the program.
- Line 324: `            bg="#64748b",`
  Remark: Creates or updates a value used by the program.
- Line 325: `            fg="white",`
  Remark: Creates or updates a value used by the program.
- Line 326: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 327: `            font=("Segoe UI", 10, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 328: `            padx=10,`
  Remark: Creates or updates a value used by the program.
- Line 329: `        ).pack(side=tk.LEFT, padx=(12, 5))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 330: `        tk.Button(`
  Remark: Runs a program instruction for the current feature.
- Line 331: `            media_frame,`
  Remark: Runs a program instruction for the current feature.
- Line 332: `            text="Send Image",`
  Remark: Creates or updates a value used by the program.
- Line 333: `            command=lambda: self._send_file("image"),`
  Remark: Creates or updates a value used by the program.
- Line 334: `            bg="#ec4899",`
  Remark: Creates or updates a value used by the program.
- Line 335: `            fg="white",`
  Remark: Creates or updates a value used by the program.
- Line 336: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 337: `            font=("Segoe UI", 10, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 338: `            padx=10,`
  Remark: Creates or updates a value used by the program.
- Line 339: `        ).pack(side=tk.LEFT, padx=5)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 340: `        tk.Button(`
  Remark: Runs a program instruction for the current feature.
- Line 341: `            media_frame,`
  Remark: Runs a program instruction for the current feature.
- Line 342: `            text="Send Video",`
  Remark: Creates or updates a value used by the program.
- Line 343: `            command=lambda: self._send_file("video"),`
  Remark: Creates or updates a value used by the program.
- Line 344: `            bg="#7c3aed",`
  Remark: Creates or updates a value used by the program.
- Line 345: `            fg="white",`
  Remark: Creates or updates a value used by the program.
- Line 346: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 347: `            font=("Segoe UI", 10, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 348: `            padx=10,`
  Remark: Creates or updates a value used by the program.
- Line 349: `        ).pack(side=tk.LEFT, padx=5)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 350: ` `
  Remark: Blank line used to separate logical code sections.
- Line 351: `        users_panel = tk.Frame(self.chat_frame, bg="#ecfdf5", padx=10, pady=10)`
  Remark: Creates or updates a value used by the program.
- Line 352: `        users_panel.grid(row=1, column=2, sticky="nse", padx=(5, 10), pady=10)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 353: `        users_panel.rowconfigure(1, weight=1)`
  Remark: Creates or updates a value used by the program.
- Line 354: `        tk.Label(users_panel, text="Online Users", bg="#ecfdf5", fg="#166534", font=("Segoe UI", 14, "bold")).grid(`
  Remark: Places a visual widget on the Tkinter screen.
- Line 355: `            row=0, column=0, sticky="w", pady=(0, 8)`
  Remark: Creates or updates a value used by the program.
- Line 356: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 357: `        self.users_box = tk.Listbox(`
  Remark: Creates or updates a value used by the program.
- Line 358: `            users_panel,`
  Remark: Runs a program instruction for the current feature.
- Line 359: `            width=24,`
  Remark: Creates or updates a value used by the program.
- Line 360: `            height=18,`
  Remark: Creates or updates a value used by the program.
- Line 361: `            bg="#ffffff",`
  Remark: Creates or updates a value used by the program.
- Line 362: `            fg="#0f172a",`
  Remark: Creates or updates a value used by the program.
- Line 363: `            selectbackground="#22c55e",`
  Remark: Creates or updates a value used by the program.
- Line 364: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 365: `            font=("Segoe UI", 10),`
  Remark: Creates or updates a value used by the program.
- Line 366: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 367: `        self.users_box.grid(row=1, column=0, sticky="nsew")`
  Remark: Places a visual widget on the Tkinter screen.
- Line 368: `        tk.Button(`
  Remark: Runs a program instruction for the current feature.
- Line 369: `            users_panel,`
  Remark: Runs a program instruction for the current feature.
- Line 370: `            text="Refresh Users",`
  Remark: Creates or updates a value used by the program.
- Line 371: `            command=self._request_users,`
  Remark: Creates or updates a value used by the program.
- Line 372: `            bg="#16a34a",`
  Remark: Creates or updates a value used by the program.
- Line 373: `            fg="white",`
  Remark: Creates or updates a value used by the program.
- Line 374: `            relief=tk.FLAT,`
  Remark: Creates or updates a value used by the program.
- Line 375: `            font=("Segoe UI", 10, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 376: `        ).grid(row=2, column=0, sticky="ew", pady=(8, 0))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 377: ` `
  Remark: Blank line used to separate logical code sections.
- Line 378: `        self.chat_status_label = tk.Label(`
  Remark: Creates or updates a value used by the program.
- Line 379: `            self.chat_frame,`
  Remark: Runs a program instruction for the current feature.
- Line 380: `            textvariable=self.chat_status_var,`
  Remark: Creates or updates a value used by the program.
- Line 381: `            bg="#dbeafe",`
  Remark: Creates or updates a value used by the program.
- Line 382: `            fg="#1d4ed8",`
  Remark: Creates or updates a value used by the program.
- Line 383: `            font=("Segoe UI", 10, "bold"),`
  Remark: Creates or updates a value used by the program.
- Line 384: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 385: `        self.chat_status_label.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=(0, 8))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 386: ` `
  Remark: Blank line used to separate logical code sections.
- Line 387: `    def _show_auth_screen(self) -> None:`
  Remark: Defines a function or method.
- Line 388: `        self.current_screen = "auth"`
  Remark: Creates or updates a value used by the program.
- Line 389: `        self.chat_frame.pack_forget()`
  Remark: Runs a program instruction for the current feature.
- Line 390: `        self.auth_frame.pack(fill=tk.BOTH, expand=True)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 391: ` `
  Remark: Blank line used to separate logical code sections.
- Line 392: `    def _show_chat_screen(self) -> None:`
  Remark: Defines a function or method.
- Line 393: `        self.current_screen = "chat"`
  Remark: Creates or updates a value used by the program.
- Line 394: `        self.auth_frame.pack_forget()`
  Remark: Runs a program instruction for the current feature.
- Line 395: `        self.chat_frame.pack(fill=tk.BOTH, expand=True)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 396: ` `
  Remark: Blank line used to separate logical code sections.
- Line 397: `    def _register_user(self) -> None:`
  Remark: Defines a function or method.
- Line 398: `        self._send_auth_packet("register")`
  Remark: Runs a program instruction for the current feature.
- Line 399: ` `
  Remark: Blank line used to separate logical code sections.
- Line 400: `    def _login(self) -> None:`
  Remark: Defines a function or method.
- Line 401: `        self._send_auth_packet("login")`
  Remark: Runs a program instruction for the current feature.
- Line 402: ` `
  Remark: Blank line used to separate logical code sections.
- Line 403: `    def _send_auth_packet(self, packet_type: str) -> None:`
  Remark: Defines a function or method.
- Line 404: `        try:`
  Remark: Starts error-handling code.
- Line 405: `            username = InputValidator.username(self.username_var.get())`
  Remark: Creates or updates a value used by the program.
- Line 406: `            password = InputValidator.password(self.password_var.get())`
  Remark: Creates or updates a value used by the program.
- Line 407: `            self.connection.send(`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 408: `                packet_type,`
  Remark: Runs a program instruction for the current feature.
- Line 409: `                username=username,`
  Remark: Creates or updates a value used by the program.
- Line 410: `                password=password,`
  Remark: Creates or updates a value used by the program.
- Line 411: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 412: `        except ValidationError as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 413: `            self._set_auth_status(str(exc), ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 414: `            messagebox.showerror("Invalid details", str(exc))`
  Remark: Runs a program instruction for the current feature.
- Line 415: `        except Exception as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 416: `            self._set_auth_status(f"Connection error: {exc}", ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 417: ` `
  Remark: Blank line used to separate logical code sections.
- Line 418: `    def _join_room(self) -> None:`
  Remark: Defines a function or method.
- Line 419: `        if not self.logged_in:`
  Remark: Checks a condition before choosing what to do.
- Line 420: `            self._set_chat_status("Please login first.", ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 421: `            return`
  Remark: Returns a result to the caller.
- Line 422: `        room = self.room_var.get().strip()`
  Remark: Creates or updates a value used by the program.
- Line 423: `        if not room:`
  Remark: Checks a condition before choosing what to do.
- Line 424: `            self._set_chat_status("Choose a room first.", ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 425: `            return`
  Remark: Returns a result to the caller.
- Line 426: `        self.connection.send("join", room=room)`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 427: ` `
  Remark: Blank line used to separate logical code sections.
- Line 428: `    def _create_room(self) -> None:`
  Remark: Defines a function or method.
- Line 429: `        if not self.logged_in:`
  Remark: Checks a condition before choosing what to do.
- Line 430: `            self._set_chat_status("Please login first.", ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 431: `            return`
  Remark: Returns a result to the caller.
- Line 432: `        room = self.new_room_var.get().strip()`
  Remark: Creates or updates a value used by the program.
- Line 433: `        if not room:`
  Remark: Checks a condition before choosing what to do.
- Line 434: `            self._set_chat_status("Write a room name to create.", ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 435: `            return`
  Remark: Returns a result to the caller.
- Line 436: `        self.connection.send("create_room", room=room)`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 437: ` `
  Remark: Blank line used to separate logical code sections.
- Line 438: `    def _request_users(self) -> None:`
  Remark: Defines a function or method.
- Line 439: `        if self.logged_in:`
  Remark: Checks a condition before choosing what to do.
- Line 440: `            self.connection.send("users")`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 441: ` `
  Remark: Blank line used to separate logical code sections.
- Line 442: `    def _request_rooms(self) -> None:`
  Remark: Defines a function or method.
- Line 443: `        if self.logged_in:`
  Remark: Checks a condition before choosing what to do.
- Line 444: `            self.connection.send("rooms")`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 445: ` `
  Remark: Blank line used to separate logical code sections.
- Line 446: `    def _send_message(self) -> None:`
  Remark: Defines a function or method.
- Line 447: `        if not self.logged_in:`
  Remark: Checks a condition before choosing what to do.
- Line 448: `            self._set_chat_status("Please login first.", ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 449: `            return`
  Remark: Returns a result to the caller.
- Line 450: ` `
  Remark: Blank line used to separate logical code sections.
- Line 451: `        body = self.message_var.get()`
  Remark: Creates or updates a value used by the program.
- Line 452: `        if not body.strip():`
  Remark: Checks a condition before choosing what to do.
- Line 453: `            return`
  Remark: Returns a result to the caller.
- Line 454: ` `
  Remark: Blank line used to separate logical code sections.
- Line 455: `        try:`
  Remark: Starts error-handling code.
- Line 456: `            self.connection.send("message", body=body)`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 457: `            self.message_var.set("")`
  Remark: Runs a program instruction for the current feature.
- Line 458: `        except Exception as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 459: `            self._set_chat_status(f"Send failed: {exc}", ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 460: ` `
  Remark: Blank line used to separate logical code sections.
- Line 461: `    def _insert_emoji(self, emoji: str) -> None:`
  Remark: Defines a function or method.
- Line 462: `        self.message_var.set(self.message_var.get() + emoji)`
  Remark: Runs a program instruction for the current feature.
- Line 463: ` `
  Remark: Blank line used to separate logical code sections.
- Line 464: `    def _send_file(self, kind: str) -> None:`
  Remark: Defines a function or method.
- Line 465: `        if not self.logged_in:`
  Remark: Checks a condition before choosing what to do.
- Line 466: `            self._set_chat_status("Please login first.", ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 467: `            return`
  Remark: Returns a result to the caller.
- Line 468: ` `
  Remark: Blank line used to separate logical code sections.
- Line 469: `        filters = {`
  Remark: Creates or updates a value used by the program.
- Line 470: `            "file": [("All files", "*.*")],`
  Remark: Runs a program instruction for the current feature.
- Line 471: `            "image": [("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"), ("All files", "*.*")],`
  Remark: Runs a program instruction for the current feature.
- Line 472: `            "video": [("Video files", "*.mp4 *.mov *.avi *.mkv *.webm"), ("All files", "*.*")],`
  Remark: Runs a program instruction for the current feature.
- Line 473: `        }`
  Remark: Runs a program instruction for the current feature.
- Line 474: `        selected_path = filedialog.askopenfilename(filetypes=filters.get(kind, filters["file"]))`
  Remark: Creates or updates a value used by the program.
- Line 475: `        if not selected_path:`
  Remark: Checks a condition before choosing what to do.
- Line 476: `            return`
  Remark: Returns a result to the caller.
- Line 477: ` `
  Remark: Blank line used to separate logical code sections.
- Line 478: `        path = Path(selected_path)`
  Remark: Creates or updates a value used by the program.
- Line 479: `        if path.stat().st_size > MAX_FILE_SIZE:`
  Remark: Checks a condition before choosing what to do.
- Line 480: `            self._set_chat_status(`
  Remark: Runs a program instruction for the current feature.
- Line 481: `                f"File is too large. Maximum size is {MAX_FILE_SIZE // (1024 * 1024)} MB.",`
  Remark: Runs a program instruction for the current feature.
- Line 482: `                ok=False,`
  Remark: Creates or updates a value used by the program.
- Line 483: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 484: `            return`
  Remark: Returns a result to the caller.
- Line 485: ` `
  Remark: Blank line used to separate logical code sections.
- Line 486: `        try:`
  Remark: Starts error-handling code.
- Line 487: `            filename = InputValidator.filename(path.name)`
  Remark: Creates or updates a value used by the program.
- Line 488: `            encoded_data = base64.b64encode(path.read_bytes()).decode("ascii")`
  Remark: Creates or updates a value used by the program.
- Line 489: `            mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"`
  Remark: Creates or updates a value used by the program.
- Line 490: `            self.connection.send(`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 491: `                "file",`
  Remark: Runs a program instruction for the current feature.
- Line 492: `                filename=filename,`
  Remark: Creates or updates a value used by the program.
- Line 493: `                kind=kind,`
  Remark: Creates or updates a value used by the program.
- Line 494: `                mime_type=mime_type,`
  Remark: Creates or updates a value used by the program.
- Line 495: `                data=encoded_data,`
  Remark: Creates or updates a value used by the program.
- Line 496: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 497: `            self._set_chat_status(f"Sending {kind}: {filename}", ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 498: `        except Exception as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 499: `            self._set_chat_status(f"Could not send {kind}: {exc}", ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 500: ` `
  Remark: Blank line used to separate logical code sections.
- Line 501: `    def _poll_incoming(self) -> None:`
  Remark: Defines a function or method.
- Line 502: `        while not self.connection.incoming.empty():`
  Remark: Repeats code while a condition remains true.
- Line 503: `            packet = self.connection.incoming.get_nowait()`
  Remark: Creates or updates a value used by the program.
- Line 504: `            self._handle_packet(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 505: `        self.after(100, self._poll_incoming)`
  Remark: Runs a program instruction for the current feature.
- Line 506: ` `
  Remark: Blank line used to separate logical code sections.
- Line 507: `    def _handle_packet(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 508: `        packet_type = packet.get("type")`
  Remark: Creates or updates a value used by the program.
- Line 509: ` `
  Remark: Blank line used to separate logical code sections.
- Line 510: `        if packet_type == "welcome":`
  Remark: Checks a condition before choosing what to do.
- Line 511: `            self._set_auth_status(str(packet.get("message", "Connected")), ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 512: `        elif packet_type == "ok":`
  Remark: Checks another condition when the previous condition was false.
- Line 513: `            self._handle_ok(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 514: `        elif packet_type == "error":`
  Remark: Checks another condition when the previous condition was false.
- Line 515: `            self._handle_error(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 516: `        elif packet_type == "history":`
  Remark: Checks another condition when the previous condition was false.
- Line 517: `            self._show_history(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 518: `        elif packet_type == "message":`
  Remark: Checks another condition when the previous condition was false.
- Line 519: `            self._append_chat(`
  Remark: Runs a program instruction for the current feature.
- Line 520: `                f"[{packet.get('created_at')}] {packet.get('sender')}: {packet.get('body')}"`
  Remark: Runs a program instruction for the current feature.
- Line 521: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 522: `        elif packet_type == "file":`
  Remark: Checks another condition when the previous condition was false.
- Line 523: `            self._handle_file_packet(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 524: `        elif packet_type == "system":`
  Remark: Checks another condition when the previous condition was false.
- Line 525: `            self._append_chat(f"* {packet.get('message')}")`
  Remark: Runs a program instruction for the current feature.
- Line 526: `        elif packet_type == "users":`
  Remark: Checks another condition when the previous condition was false.
- Line 527: `            self._show_users(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 528: `        elif packet_type == "rooms":`
  Remark: Checks another condition when the previous condition was false.
- Line 529: `            self._show_rooms(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 530: `        elif packet_type == "connection_closed":`
  Remark: Checks another condition when the previous condition was false.
- Line 531: `            message = f"Disconnected: {packet.get('message')}"`
  Remark: Creates or updates a value used by the program.
- Line 532: `            if self.current_screen == "auth":`
  Remark: Checks a condition before choosing what to do.
- Line 533: `                self._set_auth_status(message, ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 534: `            else:`
  Remark: Runs when the previous conditions were false.
- Line 535: `                self._set_chat_status(message, ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 536: ` `
  Remark: Blank line used to separate logical code sections.
- Line 537: `    def _handle_ok(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 538: `        action = packet.get("action")`
  Remark: Creates or updates a value used by the program.
- Line 539: `        message = str(packet.get("message", "OK"))`
  Remark: Creates or updates a value used by the program.
- Line 540: `        if action == "login":`
  Remark: Checks a condition before choosing what to do.
- Line 541: `            self.logged_in = True`
  Remark: Creates or updates a value used by the program.
- Line 542: `            self.login_badge_var.set(f"Logged in as {self.username_var.get().strip()}")`
  Remark: Runs a program instruction for the current feature.
- Line 543: `            self._show_chat_screen()`
  Remark: Runs a program instruction for the current feature.
- Line 544: `            self._set_chat_status(message, ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 545: `            messagebox.showinfo("Login OK", message)`
  Remark: Runs a program instruction for the current feature.
- Line 546: `            self._request_rooms()`
  Remark: Runs a program instruction for the current feature.
- Line 547: `            self._request_users()`
  Remark: Runs a program instruction for the current feature.
- Line 548: `        elif action == "register":`
  Remark: Checks another condition when the previous condition was false.
- Line 549: `            self._set_auth_status(f"{message}. Logging in...", ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 550: `            messagebox.showinfo("Register OK", f"{message}. You will be logged in now.")`
  Remark: Runs a program instruction for the current feature.
- Line 551: `            self.connection.send(`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 552: `                "login",`
  Remark: Runs a program instruction for the current feature.
- Line 553: `                username=self.username_var.get(),`
  Remark: Creates or updates a value used by the program.
- Line 554: `                password=self.password_var.get(),`
  Remark: Creates or updates a value used by the program.
- Line 555: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 556: `        elif action == "create_room":`
  Remark: Checks another condition when the previous condition was false.
- Line 557: `            room = str(packet.get("room", "general"))`
  Remark: Creates or updates a value used by the program.
- Line 558: `            self.new_room_var.set("")`
  Remark: Runs a program instruction for the current feature.
- Line 559: `            self.room_var.set(room)`
  Remark: Runs a program instruction for the current feature.
- Line 560: `            self._set_chat_status(message, ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 561: `            self.connection.send("join", room=room)`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 562: `        elif action == "join":`
  Remark: Checks another condition when the previous condition was false.
- Line 563: `            self.current_room = str(packet.get("room", "general"))`
  Remark: Creates or updates a value used by the program.
- Line 564: `            self.room_var.set(self.current_room)`
  Remark: Runs a program instruction for the current feature.
- Line 565: `            self.room_title_var.set(f"Room: {self.current_room}")`
  Remark: Runs a program instruction for the current feature.
- Line 566: `            self._clear_chat()`
  Remark: Runs a program instruction for the current feature.
- Line 567: `            self._set_chat_status(message, ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 568: `            self._request_rooms()`
  Remark: Runs a program instruction for the current feature.
- Line 569: `            self._request_users()`
  Remark: Runs a program instruction for the current feature.
- Line 570: ` `
  Remark: Blank line used to separate logical code sections.
- Line 571: `    def _handle_error(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 572: `        action = packet.get("action")`
  Remark: Creates or updates a value used by the program.
- Line 573: `        message = str(packet.get("message", "Unknown error"))`
  Remark: Creates or updates a value used by the program.
- Line 574: ` `
  Remark: Blank line used to separate logical code sections.
- Line 575: `        if action == "register" and "already exists" in message.lower():`
  Remark: Checks a condition before choosing what to do.
- Line 576: `            self._set_auth_status("Username already exists. Trying to login...", ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 577: `            self.connection.send(`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 578: `                "login",`
  Remark: Runs a program instruction for the current feature.
- Line 579: `                username=self.username_var.get(),`
  Remark: Creates or updates a value used by the program.
- Line 580: `                password=self.password_var.get(),`
  Remark: Creates or updates a value used by the program.
- Line 581: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 582: `            return`
  Remark: Returns a result to the caller.
- Line 583: ` `
  Remark: Blank line used to separate logical code sections.
- Line 584: `        if action in {"register", "login"} or self.current_screen == "auth":`
  Remark: Checks a condition before choosing what to do.
- Line 585: `            self._set_auth_status(message, ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 586: `            messagebox.showerror("Login/Register failed", message)`
  Remark: Runs a program instruction for the current feature.
- Line 587: `            return`
  Remark: Returns a result to the caller.
- Line 588: ` `
  Remark: Blank line used to separate logical code sections.
- Line 589: `        self._set_chat_status(message, ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 590: `        messagebox.showerror("Action failed", message)`
  Remark: Runs a program instruction for the current feature.
- Line 591: ` `
  Remark: Blank line used to separate logical code sections.
- Line 592: `    def _show_history(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 593: `        room = packet.get("room", "general")`
  Remark: Creates or updates a value used by the program.
- Line 594: `        self.current_room = str(room)`
  Remark: Creates or updates a value used by the program.
- Line 595: `        self.room_var.set(self.current_room)`
  Remark: Runs a program instruction for the current feature.
- Line 596: `        self.room_title_var.set(f"Room: {self.current_room}")`
  Remark: Runs a program instruction for the current feature.
- Line 597: `        self.chat_box.configure(state=tk.NORMAL)`
  Remark: Creates or updates a value used by the program.
- Line 598: `        self.chat_box.delete("1.0", tk.END)`
  Remark: Runs a program instruction for the current feature.
- Line 599: `        self.chat_box.insert(tk.END, f"--- History for room {self.current_room} ---\n")`
  Remark: Runs a program instruction for the current feature.
- Line 600: `        for message in packet.get("messages", []):`
  Remark: Loops over multiple values.
- Line 601: `            if isinstance(message, dict):`
  Remark: Checks a condition before choosing what to do.
- Line 602: `                self.chat_box.insert(`
  Remark: Runs a program instruction for the current feature.
- Line 603: `                    tk.END,`
  Remark: Runs a program instruction for the current feature.
- Line 604: `                    f"[{message.get('created_at')}] {message.get('sender')}: {message.get('body')}\n",`
  Remark: Runs a program instruction for the current feature.
- Line 605: `                )`
  Remark: Runs a program instruction for the current feature.
- Line 606: `        self.chat_box.configure(state=tk.DISABLED)`
  Remark: Creates or updates a value used by the program.
- Line 607: `        self.chat_box.see(tk.END)`
  Remark: Runs a program instruction for the current feature.
- Line 608: ` `
  Remark: Blank line used to separate logical code sections.
- Line 609: `    def _show_users(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 610: `        self.users_box.delete(0, tk.END)`
  Remark: Runs a program instruction for the current feature.
- Line 611: `        online = packet.get("online", [])`
  Remark: Creates or updates a value used by the program.
- Line 612: `        if isinstance(online, list):`
  Remark: Checks a condition before choosing what to do.
- Line 613: `            for user in online:`
  Remark: Loops over multiple values.
- Line 614: `                if isinstance(user, dict):`
  Remark: Checks a condition before choosing what to do.
- Line 615: `                    self.users_box.insert(tk.END, f"{user.get('username')} @ {user.get('room')}")`
  Remark: Runs a program instruction for the current feature.
- Line 616: ` `
  Remark: Blank line used to separate logical code sections.
- Line 617: `    def _show_rooms(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 618: `        rooms = packet.get("rooms", [])`
  Remark: Creates or updates a value used by the program.
- Line 619: `        current = str(packet.get("current", self.current_room))`
  Remark: Creates or updates a value used by the program.
- Line 620: `        self.rooms_box.delete(0, tk.END)`
  Remark: Runs a program instruction for the current feature.
- Line 621: ` `
  Remark: Blank line used to separate logical code sections.
- Line 622: `        if isinstance(rooms, list):`
  Remark: Checks a condition before choosing what to do.
- Line 623: `            for index, room in enumerate(rooms):`
  Remark: Loops over multiple values.
- Line 624: `                room_name = str(room)`
  Remark: Creates or updates a value used by the program.
- Line 625: `                self.rooms_box.insert(tk.END, room_name)`
  Remark: Runs a program instruction for the current feature.
- Line 626: `                if room_name == current:`
  Remark: Checks a condition before choosing what to do.
- Line 627: `                    self.rooms_box.selection_clear(0, tk.END)`
  Remark: Runs a program instruction for the current feature.
- Line 628: `                    self.rooms_box.selection_set(index)`
  Remark: Runs a program instruction for the current feature.
- Line 629: `                    self.rooms_box.see(index)`
  Remark: Runs a program instruction for the current feature.
- Line 630: `                    self.room_var.set(room_name)`
  Remark: Runs a program instruction for the current feature.
- Line 631: ` `
  Remark: Blank line used to separate logical code sections.
- Line 632: `    def _on_room_select(self, _event: tk.Event) -> None:`
  Remark: Defines a function or method.
- Line 633: `        selection = self.rooms_box.curselection()`
  Remark: Creates or updates a value used by the program.
- Line 634: `        if selection:`
  Remark: Checks a condition before choosing what to do.
- Line 635: `            self.room_var.set(self.rooms_box.get(selection[0]))`
  Remark: Runs a program instruction for the current feature.
- Line 636: ` `
  Remark: Blank line used to separate logical code sections.
- Line 637: `    def _handle_file_packet(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 638: `        try:`
  Remark: Starts error-handling code.
- Line 639: `            filename = InputValidator.filename(str(packet.get("filename", "download.bin")))`
  Remark: Creates or updates a value used by the program.
- Line 640: `            kind = str(packet.get("kind", "file"))`
  Remark: Creates or updates a value used by the program.
- Line 641: `            sender = str(packet.get("sender", "unknown"))`
  Remark: Creates or updates a value used by the program.
- Line 642: `            created_at = str(packet.get("created_at", ""))`
  Remark: Creates or updates a value used by the program.
- Line 643: `            encoded_data = str(packet.get("data", ""))`
  Remark: Creates or updates a value used by the program.
- Line 644: `            file_data = base64.b64decode(encoded_data.encode("ascii"), validate=True)`
  Remark: Creates or updates a value used by the program.
- Line 645: `        except Exception as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 646: `            self._set_chat_status(f"Received invalid file packet: {exc}", ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 647: `            return`
  Remark: Returns a result to the caller.
- Line 648: ` `
  Remark: Blank line used to separate logical code sections.
- Line 649: `        DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 650: `        save_path = self._unique_download_path(filename)`
  Remark: Creates or updates a value used by the program.
- Line 651: `        save_path.write_bytes(file_data)`
  Remark: Runs a program instruction for the current feature.
- Line 652: ` `
  Remark: Blank line used to separate logical code sections.
- Line 653: `        if kind == "image":`
  Remark: Checks a condition before choosing what to do.
- Line 654: `            self._append_image_preview(created_at, sender, filename, save_path)`
  Remark: Runs a program instruction for the current feature.
- Line 655: `        else:`
  Remark: Runs when the previous conditions were false.
- Line 656: `            self._append_clickable_file(created_at, sender, kind, filename, save_path)`
  Remark: Runs a program instruction for the current feature.
- Line 657: ` `
  Remark: Blank line used to separate logical code sections.
- Line 658: `    def _unique_download_path(self, filename: str) -> Path:`
  Remark: Defines a function or method.
- Line 659: `        path = DOWNLOAD_DIR / filename`
  Remark: Creates or updates a value used by the program.
- Line 660: `        if not path.exists():`
  Remark: Checks a condition before choosing what to do.
- Line 661: `            return path`
  Remark: Returns a result to the caller.
- Line 662: ` `
  Remark: Blank line used to separate logical code sections.
- Line 663: `        stem = path.stem`
  Remark: Creates or updates a value used by the program.
- Line 664: `        suffix = path.suffix`
  Remark: Creates or updates a value used by the program.
- Line 665: `        counter = 1`
  Remark: Creates or updates a value used by the program.
- Line 666: `        while True:`
  Remark: Repeats code while a condition remains true.
- Line 667: `            candidate = DOWNLOAD_DIR / f"{stem}_{counter}{suffix}"`
  Remark: Creates or updates a value used by the program.
- Line 668: `            if not candidate.exists():`
  Remark: Checks a condition before choosing what to do.
- Line 669: `                return candidate`
  Remark: Returns a result to the caller.
- Line 670: `            counter += 1`
  Remark: Creates or updates a value used by the program.
- Line 671: ` `
  Remark: Blank line used to separate logical code sections.
- Line 672: `    def _append_image_preview(`
  Remark: Defines a function or method.
- Line 673: `        self,`
  Remark: Runs a program instruction for the current feature.
- Line 674: `        created_at: str,`
  Remark: Runs a program instruction for the current feature.
- Line 675: `        sender: str,`
  Remark: Runs a program instruction for the current feature.
- Line 676: `        filename: str,`
  Remark: Runs a program instruction for the current feature.
- Line 677: `        save_path: Path,`
  Remark: Runs a program instruction for the current feature.
- Line 678: `    ) -> None:`
  Remark: Runs a program instruction for the current feature.
- Line 679: `        self._append_clickable_file(created_at, sender, "image", filename, save_path)`
  Remark: Runs a program instruction for the current feature.
- Line 680: ` `
  Remark: Blank line used to separate logical code sections.
- Line 681: `        try:`
  Remark: Starts error-handling code.
- Line 682: `            image = Image.open(save_path)`
  Remark: Creates or updates a value used by the program.
- Line 683: `            image.thumbnail((320, 220))`
  Remark: Runs a program instruction for the current feature.
- Line 684: `            preview = ImageTk.PhotoImage(image)`
  Remark: Creates or updates a value used by the program.
- Line 685: `        except Exception as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 686: `            self._append_chat(f"Could not show image preview: {exc}")`
  Remark: Runs a program instruction for the current feature.
- Line 687: `            return`
  Remark: Returns a result to the caller.
- Line 688: ` `
  Remark: Blank line used to separate logical code sections.
- Line 689: `        self.chat_images.append(preview)`
  Remark: Runs a program instruction for the current feature.
- Line 690: `        self.chat_box.configure(state=tk.NORMAL)`
  Remark: Creates or updates a value used by the program.
- Line 691: `        self.chat_box.image_create(tk.END, image=preview)`
  Remark: Creates or updates a value used by the program.
- Line 692: `        self.chat_box.insert(tk.END, "\n")`
  Remark: Runs a program instruction for the current feature.
- Line 693: `        self.chat_box.configure(state=tk.DISABLED)`
  Remark: Creates or updates a value used by the program.
- Line 694: `        self.chat_box.see(tk.END)`
  Remark: Runs a program instruction for the current feature.
- Line 695: ` `
  Remark: Blank line used to separate logical code sections.
- Line 696: `    def _append_clickable_file(`
  Remark: Defines a function or method.
- Line 697: `        self,`
  Remark: Runs a program instruction for the current feature.
- Line 698: `        created_at: str,`
  Remark: Runs a program instruction for the current feature.
- Line 699: `        sender: str,`
  Remark: Runs a program instruction for the current feature.
- Line 700: `        kind: str,`
  Remark: Runs a program instruction for the current feature.
- Line 701: `        filename: str,`
  Remark: Runs a program instruction for the current feature.
- Line 702: `        save_path: Path,`
  Remark: Runs a program instruction for the current feature.
- Line 703: `    ) -> None:`
  Remark: Runs a program instruction for the current feature.
- Line 704: `        link_tag = f"link_{len(self.chat_links)}"`
  Remark: Creates or updates a value used by the program.
- Line 705: `        self.chat_links[link_tag] = save_path`
  Remark: Creates or updates a value used by the program.
- Line 706: ` `
  Remark: Blank line used to separate logical code sections.
- Line 707: `        self.chat_box.configure(state=tk.NORMAL)`
  Remark: Creates or updates a value used by the program.
- Line 708: `        self.chat_box.insert(tk.END, f"[{created_at}] {sender} sent {kind}: ")`
  Remark: Runs a program instruction for the current feature.
- Line 709: `        self.chat_box.insert(tk.END, filename, (link_tag,))`
  Remark: Runs a program instruction for the current feature.
- Line 710: `        self.chat_box.insert(tk.END, " (click to open)\n")`
  Remark: Runs a program instruction for the current feature.
- Line 711: `        self.chat_box.tag_configure(link_tag, foreground="#2563eb", underline=True)`
  Remark: Creates or updates a value used by the program.
- Line 712: `        self.chat_box.tag_bind(link_tag, "<Button-1>", lambda _event, tag=link_tag: self._open_chat_link(tag))`
  Remark: Creates or updates a value used by the program.
- Line 713: `        self.chat_box.tag_bind(link_tag, "<Enter>", lambda _event: self.chat_box.configure(cursor="hand2"))`
  Remark: Creates or updates a value used by the program.
- Line 714: `        self.chat_box.tag_bind(link_tag, "<Leave>", lambda _event: self.chat_box.configure(cursor=""))`
  Remark: Creates or updates a value used by the program.
- Line 715: `        self.chat_box.configure(state=tk.DISABLED)`
  Remark: Creates or updates a value used by the program.
- Line 716: `        self.chat_box.see(tk.END)`
  Remark: Runs a program instruction for the current feature.
- Line 717: ` `
  Remark: Blank line used to separate logical code sections.
- Line 718: `    def _open_chat_link(self, link_tag: str) -> None:`
  Remark: Defines a function or method.
- Line 719: `        path = self.chat_links.get(link_tag)`
  Remark: Creates or updates a value used by the program.
- Line 720: `        if path is None:`
  Remark: Checks a condition before choosing what to do.
- Line 721: `            return`
  Remark: Returns a result to the caller.
- Line 722: ` `
  Remark: Blank line used to separate logical code sections.
- Line 723: `        try:`
  Remark: Starts error-handling code.
- Line 724: `            if os.name == "nt":`
  Remark: Checks a condition before choosing what to do.
- Line 725: `                os.startfile(path)`
  Remark: Runs a program instruction for the current feature.
- Line 726: `            elif sys.platform == "darwin":`
  Remark: Checks another condition when the previous condition was false.
- Line 727: `                subprocess.Popen(["open", str(path)])`
  Remark: Runs a program instruction for the current feature.
- Line 728: `            else:`
  Remark: Runs when the previous conditions were false.
- Line 729: `                subprocess.Popen(["xdg-open", str(path)])`
  Remark: Runs a program instruction for the current feature.
- Line 730: `        except Exception as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 731: `            self._set_chat_status(f"Could not open file: {exc}", ok=False)`
  Remark: Creates or updates a value used by the program.
- Line 732: ` `
  Remark: Blank line used to separate logical code sections.
- Line 733: `    def _append_chat(self, text: str) -> None:`
  Remark: Defines a function or method.
- Line 734: `        self.chat_box.configure(state=tk.NORMAL)`
  Remark: Creates or updates a value used by the program.
- Line 735: `        self.chat_box.insert(tk.END, text + "\n")`
  Remark: Runs a program instruction for the current feature.
- Line 736: `        self.chat_box.configure(state=tk.DISABLED)`
  Remark: Creates or updates a value used by the program.
- Line 737: `        self.chat_box.see(tk.END)`
  Remark: Runs a program instruction for the current feature.
- Line 738: ` `
  Remark: Blank line used to separate logical code sections.
- Line 739: `    def _clear_chat(self) -> None:`
  Remark: Defines a function or method.
- Line 740: `        self.chat_box.configure(state=tk.NORMAL)`
  Remark: Creates or updates a value used by the program.
- Line 741: `        self.chat_box.delete("1.0", tk.END)`
  Remark: Runs a program instruction for the current feature.
- Line 742: `        self.chat_box.configure(state=tk.DISABLED)`
  Remark: Creates or updates a value used by the program.
- Line 743: ` `
  Remark: Blank line used to separate logical code sections.
- Line 744: `    def _set_auth_status(self, message: str, ok: bool) -> None:`
  Remark: Defines a function or method.
- Line 745: `        self.auth_status_var.set(message)`
  Remark: Runs a program instruction for the current feature.
- Line 746: `        self.auth_status_label.configure(`
  Remark: Runs a program instruction for the current feature.
- Line 747: `            bg="#dcfce7" if ok else "#fee2e2",`
  Remark: Creates or updates a value used by the program.
- Line 748: `            fg="#166534" if ok else "#991b1b",`
  Remark: Creates or updates a value used by the program.
- Line 749: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 750: ` `
  Remark: Blank line used to separate logical code sections.
- Line 751: `    def _set_chat_status(self, message: str, ok: bool) -> None:`
  Remark: Defines a function or method.
- Line 752: `        self.chat_status_var.set(message)`
  Remark: Runs a program instruction for the current feature.
- Line 753: `        self.chat_status_label.configure(fg="#16a34a" if ok else "#dc2626")`
  Remark: Creates or updates a value used by the program.
- Line 754: ` `
  Remark: Blank line used to separate logical code sections.
- Line 755: `    def _on_close(self) -> None:`
  Remark: Defines a function or method.
- Line 756: `        self.connection.close()`
  Remark: Runs a program instruction for the current feature.
- Line 757: `        self.destroy()`
  Remark: Runs a program instruction for the current feature.
- Line 758: ` `
  Remark: Blank line used to separate logical code sections.
- Line 759: ` `
  Remark: Blank line used to separate logical code sections.
- Line 760: `def parse_args() -> argparse.Namespace:`
  Remark: Defines a function or method.
- Line 761: `    parser = argparse.ArgumentParser(description="SecureChat Tkinter client")`
  Remark: Creates or updates a value used by the program.
- Line 762: `    parser.add_argument("--host", default=DEFAULT_HOST)`
  Remark: Creates or updates a value used by the program.
- Line 763: `    parser.add_argument("--port", type=int, default=DEFAULT_PORT)`
  Remark: Creates or updates a value used by the program.
- Line 764: `    parser.add_argument("--verify-cert", action="store_true")`
  Remark: Creates or updates a value used by the program.
- Line 765: `    return parser.parse_args()`
  Remark: Returns a result to the caller.
- Line 766: ` `
  Remark: Blank line used to separate logical code sections.
- Line 767: ` `
  Remark: Blank line used to separate logical code sections.
- Line 768: `if __name__ == "__main__":`
  Remark: Checks a condition before choosing what to do.
- Line 769: `    args = parse_args()`
  Remark: Creates or updates a value used by the program.
- Line 770: `    client_connection = ChatClientConnection(`
  Remark: Creates or updates a value used by the program.
- Line 771: `        host=args.host,`
  Remark: Creates or updates a value used by the program.
- Line 772: `        port=args.port,`
  Remark: Creates or updates a value used by the program.
- Line 773: `        verify_certificate=args.verify_cert,`
  Remark: Creates or updates a value used by the program.
- Line 774: `    )`
  Remark: Runs a program instruction for the current feature.
- Line 775: `    client_connection.connect()`
  Remark: Runs a program instruction for the current feature.
- Line 776: `    app = SecureChatApp(client_connection)`
  Remark: Creates or updates a value used by the program.
- Line 777: `    app.mainloop()`
  Remark: Runs a program instruction for the current feature.
- Line 778: ` `
  Remark: Blank line used to separate logical code sections.

## `secure_chat/config.py`

- Line 1: `from pathlib import Path`
  Remark: Imports code that this file needs.
- Line 2: ` `
  Remark: Blank line used to separate logical code sections.
- Line 3: ` `
  Remark: Blank line used to separate logical code sections.
- Line 4: `PROJECT_ROOT = Path(__file__).resolve().parent.parent`
  Remark: Creates or updates a value used by the program.
- Line 5: `DATA_DIR = PROJECT_ROOT / "data"`
  Remark: Creates or updates a value used by the program.
- Line 6: `CERT_DIR = PROJECT_ROOT / "certs"`
  Remark: Creates or updates a value used by the program.
- Line 7: `DOWNLOAD_DIR = PROJECT_ROOT / "downloads"`
  Remark: Creates or updates a value used by the program.
- Line 8: `UPLOAD_DIR = DATA_DIR / "uploads"`
  Remark: Creates or updates a value used by the program.
- Line 9: ` `
  Remark: Blank line used to separate logical code sections.
- Line 10: `DATABASE_PATH = DATA_DIR / "secure_chat.db"`
  Remark: Creates or updates a value used by the program.
- Line 11: `LOG_PATH = DATA_DIR / "server.log"`
  Remark: Creates or updates a value used by the program.
- Line 12: `CERT_PATH = CERT_DIR / "server.crt"`
  Remark: Creates or updates a value used by the program.
- Line 13: `KEY_PATH = CERT_DIR / "server.key"`
  Remark: Creates or updates a value used by the program.
- Line 14: ` `
  Remark: Blank line used to separate logical code sections.
- Line 15: `DEFAULT_HOST = "127.0.0.1"`
  Remark: Creates or updates a value used by the program.
- Line 16: `DEFAULT_PORT = 5050`
  Remark: Creates or updates a value used by the program.
- Line 17: ` `
  Remark: Blank line used to separate logical code sections.
- Line 18: `# Media is sent as base64 inside JSON, so packets must be larger than plain text messages.`
  Remark: A programmer comment that explains the nearby code.
- Line 19: `MAX_PACKET_SIZE = 25 * 1024 * 1024`
  Remark: Creates or updates a value used by the program.
- Line 20: `MAX_FILE_SIZE = 15 * 1024 * 1024`
  Remark: Creates or updates a value used by the program.
- Line 21: `MAX_USERNAME_LENGTH = 20`
  Remark: Creates or updates a value used by the program.
- Line 22: `MAX_PASSWORD_LENGTH = 128`
  Remark: Creates or updates a value used by the program.
- Line 23: `MAX_ROOM_LENGTH = 30`
  Remark: Creates or updates a value used by the program.
- Line 24: `MAX_MESSAGE_LENGTH = 1000`
  Remark: Creates or updates a value used by the program.
- Line 25: `MAX_FILENAME_LENGTH = 120`
  Remark: Creates or updates a value used by the program.
- Line 26: ` `
  Remark: Blank line used to separate logical code sections.
- Line 27: `PBKDF2_ITERATIONS = 250_000`
  Remark: Creates or updates a value used by the program.
- Line 28: ` `
  Remark: Blank line used to separate logical code sections.

## `secure_chat/models.py`

- Line 1: `from dataclasses import dataclass`
  Remark: Imports code that this file needs.
- Line 2: `from datetime import datetime`
  Remark: Imports code that this file needs.
- Line 3: ` `
  Remark: Blank line used to separate logical code sections.
- Line 4: ` `
  Remark: Blank line used to separate logical code sections.
- Line 5: `@dataclass(frozen=True)`
  Remark: Decorator that changes how the next function or method behaves.
- Line 6: `class User:`
  Remark: Defines an object-oriented class used by the project.
- Line 7: `    username: str`
  Remark: Runs a program instruction for the current feature.
- Line 8: `    created_at: str`
  Remark: Runs a program instruction for the current feature.
- Line 9: ` `
  Remark: Blank line used to separate logical code sections.
- Line 10: ` `
  Remark: Blank line used to separate logical code sections.
- Line 11: `@dataclass(frozen=True)`
  Remark: Decorator that changes how the next function or method behaves.
- Line 12: `class ChatMessage:`
  Remark: Defines an object-oriented class used by the project.
- Line 13: `    sender: str`
  Remark: Runs a program instruction for the current feature.
- Line 14: `    room: str`
  Remark: Runs a program instruction for the current feature.
- Line 15: `    body: str`
  Remark: Runs a program instruction for the current feature.
- Line 16: `    created_at: str`
  Remark: Runs a program instruction for the current feature.
- Line 17: ` `
  Remark: Blank line used to separate logical code sections.
- Line 18: ` `
  Remark: Blank line used to separate logical code sections.
- Line 19: `@dataclass(frozen=True)`
  Remark: Decorator that changes how the next function or method behaves.
- Line 20: `class ClientInfo:`
  Remark: Defines an object-oriented class used by the project.
- Line 21: `    username: str`
  Remark: Runs a program instruction for the current feature.
- Line 22: `    room: str`
  Remark: Runs a program instruction for the current feature.
- Line 23: `    address: str`
  Remark: Runs a program instruction for the current feature.
- Line 24: ` `
  Remark: Blank line used to separate logical code sections.
- Line 25: ` `
  Remark: Blank line used to separate logical code sections.
- Line 26: `@dataclass(frozen=True)`
  Remark: Decorator that changes how the next function or method behaves.
- Line 27: `class ServerEvent:`
  Remark: Defines an object-oriented class used by the project.
- Line 28: `    event_type: str`
  Remark: Runs a program instruction for the current feature.
- Line 29: `    message: str`
  Remark: Runs a program instruction for the current feature.
- Line 30: `    created_at: str`
  Remark: Runs a program instruction for the current feature.
- Line 31: ` `
  Remark: Blank line used to separate logical code sections.
- Line 32: ` `
  Remark: Blank line used to separate logical code sections.
- Line 33: `def now_iso() -> str:`
  Remark: Defines a function or method.
- Line 34: `    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"`
  Remark: Returns a result to the caller.
- Line 35: ` `
  Remark: Blank line used to separate logical code sections.

## `secure_chat/protocol.py`

- Line 1: `import json`
  Remark: Imports code that this file needs.
- Line 2: `import socket`
  Remark: Imports code that this file needs.
- Line 3: `import struct`
  Remark: Imports code that this file needs.
- Line 4: `from typing import Any`
  Remark: Imports code that this file needs.
- Line 5: ` `
  Remark: Blank line used to separate logical code sections.
- Line 6: `from secure_chat.config import MAX_PACKET_SIZE`
  Remark: Imports code that this file needs.
- Line 7: ` `
  Remark: Blank line used to separate logical code sections.
- Line 8: ` `
  Remark: Blank line used to separate logical code sections.
- Line 9: `class ProtocolError(Exception):`
  Remark: Defines an object-oriented class used by the project.
- Line 10: `    """Raised when a peer sends an invalid protocol packet."""`
  Remark: Documentation string that explains a module, class, or function.
- Line 11: ` `
  Remark: Blank line used to separate logical code sections.
- Line 12: ` `
  Remark: Blank line used to separate logical code sections.
- Line 13: `class ChatProtocol:`
  Remark: Defines an object-oriented class used by the project.
- Line 14: `    """`
  Remark: Documentation string that explains a module, class, or function.
- Line 15: `    Custom length-prefixed JSON protocol.`
  Remark: Runs a program instruction for the current feature.
- Line 16: ` `
  Remark: Blank line used to separate logical code sections.
- Line 17: `    Packet layout:`
  Remark: Runs a program instruction for the current feature.
- Line 18: `    - 4 bytes unsigned big-endian payload length`
  Remark: Runs a program instruction for the current feature.
- Line 19: `    - UTF-8 JSON payload`
  Remark: Runs a program instruction for the current feature.
- Line 20: `    """`
  Remark: Documentation string that explains a module, class, or function.
- Line 21: ` `
  Remark: Blank line used to separate logical code sections.
- Line 22: `    HEADER_SIZE = 4`
  Remark: Creates or updates a value used by the program.
- Line 23: ` `
  Remark: Blank line used to separate logical code sections.
- Line 24: `    @staticmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 25: `    def send(sock: socket.socket, packet_type: str, **fields: Any) -> None:`
  Remark: Defines a function or method.
- Line 26: `        packet = {"type": packet_type, **fields}`
  Remark: Creates or updates a value used by the program.
- Line 27: `        raw = json.dumps(packet, ensure_ascii=False).encode("utf-8")`
  Remark: Creates or updates a value used by the program.
- Line 28: `        if len(raw) > MAX_PACKET_SIZE:`
  Remark: Checks a condition before choosing what to do.
- Line 29: `            raise ProtocolError("Packet is too large")`
  Remark: Raises an error when invalid behavior is detected.
- Line 30: ` `
  Remark: Blank line used to separate logical code sections.
- Line 31: `        header = struct.pack("!I", len(raw))`
  Remark: Places a visual widget on the Tkinter screen.
- Line 32: `        sock.sendall(header + raw)`
  Remark: Runs a program instruction for the current feature.
- Line 33: ` `
  Remark: Blank line used to separate logical code sections.
- Line 34: `    @staticmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 35: `    def receive(sock: socket.socket) -> dict[str, Any]:`
  Remark: Defines a function or method.
- Line 36: `        header = ChatProtocol._receive_exact(sock, ChatProtocol.HEADER_SIZE)`
  Remark: Creates or updates a value used by the program.
- Line 37: `        if not header:`
  Remark: Checks a condition before choosing what to do.
- Line 38: `            raise ConnectionError("Peer disconnected")`
  Remark: Raises an error when invalid behavior is detected.
- Line 39: ` `
  Remark: Blank line used to separate logical code sections.
- Line 40: `        (payload_size,) = struct.unpack("!I", header)`
  Remark: Places a visual widget on the Tkinter screen.
- Line 41: `        if payload_size <= 0 or payload_size > MAX_PACKET_SIZE:`
  Remark: Checks a condition before choosing what to do.
- Line 42: `            raise ProtocolError("Invalid packet size")`
  Remark: Raises an error when invalid behavior is detected.
- Line 43: ` `
  Remark: Blank line used to separate logical code sections.
- Line 44: `        payload = ChatProtocol._receive_exact(sock, payload_size)`
  Remark: Creates or updates a value used by the program.
- Line 45: `        try:`
  Remark: Starts error-handling code.
- Line 46: `            packet = json.loads(payload.decode("utf-8"))`
  Remark: Creates or updates a value used by the program.
- Line 47: `        except (UnicodeDecodeError, json.JSONDecodeError) as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 48: `            raise ProtocolError("Packet is not valid UTF-8 JSON") from exc`
  Remark: Raises an error when invalid behavior is detected.
- Line 49: ` `
  Remark: Blank line used to separate logical code sections.
- Line 50: `        if not isinstance(packet, dict) or not isinstance(packet.get("type"), str):`
  Remark: Checks a condition before choosing what to do.
- Line 51: `            raise ProtocolError("Packet must contain a string type")`
  Remark: Raises an error when invalid behavior is detected.
- Line 52: ` `
  Remark: Blank line used to separate logical code sections.
- Line 53: `        return packet`
  Remark: Returns a result to the caller.
- Line 54: ` `
  Remark: Blank line used to separate logical code sections.
- Line 55: `    @staticmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 56: `    def _receive_exact(sock: socket.socket, size: int) -> bytes:`
  Remark: Defines a function or method.
- Line 57: `        chunks: list[bytes] = []`
  Remark: Creates or updates a value used by the program.
- Line 58: `        remaining = size`
  Remark: Creates or updates a value used by the program.
- Line 59: ` `
  Remark: Blank line used to separate logical code sections.
- Line 60: `        while remaining > 0:`
  Remark: Repeats code while a condition remains true.
- Line 61: `            chunk = sock.recv(remaining)`
  Remark: Receives data from the network connection.
- Line 62: `            if not chunk:`
  Remark: Checks a condition before choosing what to do.
- Line 63: `                raise ConnectionError("Peer disconnected")`
  Remark: Raises an error when invalid behavior is detected.
- Line 64: `            chunks.append(chunk)`
  Remark: Runs a program instruction for the current feature.
- Line 65: `            remaining -= len(chunk)`
  Remark: Creates or updates a value used by the program.
- Line 66: ` `
  Remark: Blank line used to separate logical code sections.
- Line 67: `        return b"".join(chunks)`
  Remark: Returns a result to the caller.
- Line 68: ` `
  Remark: Blank line used to separate logical code sections.

## `secure_chat/security.py`

- Line 1: `import hmac`
  Remark: Imports code that this file needs.
- Line 2: `import os`
  Remark: Imports code that this file needs.
- Line 3: `import re`
  Remark: Imports code that this file needs.
- Line 4: `import ssl`
  Remark: Imports code that this file needs.
- Line 5: `from datetime import datetime, timedelta, timezone`
  Remark: Imports code that this file needs.
- Line 6: `from hashlib import pbkdf2_hmac`
  Remark: Imports code that this file needs.
- Line 7: ` `
  Remark: Blank line used to separate logical code sections.
- Line 8: `from secure_chat.config import (`
  Remark: Imports code that this file needs.
- Line 9: `    CERT_DIR,`
  Remark: Runs a program instruction for the current feature.
- Line 10: `    CERT_PATH,`
  Remark: Runs a program instruction for the current feature.
- Line 11: `    KEY_PATH,`
  Remark: Runs a program instruction for the current feature.
- Line 12: `    MAX_MESSAGE_LENGTH,`
  Remark: Runs a program instruction for the current feature.
- Line 13: `    MAX_PASSWORD_LENGTH,`
  Remark: Runs a program instruction for the current feature.
- Line 14: `    MAX_ROOM_LENGTH,`
  Remark: Runs a program instruction for the current feature.
- Line 15: `    MAX_USERNAME_LENGTH,`
  Remark: Runs a program instruction for the current feature.
- Line 16: `    MAX_FILENAME_LENGTH,`
  Remark: Runs a program instruction for the current feature.
- Line 17: `    PBKDF2_ITERATIONS,`
  Remark: Runs a program instruction for the current feature.
- Line 18: `)`
  Remark: Runs a program instruction for the current feature.
- Line 19: ` `
  Remark: Blank line used to separate logical code sections.
- Line 20: ` `
  Remark: Blank line used to separate logical code sections.
- Line 21: `class ValidationError(ValueError):`
  Remark: Defines an object-oriented class used by the project.
- Line 22: `    """Raised when user-controlled input is not allowed."""`
  Remark: Documentation string that explains a module, class, or function.
- Line 23: ` `
  Remark: Blank line used to separate logical code sections.
- Line 24: ` `
  Remark: Blank line used to separate logical code sections.
- Line 25: `class PasswordHasher:`
  Remark: Defines an object-oriented class used by the project.
- Line 26: `    @staticmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 27: `    def hash_password(password: str) -> str:`
  Remark: Defines a function or method.
- Line 28: `        salt = os.urandom(16)`
  Remark: Creates or updates a value used by the program.
- Line 29: `        digest = pbkdf2_hmac(`
  Remark: Creates or updates a value used by the program.
- Line 30: `            "sha256",`
  Remark: Runs a program instruction for the current feature.
- Line 31: `            password.encode("utf-8"),`
  Remark: Runs a program instruction for the current feature.
- Line 32: `            salt,`
  Remark: Runs a program instruction for the current feature.
- Line 33: `            PBKDF2_ITERATIONS,`
  Remark: Runs a program instruction for the current feature.
- Line 34: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 35: `        return f"{PBKDF2_ITERATIONS}${salt.hex()}${digest.hex()}"`
  Remark: Returns a result to the caller.
- Line 36: ` `
  Remark: Blank line used to separate logical code sections.
- Line 37: `    @staticmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 38: `    def verify_password(password: str, stored_hash: str) -> bool:`
  Remark: Defines a function or method.
- Line 39: `        try:`
  Remark: Starts error-handling code.
- Line 40: `            iterations_text, salt_hex, digest_hex = stored_hash.split("$")`
  Remark: Creates or updates a value used by the program.
- Line 41: `            iterations = int(iterations_text)`
  Remark: Creates or updates a value used by the program.
- Line 42: `            salt = bytes.fromhex(salt_hex)`
  Remark: Creates or updates a value used by the program.
- Line 43: `            expected_digest = bytes.fromhex(digest_hex)`
  Remark: Creates or updates a value used by the program.
- Line 44: `        except (ValueError, TypeError):`
  Remark: Handles an expected error so the program does not crash.
- Line 45: `            return False`
  Remark: Returns a result to the caller.
- Line 46: ` `
  Remark: Blank line used to separate logical code sections.
- Line 47: `        actual_digest = pbkdf2_hmac(`
  Remark: Creates or updates a value used by the program.
- Line 48: `            "sha256",`
  Remark: Runs a program instruction for the current feature.
- Line 49: `            password.encode("utf-8"),`
  Remark: Runs a program instruction for the current feature.
- Line 50: `            salt,`
  Remark: Runs a program instruction for the current feature.
- Line 51: `            iterations,`
  Remark: Runs a program instruction for the current feature.
- Line 52: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 53: `        return hmac.compare_digest(actual_digest, expected_digest)`
  Remark: Returns a result to the caller.
- Line 54: ` `
  Remark: Blank line used to separate logical code sections.
- Line 55: ` `
  Remark: Blank line used to separate logical code sections.
- Line 56: `class InputValidator:`
  Remark: Defines an object-oriented class used by the project.
- Line 57: `    USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_]{3,20}$")`
  Remark: Creates or updates a value used by the program.
- Line 58: `    ROOM_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,30}$")`
  Remark: Creates or updates a value used by the program.
- Line 59: ` `
  Remark: Blank line used to separate logical code sections.
- Line 60: `    @classmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 61: `    def username(cls, value: str) -> str:`
  Remark: Defines a function or method.
- Line 62: `        value = value.strip()`
  Remark: Creates or updates a value used by the program.
- Line 63: `        if len(value) > MAX_USERNAME_LENGTH or not cls.USERNAME_PATTERN.fullmatch(value):`
  Remark: Checks a condition before choosing what to do.
- Line 64: `            raise ValidationError("Username must be 3-20 letters, numbers, or underscores")`
  Remark: Raises an error when invalid behavior is detected.
- Line 65: `        return value`
  Remark: Returns a result to the caller.
- Line 66: ` `
  Remark: Blank line used to separate logical code sections.
- Line 67: `    @classmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 68: `    def password(cls, value: str) -> str:`
  Remark: Defines a function or method.
- Line 69: `        if not 6 <= len(value) <= MAX_PASSWORD_LENGTH:`
  Remark: Checks a condition before choosing what to do.
- Line 70: `            raise ValidationError("Password must be 6-128 characters")`
  Remark: Raises an error when invalid behavior is detected.
- Line 71: `        return value`
  Remark: Returns a result to the caller.
- Line 72: ` `
  Remark: Blank line used to separate logical code sections.
- Line 73: `    @classmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 74: `    def room(cls, value: str) -> str:`
  Remark: Defines a function or method.
- Line 75: `        value = value.strip() or "general"`
  Remark: Creates or updates a value used by the program.
- Line 76: `        if len(value) > MAX_ROOM_LENGTH or not cls.ROOM_PATTERN.fullmatch(value):`
  Remark: Checks a condition before choosing what to do.
- Line 77: `            raise ValidationError("Room must contain only letters, numbers, _ or -")`
  Remark: Raises an error when invalid behavior is detected.
- Line 78: `        return value`
  Remark: Returns a result to the caller.
- Line 79: ` `
  Remark: Blank line used to separate logical code sections.
- Line 80: `    @classmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 81: `    def message(cls, value: str) -> str:`
  Remark: Defines a function or method.
- Line 82: `        value = value.strip()`
  Remark: Creates or updates a value used by the program.
- Line 83: `        if not value:`
  Remark: Checks a condition before choosing what to do.
- Line 84: `            raise ValidationError("Message cannot be empty")`
  Remark: Raises an error when invalid behavior is detected.
- Line 85: `        if len(value) > MAX_MESSAGE_LENGTH:`
  Remark: Checks a condition before choosing what to do.
- Line 86: `            raise ValidationError(f"Message cannot be longer than {MAX_MESSAGE_LENGTH} characters")`
  Remark: Raises an error when invalid behavior is detected.
- Line 87: `        return value`
  Remark: Returns a result to the caller.
- Line 88: ` `
  Remark: Blank line used to separate logical code sections.
- Line 89: `    @classmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 90: `    def filename(cls, value: str) -> str:`
  Remark: Defines a function or method.
- Line 91: `        value = value.strip().replace("\\", "_").replace("/", "_")`
  Remark: Places a visual widget on the Tkinter screen.
- Line 92: `        if not value or value in {".", ".."}:`
  Remark: Checks a condition before choosing what to do.
- Line 93: `            raise ValidationError("Filename is not valid")`
  Remark: Raises an error when invalid behavior is detected.
- Line 94: `        if len(value) > MAX_FILENAME_LENGTH:`
  Remark: Checks a condition before choosing what to do.
- Line 95: `            raise ValidationError(f"Filename cannot be longer than {MAX_FILENAME_LENGTH} characters")`
  Remark: Raises an error when invalid behavior is detected.
- Line 96: `        return value`
  Remark: Returns a result to the caller.
- Line 97: ` `
  Remark: Blank line used to separate logical code sections.
- Line 98: ` `
  Remark: Blank line used to separate logical code sections.
- Line 99: `class TLSContextFactory:`
  Remark: Defines an object-oriented class used by the project.
- Line 100: `    @staticmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 101: `    def server_context() -> ssl.SSLContext:`
  Remark: Defines a function or method.
- Line 102: `        TLSContextFactory.ensure_development_certificate()`
  Remark: Runs a program instruction for the current feature.
- Line 103: `        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)`
  Remark: Creates or updates a value used by the program.
- Line 104: `        context.minimum_version = ssl.TLSVersion.TLSv1_2`
  Remark: Creates or updates a value used by the program.
- Line 105: `        context.load_cert_chain(certfile=CERT_PATH, keyfile=KEY_PATH)`
  Remark: Creates or updates a value used by the program.
- Line 106: `        return context`
  Remark: Returns a result to the caller.
- Line 107: ` `
  Remark: Blank line used to separate logical code sections.
- Line 108: `    @staticmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 109: `    def client_context(verify_certificate: bool = False) -> ssl.SSLContext:`
  Remark: Defines a function or method.
- Line 110: `        if verify_certificate:`
  Remark: Checks a condition before choosing what to do.
- Line 111: `            context = ssl.create_default_context(cafile=str(CERT_PATH))`
  Remark: Creates or updates a value used by the program.
- Line 112: `            context.check_hostname = False`
  Remark: Creates or updates a value used by the program.
- Line 113: `            return context`
  Remark: Returns a result to the caller.
- Line 114: ` `
  Remark: Blank line used to separate logical code sections.
- Line 115: `        # Local classroom/demo mode: traffic is encrypted, but the self-signed`
  Remark: A programmer comment that explains the nearby code.
- Line 116: `        # certificate is not authenticated by a public certificate authority.`
  Remark: A programmer comment that explains the nearby code.
- Line 117: `        context = ssl._create_unverified_context()`
  Remark: Creates or updates a value used by the program.
- Line 118: `        context.minimum_version = ssl.TLSVersion.TLSv1_2`
  Remark: Creates or updates a value used by the program.
- Line 119: `        return context`
  Remark: Returns a result to the caller.
- Line 120: ` `
  Remark: Blank line used to separate logical code sections.
- Line 121: `    @staticmethod`
  Remark: Decorator that changes how the next function or method behaves.
- Line 122: `    def ensure_development_certificate() -> None:`
  Remark: Defines a function or method.
- Line 123: `        if (`
  Remark: Checks a condition before choosing what to do.
- Line 124: `            CERT_PATH.exists()`
  Remark: Runs a program instruction for the current feature.
- Line 125: `            and CERT_PATH.stat().st_size > 0`
  Remark: Runs a program instruction for the current feature.
- Line 126: `            and KEY_PATH.exists()`
  Remark: Runs a program instruction for the current feature.
- Line 127: `            and KEY_PATH.stat().st_size > 0`
  Remark: Runs a program instruction for the current feature.
- Line 128: `        ):`
  Remark: Runs a program instruction for the current feature.
- Line 129: `            return`
  Remark: Returns a result to the caller.
- Line 130: ` `
  Remark: Blank line used to separate logical code sections.
- Line 131: `        CERT_DIR.mkdir(parents=True, exist_ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 132: `        try:`
  Remark: Starts error-handling code.
- Line 133: `            from cryptography import x509`
  Remark: Imports code that this file needs.
- Line 134: `            from cryptography.hazmat.primitives import hashes, serialization`
  Remark: Imports code that this file needs.
- Line 135: `            from cryptography.hazmat.primitives.asymmetric import rsa`
  Remark: Imports code that this file needs.
- Line 136: `            from cryptography.x509.oid import NameOID`
  Remark: Imports code that this file needs.
- Line 137: `        except ImportError as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 138: `            raise RuntimeError(`
  Remark: Raises an error when invalid behavior is detected.
- Line 139: `                "Missing TLS certificate. Install dependencies with: pip install -r requirements.txt"`
  Remark: Runs a program instruction for the current feature.
- Line 140: `            ) from exc`
  Remark: Runs a program instruction for the current feature.
- Line 141: ` `
  Remark: Blank line used to separate logical code sections.
- Line 142: `        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)`
  Remark: Creates or updates a value used by the program.
- Line 143: `        subject = issuer = x509.Name(`
  Remark: Creates or updates a value used by the program.
- Line 144: `            [x509.NameAttribute(NameOID.COMMON_NAME, "SecureChatLocal")]`
  Remark: Runs a program instruction for the current feature.
- Line 145: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 146: `        certificate = (`
  Remark: Creates or updates a value used by the program.
- Line 147: `            x509.CertificateBuilder()`
  Remark: Runs a program instruction for the current feature.
- Line 148: `            .subject_name(subject)`
  Remark: Runs a program instruction for the current feature.
- Line 149: `            .issuer_name(issuer)`
  Remark: Runs a program instruction for the current feature.
- Line 150: `            .public_key(private_key.public_key())`
  Remark: Runs a program instruction for the current feature.
- Line 151: `            .serial_number(x509.random_serial_number())`
  Remark: Runs a program instruction for the current feature.
- Line 152: `            .not_valid_before(datetime.now(timezone.utc) - timedelta(days=1))`
  Remark: Creates or updates a value used by the program.
- Line 153: `            .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))`
  Remark: Creates or updates a value used by the program.
- Line 154: `            .sign(private_key, hashes.SHA256())`
  Remark: Runs a program instruction for the current feature.
- Line 155: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 156: ` `
  Remark: Blank line used to separate logical code sections.
- Line 157: `        KEY_PATH.write_bytes(`
  Remark: Runs a program instruction for the current feature.
- Line 158: `            private_key.private_bytes(`
  Remark: Runs a program instruction for the current feature.
- Line 159: `                encoding=serialization.Encoding.PEM,`
  Remark: Creates or updates a value used by the program.
- Line 160: `                format=serialization.PrivateFormat.PKCS8,`
  Remark: Creates or updates a value used by the program.
- Line 161: `                encryption_algorithm=serialization.NoEncryption(),`
  Remark: Creates or updates a value used by the program.
- Line 162: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 163: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 164: `        CERT_PATH.write_bytes(certificate.public_bytes(serialization.Encoding.PEM))`
  Remark: Runs a program instruction for the current feature.
- Line 165: ` `
  Remark: Blank line used to separate logical code sections.

## `secure_chat/server.py`

- Line 1: `import argparse`
  Remark: Imports code that this file needs.
- Line 2: `import base64`
  Remark: Imports code that this file needs.
- Line 3: `import socket`
  Remark: Imports code that this file needs.
- Line 4: `import threading`
  Remark: Imports code that this file needs.
- Line 5: `import uuid`
  Remark: Imports code that this file needs.
- Line 6: `from typing import Optional`
  Remark: Imports code that this file needs.
- Line 7: ` `
  Remark: Blank line used to separate logical code sections.
- Line 8: `from secure_chat.config import DEFAULT_HOST, DEFAULT_PORT, LOG_PATH, MAX_FILE_SIZE, UPLOAD_DIR`
  Remark: Imports code that this file needs.
- Line 9: `from secure_chat.models import ChatMessage, ClientInfo, now_iso`
  Remark: Imports code that this file needs.
- Line 10: `from secure_chat.protocol import ChatProtocol, ProtocolError`
  Remark: Imports code that this file needs.
- Line 11: `from secure_chat.security import InputValidator, TLSContextFactory, ValidationError`
  Remark: Imports code that this file needs.
- Line 12: `from secure_chat.storage import ChatDatabase`
  Remark: Imports code that this file needs.
- Line 13: ` `
  Remark: Blank line used to separate logical code sections.
- Line 14: ` `
  Remark: Blank line used to separate logical code sections.
- Line 15: `class ClientHandler(threading.Thread):`
  Remark: Defines an object-oriented class used by the project.
- Line 16: `    def __init__(`
  Remark: Defines a function or method.
- Line 17: `        self,`
  Remark: Runs a program instruction for the current feature.
- Line 18: `        server: "SecureChatServer",`
  Remark: Runs a program instruction for the current feature.
- Line 19: `        connection: socket.socket,`
  Remark: Runs a program instruction for the current feature.
- Line 20: `        address: tuple[str, int],`
  Remark: Runs a program instruction for the current feature.
- Line 21: `    ) -> None:`
  Remark: Runs a program instruction for the current feature.
- Line 22: `        super().__init__(daemon=True)`
  Remark: Creates or updates a value used by the program.
- Line 23: `        self.server = server`
  Remark: Creates or updates a value used by the program.
- Line 24: `        self.connection = connection`
  Remark: Creates or updates a value used by the program.
- Line 25: `        self.address = f"{address[0]}:{address[1]}"`
  Remark: Creates or updates a value used by the program.
- Line 26: `        self.username: Optional[str] = None`
  Remark: Creates or updates a value used by the program.
- Line 27: `        self.room = "general"`
  Remark: Creates or updates a value used by the program.
- Line 28: `        self.running = True`
  Remark: Creates or updates a value used by the program.
- Line 29: ` `
  Remark: Blank line used to separate logical code sections.
- Line 30: `    def run(self) -> None:`
  Remark: Defines a function or method.
- Line 31: `        try:`
  Remark: Starts error-handling code.
- Line 32: `            ChatProtocol.send(self.connection, "welcome", message="Connected to SecureChat")`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 33: `            while self.running:`
  Remark: Repeats code while a condition remains true.
- Line 34: `                packet = ChatProtocol.receive(self.connection)`
  Remark: Receives data from the network connection.
- Line 35: `                self._handle_packet(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 36: `        except (ConnectionError, OSError, ProtocolError, ValidationError) as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 37: `            self.server.log(f"Client {self.address} disconnected: {exc}")`
  Remark: Runs a program instruction for the current feature.
- Line 38: `        finally:`
  Remark: Runs cleanup code after try/except work finishes.
- Line 39: `            self.running = False`
  Remark: Creates or updates a value used by the program.
- Line 40: `            self.server.remove_client(self)`
  Remark: Runs a program instruction for the current feature.
- Line 41: `            self._safe_close()`
  Remark: Runs a program instruction for the current feature.
- Line 42: ` `
  Remark: Blank line used to separate logical code sections.
- Line 43: `    def send(self, packet_type: str, **fields: object) -> None:`
  Remark: Defines a function or method.
- Line 44: `        ChatProtocol.send(self.connection, packet_type, **fields)`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 45: ` `
  Remark: Blank line used to separate logical code sections.
- Line 46: `    def _handle_packet(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 47: `        packet_type = packet["type"]`
  Remark: Creates or updates a value used by the program.
- Line 48: ` `
  Remark: Blank line used to separate logical code sections.
- Line 49: `        try:`
  Remark: Starts error-handling code.
- Line 50: `            if packet_type == "register":`
  Remark: Checks a condition before choosing what to do.
- Line 51: `                self._register(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 52: `            elif packet_type == "login":`
  Remark: Checks another condition when the previous condition was false.
- Line 53: `                self._login(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 54: `            elif packet_type == "join":`
  Remark: Checks another condition when the previous condition was false.
- Line 55: `                self._require_login()`
  Remark: Runs a program instruction for the current feature.
- Line 56: `                self._join(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 57: `            elif packet_type == "create_room":`
  Remark: Checks another condition when the previous condition was false.
- Line 58: `                self._require_login()`
  Remark: Runs a program instruction for the current feature.
- Line 59: `                self._create_room(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 60: `            elif packet_type == "rooms":`
  Remark: Checks another condition when the previous condition was false.
- Line 61: `                self._require_login()`
  Remark: Runs a program instruction for the current feature.
- Line 62: `                self._rooms()`
  Remark: Runs a program instruction for the current feature.
- Line 63: `            elif packet_type == "message":`
  Remark: Checks another condition when the previous condition was false.
- Line 64: `                self._require_login()`
  Remark: Runs a program instruction for the current feature.
- Line 65: `                self._message(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 66: `            elif packet_type == "file":`
  Remark: Checks another condition when the previous condition was false.
- Line 67: `                self._require_login()`
  Remark: Runs a program instruction for the current feature.
- Line 68: `                self._file(packet)`
  Remark: Runs a program instruction for the current feature.
- Line 69: `            elif packet_type == "users":`
  Remark: Checks another condition when the previous condition was false.
- Line 70: `                self._require_login()`
  Remark: Runs a program instruction for the current feature.
- Line 71: `                self._users()`
  Remark: Runs a program instruction for the current feature.
- Line 72: `            elif packet_type == "history":`
  Remark: Checks another condition when the previous condition was false.
- Line 73: `                self._require_login()`
  Remark: Runs a program instruction for the current feature.
- Line 74: `                self._history()`
  Remark: Runs a program instruction for the current feature.
- Line 75: `            elif packet_type == "logout":`
  Remark: Checks another condition when the previous condition was false.
- Line 76: `                self.running = False`
  Remark: Creates or updates a value used by the program.
- Line 77: `            else:`
  Remark: Runs when the previous conditions were false.
- Line 78: `                raise ProtocolError(f"Unknown packet type: {packet_type}")`
  Remark: Raises an error when invalid behavior is detected.
- Line 79: `        except ValidationError as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 80: `            self.send("error", action=packet_type, message=str(exc))`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 81: ` `
  Remark: Blank line used to separate logical code sections.
- Line 82: `    def _register(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 83: `        username = InputValidator.username(str(packet.get("username", "")))`
  Remark: Creates or updates a value used by the program.
- Line 84: `        password = InputValidator.password(str(packet.get("password", "")))`
  Remark: Creates or updates a value used by the program.
- Line 85: `        created = self.server.database.create_user(username, password)`
  Remark: Creates or updates a value used by the program.
- Line 86: ` `
  Remark: Blank line used to separate logical code sections.
- Line 87: `        if not created:`
  Remark: Checks a condition before choosing what to do.
- Line 88: `            self.send("error", action="register", message="Username already exists")`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 89: `            return`
  Remark: Returns a result to the caller.
- Line 90: ` `
  Remark: Blank line used to separate logical code sections.
- Line 91: `        self.send("ok", action="register", message="Registration successful")`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 92: ` `
  Remark: Blank line used to separate logical code sections.
- Line 93: `    def _login(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 94: `        username = InputValidator.username(str(packet.get("username", "")))`
  Remark: Creates or updates a value used by the program.
- Line 95: `        password = InputValidator.password(str(packet.get("password", "")))`
  Remark: Creates or updates a value used by the program.
- Line 96: ` `
  Remark: Blank line used to separate logical code sections.
- Line 97: `        if not self.server.database.authenticate(username, password):`
  Remark: Checks a condition before choosing what to do.
- Line 98: `            self.server.database.log_event("login_failed", f"Failed login for {username}")`
  Remark: Runs a program instruction for the current feature.
- Line 99: `            self.send("error", action="login", message="Invalid username or password")`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 100: `            return`
  Remark: Returns a result to the caller.
- Line 101: ` `
  Remark: Blank line used to separate logical code sections.
- Line 102: `        self.username = username`
  Remark: Creates or updates a value used by the program.
- Line 103: `        self.server.add_client(self)`
  Remark: Runs a program instruction for the current feature.
- Line 104: `        self.send("ok", action="login", message=f"Logged in as {username}")`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 105: `        self._rooms()`
  Remark: Runs a program instruction for the current feature.
- Line 106: `        self._history()`
  Remark: Runs a program instruction for the current feature.
- Line 107: `        self.server.broadcast_system(f"{username} joined {self.room}", self.room)`
  Remark: Runs a program instruction for the current feature.
- Line 108: ` `
  Remark: Blank line used to separate logical code sections.
- Line 109: `    def _join(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 110: `        old_room = self.room`
  Remark: Creates or updates a value used by the program.
- Line 111: `        requested_room = InputValidator.room(str(packet.get("room", "general")))`
  Remark: Creates or updates a value used by the program.
- Line 112: `        if not self.server.database.room_exists(requested_room):`
  Remark: Checks a condition before choosing what to do.
- Line 113: `            self.send("error", action="join", message="Room does not exist. Create it first.")`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 114: `            return`
  Remark: Returns a result to the caller.
- Line 115: ` `
  Remark: Blank line used to separate logical code sections.
- Line 116: `        self.room = requested_room`
  Remark: Creates or updates a value used by the program.
- Line 117: `        self.send("ok", action="join", room=self.room, message=f"Joined room {self.room}")`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 118: `        self._rooms()`
  Remark: Runs a program instruction for the current feature.
- Line 119: `        self._history()`
  Remark: Runs a program instruction for the current feature.
- Line 120: `        self.server.broadcast_system(f"{self.username} left {old_room}", old_room)`
  Remark: Runs a program instruction for the current feature.
- Line 121: `        self.server.broadcast_system(f"{self.username} joined {self.room}", self.room)`
  Remark: Runs a program instruction for the current feature.
- Line 122: ` `
  Remark: Blank line used to separate logical code sections.
- Line 123: `    def _create_room(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 124: `        assert self.username is not None`
  Remark: Documents and checks an assumption in the code.
- Line 125: `        room = InputValidator.room(str(packet.get("room", "")))`
  Remark: Creates or updates a value used by the program.
- Line 126: `        created = self.server.database.create_room(room, self.username)`
  Remark: Creates or updates a value used by the program.
- Line 127: ` `
  Remark: Blank line used to separate logical code sections.
- Line 128: `        if not created:`
  Remark: Checks a condition before choosing what to do.
- Line 129: `            self.send("error", action="create_room", message="Room already exists")`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 130: `            return`
  Remark: Returns a result to the caller.
- Line 131: ` `
  Remark: Blank line used to separate logical code sections.
- Line 132: `        self.send("ok", action="create_room", room=room, message=f"Room {room} created")`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 133: `        self.server.broadcast_rooms()`
  Remark: Runs a program instruction for the current feature.
- Line 134: ` `
  Remark: Blank line used to separate logical code sections.
- Line 135: `    def _message(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 136: `        body = InputValidator.message(str(packet.get("body", "")))`
  Remark: Creates or updates a value used by the program.
- Line 137: `        assert self.username is not None`
  Remark: Documents and checks an assumption in the code.
- Line 138: ` `
  Remark: Blank line used to separate logical code sections.
- Line 139: `        message = ChatMessage(`
  Remark: Creates or updates a value used by the program.
- Line 140: `            sender=self.username,`
  Remark: Creates or updates a value used by the program.
- Line 141: `            room=self.room,`
  Remark: Creates or updates a value used by the program.
- Line 142: `            body=body,`
  Remark: Creates or updates a value used by the program.
- Line 143: `            created_at=now_iso(),`
  Remark: Creates or updates a value used by the program.
- Line 144: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 145: `        self.server.database.save_message(message)`
  Remark: Runs a program instruction for the current feature.
- Line 146: `        self.server.broadcast_chat(message)`
  Remark: Runs a program instruction for the current feature.
- Line 147: ` `
  Remark: Blank line used to separate logical code sections.
- Line 148: `    def _file(self, packet: dict[str, object]) -> None:`
  Remark: Defines a function or method.
- Line 149: `        assert self.username is not None`
  Remark: Documents and checks an assumption in the code.
- Line 150: ` `
  Remark: Blank line used to separate logical code sections.
- Line 151: `        filename = InputValidator.filename(str(packet.get("filename", "")))`
  Remark: Creates or updates a value used by the program.
- Line 152: `        kind = str(packet.get("kind", "file"))`
  Remark: Creates or updates a value used by the program.
- Line 153: `        encoded_data = str(packet.get("data", ""))`
  Remark: Creates or updates a value used by the program.
- Line 154: ` `
  Remark: Blank line used to separate logical code sections.
- Line 155: `        try:`
  Remark: Starts error-handling code.
- Line 156: `            file_data = base64.b64decode(encoded_data.encode("ascii"), validate=True)`
  Remark: Creates or updates a value used by the program.
- Line 157: `        except Exception as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 158: `            raise ValidationError("File data is not valid base64") from exc`
  Remark: Raises an error when invalid behavior is detected.
- Line 159: ` `
  Remark: Blank line used to separate logical code sections.
- Line 160: `        if len(file_data) > MAX_FILE_SIZE:`
  Remark: Checks a condition before choosing what to do.
- Line 161: `            raise ValidationError(f"File is too large. Maximum size is {MAX_FILE_SIZE // (1024 * 1024)} MB")`
  Remark: Raises an error when invalid behavior is detected.
- Line 162: ` `
  Remark: Blank line used to separate logical code sections.
- Line 163: `        room_upload_dir = UPLOAD_DIR / self.room`
  Remark: Creates or updates a value used by the program.
- Line 164: `        room_upload_dir.mkdir(parents=True, exist_ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 165: `        stored_filename = f"{uuid.uuid4().hex}_{filename}"`
  Remark: Creates or updates a value used by the program.
- Line 166: `        (room_upload_dir / stored_filename).write_bytes(file_data)`
  Remark: Runs a program instruction for the current feature.
- Line 167: ` `
  Remark: Blank line used to separate logical code sections.
- Line 168: `        created_at = now_iso()`
  Remark: Creates or updates a value used by the program.
- Line 169: `        message = ChatMessage(`
  Remark: Creates or updates a value used by the program.
- Line 170: `            sender=self.username,`
  Remark: Creates or updates a value used by the program.
- Line 171: `            room=self.room,`
  Remark: Creates or updates a value used by the program.
- Line 172: `            body=f"[{kind}] {filename}",`
  Remark: Creates or updates a value used by the program.
- Line 173: `            created_at=created_at,`
  Remark: Creates or updates a value used by the program.
- Line 174: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 175: `        self.server.database.save_message(message)`
  Remark: Runs a program instruction for the current feature.
- Line 176: `        self.server.broadcast_file(`
  Remark: Runs a program instruction for the current feature.
- Line 177: `            sender=self.username,`
  Remark: Creates or updates a value used by the program.
- Line 178: `            room=self.room,`
  Remark: Creates or updates a value used by the program.
- Line 179: `            filename=filename,`
  Remark: Creates or updates a value used by the program.
- Line 180: `            kind=kind,`
  Remark: Creates or updates a value used by the program.
- Line 181: `            size=len(file_data),`
  Remark: Creates or updates a value used by the program.
- Line 182: `            data=encoded_data,`
  Remark: Creates or updates a value used by the program.
- Line 183: `            created_at=created_at,`
  Remark: Creates or updates a value used by the program.
- Line 184: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 185: ` `
  Remark: Blank line used to separate logical code sections.
- Line 186: `    def _users(self) -> None:`
  Remark: Defines a function or method.
- Line 187: `        users = [user.username for user in self.server.database.list_users()]`
  Remark: Creates or updates a value used by the program.
- Line 188: `        online = self.server.online_clients()`
  Remark: Creates or updates a value used by the program.
- Line 189: `        self.send("users", registered=users, online=online)`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 190: ` `
  Remark: Blank line used to separate logical code sections.
- Line 191: `    def _rooms(self) -> None:`
  Remark: Defines a function or method.
- Line 192: `        self.send("rooms", rooms=self.server.database.list_rooms(), current=self.room)`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 193: ` `
  Remark: Blank line used to separate logical code sections.
- Line 194: `    def _history(self) -> None:`
  Remark: Defines a function or method.
- Line 195: `        messages = [`
  Remark: Creates or updates a value used by the program.
- Line 196: `            {`
  Remark: Runs a program instruction for the current feature.
- Line 197: `                "sender": message.sender,`
  Remark: Runs a program instruction for the current feature.
- Line 198: `                "room": message.room,`
  Remark: Runs a program instruction for the current feature.
- Line 199: `                "body": message.body,`
  Remark: Runs a program instruction for the current feature.
- Line 200: `                "created_at": message.created_at,`
  Remark: Runs a program instruction for the current feature.
- Line 201: `            }`
  Remark: Runs a program instruction for the current feature.
- Line 202: `            for message in self.server.database.recent_messages(self.room)`
  Remark: Loops over multiple values.
- Line 203: `        ]`
  Remark: Runs a program instruction for the current feature.
- Line 204: `        self.send("history", room=self.room, messages=messages)`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 205: ` `
  Remark: Blank line used to separate logical code sections.
- Line 206: `    def _require_login(self) -> None:`
  Remark: Defines a function or method.
- Line 207: `        if self.username is None:`
  Remark: Checks a condition before choosing what to do.
- Line 208: `            raise ProtocolError("Login required")`
  Remark: Raises an error when invalid behavior is detected.
- Line 209: ` `
  Remark: Blank line used to separate logical code sections.
- Line 210: `    def _safe_close(self) -> None:`
  Remark: Defines a function or method.
- Line 211: `        try:`
  Remark: Starts error-handling code.
- Line 212: `            self.connection.close()`
  Remark: Runs a program instruction for the current feature.
- Line 213: `        except OSError:`
  Remark: Handles an expected error so the program does not crash.
- Line 214: `            pass`
  Remark: Runs a program instruction for the current feature.
- Line 215: ` `
  Remark: Blank line used to separate logical code sections.
- Line 216: ` `
  Remark: Blank line used to separate logical code sections.
- Line 217: `class SecureChatServer:`
  Remark: Defines an object-oriented class used by the project.
- Line 218: `    def __init__(self, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> None:`
  Remark: Defines a function or method.
- Line 219: `        self.host = host`
  Remark: Creates or updates a value used by the program.
- Line 220: `        self.port = port`
  Remark: Creates or updates a value used by the program.
- Line 221: `        self.database = ChatDatabase()`
  Remark: Creates or updates a value used by the program.
- Line 222: `        self.clients: set[ClientHandler] = set()`
  Remark: Creates or updates a value used by the program.
- Line 223: `        self.clients_lock = threading.Lock()`
  Remark: Creates or updates a value used by the program.
- Line 224: `        self.running = False`
  Remark: Creates or updates a value used by the program.
- Line 225: ` `
  Remark: Blank line used to separate logical code sections.
- Line 226: `    def start(self) -> None:`
  Remark: Defines a function or method.
- Line 227: `        context = TLSContextFactory.server_context()`
  Remark: Creates or updates a value used by the program.
- Line 228: `        self.running = True`
  Remark: Creates or updates a value used by the program.
- Line 229: ` `
  Remark: Blank line used to separate logical code sections.
- Line 230: `        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:`
  Remark: Opens a managed resource and closes it safely.
- Line 231: `            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`
  Remark: Runs a program instruction for the current feature.
- Line 232: `            server_socket.bind((self.host, self.port))`
  Remark: Runs a program instruction for the current feature.
- Line 233: `            server_socket.listen()`
  Remark: Runs a program instruction for the current feature.
- Line 234: `            self.log(f"Server listening on {self.host}:{self.port}")`
  Remark: Runs a program instruction for the current feature.
- Line 235: ` `
  Remark: Blank line used to separate logical code sections.
- Line 236: `            while self.running:`
  Remark: Repeats code while a condition remains true.
- Line 237: `                raw_connection, address = server_socket.accept()`
  Remark: Creates or updates a value used by the program.
- Line 238: `                try:`
  Remark: Starts error-handling code.
- Line 239: `                    tls_connection = context.wrap_socket(raw_connection, server_side=True)`
  Remark: Creates or updates a value used by the program.
- Line 240: `                except OSError as exc:`
  Remark: Handles an expected error so the program does not crash.
- Line 241: `                    self.log(f"TLS handshake failed from {address}: {exc}")`
  Remark: Runs a program instruction for the current feature.
- Line 242: `                    raw_connection.close()`
  Remark: Runs a program instruction for the current feature.
- Line 243: `                    continue`
  Remark: Runs a program instruction for the current feature.
- Line 244: ` `
  Remark: Blank line used to separate logical code sections.
- Line 245: `                ClientHandler(self, tls_connection, address).start()`
  Remark: Runs a program instruction for the current feature.
- Line 246: ` `
  Remark: Blank line used to separate logical code sections.
- Line 247: `    def add_client(self, client: ClientHandler) -> None:`
  Remark: Defines a function or method.
- Line 248: `        with self.clients_lock:`
  Remark: Opens a managed resource and closes it safely.
- Line 249: `            self.clients.add(client)`
  Remark: Runs a program instruction for the current feature.
- Line 250: `        self.database.log_event("login", f"{client.username} logged in from {client.address}")`
  Remark: Runs a program instruction for the current feature.
- Line 251: ` `
  Remark: Blank line used to separate logical code sections.
- Line 252: `    def remove_client(self, client: ClientHandler) -> None:`
  Remark: Defines a function or method.
- Line 253: `        removed = False`
  Remark: Creates or updates a value used by the program.
- Line 254: `        with self.clients_lock:`
  Remark: Opens a managed resource and closes it safely.
- Line 255: `            if client in self.clients:`
  Remark: Checks a condition before choosing what to do.
- Line 256: `                self.clients.remove(client)`
  Remark: Runs a program instruction for the current feature.
- Line 257: `                removed = True`
  Remark: Creates or updates a value used by the program.
- Line 258: ` `
  Remark: Blank line used to separate logical code sections.
- Line 259: `        if removed and client.username:`
  Remark: Checks a condition before choosing what to do.
- Line 260: `            self.broadcast_system(f"{client.username} disconnected", client.room)`
  Remark: Runs a program instruction for the current feature.
- Line 261: `            self.database.log_event("disconnect", f"{client.username} disconnected")`
  Remark: Runs a program instruction for the current feature.
- Line 262: ` `
  Remark: Blank line used to separate logical code sections.
- Line 263: `    def broadcast_chat(self, message: ChatMessage) -> None:`
  Remark: Defines a function or method.
- Line 264: `        payload = {`
  Remark: Creates or updates a value used by the program.
- Line 265: `            "sender": message.sender,`
  Remark: Runs a program instruction for the current feature.
- Line 266: `            "room": message.room,`
  Remark: Runs a program instruction for the current feature.
- Line 267: `            "body": message.body,`
  Remark: Runs a program instruction for the current feature.
- Line 268: `            "created_at": message.created_at,`
  Remark: Runs a program instruction for the current feature.
- Line 269: `        }`
  Remark: Runs a program instruction for the current feature.
- Line 270: `        self._broadcast_to_room(message.room, "message", **payload)`
  Remark: Runs a program instruction for the current feature.
- Line 271: ` `
  Remark: Blank line used to separate logical code sections.
- Line 272: `    def broadcast_file(`
  Remark: Defines a function or method.
- Line 273: `        self,`
  Remark: Runs a program instruction for the current feature.
- Line 274: `        sender: str,`
  Remark: Runs a program instruction for the current feature.
- Line 275: `        room: str,`
  Remark: Runs a program instruction for the current feature.
- Line 276: `        filename: str,`
  Remark: Runs a program instruction for the current feature.
- Line 277: `        kind: str,`
  Remark: Runs a program instruction for the current feature.
- Line 278: `        size: int,`
  Remark: Runs a program instruction for the current feature.
- Line 279: `        data: str,`
  Remark: Runs a program instruction for the current feature.
- Line 280: `        created_at: str,`
  Remark: Runs a program instruction for the current feature.
- Line 281: `    ) -> None:`
  Remark: Runs a program instruction for the current feature.
- Line 282: `        self._broadcast_to_room(`
  Remark: Runs a program instruction for the current feature.
- Line 283: `            room,`
  Remark: Runs a program instruction for the current feature.
- Line 284: `            "file",`
  Remark: Runs a program instruction for the current feature.
- Line 285: `            sender=sender,`
  Remark: Creates or updates a value used by the program.
- Line 286: `            room=room,`
  Remark: Creates or updates a value used by the program.
- Line 287: `            filename=filename,`
  Remark: Creates or updates a value used by the program.
- Line 288: `            kind=kind,`
  Remark: Creates or updates a value used by the program.
- Line 289: `            size=size,`
  Remark: Creates or updates a value used by the program.
- Line 290: `            data=data,`
  Remark: Creates or updates a value used by the program.
- Line 291: `            created_at=created_at,`
  Remark: Creates or updates a value used by the program.
- Line 292: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 293: ` `
  Remark: Blank line used to separate logical code sections.
- Line 294: `    def broadcast_system(self, text: str, room: str) -> None:`
  Remark: Defines a function or method.
- Line 295: `        self._broadcast_to_room(room, "system", room=room, message=text, created_at=now_iso())`
  Remark: Creates or updates a value used by the program.
- Line 296: ` `
  Remark: Blank line used to separate logical code sections.
- Line 297: `    def broadcast_rooms(self) -> None:`
  Remark: Defines a function or method.
- Line 298: `        rooms = self.database.list_rooms()`
  Remark: Creates or updates a value used by the program.
- Line 299: `        with self.clients_lock:`
  Remark: Opens a managed resource and closes it safely.
- Line 300: `            clients = list(self.clients)`
  Remark: Creates or updates a value used by the program.
- Line 301: ` `
  Remark: Blank line used to separate logical code sections.
- Line 302: `        for client in clients:`
  Remark: Loops over multiple values.
- Line 303: `            try:`
  Remark: Starts error-handling code.
- Line 304: `                client.send("rooms", rooms=rooms, current=client.room)`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 305: `            except OSError:`
  Remark: Handles an expected error so the program does not crash.
- Line 306: `                client.running = False`
  Remark: Creates or updates a value used by the program.
- Line 307: ` `
  Remark: Blank line used to separate logical code sections.
- Line 308: `    def online_clients(self) -> list[dict[str, str]]:`
  Remark: Defines a function or method.
- Line 309: `        with self.clients_lock:`
  Remark: Opens a managed resource and closes it safely.
- Line 310: `            return [`
  Remark: Returns a result to the caller.
- Line 311: `                ClientInfo(`
  Remark: Runs a program instruction for the current feature.
- Line 312: `                    username=client.username or "anonymous",`
  Remark: Creates or updates a value used by the program.
- Line 313: `                    room=client.room,`
  Remark: Creates or updates a value used by the program.
- Line 314: `                    address=client.address,`
  Remark: Creates or updates a value used by the program.
- Line 315: `                ).__dict__`
  Remark: Runs a program instruction for the current feature.
- Line 316: `                for client in self.clients`
  Remark: Loops over multiple values.
- Line 317: `                if client.username`
  Remark: Checks a condition before choosing what to do.
- Line 318: `            ]`
  Remark: Runs a program instruction for the current feature.
- Line 319: ` `
  Remark: Blank line used to separate logical code sections.
- Line 320: `    def _broadcast_to_room(self, target_room: str, packet_type: str, **fields: object) -> None:`
  Remark: Defines a function or method.
- Line 321: `        with self.clients_lock:`
  Remark: Opens a managed resource and closes it safely.
- Line 322: `            clients = [client for client in self.clients if client.room == target_room]`
  Remark: Creates or updates a value used by the program.
- Line 323: ` `
  Remark: Blank line used to separate logical code sections.
- Line 324: `        for client in clients:`
  Remark: Loops over multiple values.
- Line 325: `            try:`
  Remark: Starts error-handling code.
- Line 326: `                client.send(packet_type, **fields)`
  Remark: Sends data through the custom chat protocol or GUI command.
- Line 327: `            except OSError:`
  Remark: Handles an expected error so the program does not crash.
- Line 328: `                client.running = False`
  Remark: Creates or updates a value used by the program.
- Line 329: ` `
  Remark: Blank line used to separate logical code sections.
- Line 330: `    def log(self, message: str) -> None:`
  Remark: Defines a function or method.
- Line 331: `        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 332: `        line = f"[{now_iso()}] {message}"`
  Remark: Creates or updates a value used by the program.
- Line 333: `        print(line)`
  Remark: Runs a program instruction for the current feature.
- Line 334: `        with LOG_PATH.open("a", encoding="utf-8") as log_file:`
  Remark: Opens a managed resource and closes it safely.
- Line 335: `            log_file.write(line + "\n")`
  Remark: Runs a program instruction for the current feature.
- Line 336: ` `
  Remark: Blank line used to separate logical code sections.
- Line 337: ` `
  Remark: Blank line used to separate logical code sections.
- Line 338: `def parse_args() -> argparse.Namespace:`
  Remark: Defines a function or method.
- Line 339: `    parser = argparse.ArgumentParser(description="SecureChat threaded TLS server")`
  Remark: Creates or updates a value used by the program.
- Line 340: `    parser.add_argument("--host", default=DEFAULT_HOST)`
  Remark: Creates or updates a value used by the program.
- Line 341: `    parser.add_argument("--port", type=int, default=DEFAULT_PORT)`
  Remark: Creates or updates a value used by the program.
- Line 342: `    return parser.parse_args()`
  Remark: Returns a result to the caller.
- Line 343: ` `
  Remark: Blank line used to separate logical code sections.
- Line 344: ` `
  Remark: Blank line used to separate logical code sections.
- Line 345: `if __name__ == "__main__":`
  Remark: Checks a condition before choosing what to do.
- Line 346: `    args = parse_args()`
  Remark: Creates or updates a value used by the program.
- Line 347: `    SecureChatServer(host=args.host, port=args.port).start()`
  Remark: Creates or updates a value used by the program.
- Line 348: ` `
  Remark: Blank line used to separate logical code sections.

## `secure_chat/storage.py`

- Line 1: `import sqlite3`
  Remark: Imports code that this file needs.
- Line 2: `import threading`
  Remark: Imports code that this file needs.
- Line 3: `from pathlib import Path`
  Remark: Imports code that this file needs.
- Line 4: ` `
  Remark: Blank line used to separate logical code sections.
- Line 5: `from secure_chat.config import DATABASE_PATH, DATA_DIR`
  Remark: Imports code that this file needs.
- Line 6: `from secure_chat.models import ChatMessage, User, now_iso`
  Remark: Imports code that this file needs.
- Line 7: `from secure_chat.security import PasswordHasher`
  Remark: Imports code that this file needs.
- Line 8: ` `
  Remark: Blank line used to separate logical code sections.
- Line 9: ` `
  Remark: Blank line used to separate logical code sections.
- Line 10: `class ChatDatabase:`
  Remark: Defines an object-oriented class used by the project.
- Line 11: `    def __init__(self, path: Path = DATABASE_PATH) -> None:`
  Remark: Defines a function or method.
- Line 12: `        self.path = path`
  Remark: Creates or updates a value used by the program.
- Line 13: `        self._lock = threading.Lock()`
  Remark: Creates or updates a value used by the program.
- Line 14: `        DATA_DIR.mkdir(parents=True, exist_ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 15: `        self._initialize()`
  Remark: Runs a program instruction for the current feature.
- Line 16: ` `
  Remark: Blank line used to separate logical code sections.
- Line 17: `    def _connect(self) -> sqlite3.Connection:`
  Remark: Defines a function or method.
- Line 18: `        connection = sqlite3.connect(self.path, check_same_thread=False)`
  Remark: Creates or updates a value used by the program.
- Line 19: `        connection.row_factory = sqlite3.Row`
  Remark: Creates or updates a value used by the program.
- Line 20: `        return connection`
  Remark: Returns a result to the caller.
- Line 21: ` `
  Remark: Blank line used to separate logical code sections.
- Line 22: `    def _initialize(self) -> None:`
  Remark: Defines a function or method.
- Line 23: `        with self._connect() as connection:`
  Remark: Opens a managed resource and closes it safely.
- Line 24: `            connection.execute(`
  Remark: Runs a program instruction for the current feature.
- Line 25: `                """`
  Remark: Documentation string that explains a module, class, or function.
- Line 26: `                CREATE TABLE IF NOT EXISTS users (`
  Remark: Runs a program instruction for the current feature.
- Line 27: `                    username TEXT PRIMARY KEY,`
  Remark: Runs a program instruction for the current feature.
- Line 28: `                    password_hash TEXT NOT NULL,`
  Remark: Runs a program instruction for the current feature.
- Line 29: `                    created_at TEXT NOT NULL`
  Remark: Runs a program instruction for the current feature.
- Line 30: `                )`
  Remark: Runs a program instruction for the current feature.
- Line 31: `                """`
  Remark: Documentation string that explains a module, class, or function.
- Line 32: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 33: `            connection.execute(`
  Remark: Runs a program instruction for the current feature.
- Line 34: `                """`
  Remark: Documentation string that explains a module, class, or function.
- Line 35: `                CREATE TABLE IF NOT EXISTS messages (`
  Remark: Runs a program instruction for the current feature.
- Line 36: `                    id INTEGER PRIMARY KEY AUTOINCREMENT,`
  Remark: Runs a program instruction for the current feature.
- Line 37: `                    sender TEXT NOT NULL,`
  Remark: Runs a program instruction for the current feature.
- Line 38: `                    room TEXT NOT NULL,`
  Remark: Runs a program instruction for the current feature.
- Line 39: `                    body TEXT NOT NULL,`
  Remark: Runs a program instruction for the current feature.
- Line 40: `                    created_at TEXT NOT NULL,`
  Remark: Runs a program instruction for the current feature.
- Line 41: `                    FOREIGN KEY(sender) REFERENCES users(username)`
  Remark: Runs a program instruction for the current feature.
- Line 42: `                )`
  Remark: Runs a program instruction for the current feature.
- Line 43: `                """`
  Remark: Documentation string that explains a module, class, or function.
- Line 44: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 45: `            connection.execute(`
  Remark: Runs a program instruction for the current feature.
- Line 46: `                """`
  Remark: Documentation string that explains a module, class, or function.
- Line 47: `                CREATE TABLE IF NOT EXISTS rooms (`
  Remark: Runs a program instruction for the current feature.
- Line 48: `                    name TEXT PRIMARY KEY,`
  Remark: Runs a program instruction for the current feature.
- Line 49: `                    created_by TEXT NOT NULL,`
  Remark: Runs a program instruction for the current feature.
- Line 50: `                    created_at TEXT NOT NULL`
  Remark: Runs a program instruction for the current feature.
- Line 51: `                )`
  Remark: Runs a program instruction for the current feature.
- Line 52: `                """`
  Remark: Documentation string that explains a module, class, or function.
- Line 53: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 54: `            connection.execute(`
  Remark: Runs a program instruction for the current feature.
- Line 55: `                """`
  Remark: Documentation string that explains a module, class, or function.
- Line 56: `                CREATE TABLE IF NOT EXISTS audit_log (`
  Remark: Runs a program instruction for the current feature.
- Line 57: `                    id INTEGER PRIMARY KEY AUTOINCREMENT,`
  Remark: Runs a program instruction for the current feature.
- Line 58: `                    event_type TEXT NOT NULL,`
  Remark: Runs a program instruction for the current feature.
- Line 59: `                    details TEXT NOT NULL,`
  Remark: Runs a program instruction for the current feature.
- Line 60: `                    created_at TEXT NOT NULL`
  Remark: Runs a program instruction for the current feature.
- Line 61: `                )`
  Remark: Runs a program instruction for the current feature.
- Line 62: `                """`
  Remark: Documentation string that explains a module, class, or function.
- Line 63: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 64: `            connection.execute(`
  Remark: Runs a program instruction for the current feature.
- Line 65: `                "INSERT OR IGNORE INTO rooms(name, created_by, created_at) VALUES (?, ?, ?)",`
  Remark: Runs a program instruction for the current feature.
- Line 66: `                ("general", "system", now_iso()),`
  Remark: Runs a program instruction for the current feature.
- Line 67: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 68: ` `
  Remark: Blank line used to separate logical code sections.
- Line 69: `    def create_user(self, username: str, password: str) -> bool:`
  Remark: Defines a function or method.
- Line 70: `        password_hash = PasswordHasher.hash_password(password)`
  Remark: Creates or updates a value used by the program.
- Line 71: `        with self._lock, self._connect() as connection:`
  Remark: Opens a managed resource and closes it safely.
- Line 72: `            try:`
  Remark: Starts error-handling code.
- Line 73: `                connection.execute(`
  Remark: Runs a program instruction for the current feature.
- Line 74: `                    "INSERT INTO users(username, password_hash, created_at) VALUES (?, ?, ?)",`
  Remark: Runs a program instruction for the current feature.
- Line 75: `                    (username, password_hash, now_iso()),`
  Remark: Runs a program instruction for the current feature.
- Line 76: `                )`
  Remark: Runs a program instruction for the current feature.
- Line 77: `            except sqlite3.IntegrityError:`
  Remark: Handles an expected error so the program does not crash.
- Line 78: `                return False`
  Remark: Returns a result to the caller.
- Line 79: `        self.log_event("register", f"User registered: {username}")`
  Remark: Runs a program instruction for the current feature.
- Line 80: `        return True`
  Remark: Returns a result to the caller.
- Line 81: ` `
  Remark: Blank line used to separate logical code sections.
- Line 82: `    def authenticate(self, username: str, password: str) -> bool:`
  Remark: Defines a function or method.
- Line 83: `        with self._lock, self._connect() as connection:`
  Remark: Opens a managed resource and closes it safely.
- Line 84: `            row = connection.execute(`
  Remark: Creates or updates a value used by the program.
- Line 85: `                "SELECT password_hash FROM users WHERE username = ?",`
  Remark: Creates or updates a value used by the program.
- Line 86: `                (username,),`
  Remark: Runs a program instruction for the current feature.
- Line 87: `            ).fetchone()`
  Remark: Runs a program instruction for the current feature.
- Line 88: ` `
  Remark: Blank line used to separate logical code sections.
- Line 89: `        if row is None:`
  Remark: Checks a condition before choosing what to do.
- Line 90: `            return False`
  Remark: Returns a result to the caller.
- Line 91: ` `
  Remark: Blank line used to separate logical code sections.
- Line 92: `        return PasswordHasher.verify_password(password, row["password_hash"])`
  Remark: Returns a result to the caller.
- Line 93: ` `
  Remark: Blank line used to separate logical code sections.
- Line 94: `    def save_message(self, message: ChatMessage) -> None:`
  Remark: Defines a function or method.
- Line 95: `        with self._lock, self._connect() as connection:`
  Remark: Opens a managed resource and closes it safely.
- Line 96: `            connection.execute(`
  Remark: Runs a program instruction for the current feature.
- Line 97: `                "INSERT OR IGNORE INTO rooms(name, created_by, created_at) VALUES (?, ?, ?)",`
  Remark: Runs a program instruction for the current feature.
- Line 98: `                (message.room, message.sender, now_iso()),`
  Remark: Runs a program instruction for the current feature.
- Line 99: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 100: `            connection.execute(`
  Remark: Runs a program instruction for the current feature.
- Line 101: `                "INSERT INTO messages(sender, room, body, created_at) VALUES (?, ?, ?, ?)",`
  Remark: Runs a program instruction for the current feature.
- Line 102: `                (message.sender, message.room, message.body, message.created_at),`
  Remark: Runs a program instruction for the current feature.
- Line 103: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 104: ` `
  Remark: Blank line used to separate logical code sections.
- Line 105: `    def create_room(self, room: str, created_by: str) -> bool:`
  Remark: Defines a function or method.
- Line 106: `        with self._lock, self._connect() as connection:`
  Remark: Opens a managed resource and closes it safely.
- Line 107: `            try:`
  Remark: Starts error-handling code.
- Line 108: `                connection.execute(`
  Remark: Runs a program instruction for the current feature.
- Line 109: `                    "INSERT INTO rooms(name, created_by, created_at) VALUES (?, ?, ?)",`
  Remark: Runs a program instruction for the current feature.
- Line 110: `                    (room, created_by, now_iso()),`
  Remark: Runs a program instruction for the current feature.
- Line 111: `                )`
  Remark: Runs a program instruction for the current feature.
- Line 112: `            except sqlite3.IntegrityError:`
  Remark: Handles an expected error so the program does not crash.
- Line 113: `                return False`
  Remark: Returns a result to the caller.
- Line 114: `        self.log_event("room_created", f"{created_by} created room {room}")`
  Remark: Runs a program instruction for the current feature.
- Line 115: `        return True`
  Remark: Returns a result to the caller.
- Line 116: ` `
  Remark: Blank line used to separate logical code sections.
- Line 117: `    def room_exists(self, room: str) -> bool:`
  Remark: Defines a function or method.
- Line 118: `        with self._lock, self._connect() as connection:`
  Remark: Opens a managed resource and closes it safely.
- Line 119: `            row = connection.execute(`
  Remark: Creates or updates a value used by the program.
- Line 120: `                "SELECT 1 FROM rooms WHERE name = ?",`
  Remark: Creates or updates a value used by the program.
- Line 121: `                (room,),`
  Remark: Runs a program instruction for the current feature.
- Line 122: `            ).fetchone()`
  Remark: Runs a program instruction for the current feature.
- Line 123: `        return row is not None`
  Remark: Returns a result to the caller.
- Line 124: ` `
  Remark: Blank line used to separate logical code sections.
- Line 125: `    def list_rooms(self) -> list[str]:`
  Remark: Defines a function or method.
- Line 126: `        with self._lock, self._connect() as connection:`
  Remark: Opens a managed resource and closes it safely.
- Line 127: `            rows = connection.execute("SELECT name FROM rooms ORDER BY name").fetchall()`
  Remark: Creates or updates a value used by the program.
- Line 128: `        return [row["name"] for row in rows]`
  Remark: Returns a result to the caller.
- Line 129: ` `
  Remark: Blank line used to separate logical code sections.
- Line 130: `    def recent_messages(self, room: str, limit: int = 50) -> list[ChatMessage]:`
  Remark: Defines a function or method.
- Line 131: `        with self._lock, self._connect() as connection:`
  Remark: Opens a managed resource and closes it safely.
- Line 132: `            rows = connection.execute(`
  Remark: Creates or updates a value used by the program.
- Line 133: `                """`
  Remark: Documentation string that explains a module, class, or function.
- Line 134: `                SELECT sender, room, body, created_at`
  Remark: Runs a program instruction for the current feature.
- Line 135: `                FROM messages`
  Remark: Runs a program instruction for the current feature.
- Line 136: `                WHERE room = ?`
  Remark: Creates or updates a value used by the program.
- Line 137: `                ORDER BY id DESC`
  Remark: Runs a program instruction for the current feature.
- Line 138: `                LIMIT ?`
  Remark: Runs a program instruction for the current feature.
- Line 139: `                """,`
  Remark: Documentation string that explains a module, class, or function.
- Line 140: `                (room, limit),`
  Remark: Runs a program instruction for the current feature.
- Line 141: `            ).fetchall()`
  Remark: Runs a program instruction for the current feature.
- Line 142: ` `
  Remark: Blank line used to separate logical code sections.
- Line 143: `        return [`
  Remark: Returns a result to the caller.
- Line 144: `            ChatMessage(`
  Remark: Runs a program instruction for the current feature.
- Line 145: `                sender=row["sender"],`
  Remark: Creates or updates a value used by the program.
- Line 146: `                room=row["room"],`
  Remark: Creates or updates a value used by the program.
- Line 147: `                body=row["body"],`
  Remark: Creates or updates a value used by the program.
- Line 148: `                created_at=row["created_at"],`
  Remark: Creates or updates a value used by the program.
- Line 149: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 150: `            for row in reversed(rows)`
  Remark: Loops over multiple values.
- Line 151: `        ]`
  Remark: Runs a program instruction for the current feature.
- Line 152: ` `
  Remark: Blank line used to separate logical code sections.
- Line 153: `    def list_users(self) -> list[User]:`
  Remark: Defines a function or method.
- Line 154: `        with self._lock, self._connect() as connection:`
  Remark: Opens a managed resource and closes it safely.
- Line 155: `            rows = connection.execute(`
  Remark: Creates or updates a value used by the program.
- Line 156: `                "SELECT username, created_at FROM users ORDER BY username"`
  Remark: Runs a program instruction for the current feature.
- Line 157: `            ).fetchall()`
  Remark: Runs a program instruction for the current feature.
- Line 158: ` `
  Remark: Blank line used to separate logical code sections.
- Line 159: `        return [User(username=row["username"], created_at=row["created_at"]) for row in rows]`
  Remark: Returns a result to the caller.
- Line 160: ` `
  Remark: Blank line used to separate logical code sections.
- Line 161: `    def log_event(self, event_type: str, details: str) -> None:`
  Remark: Defines a function or method.
- Line 162: `        with self._lock, self._connect() as connection:`
  Remark: Opens a managed resource and closes it safely.
- Line 163: `            connection.execute(`
  Remark: Runs a program instruction for the current feature.
- Line 164: `                "INSERT INTO audit_log(event_type, details, created_at) VALUES (?, ?, ?)",`
  Remark: Runs a program instruction for the current feature.
- Line 165: `                (event_type, details, now_iso()),`
  Remark: Runs a program instruction for the current feature.
- Line 166: `            )`
  Remark: Runs a program instruction for the current feature.
- Line 167: ` `
  Remark: Blank line used to separate logical code sections.

## `tools/create_dev_certificate.py`

- Line 1: `from pathlib import Path`
  Remark: Imports code that this file needs.
- Line 2: `from datetime import datetime, timedelta, timezone`
  Remark: Imports code that this file needs.
- Line 3: ` `
  Remark: Blank line used to separate logical code sections.
- Line 4: `from cryptography import x509`
  Remark: Imports code that this file needs.
- Line 5: `from cryptography.hazmat.primitives import hashes, serialization`
  Remark: Imports code that this file needs.
- Line 6: `from cryptography.hazmat.primitives.asymmetric import rsa`
  Remark: Imports code that this file needs.
- Line 7: `from cryptography.x509.oid import NameOID`
  Remark: Imports code that this file needs.
- Line 8: ` `
  Remark: Blank line used to separate logical code sections.
- Line 9: ` `
  Remark: Blank line used to separate logical code sections.
- Line 10: `ROOT = Path(__file__).resolve().parent.parent`
  Remark: Creates or updates a value used by the program.
- Line 11: `CERT_DIR = ROOT / "certs"`
  Remark: Creates or updates a value used by the program.
- Line 12: `CERT_PATH = CERT_DIR / "server.crt"`
  Remark: Creates or updates a value used by the program.
- Line 13: `KEY_PATH = CERT_DIR / "server.key"`
  Remark: Creates or updates a value used by the program.
- Line 14: ` `
  Remark: Blank line used to separate logical code sections.
- Line 15: ` `
  Remark: Blank line used to separate logical code sections.
- Line 16: `def main() -> None:`
  Remark: Defines a function or method.
- Line 17: `    CERT_DIR.mkdir(parents=True, exist_ok=True)`
  Remark: Creates or updates a value used by the program.
- Line 18: ` `
  Remark: Blank line used to separate logical code sections.
- Line 19: `    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)`
  Remark: Creates or updates a value used by the program.
- Line 20: `    subject = issuer = x509.Name(`
  Remark: Creates or updates a value used by the program.
- Line 21: `        [x509.NameAttribute(NameOID.COMMON_NAME, "SecureChatLocal")]`
  Remark: Runs a program instruction for the current feature.
- Line 22: `    )`
  Remark: Runs a program instruction for the current feature.
- Line 23: `    certificate = (`
  Remark: Creates or updates a value used by the program.
- Line 24: `        x509.CertificateBuilder()`
  Remark: Runs a program instruction for the current feature.
- Line 25: `        .subject_name(subject)`
  Remark: Runs a program instruction for the current feature.
- Line 26: `        .issuer_name(issuer)`
  Remark: Runs a program instruction for the current feature.
- Line 27: `        .public_key(private_key.public_key())`
  Remark: Runs a program instruction for the current feature.
- Line 28: `        .serial_number(x509.random_serial_number())`
  Remark: Runs a program instruction for the current feature.
- Line 29: `        .not_valid_before(datetime.now(timezone.utc) - timedelta(days=1))`
  Remark: Creates or updates a value used by the program.
- Line 30: `        .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))`
  Remark: Creates or updates a value used by the program.
- Line 31: `        .sign(private_key, hashes.SHA256())`
  Remark: Runs a program instruction for the current feature.
- Line 32: `    )`
  Remark: Runs a program instruction for the current feature.
- Line 33: ` `
  Remark: Blank line used to separate logical code sections.
- Line 34: `    KEY_PATH.write_bytes(`
  Remark: Runs a program instruction for the current feature.
- Line 35: `        private_key.private_bytes(`
  Remark: Runs a program instruction for the current feature.
- Line 36: `            encoding=serialization.Encoding.PEM,`
  Remark: Creates or updates a value used by the program.
- Line 37: `            format=serialization.PrivateFormat.PKCS8,`
  Remark: Creates or updates a value used by the program.
- Line 38: `            encryption_algorithm=serialization.NoEncryption(),`
  Remark: Creates or updates a value used by the program.
- Line 39: `        )`
  Remark: Runs a program instruction for the current feature.
- Line 40: `    )`
  Remark: Runs a program instruction for the current feature.
- Line 41: `    CERT_PATH.write_bytes(certificate.public_bytes(serialization.Encoding.PEM))`
  Remark: Runs a program instruction for the current feature.
- Line 42: ` `
  Remark: Blank line used to separate logical code sections.
- Line 43: `    print(f"Created {CERT_PATH}")`
  Remark: Runs a program instruction for the current feature.
- Line 44: `    print(f"Created {KEY_PATH}")`
  Remark: Runs a program instruction for the current feature.
- Line 45: ` `
  Remark: Blank line used to separate logical code sections.
- Line 46: ` `
  Remark: Blank line used to separate logical code sections.
- Line 47: `if __name__ == "__main__":`
  Remark: Checks a condition before choosing what to do.
- Line 48: `    main()`
  Remark: Runs a program instruction for the current feature.
- Line 49: ` `
  Remark: Blank line used to separate logical code sections.
