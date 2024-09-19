import socket
import threading
from tkinter import simpledialog, messagebox

class Client:
    def __init__(self, ip, port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.client_socket.connect((ip, port))
            messagebox.showinfo("Joined", f"Successfully joined meeting on {ip}:{port}")
            threading.Thread(target=self.receive_messages).start()
        except Exception as e:
            messagebox.showerror("Error", f"Could not join meeting: {e}")

    def send_messages(self):
        while True:
            message = simpledialog.askstring("Message", "Enter your message:")
            if message:
                self.client_socket.send(message.encode())

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if not message:
                    break
                print(f"Received: {message}")
            except:
                break
        self.client_socket.close()
