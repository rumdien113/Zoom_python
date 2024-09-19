import socket
import threading
import requests
import tkinter as tk
from tkinter import messagebox, simpledialog
from . import Client

class Menu:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title(self.username)
        self.root.geometry("600x400")
        self.server_socket = None
        self.create_menu()

    def create_menu(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=50)

        new_meeting_btn = tk.Button(button_frame, text="New Meeting", width=20, command=self.start_new_meeting)
        new_meeting_btn.grid(row=0, column=0, padx=20, pady=10)

        join_btn = tk.Button(button_frame, text="Join", width=20, command=self.join_meeting)
        join_btn.grid(row=0, column=1, padx=20, pady=10)

        calendar_label = tk.Label(self.root, text="6:24 PM\nThursday, September 19", font=("Arial", 16))
        calendar_label.pack(pady=20)

    def start_new_meeting(self):
        room_code = simpledialog.askstring("Room Code", "Enter a room code (numeric):")
        if not room_code.isdigit():
            messagebox.showerror("Invalid Input", "Room code must be numeric.")
            return

        port = int(room_code)

        try:
            public_ip = requests.get('https://api.ipify.org').text
        except Exception as e:
            messagebox.showerror("Error", f"Could not get public IP: {e}")
            return

        try:
            self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_socket.bind((public_ip, port))
            self.server_socket.listen(5)
            messagebox.showinfo("Server Started", f"Meeting started on IP: {public_ip}, Port: {port}")
            threading.Thread(target=self.accept_clients).start()
        except Exception as e:
            messagebox.showerror("Error", f"Could not start server: {e}")

    def accept_clients(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            print(f"Client {addr} connected.")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if not message:
                    break
                print(f"Received: {message}")
            except:
                break
        client_socket.close()

    def join_meeting(self):
        ip = simpledialog.askstring("Join Meeting", "Enter the server IP:")
        room_code = simpledialog.askstring("Room Code", "Enter the room code (port):")
        if not room_code.isdigit():
            messagebox.showerror("Invalid Input", "Room code must be numeric.")
            return

        port = int(room_code)
        client = Client(ip, port)
        threading.Thread(target=client.send_messages).start()

