import tkinter as tk
from tkinter import ttk
import socket
import threading
import pyautogui
from PIL import Image, ImageTk
import random

# Server class for handling screen share
class ScreenShareServer:
    def __init__(self, ip, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.bind((ip, port))
        self.running = True
        threading.Thread(target=self.handle_clients).start()

    def handle_clients(self):
        while self.running:
            screenshot = pyautogui.screenshot()  # Capture the screen
            screen_data = screenshot.tobytes()  # Convert to bytes
            self.server_socket.sendto(screen_data, ("<client_ip>", 9999))  # Send to client
            threading.Event().wait(0.05)  # Adjust for screen refresh rate

    def stop(self):
        self.running = False
        self.server_socket.close()

# Client class for receiving screen share
class ScreenShareClient:
    def __init__(self, ip, port, canvas):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client_socket.bind((ip, port))
        self.canvas = canvas
        self.running = True
        threading.Thread(target=self.receive_screen).start()

    def receive_screen(self):
        while self.running:
            screen_data, _ = self.client_socket.recvfrom(65536)  # Receive data
            screenshot = Image.frombytes('RGB', pyautogui.size(), screen_data)  # Convert back to image
            self.display_screenshot(screenshot)

    def display_screenshot(self, screenshot):
        img = ImageTk.PhotoImage(screenshot)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
        self.canvas.image = img  # Keep a reference

    def stop(self):
        self.running = False
        self.client_socket.close()

# Main GUI with chat and screen sharing
class StreamChatApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x600")
        self.root.title("Screen Share and Chat")

        # Screen share on left
        self.screen_frame = tk.Frame(root, width=400, height=600)
        self.screen_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.screen_frame, bg='black', width=400, height=600)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Chat on right
        self.chat_frame = tk.Frame(root, width=400, height=600)
        self.chat_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.message_display = tk.Text(self.chat_frame, height=30, state='disabled')
        self.message_display.pack(pady=10)

        self.message_entry = tk.Entry(self.chat_frame, width=40)
        self.message_entry.pack(side=tk.LEFT, padx=10)

        self.send_btn = tk.Button(self.chat_frame, text="Send", command=self.send_message)
        self.send_btn.pack(side=tk.LEFT)

        self.server = None
        self.client = None

    def start_screen_share_server(self):
        ip = socket.gethostbyname(socket.gethostname())
        port = random.randint(1000, 9999)
        self.server = ScreenShareServer(ip, port)

    def join_screen_share(self, ip, port):
        self.client = ScreenShareClient(ip, port, self.canvas)

    def send_message(self):
        message = self.message_entry.get()
        if message:
            self.message_display.config(state='normal')
            self.message_display.insert(tk.END, f"You: {message}\n")
            self.message_display.config(state='disabled')
            self.message_entry.delete(0, tk.END)

root = tk.Tk()
app = StreamChatApp(root)
root.mainloop()
