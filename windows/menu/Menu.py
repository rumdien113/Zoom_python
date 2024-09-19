import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox
import random
from datetime import datetime


class Server:
    def __init__(self, ip, port, update_participants_callback):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.server_socket.listen(5)
        self.clients = []
        self.client_addresses = []  # Lưu trữ địa chỉ của các client
        self.update_participants_callback = update_participants_callback
        threading.Thread(target=self.accept_clients).start()

    def accept_clients(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            self.clients.append(client_socket)
            self.client_addresses.append(addr)  # Lưu địa chỉ client
            self.update_participants_callback(self.client_addresses)  # Cập nhật danh sách tham gia
            print(f"Client {addr} connected.")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    self.broadcast_message(message, client_socket)
            except:
                index = self.clients.index(client_socket)
                self.clients.remove(client_socket)
                self.client_addresses.pop(index)
                self.update_participants_callback(self.client_addresses)  # Cập nhật khi có client rời
                client_socket.close()
                break

    def broadcast_message(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message.encode())
                except:
                    self.clients.remove(client)
                    client.close()

    def send_message_to_clients(self, message):
        for client in self.clients:
            try:
                client.send(message.encode())
            except:
                self.clients.remove(client)
                client.close()


class Client:
    def __init__(self, ip, port, display_message_callback):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.display_message_callback = display_message_callback
        try:
            self.client_socket.connect((ip, port))
            print(f"Connected to server at {ip}:{port}")
            threading.Thread(target=self.receive_messages).start()
        except Exception as e:
            messagebox.showerror("Error", f"Could not connect to server: {e}")

    def send_message(self, message):
        if message:
            self.client_socket.send(message.encode())

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    self.display_message_callback(message)
            except:
                print("Disconnected from the server.")
                break
        self.client_socket.close()


class Menu:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.server = None
        self.client = None
        self.root.title(self.username)
        self.root.geometry("600x400")
        self.participants_list = tk.Listbox(self.root, height=10)  # Danh sách người tham gia
        self.create_menu()

    def create_menu(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        new_meeting_btn = tk.Button(button_frame, text="New Meeting", width=20, command=self.start_new_meeting)
        new_meeting_btn.grid(row=0, column=0, padx=20, pady=10)

        join_btn = tk.Button(button_frame, text="Join", width=20, command=self.join_meeting)
        join_btn.grid(row=0, column=1, padx=20, pady=10)

        self.message_display = tk.Text(self.root, height=10, width=50, state='disabled')
        self.message_display.pack(pady=10)

        self.message_entry = tk.Entry(self.root, width=40)
        self.message_entry.pack(side=tk.LEFT, padx=10)

        send_btn = tk.Button(self.root, text="Send", command=self.send_message)
        send_btn.pack(side=tk.LEFT)

        self.participants_list.pack(pady=10)  # Hiển thị danh sách người tham gia

    def start_new_meeting(self):
        try:
            local_ip = socket.gethostbyname(socket.gethostname())  # Get local IP
            port = random.randint(1000, 9999)  # Generate random 4-digit port number
            self.server = Server(local_ip, port, self.update_participants_list)
            self.client = Client(local_ip, port, self.display_message)  # Server acts as a client for messaging
            messagebox.showinfo("Server Started", f"Meeting started on IP: {local_ip}, Port: {port}\nShare this port to allow others to join.")
        except Exception as e:
            messagebox.showerror("Error", f"Could not start server: {e}")

    def join_meeting(self):
        local_ip = socket.gethostbyname(socket.gethostname())  # Get local IP
        port = simpledialog.askstring("Room Code", "Enter the room code (port):")
        if port:
            try:
                self.client = Client(local_ip, int(port), self.display_message)
            except Exception as e:
                messagebox.showerror("Error", f"Could not connect to server: {e}")

    def send_message(self):
        message = self.message_entry.get()
        if self.client and message:
            self.client.send_message(f"{self.username}: {message}")
            if self.server:  # Nếu là server thì gửi tin nhắn tới tất cả các client
                self.server.send_message_to_clients(f"{self.username} (Server): {message}")
            self.message_entry.delete(0, tk.END)

    def display_message(self, message):
        self.message_display.config(state='normal')
        self.message_display.insert(tk.END, f"{message}\n")
        self.message_display.config(state='disabled')

    def update_participants_list(self, participants):
        self.participants_list.delete(0, tk.END)  # Xóa danh sách cũ
        for addr in participants:
            self.participants_list.insert(tk.END, f"{addr}")  # Thêm từng client vào danh sách


if __name__ == "__main__":
    root = tk.Tk()
    username = simpledialog.askstring("Username", "Enter your username:")
    if username:
        app = Menu(root, username)
        root.mainloop()
