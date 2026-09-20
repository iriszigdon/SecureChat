# Code Remarks

Every Python source line is listed with a short English remark for school documentation.

## `secure_chat/__init__.py`

- Line 1: `# Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 2: `"""Secure multi-user chat project for 5-unit cyber/networking bagrut."""`
  Remark: This line is part of the executable source code.
- Line 3: ` `
  Remark: Blank line used for readability.

## `secure_chat/client_gui.py`

- Line 1: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 2: `import argparse`
  Remark: This line is part of the executable source code.
- Line 3: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 4: `import base64`
  Remark: This line is part of the executable source code.
- Line 5: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 6: `import mimetypes`
  Remark: This line is part of the executable source code.
- Line 7: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 8: `import os`
  Remark: This line is part of the executable source code.
- Line 9: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 10: `import queue`
  Remark: This line is part of the executable source code.
- Line 11: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 12: `import socket`
  Remark: This line is part of the executable source code.
- Line 13: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 14: `import ssl`
  Remark: This line is part of the executable source code.
- Line 15: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 16: `import subprocess`
  Remark: This line is part of the executable source code.
- Line 17: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 18: `import sys`
  Remark: This line is part of the executable source code.
- Line 19: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 20: `import threading`
  Remark: This line is part of the executable source code.
- Line 21: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 22: `import time`
  Remark: This line is part of the executable source code.
- Line 23: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 24: `import tkinter as tk`
  Remark: This line is part of the executable source code.
- Line 25: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 26: `from pathlib import Path`
  Remark: This line is part of the executable source code.
- Line 27: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 28: `from tkinter import filedialog, messagebox, scrolledtext, ttk`
  Remark: This line is part of the executable source code.
- Line 29: ` `
  Remark: Blank line used for readability.
- Line 30: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 31: `from PIL import Image, ImageTk`
  Remark: This line is part of the executable source code.
- Line 32: ` `
  Remark: Blank line used for readability.
- Line 33: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 34: `from secure_chat.config import DEFAULT_HOST, DEFAULT_PORT, DOWNLOAD_DIR, MAX_FILE_SIZE`
  Remark: This line is part of the executable source code.
- Line 35: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 36: `from secure_chat.protocol import ChatProtocol, ProtocolError`
  Remark: This line is part of the executable source code.
- Line 37: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 38: `from secure_chat.security import InputValidator, TLSContextFactory, ValidationError`
  Remark: This line is part of the executable source code.
- Line 39: ` `
  Remark: Blank line used for readability.
- Line 40: ` `
  Remark: Blank line used for readability.
- Line 41: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 42: `class ChatClientConnection:`
  Remark: This line is part of the executable source code.
- Line 43: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 44: `    def __init__(self, host: str, port: int, verify_certificate: bool = False) -> None:`
  Remark: This line is part of the executable source code.
- Line 45: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 46: `        self.host = host`
  Remark: This line is part of the executable source code.
- Line 47: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 48: `        self.port = port`
  Remark: This line is part of the executable source code.
- Line 49: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 50: `        self.verify_certificate = verify_certificate`
  Remark: This line is part of the executable source code.
- Line 51: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 52: `        self.socket: ssl.SSLSocket | None = None`
  Remark: This line is part of the executable source code.
- Line 53: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 54: `        self.incoming: "queue.Queue[dict[str, object]]" = queue.Queue()`
  Remark: This line is part of the executable source code.
- Line 55: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 56: `        self.running = False`
  Remark: This line is part of the executable source code.
- Line 57: ` `
  Remark: Blank line used for readability.
- Line 58: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 59: `    def connect(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 60: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 61: `        raw_socket = socket.create_connection((self.host, self.port), timeout=10)`
  Remark: This line is part of the executable source code.
- Line 62: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 63: `        context = TLSContextFactory.client_context(self.verify_certificate)`
  Remark: This line is part of the executable source code.
- Line 64: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 65: `        self.socket = context.wrap_socket(raw_socket, server_hostname=self.host)`
  Remark: This line is part of the executable source code.
- Line 66: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 67: `        self.socket.settimeout(None)`
  Remark: This line is part of the executable source code.
- Line 68: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 69: `        self.running = True`
  Remark: This line is part of the executable source code.
- Line 70: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 71: `        threading.Thread(target=self._listen, daemon=True).start()`
  Remark: This line is part of the executable source code.
- Line 72: ` `
  Remark: Blank line used for readability.
- Line 73: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 74: `    def send(self, packet_type: str, **fields: object) -> None:`
  Remark: This line is part of the executable source code.
- Line 75: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 76: `        if self.socket is None:`
  Remark: This line is part of the executable source code.
- Line 77: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 78: `            raise ConnectionError("Not connected")`
  Remark: This line is part of the executable source code.
- Line 79: `        # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 80: `        ChatProtocol.send(self.socket, packet_type, **fields)`
  Remark: This line is part of the executable source code.
- Line 81: ` `
  Remark: Blank line used for readability.
- Line 82: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 83: `    def close(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 84: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 85: `        self.running = False`
  Remark: This line is part of the executable source code.
- Line 86: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 87: `        if self.socket is not None:`
  Remark: This line is part of the executable source code.
- Line 88: `            # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 89: `            try:`
  Remark: This line is part of the executable source code.
- Line 90: `                # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 91: `                self.send("logout")`
  Remark: This line is part of the executable source code.
- Line 92: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 93: `                self.socket.close()`
  Remark: This line is part of the executable source code.
- Line 94: `            # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 95: `            except OSError:`
  Remark: This line is part of the executable source code.
- Line 96: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 97: `                pass`
  Remark: This line is part of the executable source code.
- Line 98: ` `
  Remark: Blank line used for readability.
- Line 99: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 100: `    def _listen(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 101: `        # Remark: checks an assumption that should be true.`
  Remark: checks an assumption that should be true.
- Line 102: `        assert self.socket is not None`
  Remark: This line is part of the executable source code.
- Line 103: `        # Remark: starts a loop that continues while a condition is true.`
  Remark: starts a loop that continues while a condition is true.
- Line 104: `        while self.running:`
  Remark: This line is part of the executable source code.
- Line 105: `            # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 106: `            try:`
  Remark: This line is part of the executable source code.
- Line 107: `                # Remark: receives data from the network.`
  Remark: receives data from the network.
- Line 108: `                packet = ChatProtocol.receive(self.socket)`
  Remark: This line is part of the executable source code.
- Line 109: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 110: `                self.incoming.put(packet)`
  Remark: This line is part of the executable source code.
- Line 111: `            # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 112: `            except (ConnectionError, OSError, ProtocolError) as exc:`
  Remark: This line is part of the executable source code.
- Line 113: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 114: `                self.incoming.put({"type": "connection_closed", "message": str(exc)})`
  Remark: This line is part of the executable source code.
- Line 115: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 116: `                self.running = False`
  Remark: This line is part of the executable source code.
- Line 117: ` `
  Remark: Blank line used for readability.
- Line 118: ` `
  Remark: Blank line used for readability.
- Line 119: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 120: `class SecureChatApp(tk.Tk):`
  Remark: This line is part of the executable source code.
- Line 121: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 122: `    def __init__(self, connection: ChatClientConnection) -> None:`
  Remark: This line is part of the executable source code.
- Line 123: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 124: `        super().__init__()`
  Remark: This line is part of the executable source code.
- Line 125: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 126: `        self.connection = connection`
  Remark: This line is part of the executable source code.
- Line 127: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 128: `        self.title("SecureChat - Encrypted Multi-User Chat")`
  Remark: This line is part of the executable source code.
- Line 129: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 130: `        self.geometry("980x640")`
  Remark: This line is part of the executable source code.
- Line 131: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 132: `        self.minsize(900, 580)`
  Remark: This line is part of the executable source code.
- Line 133: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 134: `        self.resizable(True, True)`
  Remark: This line is part of the executable source code.
- Line 135: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 136: `        self.configure(bg="#111827")`
  Remark: This line is part of the executable source code.
- Line 137: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 138: `        self.logged_in = False`
  Remark: This line is part of the executable source code.
- Line 139: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 140: `        self.current_room = "general"`
  Remark: This line is part of the executable source code.
- Line 141: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 142: `        self.current_screen = "auth"`
  Remark: This line is part of the executable source code.
- Line 143: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 144: `        self.chat_images: list[ImageTk.PhotoImage] = []`
  Remark: This line is part of the executable source code.
- Line 145: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 146: `        self.chat_links: dict[str, Path] = {}`
  Remark: This line is part of the executable source code.
- Line 147: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 148: `        self.last_typing_sent = 0.0`
  Remark: This line is part of the executable source code.
- Line 149: ` `
  Remark: Blank line used for readability.
- Line 150: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 151: `        self._build_ui()`
  Remark: This line is part of the executable source code.
- Line 152: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 153: `        self.protocol("WM_DELETE_WINDOW", self._on_close)`
  Remark: This line is part of the executable source code.
- Line 154: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 155: `        self.after(100, self._poll_incoming)`
  Remark: This line is part of the executable source code.
- Line 156: ` `
  Remark: Blank line used for readability.
- Line 157: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 158: `    def _build_ui(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 159: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 160: `        self.username_var = tk.StringVar()`
  Remark: This line is part of the executable source code.
- Line 161: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 162: `        self.password_var = tk.StringVar()`
  Remark: This line is part of the executable source code.
- Line 163: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 164: `        self.room_var = tk.StringVar(value="general")`
  Remark: This line is part of the executable source code.
- Line 165: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 166: `        self.new_room_var = tk.StringVar()`
  Remark: This line is part of the executable source code.
- Line 167: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 168: `        self.message_var = tk.StringVar()`
  Remark: This line is part of the executable source code.
- Line 169: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 170: `        self.auth_status_var = tk.StringVar(value="Connected. Register or login to continue.")`
  Remark: This line is part of the executable source code.
- Line 171: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 172: `        self.chat_status_var = tk.StringVar(value="")`
  Remark: This line is part of the executable source code.
- Line 173: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 174: `        self.login_badge_var = tk.StringVar(value="")`
  Remark: This line is part of the executable source code.
- Line 175: ` `
  Remark: Blank line used for readability.
- Line 176: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 177: `        self._build_auth_screen()`
  Remark: This line is part of the executable source code.
- Line 178: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 179: `        self._build_chat_screen()`
  Remark: This line is part of the executable source code.
- Line 180: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 181: `        self._show_auth_screen()`
  Remark: This line is part of the executable source code.
- Line 182: ` `
  Remark: Blank line used for readability.
- Line 183: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 184: `    def _build_auth_screen(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 185: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 186: `        self.auth_frame = tk.Frame(self, bg="#111827")`
  Remark: This line is part of the executable source code.
- Line 187: ` `
  Remark: Blank line used for readability.
- Line 188: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 189: `        card = tk.Frame(self.auth_frame, bg="#f8fafc", padx=34, pady=30)`
  Remark: This line is part of the executable source code.
- Line 190: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 191: `        card.place(relx=0.5, rely=0.5, anchor=tk.CENTER)`
  Remark: This line is part of the executable source code.
- Line 192: ` `
  Remark: Blank line used for readability.
- Line 193: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 194: `        tk.Label(`
  Remark: This line is part of the executable source code.
- Line 195: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 196: `            card,`
  Remark: This line is part of the executable source code.
- Line 197: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 198: `            text="SecureChat",`
  Remark: This line is part of the executable source code.
- Line 199: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 200: `            bg="#f8fafc",`
  Remark: This line is part of the executable source code.
- Line 201: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 202: `            fg="#2563eb",`
  Remark: This line is part of the executable source code.
- Line 203: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 204: `            font=("Segoe UI", 30, "bold"),`
  Remark: This line is part of the executable source code.
- Line 205: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 206: `        ).grid(row=0, column=0, columnspan=2, pady=(0, 6))`
  Remark: This line is part of the executable source code.
- Line 207: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 208: `        tk.Label(`
  Remark: This line is part of the executable source code.
- Line 209: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 210: `            card,`
  Remark: This line is part of the executable source code.
- Line 211: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 212: `            text="Encrypted multi-user chat",`
  Remark: This line is part of the executable source code.
- Line 213: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 214: `            bg="#f8fafc",`
  Remark: This line is part of the executable source code.
- Line 215: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 216: `            fg="#475569",`
  Remark: This line is part of the executable source code.
- Line 217: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 218: `            font=("Segoe UI", 12),`
  Remark: This line is part of the executable source code.
- Line 219: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 220: `        ).grid(row=1, column=0, columnspan=2, pady=(0, 24))`
  Remark: This line is part of the executable source code.
- Line 221: ` `
  Remark: Blank line used for readability.
- Line 222: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 223: `        tk.Label(card, text="Username", bg="#f8fafc", fg="#0f172a", font=("Segoe UI", 11, "bold")).grid(`
  Remark: This line is part of the executable source code.
- Line 224: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 225: `            row=2, column=0, sticky="w"`
  Remark: This line is part of the executable source code.
- Line 226: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 227: `        )`
  Remark: This line is part of the executable source code.
- Line 228: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 229: `        tk.Entry(`
  Remark: This line is part of the executable source code.
- Line 230: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 231: `            card,`
  Remark: This line is part of the executable source code.
- Line 232: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 233: `            textvariable=self.username_var,`
  Remark: This line is part of the executable source code.
- Line 234: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 235: `            width=30,`
  Remark: This line is part of the executable source code.
- Line 236: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 237: `            font=("Segoe UI", 12),`
  Remark: This line is part of the executable source code.
- Line 238: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 239: `            bg="#e0f2fe",`
  Remark: This line is part of the executable source code.
- Line 240: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 241: `            fg="#0f172a",`
  Remark: This line is part of the executable source code.
- Line 242: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 243: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 244: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 245: `        ).grid(row=3, column=0, columnspan=2, sticky="ew", pady=(4, 14), ipady=8)`
  Remark: This line is part of the executable source code.
- Line 246: ` `
  Remark: Blank line used for readability.
- Line 247: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 248: `        tk.Label(card, text="Password", bg="#f8fafc", fg="#0f172a", font=("Segoe UI", 11, "bold")).grid(`
  Remark: This line is part of the executable source code.
- Line 249: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 250: `            row=4, column=0, sticky="w"`
  Remark: This line is part of the executable source code.
- Line 251: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 252: `        )`
  Remark: This line is part of the executable source code.
- Line 253: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 254: `        password_entry = tk.Entry(`
  Remark: This line is part of the executable source code.
- Line 255: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 256: `            card,`
  Remark: This line is part of the executable source code.
- Line 257: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 258: `            textvariable=self.password_var,`
  Remark: This line is part of the executable source code.
- Line 259: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 260: `            show="*",`
  Remark: This line is part of the executable source code.
- Line 261: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 262: `            width=30,`
  Remark: This line is part of the executable source code.
- Line 263: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 264: `            font=("Segoe UI", 12),`
  Remark: This line is part of the executable source code.
- Line 265: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 266: `            bg="#fef3c7",`
  Remark: This line is part of the executable source code.
- Line 267: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 268: `            fg="#0f172a",`
  Remark: This line is part of the executable source code.
- Line 269: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 270: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 271: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 272: `        )`
  Remark: This line is part of the executable source code.
- Line 273: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 274: `        password_entry.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(4, 18), ipady=8)`
  Remark: This line is part of the executable source code.
- Line 275: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 276: `        password_entry.bind("<Return>", lambda _event: self._login())`
  Remark: This line is part of the executable source code.
- Line 277: ` `
  Remark: Blank line used for readability.
- Line 278: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 279: `        tk.Button(`
  Remark: This line is part of the executable source code.
- Line 280: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 281: `            card,`
  Remark: This line is part of the executable source code.
- Line 282: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 283: `            text="Register",`
  Remark: This line is part of the executable source code.
- Line 284: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 285: `            command=self._register_user,`
  Remark: This line is part of the executable source code.
- Line 286: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 287: `            bg="#22c55e",`
  Remark: This line is part of the executable source code.
- Line 288: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 289: `            fg="white",`
  Remark: This line is part of the executable source code.
- Line 290: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 291: `            activebackground="#16a34a",`
  Remark: This line is part of the executable source code.
- Line 292: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 293: `            font=("Segoe UI", 11, "bold"),`
  Remark: This line is part of the executable source code.
- Line 294: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 295: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 296: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 297: `            padx=16,`
  Remark: This line is part of the executable source code.
- Line 298: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 299: `            pady=8,`
  Remark: This line is part of the executable source code.
- Line 300: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 301: `        ).grid(row=6, column=0, sticky="ew", padx=(0, 8))`
  Remark: This line is part of the executable source code.
- Line 302: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 303: `        tk.Button(`
  Remark: This line is part of the executable source code.
- Line 304: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 305: `            card,`
  Remark: This line is part of the executable source code.
- Line 306: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 307: `            text="Login",`
  Remark: This line is part of the executable source code.
- Line 308: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 309: `            command=self._login,`
  Remark: This line is part of the executable source code.
- Line 310: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 311: `            bg="#3b82f6",`
  Remark: This line is part of the executable source code.
- Line 312: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 313: `            fg="white",`
  Remark: This line is part of the executable source code.
- Line 314: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 315: `            activebackground="#2563eb",`
  Remark: This line is part of the executable source code.
- Line 316: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 317: `            font=("Segoe UI", 11, "bold"),`
  Remark: This line is part of the executable source code.
- Line 318: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 319: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 320: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 321: `            padx=16,`
  Remark: This line is part of the executable source code.
- Line 322: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 323: `            pady=8,`
  Remark: This line is part of the executable source code.
- Line 324: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 325: `        ).grid(row=6, column=1, sticky="ew", padx=(8, 0))`
  Remark: This line is part of the executable source code.
- Line 326: ` `
  Remark: Blank line used for readability.
- Line 327: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 328: `        self.auth_status_label = tk.Label(`
  Remark: This line is part of the executable source code.
- Line 329: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 330: `            card,`
  Remark: This line is part of the executable source code.
- Line 331: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 332: `            textvariable=self.auth_status_var,`
  Remark: This line is part of the executable source code.
- Line 333: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 334: `            bg="#dbeafe",`
  Remark: This line is part of the executable source code.
- Line 335: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 336: `            fg="#2563eb",`
  Remark: This line is part of the executable source code.
- Line 337: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 338: `            wraplength=360,`
  Remark: This line is part of the executable source code.
- Line 339: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 340: `            font=("Segoe UI", 12, "bold"),`
  Remark: This line is part of the executable source code.
- Line 341: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 342: `            padx=10,`
  Remark: This line is part of the executable source code.
- Line 343: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 344: `            pady=8,`
  Remark: This line is part of the executable source code.
- Line 345: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 346: `        )`
  Remark: This line is part of the executable source code.
- Line 347: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 348: `        self.auth_status_label.grid(row=7, column=0, columnspan=2, pady=(18, 0))`
  Remark: This line is part of the executable source code.
- Line 349: ` `
  Remark: Blank line used for readability.
- Line 350: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 351: `    def _build_chat_screen(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 352: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 353: `        self.chat_frame = tk.Frame(self, bg="#dbeafe")`
  Remark: This line is part of the executable source code.
- Line 354: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 355: `        self.chat_frame.columnconfigure(1, weight=1)`
  Remark: This line is part of the executable source code.
- Line 356: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 357: `        self.chat_frame.rowconfigure(1, weight=1)`
  Remark: This line is part of the executable source code.
- Line 358: ` `
  Remark: Blank line used for readability.
- Line 359: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 360: `        header = tk.Frame(self.chat_frame, bg="#1d4ed8", padx=14, pady=12)`
  Remark: This line is part of the executable source code.
- Line 361: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 362: `        header.grid(row=0, column=0, columnspan=3, sticky="ew")`
  Remark: This line is part of the executable source code.
- Line 363: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 364: `        header.columnconfigure(1, weight=1)`
  Remark: This line is part of the executable source code.
- Line 365: ` `
  Remark: Blank line used for readability.
- Line 366: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 367: `        tk.Label(`
  Remark: This line is part of the executable source code.
- Line 368: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 369: `            header,`
  Remark: This line is part of the executable source code.
- Line 370: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 371: `            text="SecureChat",`
  Remark: This line is part of the executable source code.
- Line 372: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 373: `            bg="#1d4ed8",`
  Remark: This line is part of the executable source code.
- Line 374: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 375: `            fg="white",`
  Remark: This line is part of the executable source code.
- Line 376: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 377: `            font=("Segoe UI", 20, "bold"),`
  Remark: This line is part of the executable source code.
- Line 378: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 379: `        ).grid(row=0, column=0, sticky="w")`
  Remark: This line is part of the executable source code.
- Line 380: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 381: `        tk.Label(`
  Remark: This line is part of the executable source code.
- Line 382: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 383: `            header,`
  Remark: This line is part of the executable source code.
- Line 384: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 385: `            textvariable=self.login_badge_var,`
  Remark: This line is part of the executable source code.
- Line 386: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 387: `            bg="#1d4ed8",`
  Remark: This line is part of the executable source code.
- Line 388: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 389: `            fg="#bbf7d0",`
  Remark: This line is part of the executable source code.
- Line 390: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 391: `            font=("Segoe UI", 12, "bold"),`
  Remark: This line is part of the executable source code.
- Line 392: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 393: `        ).grid(row=0, column=1, sticky="e")`
  Remark: This line is part of the executable source code.
- Line 394: ` `
  Remark: Blank line used for readability.
- Line 395: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 396: `        rooms_panel = tk.Frame(self.chat_frame, bg="#eff6ff", padx=10, pady=10)`
  Remark: This line is part of the executable source code.
- Line 397: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 398: `        rooms_panel.grid(row=1, column=0, sticky="nsw", padx=(10, 5), pady=10)`
  Remark: This line is part of the executable source code.
- Line 399: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 400: `        rooms_panel.rowconfigure(1, weight=1)`
  Remark: This line is part of the executable source code.
- Line 401: ` `
  Remark: Blank line used for readability.
- Line 402: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 403: `        tk.Label(rooms_panel, text="Rooms", bg="#eff6ff", fg="#1e3a8a", font=("Segoe UI", 14, "bold")).grid(`
  Remark: This line is part of the executable source code.
- Line 404: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 405: `            row=0, column=0, columnspan=2, sticky="w", pady=(0, 8)`
  Remark: This line is part of the executable source code.
- Line 406: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 407: `        )`
  Remark: This line is part of the executable source code.
- Line 408: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 409: `        self.rooms_box = tk.Listbox(`
  Remark: This line is part of the executable source code.
- Line 410: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 411: `            rooms_panel,`
  Remark: This line is part of the executable source code.
- Line 412: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 413: `            width=22,`
  Remark: This line is part of the executable source code.
- Line 414: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 415: `            height=18,`
  Remark: This line is part of the executable source code.
- Line 416: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 417: `            bg="#ffffff",`
  Remark: This line is part of the executable source code.
- Line 418: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 419: `            fg="#0f172a",`
  Remark: This line is part of the executable source code.
- Line 420: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 421: `            selectbackground="#3b82f6",`
  Remark: This line is part of the executable source code.
- Line 422: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 423: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 424: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 425: `            font=("Segoe UI", 10),`
  Remark: This line is part of the executable source code.
- Line 426: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 427: `        )`
  Remark: This line is part of the executable source code.
- Line 428: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 429: `        self.rooms_box.grid(row=1, column=0, columnspan=2, sticky="nsew")`
  Remark: This line is part of the executable source code.
- Line 430: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 431: `        self.rooms_box.bind("<<ListboxSelect>>", self._on_room_select)`
  Remark: This line is part of the executable source code.
- Line 432: ` `
  Remark: Blank line used for readability.
- Line 433: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 434: `        tk.Button(`
  Remark: This line is part of the executable source code.
- Line 435: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 436: `            rooms_panel,`
  Remark: This line is part of the executable source code.
- Line 437: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 438: `            text="Join Selected",`
  Remark: This line is part of the executable source code.
- Line 439: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 440: `            command=self._join_room,`
  Remark: This line is part of the executable source code.
- Line 441: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 442: `            bg="#8b5cf6",`
  Remark: This line is part of the executable source code.
- Line 443: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 444: `            fg="white",`
  Remark: This line is part of the executable source code.
- Line 445: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 446: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 447: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 448: `            font=("Segoe UI", 10, "bold"),`
  Remark: This line is part of the executable source code.
- Line 449: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 450: `        ).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(8, 12))`
  Remark: This line is part of the executable source code.
- Line 451: ` `
  Remark: Blank line used for readability.
- Line 452: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 453: `        tk.Entry(`
  Remark: This line is part of the executable source code.
- Line 454: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 455: `            rooms_panel,`
  Remark: This line is part of the executable source code.
- Line 456: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 457: `            textvariable=self.new_room_var,`
  Remark: This line is part of the executable source code.
- Line 458: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 459: `            bg="#fef3c7",`
  Remark: This line is part of the executable source code.
- Line 460: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 461: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 462: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 463: `            font=("Segoe UI", 10),`
  Remark: This line is part of the executable source code.
- Line 464: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 465: `        ).grid(row=3, column=0, columnspan=2, sticky="ew", ipady=6)`
  Remark: This line is part of the executable source code.
- Line 466: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 467: `        tk.Button(`
  Remark: This line is part of the executable source code.
- Line 468: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 469: `            rooms_panel,`
  Remark: This line is part of the executable source code.
- Line 470: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 471: `            text="Create Room",`
  Remark: This line is part of the executable source code.
- Line 472: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 473: `            command=self._create_room,`
  Remark: This line is part of the executable source code.
- Line 474: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 475: `            bg="#f97316",`
  Remark: This line is part of the executable source code.
- Line 476: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 477: `            fg="white",`
  Remark: This line is part of the executable source code.
- Line 478: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 479: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 480: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 481: `            font=("Segoe UI", 10, "bold"),`
  Remark: This line is part of the executable source code.
- Line 482: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 483: `        ).grid(row=4, column=0, columnspan=2, sticky="ew", pady=(8, 8))`
  Remark: This line is part of the executable source code.
- Line 484: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 485: `        tk.Button(`
  Remark: This line is part of the executable source code.
- Line 486: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 487: `            rooms_panel,`
  Remark: This line is part of the executable source code.
- Line 488: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 489: `            text="Refresh Rooms",`
  Remark: This line is part of the executable source code.
- Line 490: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 491: `            command=self._request_rooms,`
  Remark: This line is part of the executable source code.
- Line 492: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 493: `            bg="#06b6d4",`
  Remark: This line is part of the executable source code.
- Line 494: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 495: `            fg="white",`
  Remark: This line is part of the executable source code.
- Line 496: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 497: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 498: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 499: `            font=("Segoe UI", 10, "bold"),`
  Remark: This line is part of the executable source code.
- Line 500: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 501: `        ).grid(row=5, column=0, columnspan=2, sticky="ew")`
  Remark: This line is part of the executable source code.
- Line 502: ` `
  Remark: Blank line used for readability.
- Line 503: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 504: `        chat_panel = tk.Frame(self.chat_frame, bg="#dbeafe", padx=5, pady=10)`
  Remark: This line is part of the executable source code.
- Line 505: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 506: `        chat_panel.grid(row=1, column=1, sticky="nsew", pady=10)`
  Remark: This line is part of the executable source code.
- Line 507: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 508: `        chat_panel.rowconfigure(1, weight=1)`
  Remark: This line is part of the executable source code.
- Line 509: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 510: `        chat_panel.columnconfigure(0, weight=1)`
  Remark: This line is part of the executable source code.
- Line 511: ` `
  Remark: Blank line used for readability.
- Line 512: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 513: `        self.room_title_var = tk.StringVar(value="Room: general")`
  Remark: This line is part of the executable source code.
- Line 514: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 515: `        tk.Label(`
  Remark: This line is part of the executable source code.
- Line 516: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 517: `            chat_panel,`
  Remark: This line is part of the executable source code.
- Line 518: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 519: `            textvariable=self.room_title_var,`
  Remark: This line is part of the executable source code.
- Line 520: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 521: `            bg="#dbeafe",`
  Remark: This line is part of the executable source code.
- Line 522: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 523: `            fg="#1e3a8a",`
  Remark: This line is part of the executable source code.
- Line 524: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 525: `            font=("Segoe UI", 14, "bold"),`
  Remark: This line is part of the executable source code.
- Line 526: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 527: `        ).grid(row=0, column=0, sticky="w", pady=(0, 8))`
  Remark: This line is part of the executable source code.
- Line 528: ` `
  Remark: Blank line used for readability.
- Line 529: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 530: `        self.chat_box = scrolledtext.ScrolledText(`
  Remark: This line is part of the executable source code.
- Line 531: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 532: `            chat_panel,`
  Remark: This line is part of the executable source code.
- Line 533: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 534: `            state=tk.DISABLED,`
  Remark: This line is part of the executable source code.
- Line 535: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 536: `            wrap=tk.WORD,`
  Remark: This line is part of the executable source code.
- Line 537: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 538: `            bg="#ffffff",`
  Remark: This line is part of the executable source code.
- Line 539: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 540: `            fg="#0f172a",`
  Remark: This line is part of the executable source code.
- Line 541: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 542: `            insertbackground="#0f172a",`
  Remark: This line is part of the executable source code.
- Line 543: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 544: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 545: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 546: `            font=("Consolas", 10),`
  Remark: This line is part of the executable source code.
- Line 547: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 548: `        )`
  Remark: This line is part of the executable source code.
- Line 549: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 550: `        self.chat_box.grid(row=1, column=0, sticky="nsew")`
  Remark: This line is part of the executable source code.
- Line 551: ` `
  Remark: Blank line used for readability.
- Line 552: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 553: `        send_frame = tk.Frame(chat_panel, bg="#dbeafe")`
  Remark: This line is part of the executable source code.
- Line 554: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 555: `        send_frame.grid(row=2, column=0, sticky="ew", pady=(10, 0))`
  Remark: This line is part of the executable source code.
- Line 556: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 557: `        send_frame.columnconfigure(0, weight=1)`
  Remark: This line is part of the executable source code.
- Line 558: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 559: `        message_entry = tk.Entry(send_frame, textvariable=self.message_var, bg="#ffffff", relief=tk.FLAT, font=("Segoe UI", 11))`
  Remark: This line is part of the executable source code.
- Line 560: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 561: `        message_entry.grid(row=0, column=0, sticky="ew", ipady=8, padx=(0, 8))`
  Remark: This line is part of the executable source code.
- Line 562: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 563: `        message_entry.bind("<Return>", lambda _event: self._send_message())`
  Remark: This line is part of the executable source code.
- Line 564: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 565: `        message_entry.bind("<KeyRelease>", lambda _event: self._send_typing_notice())`
  Remark: This line is part of the executable source code.
- Line 566: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 567: `        tk.Button(`
  Remark: This line is part of the executable source code.
- Line 568: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 569: `            send_frame,`
  Remark: This line is part of the executable source code.
- Line 570: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 571: `            text="Send",`
  Remark: This line is part of the executable source code.
- Line 572: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 573: `            command=self._send_message,`
  Remark: This line is part of the executable source code.
- Line 574: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 575: `            bg="#22c55e",`
  Remark: This line is part of the executable source code.
- Line 576: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 577: `            fg="white",`
  Remark: This line is part of the executable source code.
- Line 578: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 579: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 580: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 581: `            font=("Segoe UI", 11, "bold"),`
  Remark: This line is part of the executable source code.
- Line 582: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 583: `            padx=20,`
  Remark: This line is part of the executable source code.
- Line 584: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 585: `        ).grid(row=0, column=1)`
  Remark: This line is part of the executable source code.
- Line 586: ` `
  Remark: Blank line used for readability.
- Line 587: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 588: `        media_frame = tk.Frame(chat_panel, bg="#dbeafe")`
  Remark: This line is part of the executable source code.
- Line 589: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 590: `        media_frame.grid(row=3, column=0, sticky="ew", pady=(8, 0))`
  Remark: This line is part of the executable source code.
- Line 591: `        # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 592: `        for emoji in ["😀", "😂", "❤️", "👍", "🔥", "🎉"]:`
  Remark: This line is part of the executable source code.
- Line 593: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 594: `            tk.Button(`
  Remark: This line is part of the executable source code.
- Line 595: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 596: `                media_frame,`
  Remark: This line is part of the executable source code.
- Line 597: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 598: `                text=emoji,`
  Remark: This line is part of the executable source code.
- Line 599: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 600: `                command=lambda value=emoji: self._insert_emoji(value),`
  Remark: This line is part of the executable source code.
- Line 601: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 602: `                bg="#fef3c7",`
  Remark: This line is part of the executable source code.
- Line 603: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 604: `                relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 605: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 606: `                font=("Segoe UI Emoji", 12),`
  Remark: This line is part of the executable source code.
- Line 607: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 608: `                width=3,`
  Remark: This line is part of the executable source code.
- Line 609: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 610: `            ).pack(side=tk.LEFT, padx=(0, 5))`
  Remark: This line is part of the executable source code.
- Line 611: ` `
  Remark: Blank line used for readability.
- Line 612: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 613: `        tk.Button(`
  Remark: This line is part of the executable source code.
- Line 614: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 615: `            media_frame,`
  Remark: This line is part of the executable source code.
- Line 616: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 617: `            text="Send File",`
  Remark: This line is part of the executable source code.
- Line 618: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 619: `            command=lambda: self._send_file("file"),`
  Remark: This line is part of the executable source code.
- Line 620: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 621: `            bg="#64748b",`
  Remark: This line is part of the executable source code.
- Line 622: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 623: `            fg="white",`
  Remark: This line is part of the executable source code.
- Line 624: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 625: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 626: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 627: `            font=("Segoe UI", 10, "bold"),`
  Remark: This line is part of the executable source code.
- Line 628: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 629: `            padx=10,`
  Remark: This line is part of the executable source code.
- Line 630: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 631: `        ).pack(side=tk.LEFT, padx=(12, 5))`
  Remark: This line is part of the executable source code.
- Line 632: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 633: `        tk.Button(`
  Remark: This line is part of the executable source code.
- Line 634: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 635: `            media_frame,`
  Remark: This line is part of the executable source code.
- Line 636: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 637: `            text="Send Image",`
  Remark: This line is part of the executable source code.
- Line 638: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 639: `            command=lambda: self._send_file("image"),`
  Remark: This line is part of the executable source code.
- Line 640: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 641: `            bg="#ec4899",`
  Remark: This line is part of the executable source code.
- Line 642: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 643: `            fg="white",`
  Remark: This line is part of the executable source code.
- Line 644: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 645: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 646: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 647: `            font=("Segoe UI", 10, "bold"),`
  Remark: This line is part of the executable source code.
- Line 648: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 649: `            padx=10,`
  Remark: This line is part of the executable source code.
- Line 650: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 651: `        ).pack(side=tk.LEFT, padx=5)`
  Remark: This line is part of the executable source code.
- Line 652: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 653: `        tk.Button(`
  Remark: This line is part of the executable source code.
- Line 654: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 655: `            media_frame,`
  Remark: This line is part of the executable source code.
- Line 656: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 657: `            text="Send Video",`
  Remark: This line is part of the executable source code.
- Line 658: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 659: `            command=lambda: self._send_file("video"),`
  Remark: This line is part of the executable source code.
- Line 660: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 661: `            bg="#7c3aed",`
  Remark: This line is part of the executable source code.
- Line 662: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 663: `            fg="white",`
  Remark: This line is part of the executable source code.
- Line 664: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 665: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 666: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 667: `            font=("Segoe UI", 10, "bold"),`
  Remark: This line is part of the executable source code.
- Line 668: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 669: `            padx=10,`
  Remark: This line is part of the executable source code.
- Line 670: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 671: `        ).pack(side=tk.LEFT, padx=5)`
  Remark: This line is part of the executable source code.
- Line 672: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 673: `        tk.Button(`
  Remark: This line is part of the executable source code.
- Line 674: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 675: `            media_frame,`
  Remark: This line is part of the executable source code.
- Line 676: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 677: `            text="Commands Help",`
  Remark: This line is part of the executable source code.
- Line 678: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 679: `            command=self._show_commands_help,`
  Remark: This line is part of the executable source code.
- Line 680: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 681: `            bg="#0f172a",`
  Remark: This line is part of the executable source code.
- Line 682: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 683: `            fg="white",`
  Remark: This line is part of the executable source code.
- Line 684: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 685: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 686: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 687: `            font=("Segoe UI", 10, "bold"),`
  Remark: This line is part of the executable source code.
- Line 688: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 689: `            padx=10,`
  Remark: This line is part of the executable source code.
- Line 690: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 691: `        ).pack(side=tk.LEFT, padx=12)`
  Remark: This line is part of the executable source code.
- Line 692: ` `
  Remark: Blank line used for readability.
- Line 693: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 694: `        users_panel = tk.Frame(self.chat_frame, bg="#ecfdf5", padx=10, pady=10)`
  Remark: This line is part of the executable source code.
- Line 695: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 696: `        users_panel.grid(row=1, column=2, sticky="nse", padx=(5, 10), pady=10)`
  Remark: This line is part of the executable source code.
- Line 697: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 698: `        users_panel.rowconfigure(1, weight=1)`
  Remark: This line is part of the executable source code.
- Line 699: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 700: `        tk.Label(users_panel, text="Online Users", bg="#ecfdf5", fg="#166534", font=("Segoe UI", 14, "bold")).grid(`
  Remark: This line is part of the executable source code.
- Line 701: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 702: `            row=0, column=0, sticky="w", pady=(0, 8)`
  Remark: This line is part of the executable source code.
- Line 703: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 704: `        )`
  Remark: This line is part of the executable source code.
- Line 705: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 706: `        self.users_box = tk.Listbox(`
  Remark: This line is part of the executable source code.
- Line 707: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 708: `            users_panel,`
  Remark: This line is part of the executable source code.
- Line 709: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 710: `            width=24,`
  Remark: This line is part of the executable source code.
- Line 711: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 712: `            height=18,`
  Remark: This line is part of the executable source code.
- Line 713: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 714: `            bg="#ffffff",`
  Remark: This line is part of the executable source code.
- Line 715: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 716: `            fg="#0f172a",`
  Remark: This line is part of the executable source code.
- Line 717: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 718: `            selectbackground="#22c55e",`
  Remark: This line is part of the executable source code.
- Line 719: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 720: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 721: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 722: `            font=("Segoe UI", 10),`
  Remark: This line is part of the executable source code.
- Line 723: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 724: `        )`
  Remark: This line is part of the executable source code.
- Line 725: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 726: `        self.users_box.grid(row=1, column=0, sticky="nsew")`
  Remark: This line is part of the executable source code.
- Line 727: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 728: `        tk.Button(`
  Remark: This line is part of the executable source code.
- Line 729: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 730: `            users_panel,`
  Remark: This line is part of the executable source code.
- Line 731: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 732: `            text="Refresh Users",`
  Remark: This line is part of the executable source code.
- Line 733: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 734: `            command=self._request_users,`
  Remark: This line is part of the executable source code.
- Line 735: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 736: `            bg="#16a34a",`
  Remark: This line is part of the executable source code.
- Line 737: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 738: `            fg="white",`
  Remark: This line is part of the executable source code.
- Line 739: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 740: `            relief=tk.FLAT,`
  Remark: This line is part of the executable source code.
- Line 741: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 742: `            font=("Segoe UI", 10, "bold"),`
  Remark: This line is part of the executable source code.
- Line 743: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 744: `        ).grid(row=2, column=0, sticky="ew", pady=(8, 0))`
  Remark: This line is part of the executable source code.
- Line 745: ` `
  Remark: Blank line used for readability.
- Line 746: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 747: `        self.chat_status_label = tk.Label(`
  Remark: This line is part of the executable source code.
- Line 748: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 749: `            self.chat_frame,`
  Remark: This line is part of the executable source code.
- Line 750: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 751: `            textvariable=self.chat_status_var,`
  Remark: This line is part of the executable source code.
- Line 752: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 753: `            bg="#dbeafe",`
  Remark: This line is part of the executable source code.
- Line 754: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 755: `            fg="#1d4ed8",`
  Remark: This line is part of the executable source code.
- Line 756: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 757: `            font=("Segoe UI", 10, "bold"),`
  Remark: This line is part of the executable source code.
- Line 758: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 759: `        )`
  Remark: This line is part of the executable source code.
- Line 760: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 761: `        self.chat_status_label.grid(row=2, column=0, columnspan=3, sticky="ew", padx=10, pady=(0, 8))`
  Remark: This line is part of the executable source code.
- Line 762: ` `
  Remark: Blank line used for readability.
- Line 763: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 764: `    def _show_auth_screen(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 765: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 766: `        self.current_screen = "auth"`
  Remark: This line is part of the executable source code.
- Line 767: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 768: `        self.chat_frame.pack_forget()`
  Remark: This line is part of the executable source code.
- Line 769: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 770: `        self.auth_frame.pack(fill=tk.BOTH, expand=True)`
  Remark: This line is part of the executable source code.
- Line 771: ` `
  Remark: Blank line used for readability.
- Line 772: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 773: `    def _show_chat_screen(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 774: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 775: `        self.current_screen = "chat"`
  Remark: This line is part of the executable source code.
- Line 776: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 777: `        self.auth_frame.pack_forget()`
  Remark: This line is part of the executable source code.
- Line 778: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 779: `        self.chat_frame.pack(fill=tk.BOTH, expand=True)`
  Remark: This line is part of the executable source code.
- Line 780: ` `
  Remark: Blank line used for readability.
- Line 781: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 782: `    def _register_user(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 783: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 784: `        self._send_auth_packet("register")`
  Remark: This line is part of the executable source code.
- Line 785: ` `
  Remark: Blank line used for readability.
- Line 786: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 787: `    def _login(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 788: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 789: `        self._send_auth_packet("login")`
  Remark: This line is part of the executable source code.
- Line 790: ` `
  Remark: Blank line used for readability.
- Line 791: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 792: `    def _send_auth_packet(self, packet_type: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 793: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 794: `        try:`
  Remark: This line is part of the executable source code.
- Line 795: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 796: `            username = InputValidator.username(self.username_var.get())`
  Remark: This line is part of the executable source code.
- Line 797: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 798: `            password = InputValidator.password(self.password_var.get())`
  Remark: This line is part of the executable source code.
- Line 799: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 800: `            self.connection.send(`
  Remark: This line is part of the executable source code.
- Line 801: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 802: `                packet_type,`
  Remark: This line is part of the executable source code.
- Line 803: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 804: `                username=username,`
  Remark: This line is part of the executable source code.
- Line 805: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 806: `                password=password,`
  Remark: This line is part of the executable source code.
- Line 807: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 808: `            )`
  Remark: This line is part of the executable source code.
- Line 809: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 810: `        except ValidationError as exc:`
  Remark: This line is part of the executable source code.
- Line 811: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 812: `            self._set_auth_status(str(exc), ok=False)`
  Remark: This line is part of the executable source code.
- Line 813: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 814: `            messagebox.showerror("Invalid details", str(exc))`
  Remark: This line is part of the executable source code.
- Line 815: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 816: `        except Exception as exc:`
  Remark: This line is part of the executable source code.
- Line 817: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 818: `            self._set_auth_status(f"Connection error: {exc}", ok=False)`
  Remark: This line is part of the executable source code.
- Line 819: ` `
  Remark: Blank line used for readability.
- Line 820: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 821: `    def _join_room(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 822: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 823: `        if not self.logged_in:`
  Remark: This line is part of the executable source code.
- Line 824: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 825: `            self._set_chat_status("Please login first.", ok=False)`
  Remark: This line is part of the executable source code.
- Line 826: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 827: `            return`
  Remark: This line is part of the executable source code.
- Line 828: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 829: `        room = self.room_var.get().strip()`
  Remark: This line is part of the executable source code.
- Line 830: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 831: `        if not room:`
  Remark: This line is part of the executable source code.
- Line 832: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 833: `            self._set_chat_status("Choose a room first.", ok=False)`
  Remark: This line is part of the executable source code.
- Line 834: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 835: `            return`
  Remark: This line is part of the executable source code.
- Line 836: `        # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 837: `        self.connection.send("join", room=room)`
  Remark: This line is part of the executable source code.
- Line 838: ` `
  Remark: Blank line used for readability.
- Line 839: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 840: `    def _create_room(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 841: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 842: `        if not self.logged_in:`
  Remark: This line is part of the executable source code.
- Line 843: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 844: `            self._set_chat_status("Please login first.", ok=False)`
  Remark: This line is part of the executable source code.
- Line 845: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 846: `            return`
  Remark: This line is part of the executable source code.
- Line 847: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 848: `        room = self.new_room_var.get().strip()`
  Remark: This line is part of the executable source code.
- Line 849: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 850: `        if not room:`
  Remark: This line is part of the executable source code.
- Line 851: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 852: `            self._set_chat_status("Write a room name to create.", ok=False)`
  Remark: This line is part of the executable source code.
- Line 853: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 854: `            return`
  Remark: This line is part of the executable source code.
- Line 855: `        # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 856: `        self.connection.send("create_room", room=room)`
  Remark: This line is part of the executable source code.
- Line 857: ` `
  Remark: Blank line used for readability.
- Line 858: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 859: `    def _request_users(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 860: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 861: `        if self.logged_in:`
  Remark: This line is part of the executable source code.
- Line 862: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 863: `            self.connection.send("users")`
  Remark: This line is part of the executable source code.
- Line 864: ` `
  Remark: Blank line used for readability.
- Line 865: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 866: `    def _request_rooms(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 867: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 868: `        if self.logged_in:`
  Remark: This line is part of the executable source code.
- Line 869: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 870: `            self.connection.send("rooms")`
  Remark: This line is part of the executable source code.
- Line 871: ` `
  Remark: Blank line used for readability.
- Line 872: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 873: `    def _send_message(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 874: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 875: `        if not self.logged_in:`
  Remark: This line is part of the executable source code.
- Line 876: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 877: `            self._set_chat_status("Please login first.", ok=False)`
  Remark: This line is part of the executable source code.
- Line 878: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 879: `            return`
  Remark: This line is part of the executable source code.
- Line 880: ` `
  Remark: Blank line used for readability.
- Line 881: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 882: `        body = self.message_var.get()`
  Remark: This line is part of the executable source code.
- Line 883: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 884: `        if not body.strip():`
  Remark: This line is part of the executable source code.
- Line 885: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 886: `            return`
  Remark: This line is part of the executable source code.
- Line 887: ` `
  Remark: Blank line used for readability.
- Line 888: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 889: `        try:`
  Remark: This line is part of the executable source code.
- Line 890: `            # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 891: `            if body.strip().startswith("/"):`
  Remark: This line is part of the executable source code.
- Line 892: `                # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 893: `                self.connection.send("command", body=body.strip())`
  Remark: This line is part of the executable source code.
- Line 894: `            # Remark: handles the case where previous conditions were false.`
  Remark: handles the case where previous conditions were false.
- Line 895: `            else:`
  Remark: This line is part of the executable source code.
- Line 896: `                # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 897: `                self.connection.send("message", body=body)`
  Remark: This line is part of the executable source code.
- Line 898: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 899: `            self.message_var.set("")`
  Remark: This line is part of the executable source code.
- Line 900: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 901: `        except Exception as exc:`
  Remark: This line is part of the executable source code.
- Line 902: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 903: `            self._set_chat_status(f"Send failed: {exc}", ok=False)`
  Remark: This line is part of the executable source code.
- Line 904: ` `
  Remark: Blank line used for readability.
- Line 905: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 906: `    def _send_typing_notice(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 907: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 908: `        if not self.logged_in:`
  Remark: This line is part of the executable source code.
- Line 909: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 910: `            return`
  Remark: This line is part of the executable source code.
- Line 911: ` `
  Remark: Blank line used for readability.
- Line 912: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 913: `        current_time = time.time()`
  Remark: This line is part of the executable source code.
- Line 914: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 915: `        if current_time - self.last_typing_sent < 2:`
  Remark: This line is part of the executable source code.
- Line 916: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 917: `            return`
  Remark: This line is part of the executable source code.
- Line 918: ` `
  Remark: Blank line used for readability.
- Line 919: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 920: `        self.last_typing_sent = current_time`
  Remark: This line is part of the executable source code.
- Line 921: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 922: `        try:`
  Remark: This line is part of the executable source code.
- Line 923: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 924: `            self.connection.send("typing")`
  Remark: This line is part of the executable source code.
- Line 925: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 926: `        except Exception:`
  Remark: This line is part of the executable source code.
- Line 927: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 928: `            pass`
  Remark: This line is part of the executable source code.
- Line 929: ` `
  Remark: Blank line used for readability.
- Line 930: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 931: `    def _show_commands_help(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 932: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 933: `        commands = (`
  Remark: This line is part of the executable source code.
- Line 934: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 935: `            "Advanced commands:\\n"`
  Remark: This line is part of the executable source code.
- Line 936: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 937: `            "/dm USER MESSAGE - private message\\n"`
  Remark: This line is part of the executable source code.
- Line 938: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 939: `            "/profile set TEXT - update your profile\\n"`
  Remark: This line is part of the executable source code.
- Line 940: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 941: `            "/profile USER - view profile\\n"`
  Remark: This line is part of the executable source code.
- Line 942: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 943: `            "/search TEXT - search current room\\n"`
  Remark: This line is part of the executable source code.
- Line 944: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 945: `            "/friend USER - send friend request\\n"`
  Remark: This line is part of the executable source code.
- Line 946: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 947: `            "/accept USER - accept friend request\\n"`
  Remark: This line is part of the executable source code.
- Line 948: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 949: `            "/friends - list friends\\n"`
  Remark: This line is part of the executable source code.
- Line 950: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 951: `            "/gallery - show room image history\\n"`
  Remark: This line is part of the executable source code.
- Line 952: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 953: `            "/admin logs - security/admin dashboard\\n"`
  Remark: This line is part of the executable source code.
- Line 954: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 955: `            "/kick USER - admin kick\\n"`
  Remark: This line is part of the executable source code.
- Line 956: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 957: `            "/edit MESSAGE_ID TEXT - edit message\\n"`
  Remark: This line is part of the executable source code.
- Line 958: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 959: `            "/delete MESSAGE_ID - delete message\\n"`
  Remark: This line is part of the executable source code.
- Line 960: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 961: `            "/2fa - generate demo 2FA code\\n"`
  Remark: This line is part of the executable source code.
- Line 962: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 963: `            "Password rooms: create/join as room:password"`
  Remark: This line is part of the executable source code.
- Line 964: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 965: `        )`
  Remark: This line is part of the executable source code.
- Line 966: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 967: `        messagebox.showinfo("SecureChat Commands", commands)`
  Remark: This line is part of the executable source code.
- Line 968: ` `
  Remark: Blank line used for readability.
- Line 969: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 970: `    def _insert_emoji(self, emoji: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 971: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 972: `        self.message_var.set(self.message_var.get() + emoji)`
  Remark: This line is part of the executable source code.
- Line 973: ` `
  Remark: Blank line used for readability.
- Line 974: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 975: `    def _send_file(self, kind: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 976: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 977: `        if not self.logged_in:`
  Remark: This line is part of the executable source code.
- Line 978: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 979: `            self._set_chat_status("Please login first.", ok=False)`
  Remark: This line is part of the executable source code.
- Line 980: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 981: `            return`
  Remark: This line is part of the executable source code.
- Line 982: ` `
  Remark: Blank line used for readability.
- Line 983: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 984: `        filters = {`
  Remark: This line is part of the executable source code.
- Line 985: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 986: `            "file": [("All files", "*.*")],`
  Remark: This line is part of the executable source code.
- Line 987: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 988: `            "image": [("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"), ("All files", "*.*")],`
  Remark: This line is part of the executable source code.
- Line 989: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 990: `            "video": [("Video files", "*.mp4 *.mov *.avi *.mkv *.webm"), ("All files", "*.*")],`
  Remark: This line is part of the executable source code.
- Line 991: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 992: `        }`
  Remark: This line is part of the executable source code.
- Line 993: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 994: `        selected_path = filedialog.askopenfilename(filetypes=filters.get(kind, filters["file"]))`
  Remark: This line is part of the executable source code.
- Line 995: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 996: `        if not selected_path:`
  Remark: This line is part of the executable source code.
- Line 997: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 998: `            return`
  Remark: This line is part of the executable source code.
- Line 999: ` `
  Remark: Blank line used for readability.
- Line 1000: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1001: `        path = Path(selected_path)`
  Remark: This line is part of the executable source code.
- Line 1002: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1003: `        if path.stat().st_size > MAX_FILE_SIZE:`
  Remark: This line is part of the executable source code.
- Line 1004: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 1005: `            self._set_chat_status(`
  Remark: This line is part of the executable source code.
- Line 1006: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1007: `                f"File is too large. Maximum size is {MAX_FILE_SIZE // (1024 * 1024)} MB.",`
  Remark: This line is part of the executable source code.
- Line 1008: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1009: `                ok=False,`
  Remark: This line is part of the executable source code.
- Line 1010: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 1011: `            )`
  Remark: This line is part of the executable source code.
- Line 1012: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 1013: `            return`
  Remark: This line is part of the executable source code.
- Line 1014: ` `
  Remark: Blank line used for readability.
- Line 1015: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 1016: `        try:`
  Remark: This line is part of the executable source code.
- Line 1017: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1018: `            filename = InputValidator.filename(path.name)`
  Remark: This line is part of the executable source code.
- Line 1019: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1020: `            encoded_data = base64.b64encode(path.read_bytes()).decode("ascii")`
  Remark: This line is part of the executable source code.
- Line 1021: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1022: `            mime_type = mimetypes.guess_type(path.name)[0] or "application/octet-stream"`
  Remark: This line is part of the executable source code.
- Line 1023: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 1024: `            self.connection.send(`
  Remark: This line is part of the executable source code.
- Line 1025: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1026: `                "file",`
  Remark: This line is part of the executable source code.
- Line 1027: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1028: `                filename=filename,`
  Remark: This line is part of the executable source code.
- Line 1029: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1030: `                kind=kind,`
  Remark: This line is part of the executable source code.
- Line 1031: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1032: `                mime_type=mime_type,`
  Remark: This line is part of the executable source code.
- Line 1033: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1034: `                data=encoded_data,`
  Remark: This line is part of the executable source code.
- Line 1035: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 1036: `            )`
  Remark: This line is part of the executable source code.
- Line 1037: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1038: `            self._set_chat_status(f"Sending {kind}: {filename}", ok=True)`
  Remark: This line is part of the executable source code.
- Line 1039: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 1040: `        except Exception as exc:`
  Remark: This line is part of the executable source code.
- Line 1041: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1042: `            self._set_chat_status(f"Could not send {kind}: {exc}", ok=False)`
  Remark: This line is part of the executable source code.
- Line 1043: ` `
  Remark: Blank line used for readability.
- Line 1044: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1045: `    def _poll_incoming(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 1046: `        # Remark: starts a loop that continues while a condition is true.`
  Remark: starts a loop that continues while a condition is true.
- Line 1047: `        while not self.connection.incoming.empty():`
  Remark: This line is part of the executable source code.
- Line 1048: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1049: `            packet = self.connection.incoming.get_nowait()`
  Remark: This line is part of the executable source code.
- Line 1050: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1051: `            self._handle_packet(packet)`
  Remark: This line is part of the executable source code.
- Line 1052: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1053: `        self.after(100, self._poll_incoming)`
  Remark: This line is part of the executable source code.
- Line 1054: ` `
  Remark: Blank line used for readability.
- Line 1055: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1056: `    def _handle_packet(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 1057: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1058: `        packet_type = packet.get("type")`
  Remark: This line is part of the executable source code.
- Line 1059: ` `
  Remark: Blank line used for readability.
- Line 1060: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1061: `        if packet_type == "welcome":`
  Remark: This line is part of the executable source code.
- Line 1062: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1063: `            self._set_auth_status(str(packet.get("message", "Connected")), ok=True)`
  Remark: This line is part of the executable source code.
- Line 1064: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1065: `        elif packet_type == "ok":`
  Remark: This line is part of the executable source code.
- Line 1066: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1067: `            self._handle_ok(packet)`
  Remark: This line is part of the executable source code.
- Line 1068: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1069: `        elif packet_type == "error":`
  Remark: This line is part of the executable source code.
- Line 1070: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1071: `            self._handle_error(packet)`
  Remark: This line is part of the executable source code.
- Line 1072: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1073: `        elif packet_type == "history":`
  Remark: This line is part of the executable source code.
- Line 1074: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1075: `            self._show_history(packet)`
  Remark: This line is part of the executable source code.
- Line 1076: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1077: `        elif packet_type == "message":`
  Remark: This line is part of the executable source code.
- Line 1078: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 1079: `            self._append_chat(`
  Remark: This line is part of the executable source code.
- Line 1080: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1081: `                f"[{packet.get('created_at')}] #{packet.get('id', '?')} {packet.get('sender')}: {packet.get('body')}"`
  Remark: This line is part of the executable source code.
- Line 1082: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 1083: `            )`
  Remark: This line is part of the executable source code.
- Line 1084: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 1085: `            self.connection.send("read_receipt")`
  Remark: This line is part of the executable source code.
- Line 1086: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1087: `        elif packet_type == "file":`
  Remark: This line is part of the executable source code.
- Line 1088: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1089: `            self._handle_file_packet(packet)`
  Remark: This line is part of the executable source code.
- Line 1090: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1091: `        elif packet_type == "private_message":`
  Remark: This line is part of the executable source code.
- Line 1092: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 1093: `            self._append_chat(`
  Remark: This line is part of the executable source code.
- Line 1094: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1095: `                f"[{packet.get('created_at')}] PRIVATE {packet.get('sender')} -> {packet.get('target')}: {packet.get('body')}"`
  Remark: This line is part of the executable source code.
- Line 1096: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 1097: `            )`
  Remark: This line is part of the executable source code.
- Line 1098: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1099: `        elif packet_type == "advanced_response":`
  Remark: This line is part of the executable source code.
- Line 1100: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1101: `            self._show_advanced_response(packet)`
  Remark: This line is part of the executable source code.
- Line 1102: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1103: `        elif packet_type == "typing":`
  Remark: This line is part of the executable source code.
- Line 1104: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1105: `            self._set_chat_status(f"{packet.get('username')} is typing...", ok=True)`
  Remark: This line is part of the executable source code.
- Line 1106: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1107: `        elif packet_type == "system":`
  Remark: This line is part of the executable source code.
- Line 1108: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1109: `            self._append_chat(f"* {packet.get('message')}")`
  Remark: This line is part of the executable source code.
- Line 1110: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1111: `        elif packet_type == "users":`
  Remark: This line is part of the executable source code.
- Line 1112: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1113: `            self._show_users(packet)`
  Remark: This line is part of the executable source code.
- Line 1114: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1115: `        elif packet_type == "rooms":`
  Remark: This line is part of the executable source code.
- Line 1116: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1117: `            self._show_rooms(packet)`
  Remark: This line is part of the executable source code.
- Line 1118: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1119: `        elif packet_type == "connection_closed":`
  Remark: This line is part of the executable source code.
- Line 1120: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1121: `            message = f"Disconnected: {packet.get('message')}"`
  Remark: This line is part of the executable source code.
- Line 1122: `            # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1123: `            if self.current_screen == "auth":`
  Remark: This line is part of the executable source code.
- Line 1124: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1125: `                self._set_auth_status(message, ok=False)`
  Remark: This line is part of the executable source code.
- Line 1126: `            # Remark: handles the case where previous conditions were false.`
  Remark: handles the case where previous conditions were false.
- Line 1127: `            else:`
  Remark: This line is part of the executable source code.
- Line 1128: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1129: `                self._set_chat_status(message, ok=False)`
  Remark: This line is part of the executable source code.
- Line 1130: ` `
  Remark: Blank line used for readability.
- Line 1131: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1132: `    def _handle_ok(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 1133: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1134: `        action = packet.get("action")`
  Remark: This line is part of the executable source code.
- Line 1135: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1136: `        message = str(packet.get("message", "OK"))`
  Remark: This line is part of the executable source code.
- Line 1137: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1138: `        if action == "login":`
  Remark: This line is part of the executable source code.
- Line 1139: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1140: `            self.logged_in = True`
  Remark: This line is part of the executable source code.
- Line 1141: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1142: `            self.login_badge_var.set(f"Logged in as {self.username_var.get().strip()}")`
  Remark: This line is part of the executable source code.
- Line 1143: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1144: `            self._show_chat_screen()`
  Remark: This line is part of the executable source code.
- Line 1145: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1146: `            self._set_chat_status(message, ok=True)`
  Remark: This line is part of the executable source code.
- Line 1147: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1148: `            messagebox.showinfo("Login OK", message)`
  Remark: This line is part of the executable source code.
- Line 1149: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1150: `            self._request_rooms()`
  Remark: This line is part of the executable source code.
- Line 1151: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1152: `            self._request_users()`
  Remark: This line is part of the executable source code.
- Line 1153: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1154: `        elif action == "register":`
  Remark: This line is part of the executable source code.
- Line 1155: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1156: `            self._set_auth_status(f"{message}. Logging in...", ok=True)`
  Remark: This line is part of the executable source code.
- Line 1157: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1158: `            messagebox.showinfo("Register OK", f"{message}. You will be logged in now.")`
  Remark: This line is part of the executable source code.
- Line 1159: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 1160: `            self.connection.send(`
  Remark: This line is part of the executable source code.
- Line 1161: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1162: `                "login",`
  Remark: This line is part of the executable source code.
- Line 1163: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1164: `                username=self.username_var.get(),`
  Remark: This line is part of the executable source code.
- Line 1165: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1166: `                password=self.password_var.get(),`
  Remark: This line is part of the executable source code.
- Line 1167: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 1168: `            )`
  Remark: This line is part of the executable source code.
- Line 1169: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1170: `        elif action == "create_room":`
  Remark: This line is part of the executable source code.
- Line 1171: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1172: `            room = str(packet.get("room", "general"))`
  Remark: This line is part of the executable source code.
- Line 1173: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1174: `            self.new_room_var.set("")`
  Remark: This line is part of the executable source code.
- Line 1175: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1176: `            self.room_var.set(room)`
  Remark: This line is part of the executable source code.
- Line 1177: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1178: `            self._set_chat_status(message, ok=True)`
  Remark: This line is part of the executable source code.
- Line 1179: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 1180: `            self.connection.send("join", room=room)`
  Remark: This line is part of the executable source code.
- Line 1181: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1182: `        elif action == "join":`
  Remark: This line is part of the executable source code.
- Line 1183: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1184: `            self.current_room = str(packet.get("room", "general"))`
  Remark: This line is part of the executable source code.
- Line 1185: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1186: `            self.room_var.set(self.current_room)`
  Remark: This line is part of the executable source code.
- Line 1187: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1188: `            self.room_title_var.set(f"Room: {self.current_room}")`
  Remark: This line is part of the executable source code.
- Line 1189: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1190: `            self._clear_chat()`
  Remark: This line is part of the executable source code.
- Line 1191: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1192: `            self._set_chat_status(message, ok=True)`
  Remark: This line is part of the executable source code.
- Line 1193: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1194: `            self._request_rooms()`
  Remark: This line is part of the executable source code.
- Line 1195: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1196: `            self._request_users()`
  Remark: This line is part of the executable source code.
- Line 1197: ` `
  Remark: Blank line used for readability.
- Line 1198: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1199: `    def _handle_error(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 1200: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1201: `        action = packet.get("action")`
  Remark: This line is part of the executable source code.
- Line 1202: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1203: `        message = str(packet.get("message", "Unknown error"))`
  Remark: This line is part of the executable source code.
- Line 1204: ` `
  Remark: Blank line used for readability.
- Line 1205: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1206: `        if action == "register" and "already exists" in message.lower():`
  Remark: This line is part of the executable source code.
- Line 1207: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1208: `            self._set_auth_status("Username already exists. Trying to login...", ok=True)`
  Remark: This line is part of the executable source code.
- Line 1209: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 1210: `            self.connection.send(`
  Remark: This line is part of the executable source code.
- Line 1211: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1212: `                "login",`
  Remark: This line is part of the executable source code.
- Line 1213: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1214: `                username=self.username_var.get(),`
  Remark: This line is part of the executable source code.
- Line 1215: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1216: `                password=self.password_var.get(),`
  Remark: This line is part of the executable source code.
- Line 1217: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 1218: `            )`
  Remark: This line is part of the executable source code.
- Line 1219: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 1220: `            return`
  Remark: This line is part of the executable source code.
- Line 1221: ` `
  Remark: Blank line used for readability.
- Line 1222: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1223: `        if action in {"register", "login"} or self.current_screen == "auth":`
  Remark: This line is part of the executable source code.
- Line 1224: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1225: `            self._set_auth_status(message, ok=False)`
  Remark: This line is part of the executable source code.
- Line 1226: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1227: `            messagebox.showerror("Login/Register failed", message)`
  Remark: This line is part of the executable source code.
- Line 1228: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 1229: `            return`
  Remark: This line is part of the executable source code.
- Line 1230: ` `
  Remark: Blank line used for readability.
- Line 1231: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1232: `        self._set_chat_status(message, ok=False)`
  Remark: This line is part of the executable source code.
- Line 1233: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1234: `        messagebox.showerror("Action failed", message)`
  Remark: This line is part of the executable source code.
- Line 1235: ` `
  Remark: Blank line used for readability.
- Line 1236: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1237: `    def _show_history(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 1238: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1239: `        room = packet.get("room", "general")`
  Remark: This line is part of the executable source code.
- Line 1240: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1241: `        self.current_room = str(room)`
  Remark: This line is part of the executable source code.
- Line 1242: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1243: `        self.room_var.set(self.current_room)`
  Remark: This line is part of the executable source code.
- Line 1244: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1245: `        self.room_title_var.set(f"Room: {self.current_room}")`
  Remark: This line is part of the executable source code.
- Line 1246: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1247: `        self.chat_box.configure(state=tk.NORMAL)`
  Remark: This line is part of the executable source code.
- Line 1248: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1249: `        self.chat_box.delete("1.0", tk.END)`
  Remark: This line is part of the executable source code.
- Line 1250: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1251: `        self.chat_box.insert(tk.END, f"--- History for room {self.current_room} ---\n")`
  Remark: This line is part of the executable source code.
- Line 1252: `        # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 1253: `        for message in packet.get("messages", []):`
  Remark: This line is part of the executable source code.
- Line 1254: `            # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1255: `            if isinstance(message, dict):`
  Remark: This line is part of the executable source code.
- Line 1256: `                # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 1257: `                self.chat_box.insert(`
  Remark: This line is part of the executable source code.
- Line 1258: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1259: `                    tk.END,`
  Remark: This line is part of the executable source code.
- Line 1260: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1261: `                    f"[{message.get('created_at')}] {message.get('sender')}: {message.get('body')}\n",`
  Remark: This line is part of the executable source code.
- Line 1262: `                # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 1263: `                )`
  Remark: This line is part of the executable source code.
- Line 1264: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1265: `        self.chat_box.configure(state=tk.DISABLED)`
  Remark: This line is part of the executable source code.
- Line 1266: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1267: `        self.chat_box.see(tk.END)`
  Remark: This line is part of the executable source code.
- Line 1268: ` `
  Remark: Blank line used for readability.
- Line 1269: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1270: `    def _show_users(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 1271: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1272: `        self.users_box.delete(0, tk.END)`
  Remark: This line is part of the executable source code.
- Line 1273: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1274: `        online = packet.get("online", [])`
  Remark: This line is part of the executable source code.
- Line 1275: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1276: `        if isinstance(online, list):`
  Remark: This line is part of the executable source code.
- Line 1277: `            # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 1278: `            for user in online:`
  Remark: This line is part of the executable source code.
- Line 1279: `                # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1280: `                if isinstance(user, dict):`
  Remark: This line is part of the executable source code.
- Line 1281: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1282: `                    self.users_box.insert(tk.END, f"{user.get('username')} @ {user.get('room')}")`
  Remark: This line is part of the executable source code.
- Line 1283: ` `
  Remark: Blank line used for readability.
- Line 1284: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1285: `    def _show_rooms(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 1286: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1287: `        rooms = packet.get("rooms", [])`
  Remark: This line is part of the executable source code.
- Line 1288: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1289: `        current = str(packet.get("current", self.current_room))`
  Remark: This line is part of the executable source code.
- Line 1290: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1291: `        self.rooms_box.delete(0, tk.END)`
  Remark: This line is part of the executable source code.
- Line 1292: ` `
  Remark: Blank line used for readability.
- Line 1293: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1294: `        if isinstance(rooms, list):`
  Remark: This line is part of the executable source code.
- Line 1295: `            # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 1296: `            for index, room in enumerate(rooms):`
  Remark: This line is part of the executable source code.
- Line 1297: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1298: `                room_name = str(room)`
  Remark: This line is part of the executable source code.
- Line 1299: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1300: `                self.rooms_box.insert(tk.END, room_name)`
  Remark: This line is part of the executable source code.
- Line 1301: `                # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1302: `                if room_name == current:`
  Remark: This line is part of the executable source code.
- Line 1303: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1304: `                    self.rooms_box.selection_clear(0, tk.END)`
  Remark: This line is part of the executable source code.
- Line 1305: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1306: `                    self.rooms_box.selection_set(index)`
  Remark: This line is part of the executable source code.
- Line 1307: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1308: `                    self.rooms_box.see(index)`
  Remark: This line is part of the executable source code.
- Line 1309: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1310: `                    self.room_var.set(room_name)`
  Remark: This line is part of the executable source code.
- Line 1311: ` `
  Remark: Blank line used for readability.
- Line 1312: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1313: `    def _on_room_select(self, _event: tk.Event) -> None:`
  Remark: This line is part of the executable source code.
- Line 1314: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1315: `        selection = self.rooms_box.curselection()`
  Remark: This line is part of the executable source code.
- Line 1316: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1317: `        if selection:`
  Remark: This line is part of the executable source code.
- Line 1318: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1319: `            self.room_var.set(self.rooms_box.get(selection[0]))`
  Remark: This line is part of the executable source code.
- Line 1320: ` `
  Remark: Blank line used for readability.
- Line 1321: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1322: `    def _show_advanced_response(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 1323: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1324: `        title = str(packet.get("title", "Advanced response"))`
  Remark: This line is part of the executable source code.
- Line 1325: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1326: `        lines = packet.get("lines", [])`
  Remark: This line is part of the executable source code.
- Line 1327: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1328: `        self._append_chat(f"--- {title} ---")`
  Remark: This line is part of the executable source code.
- Line 1329: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1330: `        if isinstance(lines, list):`
  Remark: This line is part of the executable source code.
- Line 1331: `            # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 1332: `            for line in lines:`
  Remark: This line is part of the executable source code.
- Line 1333: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1334: `                self._append_chat(str(line))`
  Remark: This line is part of the executable source code.
- Line 1335: `        # Remark: handles the case where previous conditions were false.`
  Remark: handles the case where previous conditions were false.
- Line 1336: `        else:`
  Remark: This line is part of the executable source code.
- Line 1337: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1338: `            self._append_chat(str(lines))`
  Remark: This line is part of the executable source code.
- Line 1339: ` `
  Remark: Blank line used for readability.
- Line 1340: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1341: `    def _handle_file_packet(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 1342: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 1343: `        try:`
  Remark: This line is part of the executable source code.
- Line 1344: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1345: `            filename = InputValidator.filename(str(packet.get("filename", "download.bin")))`
  Remark: This line is part of the executable source code.
- Line 1346: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1347: `            kind = str(packet.get("kind", "file"))`
  Remark: This line is part of the executable source code.
- Line 1348: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1349: `            sender = str(packet.get("sender", "unknown"))`
  Remark: This line is part of the executable source code.
- Line 1350: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1351: `            created_at = str(packet.get("created_at", ""))`
  Remark: This line is part of the executable source code.
- Line 1352: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1353: `            encoded_data = str(packet.get("data", ""))`
  Remark: This line is part of the executable source code.
- Line 1354: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1355: `            file_data = base64.b64decode(encoded_data.encode("ascii"), validate=True)`
  Remark: This line is part of the executable source code.
- Line 1356: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 1357: `        except Exception as exc:`
  Remark: This line is part of the executable source code.
- Line 1358: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1359: `            self._set_chat_status(f"Received invalid file packet: {exc}", ok=False)`
  Remark: This line is part of the executable source code.
- Line 1360: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 1361: `            return`
  Remark: This line is part of the executable source code.
- Line 1362: ` `
  Remark: Blank line used for readability.
- Line 1363: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1364: `        DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)`
  Remark: This line is part of the executable source code.
- Line 1365: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1366: `        save_path = self._unique_download_path(filename)`
  Remark: This line is part of the executable source code.
- Line 1367: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1368: `        save_path.write_bytes(file_data)`
  Remark: This line is part of the executable source code.
- Line 1369: ` `
  Remark: Blank line used for readability.
- Line 1370: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1371: `        if kind == "image":`
  Remark: This line is part of the executable source code.
- Line 1372: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1373: `            self._append_image_preview(created_at, sender, filename, save_path)`
  Remark: This line is part of the executable source code.
- Line 1374: `        # Remark: handles the case where previous conditions were false.`
  Remark: handles the case where previous conditions were false.
- Line 1375: `        else:`
  Remark: This line is part of the executable source code.
- Line 1376: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1377: `            self._append_clickable_file(created_at, sender, kind, filename, save_path)`
  Remark: This line is part of the executable source code.
- Line 1378: ` `
  Remark: Blank line used for readability.
- Line 1379: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1380: `    def _unique_download_path(self, filename: str) -> Path:`
  Remark: This line is part of the executable source code.
- Line 1381: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1382: `        path = DOWNLOAD_DIR / filename`
  Remark: This line is part of the executable source code.
- Line 1383: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1384: `        if not path.exists():`
  Remark: This line is part of the executable source code.
- Line 1385: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 1386: `            return path`
  Remark: This line is part of the executable source code.
- Line 1387: ` `
  Remark: Blank line used for readability.
- Line 1388: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1389: `        stem = path.stem`
  Remark: This line is part of the executable source code.
- Line 1390: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1391: `        suffix = path.suffix`
  Remark: This line is part of the executable source code.
- Line 1392: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1393: `        counter = 1`
  Remark: This line is part of the executable source code.
- Line 1394: `        # Remark: starts a loop that continues while a condition is true.`
  Remark: starts a loop that continues while a condition is true.
- Line 1395: `        while True:`
  Remark: This line is part of the executable source code.
- Line 1396: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1397: `            candidate = DOWNLOAD_DIR / f"{stem}_{counter}{suffix}"`
  Remark: This line is part of the executable source code.
- Line 1398: `            # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1399: `            if not candidate.exists():`
  Remark: This line is part of the executable source code.
- Line 1400: `                # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 1401: `                return candidate`
  Remark: This line is part of the executable source code.
- Line 1402: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1403: `            counter += 1`
  Remark: This line is part of the executable source code.
- Line 1404: ` `
  Remark: Blank line used for readability.
- Line 1405: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1406: `    def _append_image_preview(`
  Remark: This line is part of the executable source code.
- Line 1407: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1408: `        self,`
  Remark: This line is part of the executable source code.
- Line 1409: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1410: `        created_at: str,`
  Remark: This line is part of the executable source code.
- Line 1411: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1412: `        sender: str,`
  Remark: This line is part of the executable source code.
- Line 1413: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1414: `        filename: str,`
  Remark: This line is part of the executable source code.
- Line 1415: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1416: `        save_path: Path,`
  Remark: This line is part of the executable source code.
- Line 1417: `    # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 1418: `    ) -> None:`
  Remark: This line is part of the executable source code.
- Line 1419: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1420: `        self._append_clickable_file(created_at, sender, "image", filename, save_path)`
  Remark: This line is part of the executable source code.
- Line 1421: ` `
  Remark: Blank line used for readability.
- Line 1422: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 1423: `        try:`
  Remark: This line is part of the executable source code.
- Line 1424: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1425: `            image = Image.open(save_path)`
  Remark: This line is part of the executable source code.
- Line 1426: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1427: `            image.thumbnail((320, 220))`
  Remark: This line is part of the executable source code.
- Line 1428: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1429: `            preview = ImageTk.PhotoImage(image)`
  Remark: This line is part of the executable source code.
- Line 1430: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 1431: `        except Exception as exc:`
  Remark: This line is part of the executable source code.
- Line 1432: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1433: `            self._append_chat(f"Could not show image preview: {exc}")`
  Remark: This line is part of the executable source code.
- Line 1434: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 1435: `            return`
  Remark: This line is part of the executable source code.
- Line 1436: ` `
  Remark: Blank line used for readability.
- Line 1437: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1438: `        self.chat_images.append(preview)`
  Remark: This line is part of the executable source code.
- Line 1439: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1440: `        self.chat_box.configure(state=tk.NORMAL)`
  Remark: This line is part of the executable source code.
- Line 1441: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1442: `        self.chat_box.image_create(tk.END, image=preview)`
  Remark: This line is part of the executable source code.
- Line 1443: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1444: `        self.chat_box.insert(tk.END, "\n")`
  Remark: This line is part of the executable source code.
- Line 1445: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1446: `        self.chat_box.configure(state=tk.DISABLED)`
  Remark: This line is part of the executable source code.
- Line 1447: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1448: `        self.chat_box.see(tk.END)`
  Remark: This line is part of the executable source code.
- Line 1449: ` `
  Remark: Blank line used for readability.
- Line 1450: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1451: `    def _append_clickable_file(`
  Remark: This line is part of the executable source code.
- Line 1452: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1453: `        self,`
  Remark: This line is part of the executable source code.
- Line 1454: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1455: `        created_at: str,`
  Remark: This line is part of the executable source code.
- Line 1456: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1457: `        sender: str,`
  Remark: This line is part of the executable source code.
- Line 1458: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1459: `        kind: str,`
  Remark: This line is part of the executable source code.
- Line 1460: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1461: `        filename: str,`
  Remark: This line is part of the executable source code.
- Line 1462: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1463: `        save_path: Path,`
  Remark: This line is part of the executable source code.
- Line 1464: `    # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 1465: `    ) -> None:`
  Remark: This line is part of the executable source code.
- Line 1466: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1467: `        link_tag = f"link_{len(self.chat_links)}"`
  Remark: This line is part of the executable source code.
- Line 1468: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1469: `        self.chat_links[link_tag] = save_path`
  Remark: This line is part of the executable source code.
- Line 1470: ` `
  Remark: Blank line used for readability.
- Line 1471: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1472: `        self.chat_box.configure(state=tk.NORMAL)`
  Remark: This line is part of the executable source code.
- Line 1473: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1474: `        self.chat_box.insert(tk.END, f"[{created_at}] {sender} sent {kind}: ")`
  Remark: This line is part of the executable source code.
- Line 1475: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1476: `        self.chat_box.insert(tk.END, filename, (link_tag,))`
  Remark: This line is part of the executable source code.
- Line 1477: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1478: `        self.chat_box.insert(tk.END, " (click to open)\n")`
  Remark: This line is part of the executable source code.
- Line 1479: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1480: `        self.chat_box.tag_configure(link_tag, foreground="#2563eb", underline=True)`
  Remark: This line is part of the executable source code.
- Line 1481: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1482: `        self.chat_box.tag_bind(link_tag, "<Button-1>", lambda _event, tag=link_tag: self._open_chat_link(tag))`
  Remark: This line is part of the executable source code.
- Line 1483: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1484: `        self.chat_box.tag_bind(link_tag, "<Enter>", lambda _event: self.chat_box.configure(cursor="hand2"))`
  Remark: This line is part of the executable source code.
- Line 1485: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1486: `        self.chat_box.tag_bind(link_tag, "<Leave>", lambda _event: self.chat_box.configure(cursor=""))`
  Remark: This line is part of the executable source code.
- Line 1487: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1488: `        self.chat_box.configure(state=tk.DISABLED)`
  Remark: This line is part of the executable source code.
- Line 1489: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1490: `        self.chat_box.see(tk.END)`
  Remark: This line is part of the executable source code.
- Line 1491: ` `
  Remark: Blank line used for readability.
- Line 1492: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1493: `    def _open_chat_link(self, link_tag: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 1494: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1495: `        path = self.chat_links.get(link_tag)`
  Remark: This line is part of the executable source code.
- Line 1496: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1497: `        if path is None:`
  Remark: This line is part of the executable source code.
- Line 1498: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 1499: `            return`
  Remark: This line is part of the executable source code.
- Line 1500: ` `
  Remark: Blank line used for readability.
- Line 1501: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 1502: `        try:`
  Remark: This line is part of the executable source code.
- Line 1503: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 1504: `            self.connection.send("download_event", filename=path.name)`
  Remark: This line is part of the executable source code.
- Line 1505: `            # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1506: `            if os.name == "nt":`
  Remark: This line is part of the executable source code.
- Line 1507: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1508: `                os.startfile(path)`
  Remark: This line is part of the executable source code.
- Line 1509: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 1510: `            elif sys.platform == "darwin":`
  Remark: This line is part of the executable source code.
- Line 1511: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1512: `                subprocess.Popen(["open", str(path)])`
  Remark: This line is part of the executable source code.
- Line 1513: `            # Remark: handles the case where previous conditions were false.`
  Remark: handles the case where previous conditions were false.
- Line 1514: `            else:`
  Remark: This line is part of the executable source code.
- Line 1515: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1516: `                subprocess.Popen(["xdg-open", str(path)])`
  Remark: This line is part of the executable source code.
- Line 1517: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 1518: `        except Exception as exc:`
  Remark: This line is part of the executable source code.
- Line 1519: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1520: `            self._set_chat_status(f"Could not open file: {exc}", ok=False)`
  Remark: This line is part of the executable source code.
- Line 1521: ` `
  Remark: Blank line used for readability.
- Line 1522: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1523: `    def _append_chat(self, text: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 1524: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1525: `        self.chat_box.configure(state=tk.NORMAL)`
  Remark: This line is part of the executable source code.
- Line 1526: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1527: `        self.chat_box.insert(tk.END, text + "\n")`
  Remark: This line is part of the executable source code.
- Line 1528: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1529: `        self.chat_box.configure(state=tk.DISABLED)`
  Remark: This line is part of the executable source code.
- Line 1530: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1531: `        self.chat_box.see(tk.END)`
  Remark: This line is part of the executable source code.
- Line 1532: ` `
  Remark: Blank line used for readability.
- Line 1533: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1534: `    def _clear_chat(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 1535: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1536: `        self.chat_box.configure(state=tk.NORMAL)`
  Remark: This line is part of the executable source code.
- Line 1537: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1538: `        self.chat_box.delete("1.0", tk.END)`
  Remark: This line is part of the executable source code.
- Line 1539: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1540: `        self.chat_box.configure(state=tk.DISABLED)`
  Remark: This line is part of the executable source code.
- Line 1541: ` `
  Remark: Blank line used for readability.
- Line 1542: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1543: `    def _set_auth_status(self, message: str, ok: bool) -> None:`
  Remark: This line is part of the executable source code.
- Line 1544: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1545: `        self.auth_status_var.set(message)`
  Remark: This line is part of the executable source code.
- Line 1546: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 1547: `        self.auth_status_label.configure(`
  Remark: This line is part of the executable source code.
- Line 1548: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1549: `            bg="#dcfce7" if ok else "#fee2e2",`
  Remark: This line is part of the executable source code.
- Line 1550: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1551: `            fg="#166534" if ok else "#991b1b",`
  Remark: This line is part of the executable source code.
- Line 1552: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 1553: `        )`
  Remark: This line is part of the executable source code.
- Line 1554: ` `
  Remark: Blank line used for readability.
- Line 1555: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1556: `    def _set_chat_status(self, message: str, ok: bool) -> None:`
  Remark: This line is part of the executable source code.
- Line 1557: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1558: `        self.chat_status_var.set(message)`
  Remark: This line is part of the executable source code.
- Line 1559: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1560: `        self.chat_status_label.configure(fg="#16a34a" if ok else "#dc2626")`
  Remark: This line is part of the executable source code.
- Line 1561: ` `
  Remark: Blank line used for readability.
- Line 1562: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1563: `    def _on_close(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 1564: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1565: `        self.connection.close()`
  Remark: This line is part of the executable source code.
- Line 1566: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1567: `        self.destroy()`
  Remark: This line is part of the executable source code.
- Line 1568: ` `
  Remark: Blank line used for readability.
- Line 1569: ` `
  Remark: Blank line used for readability.
- Line 1570: `# Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 1571: `def parse_args() -> argparse.Namespace:`
  Remark: This line is part of the executable source code.
- Line 1572: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1573: `    parser = argparse.ArgumentParser(description="SecureChat Tkinter client")`
  Remark: This line is part of the executable source code.
- Line 1574: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1575: `    parser.add_argument("--host", default=DEFAULT_HOST)`
  Remark: This line is part of the executable source code.
- Line 1576: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1577: `    parser.add_argument("--port", type=int, default=DEFAULT_PORT)`
  Remark: This line is part of the executable source code.
- Line 1578: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1579: `    parser.add_argument("--verify-cert", action="store_true")`
  Remark: This line is part of the executable source code.
- Line 1580: `    # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 1581: `    return parser.parse_args()`
  Remark: This line is part of the executable source code.
- Line 1582: ` `
  Remark: Blank line used for readability.
- Line 1583: ` `
  Remark: Blank line used for readability.
- Line 1584: `# Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 1585: `if __name__ == "__main__":`
  Remark: This line is part of the executable source code.
- Line 1586: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1587: `    args = parse_args()`
  Remark: This line is part of the executable source code.
- Line 1588: `    # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 1589: `    client_connection = ChatClientConnection(`
  Remark: This line is part of the executable source code.
- Line 1590: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1591: `        host=args.host,`
  Remark: This line is part of the executable source code.
- Line 1592: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1593: `        port=args.port,`
  Remark: This line is part of the executable source code.
- Line 1594: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1595: `        verify_certificate=args.verify_cert,`
  Remark: This line is part of the executable source code.
- Line 1596: `    # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 1597: `    )`
  Remark: This line is part of the executable source code.
- Line 1598: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1599: `    client_connection.connect()`
  Remark: This line is part of the executable source code.
- Line 1600: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 1601: `    app = SecureChatApp(client_connection)`
  Remark: This line is part of the executable source code.
- Line 1602: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 1603: `    app.mainloop()`
  Remark: This line is part of the executable source code.
- Line 1604: ` `
  Remark: Blank line used for readability.

## `secure_chat/config.py`

- Line 1: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 2: `from pathlib import Path`
  Remark: This line is part of the executable source code.
- Line 3: ` `
  Remark: Blank line used for readability.
- Line 4: ` `
  Remark: Blank line used for readability.
- Line 5: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 6: `PROJECT_ROOT = Path(__file__).resolve().parent.parent`
  Remark: This line is part of the executable source code.
- Line 7: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 8: `DATA_DIR = PROJECT_ROOT / "data"`
  Remark: This line is part of the executable source code.
- Line 9: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 10: `CERT_DIR = PROJECT_ROOT / "certs"`
  Remark: This line is part of the executable source code.
- Line 11: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 12: `DOWNLOAD_DIR = PROJECT_ROOT / "downloads"`
  Remark: This line is part of the executable source code.
- Line 13: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 14: `UPLOAD_DIR = DATA_DIR / "uploads"`
  Remark: This line is part of the executable source code.
- Line 15: ` `
  Remark: Blank line used for readability.
- Line 16: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 17: `DATABASE_PATH = DATA_DIR / "secure_chat.db"`
  Remark: This line is part of the executable source code.
- Line 18: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 19: `LOG_PATH = DATA_DIR / "server.log"`
  Remark: This line is part of the executable source code.
- Line 20: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 21: `CERT_PATH = CERT_DIR / "server.crt"`
  Remark: This line is part of the executable source code.
- Line 22: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 23: `KEY_PATH = CERT_DIR / "server.key"`
  Remark: This line is part of the executable source code.
- Line 24: ` `
  Remark: Blank line used for readability.
- Line 25: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 26: `DEFAULT_HOST = "127.0.0.1"`
  Remark: This line is part of the executable source code.
- Line 27: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 28: `DEFAULT_PORT = 5050`
  Remark: This line is part of the executable source code.
- Line 29: ` `
  Remark: Blank line used for readability.
- Line 30: `# Media is sent as base64 inside JSON, so packets must be larger than plain text messages.`
  Remark: This is an existing programmer comment.
- Line 31: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 32: `MAX_PACKET_SIZE = 25 * 1024 * 1024`
  Remark: This line is part of the executable source code.
- Line 33: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 34: `MAX_FILE_SIZE = 15 * 1024 * 1024`
  Remark: This line is part of the executable source code.
- Line 35: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 36: `MAX_USERNAME_LENGTH = 20`
  Remark: This line is part of the executable source code.
- Line 37: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 38: `MAX_PASSWORD_LENGTH = 128`
  Remark: This line is part of the executable source code.
- Line 39: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 40: `MAX_ROOM_LENGTH = 30`
  Remark: This line is part of the executable source code.
- Line 41: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 42: `MAX_MESSAGE_LENGTH = 1000`
  Remark: This line is part of the executable source code.
- Line 43: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 44: `MAX_FILENAME_LENGTH = 120`
  Remark: This line is part of the executable source code.
- Line 45: ` `
  Remark: Blank line used for readability.
- Line 46: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 47: `PBKDF2_ITERATIONS = 250_000`
  Remark: This line is part of the executable source code.
- Line 48: ` `
  Remark: Blank line used for readability.

## `secure_chat/models.py`

- Line 1: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 2: `from dataclasses import dataclass`
  Remark: This line is part of the executable source code.
- Line 3: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 4: `from datetime import datetime`
  Remark: This line is part of the executable source code.
- Line 5: ` `
  Remark: Blank line used for readability.
- Line 6: ` `
  Remark: Blank line used for readability.
- Line 7: `# Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 8: `@dataclass(frozen=True)`
  Remark: This line is part of the executable source code.
- Line 9: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 10: `class User:`
  Remark: This line is part of the executable source code.
- Line 11: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 12: `    username: str`
  Remark: This line is part of the executable source code.
- Line 13: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 14: `    created_at: str`
  Remark: This line is part of the executable source code.
- Line 15: ` `
  Remark: Blank line used for readability.
- Line 16: ` `
  Remark: Blank line used for readability.
- Line 17: `# Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 18: `@dataclass(frozen=True)`
  Remark: This line is part of the executable source code.
- Line 19: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 20: `class ChatMessage:`
  Remark: This line is part of the executable source code.
- Line 21: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 22: `    sender: str`
  Remark: This line is part of the executable source code.
- Line 23: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 24: `    room: str`
  Remark: This line is part of the executable source code.
- Line 25: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 26: `    body: str`
  Remark: This line is part of the executable source code.
- Line 27: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 28: `    created_at: str`
  Remark: This line is part of the executable source code.
- Line 29: ` `
  Remark: Blank line used for readability.
- Line 30: ` `
  Remark: Blank line used for readability.
- Line 31: `# Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 32: `@dataclass(frozen=True)`
  Remark: This line is part of the executable source code.
- Line 33: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 34: `class ClientInfo:`
  Remark: This line is part of the executable source code.
- Line 35: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 36: `    username: str`
  Remark: This line is part of the executable source code.
- Line 37: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 38: `    room: str`
  Remark: This line is part of the executable source code.
- Line 39: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 40: `    address: str`
  Remark: This line is part of the executable source code.
- Line 41: ` `
  Remark: Blank line used for readability.
- Line 42: ` `
  Remark: Blank line used for readability.
- Line 43: `# Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 44: `@dataclass(frozen=True)`
  Remark: This line is part of the executable source code.
- Line 45: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 46: `class ServerEvent:`
  Remark: This line is part of the executable source code.
- Line 47: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 48: `    event_type: str`
  Remark: This line is part of the executable source code.
- Line 49: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 50: `    message: str`
  Remark: This line is part of the executable source code.
- Line 51: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 52: `    created_at: str`
  Remark: This line is part of the executable source code.
- Line 53: ` `
  Remark: Blank line used for readability.
- Line 54: ` `
  Remark: Blank line used for readability.
- Line 55: `# Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 56: `def now_iso() -> str:`
  Remark: This line is part of the executable source code.
- Line 57: `    # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 58: `    return datetime.utcnow().replace(microsecond=0).isoformat() + "Z"`
  Remark: This line is part of the executable source code.
- Line 59: ` `
  Remark: Blank line used for readability.

## `secure_chat/protocol.py`

- Line 1: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 2: `import json`
  Remark: This line is part of the executable source code.
- Line 3: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 4: `import socket`
  Remark: This line is part of the executable source code.
- Line 5: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 6: `import struct`
  Remark: This line is part of the executable source code.
- Line 7: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 8: `from typing import Any`
  Remark: This line is part of the executable source code.
- Line 9: ` `
  Remark: Blank line used for readability.
- Line 10: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 11: `from secure_chat.config import MAX_PACKET_SIZE`
  Remark: This line is part of the executable source code.
- Line 12: ` `
  Remark: Blank line used for readability.
- Line 13: ` `
  Remark: Blank line used for readability.
- Line 14: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 15: `class ProtocolError(Exception):`
  Remark: This line is part of the executable source code.
- Line 16: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 17: `    """Raised when a peer sends an invalid protocol packet."""`
  Remark: This line is part of the executable source code.
- Line 18: ` `
  Remark: Blank line used for readability.
- Line 19: ` `
  Remark: Blank line used for readability.
- Line 20: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 21: `class ChatProtocol:`
  Remark: This line is part of the executable source code.
- Line 22: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 23: `    """`
  Remark: This line is part of the executable source code.
- Line 24: `    Custom length-prefixed JSON protocol.`
  Remark: This line is part of the executable source code.
- Line 25: ` `
  Remark: Blank line used for readability.
- Line 26: `    Packet layout:`
  Remark: This line is part of the executable source code.
- Line 27: `    - 4 bytes unsigned big-endian payload length`
  Remark: This line is part of the executable source code.
- Line 28: `    - UTF-8 JSON payload`
  Remark: This line is part of the executable source code.
- Line 29: `    """`
  Remark: This line is part of the executable source code.
- Line 30: ` `
  Remark: Blank line used for readability.
- Line 31: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 32: `    HEADER_SIZE = 4`
  Remark: This line is part of the executable source code.
- Line 33: ` `
  Remark: Blank line used for readability.
- Line 34: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 35: `    @staticmethod`
  Remark: This line is part of the executable source code.
- Line 36: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 37: `    def send(sock: socket.socket, packet_type: str, **fields: Any) -> None:`
  Remark: This line is part of the executable source code.
- Line 38: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 39: `        packet = {"type": packet_type, **fields}`
  Remark: This line is part of the executable source code.
- Line 40: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 41: `        raw = json.dumps(packet, ensure_ascii=False).encode("utf-8")`
  Remark: This line is part of the executable source code.
- Line 42: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 43: `        if len(raw) > MAX_PACKET_SIZE:`
  Remark: This line is part of the executable source code.
- Line 44: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 45: `            raise ProtocolError("Packet is too large")`
  Remark: This line is part of the executable source code.
- Line 46: ` `
  Remark: Blank line used for readability.
- Line 47: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 48: `        header = struct.pack("!I", len(raw))`
  Remark: This line is part of the executable source code.
- Line 49: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 50: `        sock.sendall(header + raw)`
  Remark: This line is part of the executable source code.
- Line 51: ` `
  Remark: Blank line used for readability.
- Line 52: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 53: `    @staticmethod`
  Remark: This line is part of the executable source code.
- Line 54: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 55: `    def receive(sock: socket.socket) -> dict[str, Any]:`
  Remark: This line is part of the executable source code.
- Line 56: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 57: `        header = ChatProtocol._receive_exact(sock, ChatProtocol.HEADER_SIZE)`
  Remark: This line is part of the executable source code.
- Line 58: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 59: `        if not header:`
  Remark: This line is part of the executable source code.
- Line 60: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 61: `            raise ConnectionError("Peer disconnected")`
  Remark: This line is part of the executable source code.
- Line 62: ` `
  Remark: Blank line used for readability.
- Line 63: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 64: `        (payload_size,) = struct.unpack("!I", header)`
  Remark: This line is part of the executable source code.
- Line 65: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 66: `        if payload_size <= 0 or payload_size > MAX_PACKET_SIZE:`
  Remark: This line is part of the executable source code.
- Line 67: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 68: `            raise ProtocolError("Invalid packet size")`
  Remark: This line is part of the executable source code.
- Line 69: ` `
  Remark: Blank line used for readability.
- Line 70: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 71: `        payload = ChatProtocol._receive_exact(sock, payload_size)`
  Remark: This line is part of the executable source code.
- Line 72: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 73: `        try:`
  Remark: This line is part of the executable source code.
- Line 74: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 75: `            packet = json.loads(payload.decode("utf-8"))`
  Remark: This line is part of the executable source code.
- Line 76: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 77: `        except (UnicodeDecodeError, json.JSONDecodeError) as exc:`
  Remark: This line is part of the executable source code.
- Line 78: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 79: `            raise ProtocolError("Packet is not valid UTF-8 JSON") from exc`
  Remark: This line is part of the executable source code.
- Line 80: ` `
  Remark: Blank line used for readability.
- Line 81: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 82: `        if not isinstance(packet, dict) or not isinstance(packet.get("type"), str):`
  Remark: This line is part of the executable source code.
- Line 83: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 84: `            raise ProtocolError("Packet must contain a string type")`
  Remark: This line is part of the executable source code.
- Line 85: ` `
  Remark: Blank line used for readability.
- Line 86: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 87: `        return packet`
  Remark: This line is part of the executable source code.
- Line 88: ` `
  Remark: Blank line used for readability.
- Line 89: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 90: `    @staticmethod`
  Remark: This line is part of the executable source code.
- Line 91: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 92: `    def _receive_exact(sock: socket.socket, size: int) -> bytes:`
  Remark: This line is part of the executable source code.
- Line 93: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 94: `        chunks: list[bytes] = []`
  Remark: This line is part of the executable source code.
- Line 95: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 96: `        remaining = size`
  Remark: This line is part of the executable source code.
- Line 97: ` `
  Remark: Blank line used for readability.
- Line 98: `        # Remark: starts a loop that continues while a condition is true.`
  Remark: starts a loop that continues while a condition is true.
- Line 99: `        while remaining > 0:`
  Remark: This line is part of the executable source code.
- Line 100: `            # Remark: receives data from the network.`
  Remark: receives data from the network.
- Line 101: `            chunk = sock.recv(remaining)`
  Remark: This line is part of the executable source code.
- Line 102: `            # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 103: `            if not chunk:`
  Remark: This line is part of the executable source code.
- Line 104: `                # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 105: `                raise ConnectionError("Peer disconnected")`
  Remark: This line is part of the executable source code.
- Line 106: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 107: `            chunks.append(chunk)`
  Remark: This line is part of the executable source code.
- Line 108: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 109: `            remaining -= len(chunk)`
  Remark: This line is part of the executable source code.
- Line 110: ` `
  Remark: Blank line used for readability.
- Line 111: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 112: `        return b"".join(chunks)`
  Remark: This line is part of the executable source code.
- Line 113: ` `
  Remark: Blank line used for readability.

## `secure_chat/security.py`

- Line 1: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 2: `import hmac`
  Remark: This line is part of the executable source code.
- Line 3: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 4: `import os`
  Remark: This line is part of the executable source code.
- Line 5: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 6: `import re`
  Remark: This line is part of the executable source code.
- Line 7: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 8: `import ssl`
  Remark: This line is part of the executable source code.
- Line 9: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 10: `from datetime import datetime, timedelta, timezone`
  Remark: This line is part of the executable source code.
- Line 11: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 12: `from hashlib import pbkdf2_hmac`
  Remark: This line is part of the executable source code.
- Line 13: ` `
  Remark: Blank line used for readability.
- Line 14: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 15: `from secure_chat.config import (`
  Remark: This line is part of the executable source code.
- Line 16: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 17: `    CERT_DIR,`
  Remark: This line is part of the executable source code.
- Line 18: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 19: `    CERT_PATH,`
  Remark: This line is part of the executable source code.
- Line 20: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 21: `    KEY_PATH,`
  Remark: This line is part of the executable source code.
- Line 22: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 23: `    MAX_MESSAGE_LENGTH,`
  Remark: This line is part of the executable source code.
- Line 24: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 25: `    MAX_PASSWORD_LENGTH,`
  Remark: This line is part of the executable source code.
- Line 26: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 27: `    MAX_ROOM_LENGTH,`
  Remark: This line is part of the executable source code.
- Line 28: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 29: `    MAX_USERNAME_LENGTH,`
  Remark: This line is part of the executable source code.
- Line 30: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 31: `    MAX_FILENAME_LENGTH,`
  Remark: This line is part of the executable source code.
- Line 32: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 33: `    PBKDF2_ITERATIONS,`
  Remark: This line is part of the executable source code.
- Line 34: `# Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 35: `)`
  Remark: This line is part of the executable source code.
- Line 36: ` `
  Remark: Blank line used for readability.
- Line 37: ` `
  Remark: Blank line used for readability.
- Line 38: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 39: `class ValidationError(ValueError):`
  Remark: This line is part of the executable source code.
- Line 40: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 41: `    """Raised when user-controlled input is not allowed."""`
  Remark: This line is part of the executable source code.
- Line 42: ` `
  Remark: Blank line used for readability.
- Line 43: ` `
  Remark: Blank line used for readability.
- Line 44: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 45: `class PasswordHasher:`
  Remark: This line is part of the executable source code.
- Line 46: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 47: `    @staticmethod`
  Remark: This line is part of the executable source code.
- Line 48: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 49: `    def hash_password(password: str) -> str:`
  Remark: This line is part of the executable source code.
- Line 50: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 51: `        salt = os.urandom(16)`
  Remark: This line is part of the executable source code.
- Line 52: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 53: `        digest = pbkdf2_hmac(`
  Remark: This line is part of the executable source code.
- Line 54: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 55: `            "sha256",`
  Remark: This line is part of the executable source code.
- Line 56: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 57: `            password.encode("utf-8"),`
  Remark: This line is part of the executable source code.
- Line 58: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 59: `            salt,`
  Remark: This line is part of the executable source code.
- Line 60: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 61: `            PBKDF2_ITERATIONS,`
  Remark: This line is part of the executable source code.
- Line 62: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 63: `        )`
  Remark: This line is part of the executable source code.
- Line 64: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 65: `        return f"{PBKDF2_ITERATIONS}${salt.hex()}${digest.hex()}"`
  Remark: This line is part of the executable source code.
- Line 66: ` `
  Remark: Blank line used for readability.
- Line 67: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 68: `    @staticmethod`
  Remark: This line is part of the executable source code.
- Line 69: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 70: `    def verify_password(password: str, stored_hash: str) -> bool:`
  Remark: This line is part of the executable source code.
- Line 71: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 72: `        try:`
  Remark: This line is part of the executable source code.
- Line 73: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 74: `            iterations_text, salt_hex, digest_hex = stored_hash.split("$")`
  Remark: This line is part of the executable source code.
- Line 75: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 76: `            iterations = int(iterations_text)`
  Remark: This line is part of the executable source code.
- Line 77: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 78: `            salt = bytes.fromhex(salt_hex)`
  Remark: This line is part of the executable source code.
- Line 79: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 80: `            expected_digest = bytes.fromhex(digest_hex)`
  Remark: This line is part of the executable source code.
- Line 81: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 82: `        except (ValueError, TypeError):`
  Remark: This line is part of the executable source code.
- Line 83: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 84: `            return False`
  Remark: This line is part of the executable source code.
- Line 85: ` `
  Remark: Blank line used for readability.
- Line 86: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 87: `        actual_digest = pbkdf2_hmac(`
  Remark: This line is part of the executable source code.
- Line 88: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 89: `            "sha256",`
  Remark: This line is part of the executable source code.
- Line 90: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 91: `            password.encode("utf-8"),`
  Remark: This line is part of the executable source code.
- Line 92: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 93: `            salt,`
  Remark: This line is part of the executable source code.
- Line 94: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 95: `            iterations,`
  Remark: This line is part of the executable source code.
- Line 96: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 97: `        )`
  Remark: This line is part of the executable source code.
- Line 98: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 99: `        return hmac.compare_digest(actual_digest, expected_digest)`
  Remark: This line is part of the executable source code.
- Line 100: ` `
  Remark: Blank line used for readability.
- Line 101: ` `
  Remark: Blank line used for readability.
- Line 102: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 103: `class InputValidator:`
  Remark: This line is part of the executable source code.
- Line 104: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 105: `    USERNAME_PATTERN = re.compile(r"^[A-Za-z0-9_]{3,20}$")`
  Remark: This line is part of the executable source code.
- Line 106: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 107: `    ROOM_PATTERN = re.compile(r"^[A-Za-z0-9_-]{1,30}$")`
  Remark: This line is part of the executable source code.
- Line 108: ` `
  Remark: Blank line used for readability.
- Line 109: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 110: `    @classmethod`
  Remark: This line is part of the executable source code.
- Line 111: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 112: `    def username(cls, value: str) -> str:`
  Remark: This line is part of the executable source code.
- Line 113: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 114: `        value = value.strip()`
  Remark: This line is part of the executable source code.
- Line 115: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 116: `        if len(value) > MAX_USERNAME_LENGTH or not cls.USERNAME_PATTERN.fullmatch(value):`
  Remark: This line is part of the executable source code.
- Line 117: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 118: `            raise ValidationError("Username must be 3-20 letters, numbers, or underscores")`
  Remark: This line is part of the executable source code.
- Line 119: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 120: `        return value`
  Remark: This line is part of the executable source code.
- Line 121: ` `
  Remark: Blank line used for readability.
- Line 122: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 123: `    @classmethod`
  Remark: This line is part of the executable source code.
- Line 124: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 125: `    def password(cls, value: str) -> str:`
  Remark: This line is part of the executable source code.
- Line 126: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 127: `        if not 6 <= len(value) <= MAX_PASSWORD_LENGTH:`
  Remark: This line is part of the executable source code.
- Line 128: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 129: `            raise ValidationError("Password must be 6-128 characters")`
  Remark: This line is part of the executable source code.
- Line 130: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 131: `        return value`
  Remark: This line is part of the executable source code.
- Line 132: ` `
  Remark: Blank line used for readability.
- Line 133: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 134: `    @classmethod`
  Remark: This line is part of the executable source code.
- Line 135: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 136: `    def room(cls, value: str) -> str:`
  Remark: This line is part of the executable source code.
- Line 137: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 138: `        value = value.strip() or "general"`
  Remark: This line is part of the executable source code.
- Line 139: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 140: `        if len(value) > MAX_ROOM_LENGTH or not cls.ROOM_PATTERN.fullmatch(value):`
  Remark: This line is part of the executable source code.
- Line 141: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 142: `            raise ValidationError("Room must contain only letters, numbers, _ or -")`
  Remark: This line is part of the executable source code.
- Line 143: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 144: `        return value`
  Remark: This line is part of the executable source code.
- Line 145: ` `
  Remark: Blank line used for readability.
- Line 146: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 147: `    @classmethod`
  Remark: This line is part of the executable source code.
- Line 148: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 149: `    def message(cls, value: str) -> str:`
  Remark: This line is part of the executable source code.
- Line 150: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 151: `        value = value.strip()`
  Remark: This line is part of the executable source code.
- Line 152: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 153: `        if not value:`
  Remark: This line is part of the executable source code.
- Line 154: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 155: `            raise ValidationError("Message cannot be empty")`
  Remark: This line is part of the executable source code.
- Line 156: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 157: `        if len(value) > MAX_MESSAGE_LENGTH:`
  Remark: This line is part of the executable source code.
- Line 158: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 159: `            raise ValidationError(f"Message cannot be longer than {MAX_MESSAGE_LENGTH} characters")`
  Remark: This line is part of the executable source code.
- Line 160: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 161: `        return value`
  Remark: This line is part of the executable source code.
- Line 162: ` `
  Remark: Blank line used for readability.
- Line 163: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 164: `    @classmethod`
  Remark: This line is part of the executable source code.
- Line 165: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 166: `    def filename(cls, value: str) -> str:`
  Remark: This line is part of the executable source code.
- Line 167: `        # Remark: places a widget in the graphical interface.`
  Remark: places a widget in the graphical interface.
- Line 168: `        value = value.strip().replace("\\", "_").replace("/", "_")`
  Remark: This line is part of the executable source code.
- Line 169: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 170: `        if not value or value in {".", ".."}:`
  Remark: This line is part of the executable source code.
- Line 171: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 172: `            raise ValidationError("Filename is not valid")`
  Remark: This line is part of the executable source code.
- Line 173: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 174: `        if len(value) > MAX_FILENAME_LENGTH:`
  Remark: This line is part of the executable source code.
- Line 175: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 176: `            raise ValidationError(f"Filename cannot be longer than {MAX_FILENAME_LENGTH} characters")`
  Remark: This line is part of the executable source code.
- Line 177: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 178: `        return value`
  Remark: This line is part of the executable source code.
- Line 179: ` `
  Remark: Blank line used for readability.
- Line 180: ` `
  Remark: Blank line used for readability.
- Line 181: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 182: `class TLSContextFactory:`
  Remark: This line is part of the executable source code.
- Line 183: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 184: `    @staticmethod`
  Remark: This line is part of the executable source code.
- Line 185: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 186: `    def server_context() -> ssl.SSLContext:`
  Remark: This line is part of the executable source code.
- Line 187: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 188: `        TLSContextFactory.ensure_development_certificate()`
  Remark: This line is part of the executable source code.
- Line 189: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 190: `        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)`
  Remark: This line is part of the executable source code.
- Line 191: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 192: `        context.minimum_version = ssl.TLSVersion.TLSv1_2`
  Remark: This line is part of the executable source code.
- Line 193: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 194: `        context.load_cert_chain(certfile=CERT_PATH, keyfile=KEY_PATH)`
  Remark: This line is part of the executable source code.
- Line 195: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 196: `        return context`
  Remark: This line is part of the executable source code.
- Line 197: ` `
  Remark: Blank line used for readability.
- Line 198: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 199: `    @staticmethod`
  Remark: This line is part of the executable source code.
- Line 200: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 201: `    def client_context(verify_certificate: bool = False) -> ssl.SSLContext:`
  Remark: This line is part of the executable source code.
- Line 202: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 203: `        if verify_certificate:`
  Remark: This line is part of the executable source code.
- Line 204: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 205: `            context = ssl.create_default_context(cafile=str(CERT_PATH))`
  Remark: This line is part of the executable source code.
- Line 206: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 207: `            context.check_hostname = False`
  Remark: This line is part of the executable source code.
- Line 208: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 209: `            return context`
  Remark: This line is part of the executable source code.
- Line 210: ` `
  Remark: Blank line used for readability.
- Line 211: `        # Local classroom/demo mode: traffic is encrypted, but the self-signed`
  Remark: This is an existing programmer comment.
- Line 212: `        # certificate is not authenticated by a public certificate authority.`
  Remark: This is an existing programmer comment.
- Line 213: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 214: `        context = ssl._create_unverified_context()`
  Remark: This line is part of the executable source code.
- Line 215: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 216: `        context.minimum_version = ssl.TLSVersion.TLSv1_2`
  Remark: This line is part of the executable source code.
- Line 217: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 218: `        return context`
  Remark: This line is part of the executable source code.
- Line 219: ` `
  Remark: Blank line used for readability.
- Line 220: `    # Remark: applies a decorator to the next function or method.`
  Remark: applies a decorator to the next function or method.
- Line 221: `    @staticmethod`
  Remark: This line is part of the executable source code.
- Line 222: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 223: `    def ensure_development_certificate() -> None:`
  Remark: This line is part of the executable source code.
- Line 224: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 225: `        if (`
  Remark: This line is part of the executable source code.
- Line 226: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 227: `            CERT_PATH.exists()`
  Remark: This line is part of the executable source code.
- Line 228: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 229: `            and CERT_PATH.stat().st_size > 0`
  Remark: This line is part of the executable source code.
- Line 230: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 231: `            and KEY_PATH.exists()`
  Remark: This line is part of the executable source code.
- Line 232: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 233: `            and KEY_PATH.stat().st_size > 0`
  Remark: This line is part of the executable source code.
- Line 234: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 235: `        ):`
  Remark: This line is part of the executable source code.
- Line 236: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 237: `            return`
  Remark: This line is part of the executable source code.
- Line 238: ` `
  Remark: Blank line used for readability.
- Line 239: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 240: `        CERT_DIR.mkdir(parents=True, exist_ok=True)`
  Remark: This line is part of the executable source code.
- Line 241: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 242: `        try:`
  Remark: This line is part of the executable source code.
- Line 243: `            # Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 244: `            from cryptography import x509`
  Remark: This line is part of the executable source code.
- Line 245: `            # Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 246: `            from cryptography.hazmat.primitives import hashes, serialization`
  Remark: This line is part of the executable source code.
- Line 247: `            # Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 248: `            from cryptography.hazmat.primitives.asymmetric import rsa`
  Remark: This line is part of the executable source code.
- Line 249: `            # Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 250: `            from cryptography.x509.oid import NameOID`
  Remark: This line is part of the executable source code.
- Line 251: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 252: `        except ImportError as exc:`
  Remark: This line is part of the executable source code.
- Line 253: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 254: `            raise RuntimeError(`
  Remark: This line is part of the executable source code.
- Line 255: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 256: `                "Missing TLS certificate. Install dependencies with: pip install -r requirements.txt"`
  Remark: This line is part of the executable source code.
- Line 257: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 258: `            ) from exc`
  Remark: This line is part of the executable source code.
- Line 259: ` `
  Remark: Blank line used for readability.
- Line 260: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 261: `        private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)`
  Remark: This line is part of the executable source code.
- Line 262: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 263: `        subject = issuer = x509.Name(`
  Remark: This line is part of the executable source code.
- Line 264: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 265: `            [x509.NameAttribute(NameOID.COMMON_NAME, "SecureChatLocal")]`
  Remark: This line is part of the executable source code.
- Line 266: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 267: `        )`
  Remark: This line is part of the executable source code.
- Line 268: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 269: `        certificate = (`
  Remark: This line is part of the executable source code.
- Line 270: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 271: `            x509.CertificateBuilder()`
  Remark: This line is part of the executable source code.
- Line 272: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 273: `            .subject_name(subject)`
  Remark: This line is part of the executable source code.
- Line 274: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 275: `            .issuer_name(issuer)`
  Remark: This line is part of the executable source code.
- Line 276: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 277: `            .public_key(private_key.public_key())`
  Remark: This line is part of the executable source code.
- Line 278: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 279: `            .serial_number(x509.random_serial_number())`
  Remark: This line is part of the executable source code.
- Line 280: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 281: `            .not_valid_before(datetime.now(timezone.utc) - timedelta(days=1))`
  Remark: This line is part of the executable source code.
- Line 282: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 283: `            .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))`
  Remark: This line is part of the executable source code.
- Line 284: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 285: `            .sign(private_key, hashes.SHA256())`
  Remark: This line is part of the executable source code.
- Line 286: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 287: `        )`
  Remark: This line is part of the executable source code.
- Line 288: ` `
  Remark: Blank line used for readability.
- Line 289: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 290: `        KEY_PATH.write_bytes(`
  Remark: This line is part of the executable source code.
- Line 291: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 292: `            private_key.private_bytes(`
  Remark: This line is part of the executable source code.
- Line 293: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 294: `                encoding=serialization.Encoding.PEM,`
  Remark: This line is part of the executable source code.
- Line 295: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 296: `                format=serialization.PrivateFormat.PKCS8,`
  Remark: This line is part of the executable source code.
- Line 297: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 298: `                encryption_algorithm=serialization.NoEncryption(),`
  Remark: This line is part of the executable source code.
- Line 299: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 300: `            )`
  Remark: This line is part of the executable source code.
- Line 301: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 302: `        )`
  Remark: This line is part of the executable source code.
- Line 303: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 304: `        CERT_PATH.write_bytes(certificate.public_bytes(serialization.Encoding.PEM))`
  Remark: This line is part of the executable source code.
- Line 305: ` `
  Remark: Blank line used for readability.

## `secure_chat/server.py`

- Line 1: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 2: `import argparse`
  Remark: This line is part of the executable source code.
- Line 3: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 4: `import base64`
  Remark: This line is part of the executable source code.
- Line 5: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 6: `import random`
  Remark: This line is part of the executable source code.
- Line 7: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 8: `import socket`
  Remark: This line is part of the executable source code.
- Line 9: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 10: `import threading`
  Remark: This line is part of the executable source code.
- Line 11: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 12: `import uuid`
  Remark: This line is part of the executable source code.
- Line 13: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 14: `from typing import Optional`
  Remark: This line is part of the executable source code.
- Line 15: ` `
  Remark: Blank line used for readability.
- Line 16: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 17: `from secure_chat.config import DEFAULT_HOST, DEFAULT_PORT, LOG_PATH, MAX_FILE_SIZE, UPLOAD_DIR`
  Remark: This line is part of the executable source code.
- Line 18: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 19: `from secure_chat.models import ChatMessage, ClientInfo, now_iso`
  Remark: This line is part of the executable source code.
- Line 20: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 21: `from secure_chat.protocol import ChatProtocol, ProtocolError`
  Remark: This line is part of the executable source code.
- Line 22: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 23: `from secure_chat.security import InputValidator, TLSContextFactory, ValidationError`
  Remark: This line is part of the executable source code.
- Line 24: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 25: `from secure_chat.storage import ChatDatabase`
  Remark: This line is part of the executable source code.
- Line 26: ` `
  Remark: Blank line used for readability.
- Line 27: ` `
  Remark: Blank line used for readability.
- Line 28: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 29: `class ClientHandler(threading.Thread):`
  Remark: This line is part of the executable source code.
- Line 30: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 31: `    def __init__(`
  Remark: This line is part of the executable source code.
- Line 32: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 33: `        self,`
  Remark: This line is part of the executable source code.
- Line 34: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 35: `        server: "SecureChatServer",`
  Remark: This line is part of the executable source code.
- Line 36: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 37: `        connection: socket.socket,`
  Remark: This line is part of the executable source code.
- Line 38: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 39: `        address: tuple[str, int],`
  Remark: This line is part of the executable source code.
- Line 40: `    # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 41: `    ) -> None:`
  Remark: This line is part of the executable source code.
- Line 42: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 43: `        super().__init__(daemon=True)`
  Remark: This line is part of the executable source code.
- Line 44: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 45: `        self.server = server`
  Remark: This line is part of the executable source code.
- Line 46: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 47: `        self.connection = connection`
  Remark: This line is part of the executable source code.
- Line 48: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 49: `        self.address = f"{address[0]}:{address[1]}"`
  Remark: This line is part of the executable source code.
- Line 50: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 51: `        self.username: Optional[str] = None`
  Remark: This line is part of the executable source code.
- Line 52: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 53: `        self.room = "general"`
  Remark: This line is part of the executable source code.
- Line 54: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 55: `        self.running = True`
  Remark: This line is part of the executable source code.
- Line 56: ` `
  Remark: Blank line used for readability.
- Line 57: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 58: `    def run(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 59: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 60: `        try:`
  Remark: This line is part of the executable source code.
- Line 61: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 62: `            ChatProtocol.send(self.connection, "welcome", message="Connected to SecureChat")`
  Remark: This line is part of the executable source code.
- Line 63: `            # Remark: starts a loop that continues while a condition is true.`
  Remark: starts a loop that continues while a condition is true.
- Line 64: `            while self.running:`
  Remark: This line is part of the executable source code.
- Line 65: `                # Remark: receives data from the network.`
  Remark: receives data from the network.
- Line 66: `                packet = ChatProtocol.receive(self.connection)`
  Remark: This line is part of the executable source code.
- Line 67: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 68: `                self._handle_packet(packet)`
  Remark: This line is part of the executable source code.
- Line 69: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 70: `        except (ConnectionError, OSError, ProtocolError, ValidationError) as exc:`
  Remark: This line is part of the executable source code.
- Line 71: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 72: `            self.server.log(f"Client {self.address} disconnected: {exc}")`
  Remark: This line is part of the executable source code.
- Line 73: `        # Remark: runs cleanup code after protected code finishes.`
  Remark: runs cleanup code after protected code finishes.
- Line 74: `        finally:`
  Remark: This line is part of the executable source code.
- Line 75: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 76: `            self.running = False`
  Remark: This line is part of the executable source code.
- Line 77: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 78: `            self.server.remove_client(self)`
  Remark: This line is part of the executable source code.
- Line 79: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 80: `            self._safe_close()`
  Remark: This line is part of the executable source code.
- Line 81: ` `
  Remark: Blank line used for readability.
- Line 82: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 83: `    def send(self, packet_type: str, **fields: object) -> None:`
  Remark: This line is part of the executable source code.
- Line 84: `        # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 85: `        ChatProtocol.send(self.connection, packet_type, **fields)`
  Remark: This line is part of the executable source code.
- Line 86: ` `
  Remark: Blank line used for readability.
- Line 87: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 88: `    def _handle_packet(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 89: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 90: `        packet_type = packet["type"]`
  Remark: This line is part of the executable source code.
- Line 91: ` `
  Remark: Blank line used for readability.
- Line 92: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 93: `        try:`
  Remark: This line is part of the executable source code.
- Line 94: `            # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 95: `            if packet_type == "register":`
  Remark: This line is part of the executable source code.
- Line 96: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 97: `                self._register(packet)`
  Remark: This line is part of the executable source code.
- Line 98: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 99: `            elif packet_type == "login":`
  Remark: This line is part of the executable source code.
- Line 100: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 101: `                self._login(packet)`
  Remark: This line is part of the executable source code.
- Line 102: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 103: `            elif packet_type == "join":`
  Remark: This line is part of the executable source code.
- Line 104: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 105: `                self._require_login()`
  Remark: This line is part of the executable source code.
- Line 106: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 107: `                self._join(packet)`
  Remark: This line is part of the executable source code.
- Line 108: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 109: `            elif packet_type == "create_room":`
  Remark: This line is part of the executable source code.
- Line 110: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 111: `                self._require_login()`
  Remark: This line is part of the executable source code.
- Line 112: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 113: `                self._create_room(packet)`
  Remark: This line is part of the executable source code.
- Line 114: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 115: `            elif packet_type == "rooms":`
  Remark: This line is part of the executable source code.
- Line 116: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 117: `                self._require_login()`
  Remark: This line is part of the executable source code.
- Line 118: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 119: `                self._rooms()`
  Remark: This line is part of the executable source code.
- Line 120: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 121: `            elif packet_type == "message":`
  Remark: This line is part of the executable source code.
- Line 122: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 123: `                self._require_login()`
  Remark: This line is part of the executable source code.
- Line 124: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 125: `                self._message(packet)`
  Remark: This line is part of the executable source code.
- Line 126: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 127: `            elif packet_type == "file":`
  Remark: This line is part of the executable source code.
- Line 128: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 129: `                self._require_login()`
  Remark: This line is part of the executable source code.
- Line 130: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 131: `                self._file(packet)`
  Remark: This line is part of the executable source code.
- Line 132: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 133: `            elif packet_type == "command":`
  Remark: This line is part of the executable source code.
- Line 134: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 135: `                self._require_login()`
  Remark: This line is part of the executable source code.
- Line 136: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 137: `                self._command(packet)`
  Remark: This line is part of the executable source code.
- Line 138: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 139: `            elif packet_type == "typing":`
  Remark: This line is part of the executable source code.
- Line 140: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 141: `                self._require_login()`
  Remark: This line is part of the executable source code.
- Line 142: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 143: `                self.server.broadcast_typing(self.username or "", self.room)`
  Remark: This line is part of the executable source code.
- Line 144: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 145: `            elif packet_type == "read_receipt":`
  Remark: This line is part of the executable source code.
- Line 146: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 147: `                self._require_login()`
  Remark: This line is part of the executable source code.
- Line 148: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 149: `                self.server.broadcast_system(f"{self.username} read the latest messages", self.room)`
  Remark: This line is part of the executable source code.
- Line 150: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 151: `            elif packet_type == "download_event":`
  Remark: This line is part of the executable source code.
- Line 152: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 153: `                self._require_login()`
  Remark: This line is part of the executable source code.
- Line 154: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 155: `                filename = InputValidator.filename(str(packet.get("filename", "")))`
  Remark: This line is part of the executable source code.
- Line 156: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 157: `                self.server.database.record_download(self.username or "", filename)`
  Remark: This line is part of the executable source code.
- Line 158: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 159: `                self.server.database.log_event("download", f"{self.username} opened {filename}")`
  Remark: This line is part of the executable source code.
- Line 160: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 161: `            elif packet_type == "users":`
  Remark: This line is part of the executable source code.
- Line 162: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 163: `                self._require_login()`
  Remark: This line is part of the executable source code.
- Line 164: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 165: `                self._users()`
  Remark: This line is part of the executable source code.
- Line 166: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 167: `            elif packet_type == "history":`
  Remark: This line is part of the executable source code.
- Line 168: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 169: `                self._require_login()`
  Remark: This line is part of the executable source code.
- Line 170: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 171: `                self._history()`
  Remark: This line is part of the executable source code.
- Line 172: `            # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 173: `            elif packet_type == "logout":`
  Remark: This line is part of the executable source code.
- Line 174: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 175: `                self.running = False`
  Remark: This line is part of the executable source code.
- Line 176: `            # Remark: handles the case where previous conditions were false.`
  Remark: handles the case where previous conditions were false.
- Line 177: `            else:`
  Remark: This line is part of the executable source code.
- Line 178: `                # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 179: `                raise ProtocolError(f"Unknown packet type: {packet_type}")`
  Remark: This line is part of the executable source code.
- Line 180: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 181: `        except ValidationError as exc:`
  Remark: This line is part of the executable source code.
- Line 182: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 183: `            self.send("error", action=packet_type, message=str(exc))`
  Remark: This line is part of the executable source code.
- Line 184: ` `
  Remark: Blank line used for readability.
- Line 185: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 186: `    def _register(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 187: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 188: `        username = InputValidator.username(str(packet.get("username", "")))`
  Remark: This line is part of the executable source code.
- Line 189: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 190: `        password = InputValidator.password(str(packet.get("password", "")))`
  Remark: This line is part of the executable source code.
- Line 191: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 192: `        created = self.server.database.create_user(username, password)`
  Remark: This line is part of the executable source code.
- Line 193: ` `
  Remark: Blank line used for readability.
- Line 194: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 195: `        if not created:`
  Remark: This line is part of the executable source code.
- Line 196: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 197: `            self.send("error", action="register", message="Username already exists")`
  Remark: This line is part of the executable source code.
- Line 198: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 199: `            return`
  Remark: This line is part of the executable source code.
- Line 200: ` `
  Remark: Blank line used for readability.
- Line 201: `        # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 202: `        self.send("ok", action="register", message="Registration successful")`
  Remark: This line is part of the executable source code.
- Line 203: ` `
  Remark: Blank line used for readability.
- Line 204: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 205: `    def _login(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 206: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 207: `        username = InputValidator.username(str(packet.get("username", "")))`
  Remark: This line is part of the executable source code.
- Line 208: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 209: `        password = InputValidator.password(str(packet.get("password", "")))`
  Remark: This line is part of the executable source code.
- Line 210: ` `
  Remark: Blank line used for readability.
- Line 211: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 212: `        if not self.server.database.authenticate(username, password):`
  Remark: This line is part of the executable source code.
- Line 213: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 214: `            self.server.database.log_event("login_failed", f"Failed login for {username}")`
  Remark: This line is part of the executable source code.
- Line 215: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 216: `            self.send("error", action="login", message="Invalid username or password")`
  Remark: This line is part of the executable source code.
- Line 217: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 218: `            return`
  Remark: This line is part of the executable source code.
- Line 219: ` `
  Remark: Blank line used for readability.
- Line 220: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 221: `        self.username = username`
  Remark: This line is part of the executable source code.
- Line 222: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 223: `        self.server.add_client(self)`
  Remark: This line is part of the executable source code.
- Line 224: `        # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 225: `        self.send("ok", action="login", message=f"Logged in as {username}")`
  Remark: This line is part of the executable source code.
- Line 226: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 227: `        self._rooms()`
  Remark: This line is part of the executable source code.
- Line 228: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 229: `        self._history()`
  Remark: This line is part of the executable source code.
- Line 230: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 231: `        self.server.broadcast_system(f"{username} joined {self.room}", self.room)`
  Remark: This line is part of the executable source code.
- Line 232: ` `
  Remark: Blank line used for readability.
- Line 233: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 234: `    def _join(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 235: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 236: `        old_room = self.room`
  Remark: This line is part of the executable source code.
- Line 237: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 238: `        requested_room, password = self._split_room_password(str(packet.get("room", "general")))`
  Remark: This line is part of the executable source code.
- Line 239: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 240: `        requested_room = InputValidator.room(requested_room)`
  Remark: This line is part of the executable source code.
- Line 241: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 242: `        if not self.server.database.room_exists(requested_room):`
  Remark: This line is part of the executable source code.
- Line 243: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 244: `            self.send("error", action="join", message="Room does not exist. Create it first.")`
  Remark: This line is part of the executable source code.
- Line 245: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 246: `            return`
  Remark: This line is part of the executable source code.
- Line 247: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 248: `        if not self.server.database.can_join_room(requested_room, password):`
  Remark: This line is part of the executable source code.
- Line 249: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 250: `            self.send("error", action="join", message="Room password is incorrect.")`
  Remark: This line is part of the executable source code.
- Line 251: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 252: `            return`
  Remark: This line is part of the executable source code.
- Line 253: ` `
  Remark: Blank line used for readability.
- Line 254: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 255: `        self.room = requested_room`
  Remark: This line is part of the executable source code.
- Line 256: `        # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 257: `        self.send("ok", action="join", room=self.room, message=f"Joined room {self.room}")`
  Remark: This line is part of the executable source code.
- Line 258: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 259: `        self._rooms()`
  Remark: This line is part of the executable source code.
- Line 260: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 261: `        self._history()`
  Remark: This line is part of the executable source code.
- Line 262: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 263: `        self.server.broadcast_system(f"{self.username} left {old_room}", old_room)`
  Remark: This line is part of the executable source code.
- Line 264: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 265: `        self.server.broadcast_system(f"{self.username} joined {self.room}", self.room)`
  Remark: This line is part of the executable source code.
- Line 266: ` `
  Remark: Blank line used for readability.
- Line 267: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 268: `    def _create_room(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 269: `        # Remark: checks an assumption that should be true.`
  Remark: checks an assumption that should be true.
- Line 270: `        assert self.username is not None`
  Remark: This line is part of the executable source code.
- Line 271: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 272: `        room_text = str(packet.get("room", ""))`
  Remark: This line is part of the executable source code.
- Line 273: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 274: `        room, password = self._split_room_password(room_text)`
  Remark: This line is part of the executable source code.
- Line 275: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 276: `        room = InputValidator.room(room)`
  Remark: This line is part of the executable source code.
- Line 277: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 278: `        created = self.server.database.create_room(room, self.username, password)`
  Remark: This line is part of the executable source code.
- Line 279: ` `
  Remark: Blank line used for readability.
- Line 280: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 281: `        if not created:`
  Remark: This line is part of the executable source code.
- Line 282: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 283: `            self.send("error", action="create_room", message="Room already exists")`
  Remark: This line is part of the executable source code.
- Line 284: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 285: `            return`
  Remark: This line is part of the executable source code.
- Line 286: ` `
  Remark: Blank line used for readability.
- Line 287: `        # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 288: `        self.send("ok", action="create_room", room=room, message=f"Room {room} created")`
  Remark: This line is part of the executable source code.
- Line 289: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 290: `        self.server.broadcast_rooms()`
  Remark: This line is part of the executable source code.
- Line 291: ` `
  Remark: Blank line used for readability.
- Line 292: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 293: `    def _split_room_password(self, room_text: str) -> tuple[str, str]:`
  Remark: This line is part of the executable source code.
- Line 294: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 295: `        if ":" not in room_text:`
  Remark: This line is part of the executable source code.
- Line 296: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 297: `            return room_text, ""`
  Remark: This line is part of the executable source code.
- Line 298: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 299: `        room, password = room_text.split(":", 1)`
  Remark: This line is part of the executable source code.
- Line 300: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 301: `        return room, password`
  Remark: This line is part of the executable source code.
- Line 302: ` `
  Remark: Blank line used for readability.
- Line 303: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 304: `    def _message(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 305: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 306: `        body = InputValidator.message(str(packet.get("body", "")))`
  Remark: This line is part of the executable source code.
- Line 307: `        # Remark: checks an assumption that should be true.`
  Remark: checks an assumption that should be true.
- Line 308: `        assert self.username is not None`
  Remark: This line is part of the executable source code.
- Line 309: ` `
  Remark: Blank line used for readability.
- Line 310: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 311: `        message = ChatMessage(`
  Remark: This line is part of the executable source code.
- Line 312: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 313: `            sender=self.username,`
  Remark: This line is part of the executable source code.
- Line 314: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 315: `            room=self.room,`
  Remark: This line is part of the executable source code.
- Line 316: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 317: `            body=body,`
  Remark: This line is part of the executable source code.
- Line 318: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 319: `            created_at=now_iso(),`
  Remark: This line is part of the executable source code.
- Line 320: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 321: `        )`
  Remark: This line is part of the executable source code.
- Line 322: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 323: `        message_id = self.server.database.save_message(message)`
  Remark: This line is part of the executable source code.
- Line 324: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 325: `        self.server.broadcast_chat(message, message_id)`
  Remark: This line is part of the executable source code.
- Line 326: ` `
  Remark: Blank line used for readability.
- Line 327: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 328: `    def _file(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 329: `        # Remark: checks an assumption that should be true.`
  Remark: checks an assumption that should be true.
- Line 330: `        assert self.username is not None`
  Remark: This line is part of the executable source code.
- Line 331: ` `
  Remark: Blank line used for readability.
- Line 332: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 333: `        filename = InputValidator.filename(str(packet.get("filename", "")))`
  Remark: This line is part of the executable source code.
- Line 334: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 335: `        kind = str(packet.get("kind", "file"))`
  Remark: This line is part of the executable source code.
- Line 336: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 337: `        encoded_data = str(packet.get("data", ""))`
  Remark: This line is part of the executable source code.
- Line 338: ` `
  Remark: Blank line used for readability.
- Line 339: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 340: `        try:`
  Remark: This line is part of the executable source code.
- Line 341: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 342: `            file_data = base64.b64decode(encoded_data.encode("ascii"), validate=True)`
  Remark: This line is part of the executable source code.
- Line 343: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 344: `        except Exception as exc:`
  Remark: This line is part of the executable source code.
- Line 345: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 346: `            raise ValidationError("File data is not valid base64") from exc`
  Remark: This line is part of the executable source code.
- Line 347: ` `
  Remark: Blank line used for readability.
- Line 348: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 349: `        if len(file_data) > MAX_FILE_SIZE:`
  Remark: This line is part of the executable source code.
- Line 350: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 351: `            raise ValidationError(f"File is too large. Maximum size is {MAX_FILE_SIZE // (1024 * 1024)} MB")`
  Remark: This line is part of the executable source code.
- Line 352: ` `
  Remark: Blank line used for readability.
- Line 353: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 354: `        room_upload_dir = UPLOAD_DIR / self.room`
  Remark: This line is part of the executable source code.
- Line 355: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 356: `        room_upload_dir.mkdir(parents=True, exist_ok=True)`
  Remark: This line is part of the executable source code.
- Line 357: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 358: `        stored_filename = f"{uuid.uuid4().hex}_{filename}"`
  Remark: This line is part of the executable source code.
- Line 359: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 360: `        (room_upload_dir / stored_filename).write_bytes(file_data)`
  Remark: This line is part of the executable source code.
- Line 361: ` `
  Remark: Blank line used for readability.
- Line 362: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 363: `        created_at = now_iso()`
  Remark: This line is part of the executable source code.
- Line 364: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 365: `        message = ChatMessage(`
  Remark: This line is part of the executable source code.
- Line 366: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 367: `            sender=self.username,`
  Remark: This line is part of the executable source code.
- Line 368: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 369: `            room=self.room,`
  Remark: This line is part of the executable source code.
- Line 370: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 371: `            body=f"[{kind}] {filename}",`
  Remark: This line is part of the executable source code.
- Line 372: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 373: `            created_at=created_at,`
  Remark: This line is part of the executable source code.
- Line 374: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 375: `        )`
  Remark: This line is part of the executable source code.
- Line 376: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 377: `        self.server.database.save_message(message)`
  Remark: This line is part of the executable source code.
- Line 378: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 379: `        self.server.broadcast_file(`
  Remark: This line is part of the executable source code.
- Line 380: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 381: `            sender=self.username,`
  Remark: This line is part of the executable source code.
- Line 382: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 383: `            room=self.room,`
  Remark: This line is part of the executable source code.
- Line 384: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 385: `            filename=filename,`
  Remark: This line is part of the executable source code.
- Line 386: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 387: `            kind=kind,`
  Remark: This line is part of the executable source code.
- Line 388: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 389: `            size=len(file_data),`
  Remark: This line is part of the executable source code.
- Line 390: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 391: `            data=encoded_data,`
  Remark: This line is part of the executable source code.
- Line 392: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 393: `            created_at=created_at,`
  Remark: This line is part of the executable source code.
- Line 394: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 395: `        )`
  Remark: This line is part of the executable source code.
- Line 396: ` `
  Remark: Blank line used for readability.
- Line 397: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 398: `    def _command(self, packet: dict[str, object]) -> None:`
  Remark: This line is part of the executable source code.
- Line 399: `        # Remark: checks an assumption that should be true.`
  Remark: checks an assumption that should be true.
- Line 400: `        assert self.username is not None`
  Remark: This line is part of the executable source code.
- Line 401: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 402: `        command = str(packet.get("body", "")).strip()`
  Remark: This line is part of the executable source code.
- Line 403: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 404: `        parts = command.split(" ", 2)`
  Remark: This line is part of the executable source code.
- Line 405: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 406: `        name = parts[0].lower() if parts else ""`
  Remark: This line is part of the executable source code.
- Line 407: ` `
  Remark: Blank line used for readability.
- Line 408: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 409: `        if name == "/dm" and len(parts) == 3:`
  Remark: This line is part of the executable source code.
- Line 410: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 411: `            self.server.send_private_message(self.username, parts[1], parts[2])`
  Remark: This line is part of the executable source code.
- Line 412: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 413: `        elif name == "/profile" and len(parts) >= 2:`
  Remark: This line is part of the executable source code.
- Line 414: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 415: `            self._profile_command(parts)`
  Remark: This line is part of the executable source code.
- Line 416: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 417: `        elif name == "/search" and len(parts) >= 2:`
  Remark: This line is part of the executable source code.
- Line 418: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 419: `            term = command.split(" ", 1)[1]`
  Remark: This line is part of the executable source code.
- Line 420: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 421: `            self._advanced_response("Search results", self.server.database.search_messages(self.room, term))`
  Remark: This line is part of the executable source code.
- Line 422: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 423: `        elif name == "/friend" and len(parts) >= 2:`
  Remark: This line is part of the executable source code.
- Line 424: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 425: `            ok = self.server.database.send_friend_request(self.username, parts[1])`
  Remark: This line is part of the executable source code.
- Line 426: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 427: `            self._advanced_response("Friend request", ["Sent" if ok else "Request already exists"])`
  Remark: This line is part of the executable source code.
- Line 428: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 429: `        elif name == "/accept" and len(parts) >= 2:`
  Remark: This line is part of the executable source code.
- Line 430: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 431: `            ok = self.server.database.accept_friend_request(parts[1], self.username)`
  Remark: This line is part of the executable source code.
- Line 432: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 433: `            self._advanced_response("Friend request", ["Accepted" if ok else "No pending request found"])`
  Remark: This line is part of the executable source code.
- Line 434: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 435: `        elif name == "/friends":`
  Remark: This line is part of the executable source code.
- Line 436: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 437: `            self._advanced_response("Friends", self.server.database.list_friends(self.username))`
  Remark: This line is part of the executable source code.
- Line 438: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 439: `        elif name == "/gallery":`
  Remark: This line is part of the executable source code.
- Line 440: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 441: `            self._advanced_response("Image gallery", self.server.database.image_gallery(self.room))`
  Remark: This line is part of the executable source code.
- Line 442: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 443: `        elif name == "/admin" and len(parts) >= 2:`
  Remark: This line is part of the executable source code.
- Line 444: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 445: `            self._admin_command(command)`
  Remark: This line is part of the executable source code.
- Line 446: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 447: `        elif name == "/kick" and len(parts) >= 2:`
  Remark: This line is part of the executable source code.
- Line 448: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 449: `            self._kick_command(parts[1])`
  Remark: This line is part of the executable source code.
- Line 450: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 451: `        elif name == "/edit" and len(parts) == 3:`
  Remark: This line is part of the executable source code.
- Line 452: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 453: `            self._edit_command(parts[1], parts[2])`
  Remark: This line is part of the executable source code.
- Line 454: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 455: `        elif name == "/delete" and len(parts) >= 2:`
  Remark: This line is part of the executable source code.
- Line 456: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 457: `            self._delete_command(parts[1])`
  Remark: This line is part of the executable source code.
- Line 458: `        # Remark: checks another possible condition.`
  Remark: checks another possible condition.
- Line 459: `        elif name == "/2fa":`
  Remark: This line is part of the executable source code.
- Line 460: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 461: `            code = f"{random.randint(0, 999999):06d}"`
  Remark: This line is part of the executable source code.
- Line 462: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 463: `            self.server.database.log_event("2fa", f"{self.username} generated demo 2FA code {code}")`
  Remark: This line is part of the executable source code.
- Line 464: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 465: `            self._advanced_response("Demo 2FA", [f"Your one-time demo code is {code}"])`
  Remark: This line is part of the executable source code.
- Line 466: `        # Remark: handles the case where previous conditions were false.`
  Remark: handles the case where previous conditions were false.
- Line 467: `        else:`
  Remark: This line is part of the executable source code.
- Line 468: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 469: `            self._advanced_response("Unknown command", [self._command_help()])`
  Remark: This line is part of the executable source code.
- Line 470: ` `
  Remark: Blank line used for readability.
- Line 471: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 472: `    def _profile_command(self, parts: list[str]) -> None:`
  Remark: This line is part of the executable source code.
- Line 473: `        # Remark: checks an assumption that should be true.`
  Remark: checks an assumption that should be true.
- Line 474: `        assert self.username is not None`
  Remark: This line is part of the executable source code.
- Line 475: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 476: `        if parts[1].lower() == "set" and len(parts) == 3:`
  Remark: This line is part of the executable source code.
- Line 477: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 478: `            self.server.database.update_profile(self.username, parts[2])`
  Remark: This line is part of the executable source code.
- Line 479: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 480: `            self._advanced_response("Profile", ["Profile status updated"])`
  Remark: This line is part of the executable source code.
- Line 481: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 482: `            return`
  Remark: This line is part of the executable source code.
- Line 483: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 484: `        target = parts[1]`
  Remark: This line is part of the executable source code.
- Line 485: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 486: `        self._advanced_response("Profile", [f"{target}: {self.server.database.get_profile(target)}"])`
  Remark: This line is part of the executable source code.
- Line 487: ` `
  Remark: Blank line used for readability.
- Line 488: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 489: `    def _admin_command(self, command: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 490: `        # Remark: checks an assumption that should be true.`
  Remark: checks an assumption that should be true.
- Line 491: `        assert self.username is not None`
  Remark: This line is part of the executable source code.
- Line 492: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 493: `        if not self.server.database.is_admin(self.username):`
  Remark: This line is part of the executable source code.
- Line 494: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 495: `            self._advanced_response("Admin", ["Only admin users can run this command"])`
  Remark: This line is part of the executable source code.
- Line 496: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 497: `            return`
  Remark: This line is part of the executable source code.
- Line 498: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 499: `        if command.strip().lower() == "/admin logs":`
  Remark: This line is part of the executable source code.
- Line 500: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 501: `            self._advanced_response("Admin logs", self.server.database.audit_events())`
  Remark: This line is part of the executable source code.
- Line 502: `        # Remark: handles the case where previous conditions were false.`
  Remark: handles the case where previous conditions were false.
- Line 503: `        else:`
  Remark: This line is part of the executable source code.
- Line 504: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 505: `            self._advanced_response("Admin", ["/admin logs"])`
  Remark: This line is part of the executable source code.
- Line 506: ` `
  Remark: Blank line used for readability.
- Line 507: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 508: `    def _kick_command(self, target: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 509: `        # Remark: checks an assumption that should be true.`
  Remark: checks an assumption that should be true.
- Line 510: `        assert self.username is not None`
  Remark: This line is part of the executable source code.
- Line 511: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 512: `        if not self.server.database.is_admin(self.username):`
  Remark: This line is part of the executable source code.
- Line 513: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 514: `            self._advanced_response("Admin", ["Only admin users can kick users"])`
  Remark: This line is part of the executable source code.
- Line 515: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 516: `            return`
  Remark: This line is part of the executable source code.
- Line 517: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 518: `        kicked = self.server.kick_user(target)`
  Remark: This line is part of the executable source code.
- Line 519: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 520: `        self._advanced_response("Admin", [f"Kicked {target}" if kicked else "User is not online"])`
  Remark: This line is part of the executable source code.
- Line 521: ` `
  Remark: Blank line used for readability.
- Line 522: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 523: `    def _edit_command(self, message_id_text: str, body: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 524: `        # Remark: checks an assumption that should be true.`
  Remark: checks an assumption that should be true.
- Line 525: `        assert self.username is not None`
  Remark: This line is part of the executable source code.
- Line 526: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 527: `        if not message_id_text.isdigit():`
  Remark: This line is part of the executable source code.
- Line 528: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 529: `            self._advanced_response("Edit message", ["Message id must be a number"])`
  Remark: This line is part of the executable source code.
- Line 530: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 531: `            return`
  Remark: This line is part of the executable source code.
- Line 532: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 533: `        ok = self.server.database.edit_message(`
  Remark: This line is part of the executable source code.
- Line 534: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 535: `            int(message_id_text),`
  Remark: This line is part of the executable source code.
- Line 536: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 537: `            self.username,`
  Remark: This line is part of the executable source code.
- Line 538: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 539: `            body,`
  Remark: This line is part of the executable source code.
- Line 540: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 541: `            self.server.database.is_admin(self.username),`
  Remark: This line is part of the executable source code.
- Line 542: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 543: `        )`
  Remark: This line is part of the executable source code.
- Line 544: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 545: `        self._advanced_response("Edit message", ["Message edited" if ok else "Cannot edit that message"])`
  Remark: This line is part of the executable source code.
- Line 546: ` `
  Remark: Blank line used for readability.
- Line 547: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 548: `    def _delete_command(self, message_id_text: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 549: `        # Remark: checks an assumption that should be true.`
  Remark: checks an assumption that should be true.
- Line 550: `        assert self.username is not None`
  Remark: This line is part of the executable source code.
- Line 551: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 552: `        if not message_id_text.isdigit():`
  Remark: This line is part of the executable source code.
- Line 553: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 554: `            self._advanced_response("Delete message", ["Message id must be a number"])`
  Remark: This line is part of the executable source code.
- Line 555: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 556: `            return`
  Remark: This line is part of the executable source code.
- Line 557: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 558: `        ok = self.server.database.delete_message(`
  Remark: This line is part of the executable source code.
- Line 559: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 560: `            int(message_id_text),`
  Remark: This line is part of the executable source code.
- Line 561: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 562: `            self.username,`
  Remark: This line is part of the executable source code.
- Line 563: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 564: `            self.server.database.is_admin(self.username),`
  Remark: This line is part of the executable source code.
- Line 565: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 566: `        )`
  Remark: This line is part of the executable source code.
- Line 567: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 568: `        self._advanced_response("Delete message", ["Message deleted" if ok else "Cannot delete that message"])`
  Remark: This line is part of the executable source code.
- Line 569: ` `
  Remark: Blank line used for readability.
- Line 570: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 571: `    def _advanced_response(self, title: str, lines: list[str]) -> None:`
  Remark: This line is part of the executable source code.
- Line 572: `        # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 573: `        self.send("advanced_response", title=title, lines=lines or ["No results"])`
  Remark: This line is part of the executable source code.
- Line 574: ` `
  Remark: Blank line used for readability.
- Line 575: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 576: `    def _command_help(self) -> str:`
  Remark: This line is part of the executable source code.
- Line 577: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 578: `        return "/dm user text, /profile set text, /profile user, /search text, /friend user, /accept user, /friends, /gallery, /admin logs, /kick user, /edit id text, /delete id, /2fa"`
  Remark: This line is part of the executable source code.
- Line 579: ` `
  Remark: Blank line used for readability.
- Line 580: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 581: `    def _users(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 582: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 583: `        users = [user.username for user in self.server.database.list_users()]`
  Remark: This line is part of the executable source code.
- Line 584: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 585: `        online = self.server.online_clients()`
  Remark: This line is part of the executable source code.
- Line 586: `        # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 587: `        self.send("users", registered=users, online=online)`
  Remark: This line is part of the executable source code.
- Line 588: ` `
  Remark: Blank line used for readability.
- Line 589: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 590: `    def _rooms(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 591: `        # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 592: `        self.send("rooms", rooms=self.server.database.list_rooms(), current=self.room)`
  Remark: This line is part of the executable source code.
- Line 593: ` `
  Remark: Blank line used for readability.
- Line 594: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 595: `    def _history(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 596: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 597: `        messages = [`
  Remark: This line is part of the executable source code.
- Line 598: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 599: `            {`
  Remark: This line is part of the executable source code.
- Line 600: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 601: `                "sender": message.sender,`
  Remark: This line is part of the executable source code.
- Line 602: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 603: `                "room": message.room,`
  Remark: This line is part of the executable source code.
- Line 604: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 605: `                "body": message.body,`
  Remark: This line is part of the executable source code.
- Line 606: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 607: `                "created_at": message.created_at,`
  Remark: This line is part of the executable source code.
- Line 608: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 609: `            }`
  Remark: This line is part of the executable source code.
- Line 610: `            # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 611: `            for message in self.server.database.recent_messages(self.room)`
  Remark: This line is part of the executable source code.
- Line 612: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 613: `        ]`
  Remark: This line is part of the executable source code.
- Line 614: `        # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 615: `        self.send("history", room=self.room, messages=messages)`
  Remark: This line is part of the executable source code.
- Line 616: ` `
  Remark: Blank line used for readability.
- Line 617: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 618: `    def _require_login(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 619: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 620: `        if self.username is None:`
  Remark: This line is part of the executable source code.
- Line 621: `            # Remark: raises an error for invalid behavior.`
  Remark: raises an error for invalid behavior.
- Line 622: `            raise ProtocolError("Login required")`
  Remark: This line is part of the executable source code.
- Line 623: ` `
  Remark: Blank line used for readability.
- Line 624: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 625: `    def _safe_close(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 626: `        # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 627: `        try:`
  Remark: This line is part of the executable source code.
- Line 628: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 629: `            self.connection.close()`
  Remark: This line is part of the executable source code.
- Line 630: `        # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 631: `        except OSError:`
  Remark: This line is part of the executable source code.
- Line 632: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 633: `            pass`
  Remark: This line is part of the executable source code.
- Line 634: ` `
  Remark: Blank line used for readability.
- Line 635: ` `
  Remark: Blank line used for readability.
- Line 636: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 637: `class SecureChatServer:`
  Remark: This line is part of the executable source code.
- Line 638: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 639: `    def __init__(self, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> None:`
  Remark: This line is part of the executable source code.
- Line 640: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 641: `        self.host = host`
  Remark: This line is part of the executable source code.
- Line 642: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 643: `        self.port = port`
  Remark: This line is part of the executable source code.
- Line 644: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 645: `        self.database = ChatDatabase()`
  Remark: This line is part of the executable source code.
- Line 646: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 647: `        self.clients: set[ClientHandler] = set()`
  Remark: This line is part of the executable source code.
- Line 648: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 649: `        self.clients_lock = threading.Lock()`
  Remark: This line is part of the executable source code.
- Line 650: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 651: `        self.running = False`
  Remark: This line is part of the executable source code.
- Line 652: ` `
  Remark: Blank line used for readability.
- Line 653: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 654: `    def start(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 655: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 656: `        context = TLSContextFactory.server_context()`
  Remark: This line is part of the executable source code.
- Line 657: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 658: `        self.running = True`
  Remark: This line is part of the executable source code.
- Line 659: ` `
  Remark: Blank line used for readability.
- Line 660: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 661: `        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:`
  Remark: This line is part of the executable source code.
- Line 662: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 663: `            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`
  Remark: This line is part of the executable source code.
- Line 664: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 665: `            server_socket.bind((self.host, self.port))`
  Remark: This line is part of the executable source code.
- Line 666: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 667: `            server_socket.listen()`
  Remark: This line is part of the executable source code.
- Line 668: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 669: `            self.log(f"Server listening on {self.host}:{self.port}")`
  Remark: This line is part of the executable source code.
- Line 670: ` `
  Remark: Blank line used for readability.
- Line 671: `            # Remark: starts a loop that continues while a condition is true.`
  Remark: starts a loop that continues while a condition is true.
- Line 672: `            while self.running:`
  Remark: This line is part of the executable source code.
- Line 673: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 674: `                raw_connection, address = server_socket.accept()`
  Remark: This line is part of the executable source code.
- Line 675: `                # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 676: `                try:`
  Remark: This line is part of the executable source code.
- Line 677: `                    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 678: `                    tls_connection = context.wrap_socket(raw_connection, server_side=True)`
  Remark: This line is part of the executable source code.
- Line 679: `                # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 680: `                except OSError as exc:`
  Remark: This line is part of the executable source code.
- Line 681: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 682: `                    self.log(f"TLS handshake failed from {address}: {exc}")`
  Remark: This line is part of the executable source code.
- Line 683: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 684: `                    raw_connection.close()`
  Remark: This line is part of the executable source code.
- Line 685: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 686: `                    continue`
  Remark: This line is part of the executable source code.
- Line 687: ` `
  Remark: Blank line used for readability.
- Line 688: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 689: `                ClientHandler(self, tls_connection, address).start()`
  Remark: This line is part of the executable source code.
- Line 690: ` `
  Remark: Blank line used for readability.
- Line 691: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 692: `    def add_client(self, client: ClientHandler) -> None:`
  Remark: This line is part of the executable source code.
- Line 693: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 694: `        with self.clients_lock:`
  Remark: This line is part of the executable source code.
- Line 695: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 696: `            self.clients.add(client)`
  Remark: This line is part of the executable source code.
- Line 697: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 698: `        self.database.log_event("login", f"{client.username} logged in from {client.address}")`
  Remark: This line is part of the executable source code.
- Line 699: ` `
  Remark: Blank line used for readability.
- Line 700: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 701: `    def remove_client(self, client: ClientHandler) -> None:`
  Remark: This line is part of the executable source code.
- Line 702: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 703: `        removed = False`
  Remark: This line is part of the executable source code.
- Line 704: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 705: `        with self.clients_lock:`
  Remark: This line is part of the executable source code.
- Line 706: `            # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 707: `            if client in self.clients:`
  Remark: This line is part of the executable source code.
- Line 708: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 709: `                self.clients.remove(client)`
  Remark: This line is part of the executable source code.
- Line 710: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 711: `                removed = True`
  Remark: This line is part of the executable source code.
- Line 712: ` `
  Remark: Blank line used for readability.
- Line 713: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 714: `        if removed and client.username:`
  Remark: This line is part of the executable source code.
- Line 715: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 716: `            self.broadcast_system(f"{client.username} disconnected", client.room)`
  Remark: This line is part of the executable source code.
- Line 717: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 718: `            self.database.log_event("disconnect", f"{client.username} disconnected")`
  Remark: This line is part of the executable source code.
- Line 719: ` `
  Remark: Blank line used for readability.
- Line 720: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 721: `    def broadcast_chat(self, message: ChatMessage, message_id: int) -> None:`
  Remark: This line is part of the executable source code.
- Line 722: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 723: `        payload = {`
  Remark: This line is part of the executable source code.
- Line 724: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 725: `            "id": message_id,`
  Remark: This line is part of the executable source code.
- Line 726: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 727: `            "sender": message.sender,`
  Remark: This line is part of the executable source code.
- Line 728: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 729: `            "room": message.room,`
  Remark: This line is part of the executable source code.
- Line 730: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 731: `            "body": message.body,`
  Remark: This line is part of the executable source code.
- Line 732: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 733: `            "created_at": message.created_at,`
  Remark: This line is part of the executable source code.
- Line 734: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 735: `        }`
  Remark: This line is part of the executable source code.
- Line 736: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 737: `        self._broadcast_to_room(message.room, "message", **payload)`
  Remark: This line is part of the executable source code.
- Line 738: ` `
  Remark: Blank line used for readability.
- Line 739: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 740: `    def broadcast_file(`
  Remark: This line is part of the executable source code.
- Line 741: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 742: `        self,`
  Remark: This line is part of the executable source code.
- Line 743: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 744: `        sender: str,`
  Remark: This line is part of the executable source code.
- Line 745: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 746: `        room: str,`
  Remark: This line is part of the executable source code.
- Line 747: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 748: `        filename: str,`
  Remark: This line is part of the executable source code.
- Line 749: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 750: `        kind: str,`
  Remark: This line is part of the executable source code.
- Line 751: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 752: `        size: int,`
  Remark: This line is part of the executable source code.
- Line 753: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 754: `        data: str,`
  Remark: This line is part of the executable source code.
- Line 755: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 756: `        created_at: str,`
  Remark: This line is part of the executable source code.
- Line 757: `    # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 758: `    ) -> None:`
  Remark: This line is part of the executable source code.
- Line 759: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 760: `        self._broadcast_to_room(`
  Remark: This line is part of the executable source code.
- Line 761: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 762: `            room,`
  Remark: This line is part of the executable source code.
- Line 763: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 764: `            "file",`
  Remark: This line is part of the executable source code.
- Line 765: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 766: `            sender=sender,`
  Remark: This line is part of the executable source code.
- Line 767: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 768: `            room=room,`
  Remark: This line is part of the executable source code.
- Line 769: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 770: `            filename=filename,`
  Remark: This line is part of the executable source code.
- Line 771: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 772: `            kind=kind,`
  Remark: This line is part of the executable source code.
- Line 773: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 774: `            size=size,`
  Remark: This line is part of the executable source code.
- Line 775: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 776: `            data=data,`
  Remark: This line is part of the executable source code.
- Line 777: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 778: `            created_at=created_at,`
  Remark: This line is part of the executable source code.
- Line 779: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 780: `        )`
  Remark: This line is part of the executable source code.
- Line 781: ` `
  Remark: Blank line used for readability.
- Line 782: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 783: `    def broadcast_system(self, text: str, room: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 784: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 785: `        self._broadcast_to_room(room, "system", room=room, message=text, created_at=now_iso())`
  Remark: This line is part of the executable source code.
- Line 786: ` `
  Remark: Blank line used for readability.
- Line 787: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 788: `    def broadcast_typing(self, username: str, room: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 789: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 790: `        self._broadcast_to_room(room, "typing", username=username, room=room)`
  Remark: This line is part of the executable source code.
- Line 791: ` `
  Remark: Blank line used for readability.
- Line 792: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 793: `    def send_private_message(self, sender: str, target: str, body: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 794: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 795: `        delivered = False`
  Remark: This line is part of the executable source code.
- Line 796: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 797: `        with self.clients_lock:`
  Remark: This line is part of the executable source code.
- Line 798: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 799: `            clients = [client for client in self.clients if client.username in {sender, target}]`
  Remark: This line is part of the executable source code.
- Line 800: ` `
  Remark: Blank line used for readability.
- Line 801: `        # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 802: `        for client in clients:`
  Remark: This line is part of the executable source code.
- Line 803: `            # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 804: `            try:`
  Remark: This line is part of the executable source code.
- Line 805: `                # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 806: `                client.send("private_message", sender=sender, target=target, body=body, created_at=now_iso())`
  Remark: This line is part of the executable source code.
- Line 807: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 808: `                delivered = True`
  Remark: This line is part of the executable source code.
- Line 809: `            # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 810: `            except OSError:`
  Remark: This line is part of the executable source code.
- Line 811: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 812: `                client.running = False`
  Remark: This line is part of the executable source code.
- Line 813: ` `
  Remark: Blank line used for readability.
- Line 814: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 815: `        self.database.log_event("private_message", f"{sender} sent private message to {target}")`
  Remark: This line is part of the executable source code.
- Line 816: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 817: `        if not delivered:`
  Remark: This line is part of the executable source code.
- Line 818: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 819: `            self.send_system_to_user(sender, f"User {target} is not online")`
  Remark: This line is part of the executable source code.
- Line 820: ` `
  Remark: Blank line used for readability.
- Line 821: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 822: `    def send_system_to_user(self, username: str, text: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 823: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 824: `        with self.clients_lock:`
  Remark: This line is part of the executable source code.
- Line 825: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 826: `            clients = [client for client in self.clients if client.username == username]`
  Remark: This line is part of the executable source code.
- Line 827: ` `
  Remark: Blank line used for readability.
- Line 828: `        # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 829: `        for client in clients:`
  Remark: This line is part of the executable source code.
- Line 830: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 831: `            client.send("system", room=client.room, message=text, created_at=now_iso())`
  Remark: This line is part of the executable source code.
- Line 832: ` `
  Remark: Blank line used for readability.
- Line 833: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 834: `    def kick_user(self, username: str) -> bool:`
  Remark: This line is part of the executable source code.
- Line 835: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 836: `        with self.clients_lock:`
  Remark: This line is part of the executable source code.
- Line 837: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 838: `            targets = [client for client in self.clients if client.username == username]`
  Remark: This line is part of the executable source code.
- Line 839: ` `
  Remark: Blank line used for readability.
- Line 840: `        # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 841: `        for client in targets:`
  Remark: This line is part of the executable source code.
- Line 842: `            # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 843: `            client.send("error", action="kick", message="You were kicked by an admin")`
  Remark: This line is part of the executable source code.
- Line 844: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 845: `            client.running = False`
  Remark: This line is part of the executable source code.
- Line 846: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 847: `            client._safe_close()`
  Remark: This line is part of the executable source code.
- Line 848: ` `
  Remark: Blank line used for readability.
- Line 849: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 850: `        if targets:`
  Remark: This line is part of the executable source code.
- Line 851: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 852: `            self.database.log_event("kick", f"{username} was kicked by admin")`
  Remark: This line is part of the executable source code.
- Line 853: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 854: `        return bool(targets)`
  Remark: This line is part of the executable source code.
- Line 855: ` `
  Remark: Blank line used for readability.
- Line 856: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 857: `    def broadcast_rooms(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 858: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 859: `        rooms = self.database.list_rooms()`
  Remark: This line is part of the executable source code.
- Line 860: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 861: `        with self.clients_lock:`
  Remark: This line is part of the executable source code.
- Line 862: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 863: `            clients = list(self.clients)`
  Remark: This line is part of the executable source code.
- Line 864: ` `
  Remark: Blank line used for readability.
- Line 865: `        # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 866: `        for client in clients:`
  Remark: This line is part of the executable source code.
- Line 867: `            # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 868: `            try:`
  Remark: This line is part of the executable source code.
- Line 869: `                # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 870: `                client.send("rooms", rooms=rooms, current=client.room)`
  Remark: This line is part of the executable source code.
- Line 871: `            # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 872: `            except OSError:`
  Remark: This line is part of the executable source code.
- Line 873: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 874: `                client.running = False`
  Remark: This line is part of the executable source code.
- Line 875: ` `
  Remark: Blank line used for readability.
- Line 876: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 877: `    def online_clients(self) -> list[dict[str, str]]:`
  Remark: This line is part of the executable source code.
- Line 878: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 879: `        with self.clients_lock:`
  Remark: This line is part of the executable source code.
- Line 880: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 881: `            return [`
  Remark: This line is part of the executable source code.
- Line 882: `                # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 883: `                ClientInfo(`
  Remark: This line is part of the executable source code.
- Line 884: `                    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 885: `                    username=client.username or "anonymous",`
  Remark: This line is part of the executable source code.
- Line 886: `                    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 887: `                    room=client.room,`
  Remark: This line is part of the executable source code.
- Line 888: `                    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 889: `                    address=client.address,`
  Remark: This line is part of the executable source code.
- Line 890: `                # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 891: `                ).__dict__`
  Remark: This line is part of the executable source code.
- Line 892: `                # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 893: `                for client in self.clients`
  Remark: This line is part of the executable source code.
- Line 894: `                # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 895: `                if client.username`
  Remark: This line is part of the executable source code.
- Line 896: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 897: `            ]`
  Remark: This line is part of the executable source code.
- Line 898: ` `
  Remark: Blank line used for readability.
- Line 899: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 900: `    def _broadcast_to_room(self, target_room: str, packet_type: str, **fields: object) -> None:`
  Remark: This line is part of the executable source code.
- Line 901: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 902: `        with self.clients_lock:`
  Remark: This line is part of the executable source code.
- Line 903: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 904: `            clients = [client for client in self.clients if client.room == target_room]`
  Remark: This line is part of the executable source code.
- Line 905: ` `
  Remark: Blank line used for readability.
- Line 906: `        # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 907: `        for client in clients:`
  Remark: This line is part of the executable source code.
- Line 908: `            # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 909: `            try:`
  Remark: This line is part of the executable source code.
- Line 910: `                # Remark: sends data or connects a GUI action.`
  Remark: sends data or connects a GUI action.
- Line 911: `                client.send(packet_type, **fields)`
  Remark: This line is part of the executable source code.
- Line 912: `            # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 913: `            except OSError:`
  Remark: This line is part of the executable source code.
- Line 914: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 915: `                client.running = False`
  Remark: This line is part of the executable source code.
- Line 916: ` `
  Remark: Blank line used for readability.
- Line 917: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 918: `    def log(self, message: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 919: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 920: `        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)`
  Remark: This line is part of the executable source code.
- Line 921: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 922: `        line = f"[{now_iso()}] {message}"`
  Remark: This line is part of the executable source code.
- Line 923: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 924: `        print(line)`
  Remark: This line is part of the executable source code.
- Line 925: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 926: `        with LOG_PATH.open("a", encoding="utf-8") as log_file:`
  Remark: This line is part of the executable source code.
- Line 927: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 928: `            log_file.write(line + "\n")`
  Remark: This line is part of the executable source code.
- Line 929: ` `
  Remark: Blank line used for readability.
- Line 930: ` `
  Remark: Blank line used for readability.
- Line 931: `# Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 932: `def parse_args() -> argparse.Namespace:`
  Remark: This line is part of the executable source code.
- Line 933: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 934: `    parser = argparse.ArgumentParser(description="SecureChat threaded TLS server")`
  Remark: This line is part of the executable source code.
- Line 935: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 936: `    parser.add_argument("--host", default=DEFAULT_HOST)`
  Remark: This line is part of the executable source code.
- Line 937: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 938: `    parser.add_argument("--port", type=int, default=DEFAULT_PORT)`
  Remark: This line is part of the executable source code.
- Line 939: `    # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 940: `    return parser.parse_args()`
  Remark: This line is part of the executable source code.
- Line 941: ` `
  Remark: Blank line used for readability.
- Line 942: ` `
  Remark: Blank line used for readability.
- Line 943: `# Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 944: `if __name__ == "__main__":`
  Remark: This line is part of the executable source code.
- Line 945: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 946: `    args = parse_args()`
  Remark: This line is part of the executable source code.
- Line 947: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 948: `    SecureChatServer(host=args.host, port=args.port).start()`
  Remark: This line is part of the executable source code.
- Line 949: ` `
  Remark: Blank line used for readability.

## `secure_chat/storage.py`

- Line 1: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 2: `import sqlite3`
  Remark: This line is part of the executable source code.
- Line 3: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 4: `import threading`
  Remark: This line is part of the executable source code.
- Line 5: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 6: `from pathlib import Path`
  Remark: This line is part of the executable source code.
- Line 7: ` `
  Remark: Blank line used for readability.
- Line 8: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 9: `from secure_chat.config import DATABASE_PATH, DATA_DIR`
  Remark: This line is part of the executable source code.
- Line 10: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 11: `from secure_chat.models import ChatMessage, User, now_iso`
  Remark: This line is part of the executable source code.
- Line 12: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 13: `from secure_chat.security import PasswordHasher`
  Remark: This line is part of the executable source code.
- Line 14: ` `
  Remark: Blank line used for readability.
- Line 15: ` `
  Remark: Blank line used for readability.
- Line 16: `# Remark: defines a class for object-oriented structure.`
  Remark: defines a class for object-oriented structure.
- Line 17: `class ChatDatabase:`
  Remark: This line is part of the executable source code.
- Line 18: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 19: `    def __init__(self, path: Path = DATABASE_PATH) -> None:`
  Remark: This line is part of the executable source code.
- Line 20: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 21: `        self.path = path`
  Remark: This line is part of the executable source code.
- Line 22: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 23: `        self._lock = threading.Lock()`
  Remark: This line is part of the executable source code.
- Line 24: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 25: `        DATA_DIR.mkdir(parents=True, exist_ok=True)`
  Remark: This line is part of the executable source code.
- Line 26: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 27: `        self._initialize()`
  Remark: This line is part of the executable source code.
- Line 28: ` `
  Remark: Blank line used for readability.
- Line 29: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 30: `    def _connect(self) -> sqlite3.Connection:`
  Remark: This line is part of the executable source code.
- Line 31: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 32: `        connection = sqlite3.connect(self.path, check_same_thread=False)`
  Remark: This line is part of the executable source code.
- Line 33: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 34: `        connection.row_factory = sqlite3.Row`
  Remark: This line is part of the executable source code.
- Line 35: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 36: `        return connection`
  Remark: This line is part of the executable source code.
- Line 37: ` `
  Remark: Blank line used for readability.
- Line 38: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 39: `    def _initialize(self) -> None:`
  Remark: This line is part of the executable source code.
- Line 40: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 41: `        with self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 42: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 43: `            connection.execute(`
  Remark: This line is part of the executable source code.
- Line 44: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 45: `                """`
  Remark: This line is part of the executable source code.
- Line 46: `                CREATE TABLE IF NOT EXISTS users (`
  Remark: This line is part of the executable source code.
- Line 47: `                    username TEXT PRIMARY KEY,`
  Remark: This line is part of the executable source code.
- Line 48: `                    password_hash TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 49: `                    created_at TEXT NOT NULL`
  Remark: This line is part of the executable source code.
- Line 50: `                )`
  Remark: This line is part of the executable source code.
- Line 51: `                """`
  Remark: This line is part of the executable source code.
- Line 52: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 53: `            )`
  Remark: This line is part of the executable source code.
- Line 54: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 55: `            self._add_column_if_missing(connection, "users", "is_admin", "INTEGER NOT NULL DEFAULT 0")`
  Remark: This line is part of the executable source code.
- Line 56: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 57: `            self._add_column_if_missing(connection, "users", "profile_status", "TEXT NOT NULL DEFAULT ''")`
  Remark: This line is part of the executable source code.
- Line 58: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 59: `            connection.execute(`
  Remark: This line is part of the executable source code.
- Line 60: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 61: `                """`
  Remark: This line is part of the executable source code.
- Line 62: `                CREATE TABLE IF NOT EXISTS messages (`
  Remark: This line is part of the executable source code.
- Line 63: `                    id INTEGER PRIMARY KEY AUTOINCREMENT,`
  Remark: This line is part of the executable source code.
- Line 64: `                    sender TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 65: `                    room TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 66: `                    body TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 67: `                    created_at TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 68: `                    FOREIGN KEY(sender) REFERENCES users(username)`
  Remark: This line is part of the executable source code.
- Line 69: `                )`
  Remark: This line is part of the executable source code.
- Line 70: `                """`
  Remark: This line is part of the executable source code.
- Line 71: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 72: `            )`
  Remark: This line is part of the executable source code.
- Line 73: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 74: `            self._add_column_if_missing(connection, "messages", "edited_at", "TEXT")`
  Remark: This line is part of the executable source code.
- Line 75: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 76: `            self._add_column_if_missing(connection, "messages", "deleted", "INTEGER NOT NULL DEFAULT 0")`
  Remark: This line is part of the executable source code.
- Line 77: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 78: `            connection.execute(`
  Remark: This line is part of the executable source code.
- Line 79: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 80: `                """`
  Remark: This line is part of the executable source code.
- Line 81: `                CREATE TABLE IF NOT EXISTS rooms (`
  Remark: This line is part of the executable source code.
- Line 82: `                    name TEXT PRIMARY KEY,`
  Remark: This line is part of the executable source code.
- Line 83: `                    created_by TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 84: `                    created_at TEXT NOT NULL`
  Remark: This line is part of the executable source code.
- Line 85: `                )`
  Remark: This line is part of the executable source code.
- Line 86: `                """`
  Remark: This line is part of the executable source code.
- Line 87: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 88: `            )`
  Remark: This line is part of the executable source code.
- Line 89: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 90: `            self._add_column_if_missing(connection, "rooms", "password_hash", "TEXT")`
  Remark: This line is part of the executable source code.
- Line 91: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 92: `            self._add_column_if_missing(connection, "rooms", "owner", "TEXT")`
  Remark: This line is part of the executable source code.
- Line 93: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 94: `            connection.execute(`
  Remark: This line is part of the executable source code.
- Line 95: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 96: `                """`
  Remark: This line is part of the executable source code.
- Line 97: `                CREATE TABLE IF NOT EXISTS friends (`
  Remark: This line is part of the executable source code.
- Line 98: `                    requester TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 99: `                    receiver TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 100: `                    status TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 101: `                    created_at TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 102: `                    PRIMARY KEY(requester, receiver)`
  Remark: This line is part of the executable source code.
- Line 103: `                )`
  Remark: This line is part of the executable source code.
- Line 104: `                """`
  Remark: This line is part of the executable source code.
- Line 105: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 106: `            )`
  Remark: This line is part of the executable source code.
- Line 107: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 108: `            connection.execute(`
  Remark: This line is part of the executable source code.
- Line 109: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 110: `                """`
  Remark: This line is part of the executable source code.
- Line 111: `                CREATE TABLE IF NOT EXISTS downloads (`
  Remark: This line is part of the executable source code.
- Line 112: `                    id INTEGER PRIMARY KEY AUTOINCREMENT,`
  Remark: This line is part of the executable source code.
- Line 113: `                    username TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 114: `                    filename TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 115: `                    created_at TEXT NOT NULL`
  Remark: This line is part of the executable source code.
- Line 116: `                )`
  Remark: This line is part of the executable source code.
- Line 117: `                """`
  Remark: This line is part of the executable source code.
- Line 118: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 119: `            )`
  Remark: This line is part of the executable source code.
- Line 120: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 121: `            connection.execute(`
  Remark: This line is part of the executable source code.
- Line 122: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 123: `                """`
  Remark: This line is part of the executable source code.
- Line 124: `                CREATE TABLE IF NOT EXISTS audit_log (`
  Remark: This line is part of the executable source code.
- Line 125: `                    id INTEGER PRIMARY KEY AUTOINCREMENT,`
  Remark: This line is part of the executable source code.
- Line 126: `                    event_type TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 127: `                    details TEXT NOT NULL,`
  Remark: This line is part of the executable source code.
- Line 128: `                    created_at TEXT NOT NULL`
  Remark: This line is part of the executable source code.
- Line 129: `                )`
  Remark: This line is part of the executable source code.
- Line 130: `                """`
  Remark: This line is part of the executable source code.
- Line 131: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 132: `            )`
  Remark: This line is part of the executable source code.
- Line 133: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 134: `            connection.execute(`
  Remark: This line is part of the executable source code.
- Line 135: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 136: `                "INSERT OR IGNORE INTO rooms(name, created_by, created_at) VALUES (?, ?, ?)",`
  Remark: This line is part of the executable source code.
- Line 137: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 138: `                ("general", "system", now_iso()),`
  Remark: This line is part of the executable source code.
- Line 139: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 140: `            )`
  Remark: This line is part of the executable source code.
- Line 141: ` `
  Remark: Blank line used for readability.
- Line 142: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 143: `    def _add_column_if_missing(self, connection: sqlite3.Connection, table: str, column: str, definition: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 144: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 145: `        columns = [row["name"] for row in connection.execute(f"PRAGMA table_info({table})").fetchall()]`
  Remark: This line is part of the executable source code.
- Line 146: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 147: `        if column not in columns:`
  Remark: This line is part of the executable source code.
- Line 148: `            # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 149: `            connection.execute(f"ALTER TABLE {table} ADD COLUMN {column} {definition}")`
  Remark: This line is part of the executable source code.
- Line 150: ` `
  Remark: Blank line used for readability.
- Line 151: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 152: `    def create_user(self, username: str, password: str) -> bool:`
  Remark: This line is part of the executable source code.
- Line 153: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 154: `        password_hash = PasswordHasher.hash_password(password)`
  Remark: This line is part of the executable source code.
- Line 155: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 156: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 157: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 158: `            user_count = connection.execute("SELECT COUNT(*) AS count FROM users").fetchone()["count"]`
  Remark: This line is part of the executable source code.
- Line 159: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 160: `            is_admin = 1 if user_count == 0 or username.lower() == "admin" else 0`
  Remark: This line is part of the executable source code.
- Line 161: `            # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 162: `            try:`
  Remark: This line is part of the executable source code.
- Line 163: `                # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 164: `                connection.execute(`
  Remark: This line is part of the executable source code.
- Line 165: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 166: `                    "INSERT INTO users(username, password_hash, created_at, is_admin) VALUES (?, ?, ?, ?)",`
  Remark: This line is part of the executable source code.
- Line 167: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 168: `                    (username, password_hash, now_iso(), is_admin),`
  Remark: This line is part of the executable source code.
- Line 169: `                # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 170: `                )`
  Remark: This line is part of the executable source code.
- Line 171: `            # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 172: `            except sqlite3.IntegrityError:`
  Remark: This line is part of the executable source code.
- Line 173: `                # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 174: `                return False`
  Remark: This line is part of the executable source code.
- Line 175: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 176: `        self.log_event("register", f"User registered: {username}")`
  Remark: This line is part of the executable source code.
- Line 177: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 178: `        return True`
  Remark: This line is part of the executable source code.
- Line 179: ` `
  Remark: Blank line used for readability.
- Line 180: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 181: `    def authenticate(self, username: str, password: str) -> bool:`
  Remark: This line is part of the executable source code.
- Line 182: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 183: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 184: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 185: `            row = connection.execute(`
  Remark: This line is part of the executable source code.
- Line 186: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 187: `                "SELECT password_hash FROM users WHERE username = ?",`
  Remark: This line is part of the executable source code.
- Line 188: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 189: `                (username,),`
  Remark: This line is part of the executable source code.
- Line 190: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 191: `            ).fetchone()`
  Remark: This line is part of the executable source code.
- Line 192: ` `
  Remark: Blank line used for readability.
- Line 193: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 194: `        if row is None:`
  Remark: This line is part of the executable source code.
- Line 195: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 196: `            return False`
  Remark: This line is part of the executable source code.
- Line 197: ` `
  Remark: Blank line used for readability.
- Line 198: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 199: `        return PasswordHasher.verify_password(password, row["password_hash"])`
  Remark: This line is part of the executable source code.
- Line 200: ` `
  Remark: Blank line used for readability.
- Line 201: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 202: `    def save_message(self, message: ChatMessage) -> int:`
  Remark: This line is part of the executable source code.
- Line 203: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 204: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 205: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 206: `            connection.execute(`
  Remark: This line is part of the executable source code.
- Line 207: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 208: `                "INSERT OR IGNORE INTO rooms(name, created_by, created_at) VALUES (?, ?, ?)",`
  Remark: This line is part of the executable source code.
- Line 209: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 210: `                (message.room, message.sender, now_iso()),`
  Remark: This line is part of the executable source code.
- Line 211: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 212: `            )`
  Remark: This line is part of the executable source code.
- Line 213: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 214: `            cursor = connection.execute(`
  Remark: This line is part of the executable source code.
- Line 215: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 216: `                "INSERT INTO messages(sender, room, body, created_at) VALUES (?, ?, ?, ?)",`
  Remark: This line is part of the executable source code.
- Line 217: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 218: `                (message.sender, message.room, message.body, message.created_at),`
  Remark: This line is part of the executable source code.
- Line 219: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 220: `            )`
  Remark: This line is part of the executable source code.
- Line 221: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 222: `            return int(cursor.lastrowid)`
  Remark: This line is part of the executable source code.
- Line 223: ` `
  Remark: Blank line used for readability.
- Line 224: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 225: `    def create_room(self, room: str, created_by: str, password: str = "") -> bool:`
  Remark: This line is part of the executable source code.
- Line 226: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 227: `        password_hash = PasswordHasher.hash_password(password) if password else None`
  Remark: This line is part of the executable source code.
- Line 228: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 229: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 230: `            # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 231: `            try:`
  Remark: This line is part of the executable source code.
- Line 232: `                # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 233: `                connection.execute(`
  Remark: This line is part of the executable source code.
- Line 234: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 235: `                    "INSERT INTO rooms(name, created_by, created_at, owner, password_hash) VALUES (?, ?, ?, ?, ?)",`
  Remark: This line is part of the executable source code.
- Line 236: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 237: `                    (room, created_by, now_iso(), created_by, password_hash),`
  Remark: This line is part of the executable source code.
- Line 238: `                # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 239: `                )`
  Remark: This line is part of the executable source code.
- Line 240: `            # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 241: `            except sqlite3.IntegrityError:`
  Remark: This line is part of the executable source code.
- Line 242: `                # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 243: `                return False`
  Remark: This line is part of the executable source code.
- Line 244: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 245: `        self.log_event("room_created", f"{created_by} created room {room}")`
  Remark: This line is part of the executable source code.
- Line 246: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 247: `        return True`
  Remark: This line is part of the executable source code.
- Line 248: ` `
  Remark: Blank line used for readability.
- Line 249: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 250: `    def room_exists(self, room: str) -> bool:`
  Remark: This line is part of the executable source code.
- Line 251: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 252: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 253: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 254: `            row = connection.execute(`
  Remark: This line is part of the executable source code.
- Line 255: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 256: `                "SELECT 1 FROM rooms WHERE name = ?",`
  Remark: This line is part of the executable source code.
- Line 257: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 258: `                (room,),`
  Remark: This line is part of the executable source code.
- Line 259: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 260: `            ).fetchone()`
  Remark: This line is part of the executable source code.
- Line 261: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 262: `        return row is not None`
  Remark: This line is part of the executable source code.
- Line 263: ` `
  Remark: Blank line used for readability.
- Line 264: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 265: `    def can_join_room(self, room: str, password: str = "") -> bool:`
  Remark: This line is part of the executable source code.
- Line 266: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 267: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 268: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 269: `            row = connection.execute(`
  Remark: This line is part of the executable source code.
- Line 270: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 271: `                "SELECT password_hash FROM rooms WHERE name = ?",`
  Remark: This line is part of the executable source code.
- Line 272: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 273: `                (room,),`
  Remark: This line is part of the executable source code.
- Line 274: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 275: `            ).fetchone()`
  Remark: This line is part of the executable source code.
- Line 276: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 277: `        if row is None:`
  Remark: This line is part of the executable source code.
- Line 278: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 279: `            return False`
  Remark: This line is part of the executable source code.
- Line 280: `        # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 281: `        if not row["password_hash"]:`
  Remark: This line is part of the executable source code.
- Line 282: `            # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 283: `            return True`
  Remark: This line is part of the executable source code.
- Line 284: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 285: `        return PasswordHasher.verify_password(password, row["password_hash"])`
  Remark: This line is part of the executable source code.
- Line 286: ` `
  Remark: Blank line used for readability.
- Line 287: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 288: `    def list_rooms(self) -> list[str]:`
  Remark: This line is part of the executable source code.
- Line 289: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 290: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 291: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 292: `            rows = connection.execute("SELECT name FROM rooms ORDER BY name").fetchall()`
  Remark: This line is part of the executable source code.
- Line 293: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 294: `        return [row["name"] for row in rows]`
  Remark: This line is part of the executable source code.
- Line 295: ` `
  Remark: Blank line used for readability.
- Line 296: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 297: `    def recent_messages(self, room: str, limit: int = 50) -> list[ChatMessage]:`
  Remark: This line is part of the executable source code.
- Line 298: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 299: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 300: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 301: `            rows = connection.execute(`
  Remark: This line is part of the executable source code.
- Line 302: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 303: `                """`
  Remark: This line is part of the executable source code.
- Line 304: `                SELECT sender, room, body, created_at`
  Remark: This line is part of the executable source code.
- Line 305: `                FROM messages`
  Remark: This line is part of the executable source code.
- Line 306: `                WHERE room = ? AND deleted = 0`
  Remark: This line is part of the executable source code.
- Line 307: `                ORDER BY id DESC`
  Remark: This line is part of the executable source code.
- Line 308: `                LIMIT ?`
  Remark: This line is part of the executable source code.
- Line 309: `                """,`
  Remark: This line is part of the executable source code.
- Line 310: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 311: `                (room, limit),`
  Remark: This line is part of the executable source code.
- Line 312: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 313: `            ).fetchall()`
  Remark: This line is part of the executable source code.
- Line 314: ` `
  Remark: Blank line used for readability.
- Line 315: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 316: `        return [`
  Remark: This line is part of the executable source code.
- Line 317: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 318: `            ChatMessage(`
  Remark: This line is part of the executable source code.
- Line 319: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 320: `                sender=row["sender"],`
  Remark: This line is part of the executable source code.
- Line 321: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 322: `                room=row["room"],`
  Remark: This line is part of the executable source code.
- Line 323: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 324: `                body=row["body"],`
  Remark: This line is part of the executable source code.
- Line 325: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 326: `                created_at=row["created_at"],`
  Remark: This line is part of the executable source code.
- Line 327: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 328: `            )`
  Remark: This line is part of the executable source code.
- Line 329: `            # Remark: starts a loop over multiple values.`
  Remark: starts a loop over multiple values.
- Line 330: `            for row in reversed(rows)`
  Remark: This line is part of the executable source code.
- Line 331: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 332: `        ]`
  Remark: This line is part of the executable source code.
- Line 333: ` `
  Remark: Blank line used for readability.
- Line 334: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 335: `    def list_users(self) -> list[User]:`
  Remark: This line is part of the executable source code.
- Line 336: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 337: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 338: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 339: `            rows = connection.execute(`
  Remark: This line is part of the executable source code.
- Line 340: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 341: `                "SELECT username, created_at FROM users ORDER BY username"`
  Remark: This line is part of the executable source code.
- Line 342: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 343: `            ).fetchall()`
  Remark: This line is part of the executable source code.
- Line 344: ` `
  Remark: Blank line used for readability.
- Line 345: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 346: `        return [User(username=row["username"], created_at=row["created_at"]) for row in rows]`
  Remark: This line is part of the executable source code.
- Line 347: ` `
  Remark: Blank line used for readability.
- Line 348: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 349: `    def is_admin(self, username: str) -> bool:`
  Remark: This line is part of the executable source code.
- Line 350: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 351: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 352: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 353: `            row = connection.execute(`
  Remark: This line is part of the executable source code.
- Line 354: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 355: `                "SELECT is_admin FROM users WHERE username = ?",`
  Remark: This line is part of the executable source code.
- Line 356: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 357: `                (username,),`
  Remark: This line is part of the executable source code.
- Line 358: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 359: `            ).fetchone()`
  Remark: This line is part of the executable source code.
- Line 360: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 361: `        return bool(row and row["is_admin"])`
  Remark: This line is part of the executable source code.
- Line 362: ` `
  Remark: Blank line used for readability.
- Line 363: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 364: `    def update_profile(self, username: str, status: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 365: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 366: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 367: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 368: `            connection.execute(`
  Remark: This line is part of the executable source code.
- Line 369: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 370: `                "UPDATE users SET profile_status = ? WHERE username = ?",`
  Remark: This line is part of the executable source code.
- Line 371: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 372: `                (status, username),`
  Remark: This line is part of the executable source code.
- Line 373: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 374: `            )`
  Remark: This line is part of the executable source code.
- Line 375: ` `
  Remark: Blank line used for readability.
- Line 376: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 377: `    def get_profile(self, username: str) -> str:`
  Remark: This line is part of the executable source code.
- Line 378: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 379: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 380: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 381: `            row = connection.execute(`
  Remark: This line is part of the executable source code.
- Line 382: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 383: `                "SELECT profile_status FROM users WHERE username = ?",`
  Remark: This line is part of the executable source code.
- Line 384: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 385: `                (username,),`
  Remark: This line is part of the executable source code.
- Line 386: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 387: `            ).fetchone()`
  Remark: This line is part of the executable source code.
- Line 388: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 389: `        return row["profile_status"] if row else "User not found"`
  Remark: This line is part of the executable source code.
- Line 390: ` `
  Remark: Blank line used for readability.
- Line 391: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 392: `    def search_messages(self, room: str, term: str, limit: int = 20) -> list[str]:`
  Remark: This line is part of the executable source code.
- Line 393: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 394: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 395: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 396: `            rows = connection.execute(`
  Remark: This line is part of the executable source code.
- Line 397: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 398: `                """`
  Remark: This line is part of the executable source code.
- Line 399: `                SELECT id, sender, body, created_at`
  Remark: This line is part of the executable source code.
- Line 400: `                FROM messages`
  Remark: This line is part of the executable source code.
- Line 401: `                WHERE room = ? AND body LIKE ? AND deleted = 0`
  Remark: This line is part of the executable source code.
- Line 402: `                ORDER BY id DESC`
  Remark: This line is part of the executable source code.
- Line 403: `                LIMIT ?`
  Remark: This line is part of the executable source code.
- Line 404: `                """,`
  Remark: This line is part of the executable source code.
- Line 405: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 406: `                (room, f"%{term}%", limit),`
  Remark: This line is part of the executable source code.
- Line 407: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 408: `            ).fetchall()`
  Remark: This line is part of the executable source code.
- Line 409: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 410: `        return [f"#{row['id']} [{row['created_at']}] {row['sender']}: {row['body']}" for row in rows]`
  Remark: This line is part of the executable source code.
- Line 411: ` `
  Remark: Blank line used for readability.
- Line 412: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 413: `    def image_gallery(self, room: str, limit: int = 20) -> list[str]:`
  Remark: This line is part of the executable source code.
- Line 414: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 415: `        return self.search_messages(room, "[image]", limit)`
  Remark: This line is part of the executable source code.
- Line 416: ` `
  Remark: Blank line used for readability.
- Line 417: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 418: `    def edit_message(self, message_id: int, username: str, body: str, is_admin: bool) -> bool:`
  Remark: This line is part of the executable source code.
- Line 419: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 420: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 421: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 422: `            row = connection.execute("SELECT sender FROM messages WHERE id = ?", (message_id,)).fetchone()`
  Remark: This line is part of the executable source code.
- Line 423: `            # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 424: `            if row is None or (row["sender"] != username and not is_admin):`
  Remark: This line is part of the executable source code.
- Line 425: `                # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 426: `                return False`
  Remark: This line is part of the executable source code.
- Line 427: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 428: `            connection.execute(`
  Remark: This line is part of the executable source code.
- Line 429: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 430: `                "UPDATE messages SET body = ?, edited_at = ? WHERE id = ?",`
  Remark: This line is part of the executable source code.
- Line 431: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 432: `                (body, now_iso(), message_id),`
  Remark: This line is part of the executable source code.
- Line 433: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 434: `            )`
  Remark: This line is part of the executable source code.
- Line 435: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 436: `        return True`
  Remark: This line is part of the executable source code.
- Line 437: ` `
  Remark: Blank line used for readability.
- Line 438: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 439: `    def delete_message(self, message_id: int, username: str, is_admin: bool) -> bool:`
  Remark: This line is part of the executable source code.
- Line 440: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 441: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 442: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 443: `            row = connection.execute("SELECT sender FROM messages WHERE id = ?", (message_id,)).fetchone()`
  Remark: This line is part of the executable source code.
- Line 444: `            # Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 445: `            if row is None or (row["sender"] != username and not is_admin):`
  Remark: This line is part of the executable source code.
- Line 446: `                # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 447: `                return False`
  Remark: This line is part of the executable source code.
- Line 448: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 449: `            connection.execute("UPDATE messages SET deleted = 1 WHERE id = ?", (message_id,))`
  Remark: This line is part of the executable source code.
- Line 450: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 451: `        return True`
  Remark: This line is part of the executable source code.
- Line 452: ` `
  Remark: Blank line used for readability.
- Line 453: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 454: `    def send_friend_request(self, requester: str, receiver: str) -> bool:`
  Remark: This line is part of the executable source code.
- Line 455: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 456: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 457: `            # Remark: starts protected code that may raise an error.`
  Remark: starts protected code that may raise an error.
- Line 458: `            try:`
  Remark: This line is part of the executable source code.
- Line 459: `                # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 460: `                connection.execute(`
  Remark: This line is part of the executable source code.
- Line 461: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 462: `                    "INSERT INTO friends(requester, receiver, status, created_at) VALUES (?, ?, ?, ?)",`
  Remark: This line is part of the executable source code.
- Line 463: `                    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 464: `                    (requester, receiver, "pending", now_iso()),`
  Remark: This line is part of the executable source code.
- Line 465: `                # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 466: `                )`
  Remark: This line is part of the executable source code.
- Line 467: `            # Remark: handles an expected error safely.`
  Remark: handles an expected error safely.
- Line 468: `            except sqlite3.IntegrityError:`
  Remark: This line is part of the executable source code.
- Line 469: `                # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 470: `                return False`
  Remark: This line is part of the executable source code.
- Line 471: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 472: `        return True`
  Remark: This line is part of the executable source code.
- Line 473: ` `
  Remark: Blank line used for readability.
- Line 474: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 475: `    def accept_friend_request(self, requester: str, receiver: str) -> bool:`
  Remark: This line is part of the executable source code.
- Line 476: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 477: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 478: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 479: `            cursor = connection.execute(`
  Remark: This line is part of the executable source code.
- Line 480: `                # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 481: `                "UPDATE friends SET status = 'accepted' WHERE requester = ? AND receiver = ?",`
  Remark: This line is part of the executable source code.
- Line 482: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 483: `                (requester, receiver),`
  Remark: This line is part of the executable source code.
- Line 484: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 485: `            )`
  Remark: This line is part of the executable source code.
- Line 486: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 487: `        return cursor.rowcount > 0`
  Remark: This line is part of the executable source code.
- Line 488: ` `
  Remark: Blank line used for readability.
- Line 489: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 490: `    def list_friends(self, username: str) -> list[str]:`
  Remark: This line is part of the executable source code.
- Line 491: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 492: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 493: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 494: `            rows = connection.execute(`
  Remark: This line is part of the executable source code.
- Line 495: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 496: `                """`
  Remark: This line is part of the executable source code.
- Line 497: `                SELECT requester, receiver`
  Remark: This line is part of the executable source code.
- Line 498: `                FROM friends`
  Remark: This line is part of the executable source code.
- Line 499: `                WHERE status = 'accepted' AND (requester = ? OR receiver = ?)`
  Remark: This line is part of the executable source code.
- Line 500: `                """,`
  Remark: This line is part of the executable source code.
- Line 501: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 502: `                (username, username),`
  Remark: This line is part of the executable source code.
- Line 503: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 504: `            ).fetchall()`
  Remark: This line is part of the executable source code.
- Line 505: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 506: `        return [row["receiver"] if row["requester"] == username else row["requester"] for row in rows]`
  Remark: This line is part of the executable source code.
- Line 507: ` `
  Remark: Blank line used for readability.
- Line 508: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 509: `    def record_download(self, username: str, filename: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 510: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 511: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 512: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 513: `            connection.execute(`
  Remark: This line is part of the executable source code.
- Line 514: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 515: `                "INSERT INTO downloads(username, filename, created_at) VALUES (?, ?, ?)",`
  Remark: This line is part of the executable source code.
- Line 516: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 517: `                (username, filename, now_iso()),`
  Remark: This line is part of the executable source code.
- Line 518: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 519: `            )`
  Remark: This line is part of the executable source code.
- Line 520: ` `
  Remark: Blank line used for readability.
- Line 521: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 522: `    def audit_events(self, limit: int = 20) -> list[str]:`
  Remark: This line is part of the executable source code.
- Line 523: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 524: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 525: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 526: `            rows = connection.execute(`
  Remark: This line is part of the executable source code.
- Line 527: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 528: `                "SELECT event_type, details, created_at FROM audit_log ORDER BY id DESC LIMIT ?",`
  Remark: This line is part of the executable source code.
- Line 529: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 530: `                (limit,),`
  Remark: This line is part of the executable source code.
- Line 531: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 532: `            ).fetchall()`
  Remark: This line is part of the executable source code.
- Line 533: `        # Remark: returns a value to the caller.`
  Remark: returns a value to the caller.
- Line 534: `        return [f"[{row['created_at']}] {row['event_type']}: {row['details']}" for row in rows]`
  Remark: This line is part of the executable source code.
- Line 535: ` `
  Remark: Blank line used for readability.
- Line 536: `    # Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 537: `    def log_event(self, event_type: str, details: str) -> None:`
  Remark: This line is part of the executable source code.
- Line 538: `        # Remark: uses a managed resource safely.`
  Remark: uses a managed resource safely.
- Line 539: `        with self._lock, self._connect() as connection:`
  Remark: This line is part of the executable source code.
- Line 540: `            # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 541: `            connection.execute(`
  Remark: This line is part of the executable source code.
- Line 542: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 543: `                "INSERT INTO audit_log(event_type, details, created_at) VALUES (?, ?, ?)",`
  Remark: This line is part of the executable source code.
- Line 544: `                # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 545: `                (event_type, details, now_iso()),`
  Remark: This line is part of the executable source code.
- Line 546: `            # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 547: `            )`
  Remark: This line is part of the executable source code.
- Line 548: ` `
  Remark: Blank line used for readability.

## `tools/create_dev_certificate.py`

- Line 1: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 2: `from pathlib import Path`
  Remark: This line is part of the executable source code.
- Line 3: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 4: `from datetime import datetime, timedelta, timezone`
  Remark: This line is part of the executable source code.
- Line 5: ` `
  Remark: Blank line used for readability.
- Line 6: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 7: `from cryptography import x509`
  Remark: This line is part of the executable source code.
- Line 8: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 9: `from cryptography.hazmat.primitives import hashes, serialization`
  Remark: This line is part of the executable source code.
- Line 10: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 11: `from cryptography.hazmat.primitives.asymmetric import rsa`
  Remark: This line is part of the executable source code.
- Line 12: `# Remark: imports a module or object needed by this file.`
  Remark: imports a module or object needed by this file.
- Line 13: `from cryptography.x509.oid import NameOID`
  Remark: This line is part of the executable source code.
- Line 14: ` `
  Remark: Blank line used for readability.
- Line 15: ` `
  Remark: Blank line used for readability.
- Line 16: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 17: `ROOT = Path(__file__).resolve().parent.parent`
  Remark: This line is part of the executable source code.
- Line 18: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 19: `CERT_DIR = ROOT / "certs"`
  Remark: This line is part of the executable source code.
- Line 20: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 21: `CERT_PATH = CERT_DIR / "server.crt"`
  Remark: This line is part of the executable source code.
- Line 22: `# Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 23: `KEY_PATH = CERT_DIR / "server.key"`
  Remark: This line is part of the executable source code.
- Line 24: ` `
  Remark: Blank line used for readability.
- Line 25: ` `
  Remark: Blank line used for readability.
- Line 26: `# Remark: defines a function or method.`
  Remark: defines a function or method.
- Line 27: `def main() -> None:`
  Remark: This line is part of the executable source code.
- Line 28: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 29: `    CERT_DIR.mkdir(parents=True, exist_ok=True)`
  Remark: This line is part of the executable source code.
- Line 30: ` `
  Remark: Blank line used for readability.
- Line 31: `    # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 32: `    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)`
  Remark: This line is part of the executable source code.
- Line 33: `    # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 34: `    subject = issuer = x509.Name(`
  Remark: This line is part of the executable source code.
- Line 35: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 36: `        [x509.NameAttribute(NameOID.COMMON_NAME, "SecureChatLocal")]`
  Remark: This line is part of the executable source code.
- Line 37: `    # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 38: `    )`
  Remark: This line is part of the executable source code.
- Line 39: `    # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 40: `    certificate = (`
  Remark: This line is part of the executable source code.
- Line 41: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 42: `        x509.CertificateBuilder()`
  Remark: This line is part of the executable source code.
- Line 43: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 44: `        .subject_name(subject)`
  Remark: This line is part of the executable source code.
- Line 45: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 46: `        .issuer_name(issuer)`
  Remark: This line is part of the executable source code.
- Line 47: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 48: `        .public_key(private_key.public_key())`
  Remark: This line is part of the executable source code.
- Line 49: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 50: `        .serial_number(x509.random_serial_number())`
  Remark: This line is part of the executable source code.
- Line 51: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 52: `        .not_valid_before(datetime.now(timezone.utc) - timedelta(days=1))`
  Remark: This line is part of the executable source code.
- Line 53: `        # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 54: `        .not_valid_after(datetime.now(timezone.utc) + timedelta(days=365))`
  Remark: This line is part of the executable source code.
- Line 55: `        # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 56: `        .sign(private_key, hashes.SHA256())`
  Remark: This line is part of the executable source code.
- Line 57: `    # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 58: `    )`
  Remark: This line is part of the executable source code.
- Line 59: ` `
  Remark: Blank line used for readability.
- Line 60: `    # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 61: `    KEY_PATH.write_bytes(`
  Remark: This line is part of the executable source code.
- Line 62: `        # Remark: starts a multi-line expression.`
  Remark: starts a multi-line expression.
- Line 63: `        private_key.private_bytes(`
  Remark: This line is part of the executable source code.
- Line 64: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 65: `            encoding=serialization.Encoding.PEM,`
  Remark: This line is part of the executable source code.
- Line 66: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 67: `            format=serialization.PrivateFormat.PKCS8,`
  Remark: This line is part of the executable source code.
- Line 68: `            # Remark: creates or updates a program value.`
  Remark: creates or updates a program value.
- Line 69: `            encryption_algorithm=serialization.NoEncryption(),`
  Remark: This line is part of the executable source code.
- Line 70: `        # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 71: `        )`
  Remark: This line is part of the executable source code.
- Line 72: `    # Remark: closes a multi-line expression.`
  Remark: closes a multi-line expression.
- Line 73: `    )`
  Remark: This line is part of the executable source code.
- Line 74: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 75: `    CERT_PATH.write_bytes(certificate.public_bytes(serialization.Encoding.PEM))`
  Remark: This line is part of the executable source code.
- Line 76: ` `
  Remark: Blank line used for readability.
- Line 77: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 78: `    print(f"Created {CERT_PATH}")`
  Remark: This line is part of the executable source code.
- Line 79: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 80: `    print(f"Created {KEY_PATH}")`
  Remark: This line is part of the executable source code.
- Line 81: ` `
  Remark: Blank line used for readability.
- Line 82: ` `
  Remark: Blank line used for readability.
- Line 83: `# Remark: checks a condition before continuing.`
  Remark: checks a condition before continuing.
- Line 84: `if __name__ == "__main__":`
  Remark: This line is part of the executable source code.
- Line 85: `    # Remark: runs this instruction as part of the program logic.`
  Remark: runs this instruction as part of the program logic.
- Line 86: `    main()`
  Remark: This line is part of the executable source code.
- Line 87: ` `
  Remark: Blank line used for readability.
