import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk
import random
from datetime import datetime

class Server:
    def __init__(self, ip, port, update_participants_callback):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((ip, port))
        self.server_socket.listen(5)
        self.clients = []
        self.client_info = []  # Lưu thông tin của các client: (socket, addr, username, join_time)
        self.update_participants_callback = update_participants_callback
        self.running = True
        threading.Thread(target=self.accept_clients).start()

    def accept_clients(self):
        while self.running:
            try:
                client_socket, addr = self.server_socket.accept()
                username = client_socket.recv(1024).decode()  # Nhận tên người dùng từ client
                join_time = datetime.now().strftime('%H:%M:%S')  # Lấy thời gian tham gia
                self.clients.append(client_socket)
                self.client_info.append((client_socket, addr, username, join_time))  # Lưu thông tin client

                self.update_participants()  # Cập nhật danh sách người tham gia

                print(f"Client {username} ({addr}) connected at {join_time}.")
                threading.Thread(target=self.handle_client, args=(client_socket,)).start()
            except Exception as e:
                print(f"Error accepting client: {e}")
                break

            # Kiểm tra xem có còn client không
            if not self.clients:
                self.stop_server()  # Ngừng server nếu không còn client

    def update_participants(self):
        # Cập nhật danh sách người tham gia cho tất cả các client
        participants_data = [(info[1], info[2], info[3]) for info in self.client_info]  # Lấy IP, tên, và thời gian
        self.update_participants_callback(participants_data)
        for client in self.clients:
            try:
                client.send(f"UPDATE_PARTICIPANTS:{participants_data}".encode())
            except Exception as e:
                print(f"Error sending participants update: {e}")
                self.clients.remove(client)
                client.close()

    def handle_client(self, client_socket):
        while self.running:
            try:
                message = client_socket.recv(1024).decode()
                if message:
                    if message.startswith("DISCONNECT:"):
                        # Xử lý thông báo ngắt kết nối
                        username = message.split(":", 1)[1]
                        self.handle_disconnect(client_socket, username)
                    else:
                        self.broadcast_message(message, client_socket)
            except Exception as e:
                print(f"Error handling client message: {e}")
                break

    def handle_disconnect(self, client_socket, username):
        # Xóa client khỏi danh sách và thông báo cho các client còn lại
        self.clients.remove(client_socket)
        self.client_info = [info for info in self.client_info if info[0] != client_socket]
        self.update_participants()

        disconnect_message = f"{username} has disconnected at {datetime.now().strftime('%H:%M:%S')}."
        self.broadcast_message(disconnect_message, None)  # Gửi thông báo đến tất cả các client

        # Kiểm tra xem có còn client không
        if not self.clients:
            self.stop_server()  # Ngừng server nếu không còn client

    def broadcast_message(self, message, sender_socket):
        for client in self.clients:
            if client != sender_socket:
                try:
                    client.send(message.encode())
                except Exception as e:
                    print(f"Error broadcasting message: {e}")
                    self.clients.remove(client)
                    client.close()

    def stop_server(self):
        self.running = False
        for client in self.clients:
            client.close()
        self.server_socket.close()
        print("Server stopped.")


class Client:
    def __init__(self, ip, port, display_message_callback, update_participants_callback, username):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.display_message_callback = display_message_callback
        self.update_participants_callback = update_participants_callback
        self.username = username
        try:
            self.client_socket.connect((ip, port))
            self.client_socket.send(username.encode())  # Gửi tên người dùng lên server
            print(f"Connected to server at {ip}:{port}")
            threading.Thread(target=self.receive_messages).start()
        except Exception as e:
            messagebox.showerror("Error", f"Could not connect to server: {e}")

    def send_message(self, message):
        if message:
            self.client_socket.send(message.encode())
            self.display_message_callback(message)  # Hiển thị tin nhắn đã gửi

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message.startswith("UPDATE_PARTICIPANTS:"):
                    # Nhận danh sách người tham gia
                    participants_data = eval(message.split(":", 1)[1])  # Chuyển đổi chuỗi thành danh sách
                    self.update_participants_callback(participants_data)
                else:
                    self.display_message_callback(message)
            except Exception as e:
                print(f"Error receiving message: {e}")
                break
        self.client_socket.close()

    def disconnect(self):
        self.client_socket.send(f"DISCONNECT:{self.username}".encode())  # Gửi thông báo ngắt kết nối
        self.client_socket.close()

class Menu:
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.server = None
        self.client = None
        self.root.title(self.username)
        self.root.geometry("700x600")
        self.local_ip = None
        self.port = None
        self.create_menu()

    def create_menu(self):
        self.notebook = ttk.Notebook(self.root)
        self.chat_tab = tk.Frame(self.notebook)
        self.participants_tab = tk.Frame(self.notebook)

        self.notebook.add(self.chat_tab, text="Chat")
        self.notebook.add(self.participants_tab, text="Participants")
        self.notebook.pack(expand=True, fill="both")

        # Chat tab layout
        button_frame = tk.Frame(self.chat_tab)
        button_frame.pack(pady=20)

        self.new_meeting_btn = tk.Button(button_frame, text="New Meeting", width=20, command=self.start_new_meeting)
        self.new_meeting_btn.grid(row=0, column=0, padx=20, pady=10)

        self.join_btn = tk.Button(button_frame, text="Join", width=20, command=self.join_meeting)
        self.join_btn.grid(row=0, column=1, padx=20, pady=10)

        self.disconnect_btn = tk.Button(button_frame, text="Disconnect", width=20, command=self.disconnect)
        self.disconnect_btn.grid(row=0, column=2, padx=20, pady=10)
        self.disconnect_btn.grid_forget()  # Ẩn nút Disconnect khi không kết nối

        self.message_display = tk.Text(self.chat_tab, height=10, width=50, state='disabled')
        self.message_display.pack(pady=10)

        self.message_entry = tk.Entry(self.chat_tab, width=40)
        self.message_entry.pack(side=tk.LEFT, padx=10)

        send_btn = tk.Button(self.chat_tab, text="Send", command=self.send_message)
        send_btn.pack(side=tk.LEFT)

        # Participants tab layout
        self.participants_list = tk.Listbox(self.participants_tab, height=20, width=50)
        self.participants_list.pack(pady=10)

    def start_new_meeting(self):
        try:
            self.local_ip = socket.gethostbyname(socket.gethostname())  # Get local IP
            self.port = random.randint(1000, 9999)  # Generate random 4-digit port number
            self.server = Server(self.local_ip, self.port, self.update_participants_list)
            self.client = Client(self.local_ip, self.port, self.display_message, self.update_participants_list,
                                 self.username)  # Server acts as a client for messaging
            messagebox.showinfo("Server Started",
                                f"Meeting started on IP: {self.local_ip}, Port: {self.port}\nShare this port to allow others to join.")
            self.show_copy_button()  # Hiển thị nút sao chép địa chỉ sau khi bắt đầu cuộc họp
            self.show_stop_button()  # Hiển thị nút Stop Server
            self.hide_buttons()  # Ẩn nút sau khi kết nối thành công
        except Exception as e:
            messagebox.showerror("Error", f"Could not start server: {e}")

    def join_meeting(self):
        local_ip = socket.gethostbyname(socket.gethostname())  # Get local IP
        port = simpledialog.askstring("Room Code", "Enter the room code (port):")
        if port:
            try:
                self.client = Client(local_ip, int(port), self.display_message, self.update_participants_list,
                                     self.username)
                self.hide_buttons()  # Ẩn nút sau khi kết nối thành công
                self.show_disconnect_button()  # Hiển thị nút Disconnect cho client
            except Exception as e:
                messagebox.showerror("Error", f"Could not connect to server: {e}")

    def hide_buttons(self):
        """Ẩn các nút New Meeting và Join sau khi kết nối thành công"""
        self.new_meeting_btn.grid_forget()
        self.join_btn.grid_forget()

    def show_copy_button(self):
        """Hiển thị nút để sao chép địa chỉ IP và port"""
        copy_frame = tk.Frame(self.chat_tab)
        copy_frame.pack(pady=10)

        self.copy_btn = tk.Button(copy_frame, text="Copy Port Room", command=self.copy_ip_port)
        self.copy_btn.pack(padx=10, pady=10)

    def show_stop_button(self):
        """Hiển thị nút dừng server"""
        self.stop_frame = tk.Frame(self.chat_tab)
        self.stop_frame.pack(pady=10)

        self.stop_btn = tk.Button(self.stop_frame, text="Stop Server", bg="red", fg="white", command=self.stop_server)
        self.stop_btn.pack(padx=10, pady=10)

    def show_disconnect_button(self):
        """Hiển thị nút ngắt kết nối"""
        self.disconnect_btn.grid(row=0, column=2, padx=20, pady=10)  # Hiển thị nút Disconnect cho client

    def copy_ip_port(self):
        """Sao chép địa chỉ IP và port vào clipboard"""
        if self.local_ip and self.port:
            self.root.clipboard_clear()  # Xóa clipboard hiện tại
            self.root.clipboard_append(f"{self.port}")  # Sao chép IP:port vào clipboard
            messagebox.showinfo("Copied", "Port copied to clipboard!")

    def stop_server(self):
        """Dừng server và ngắt kết nối"""
        if self.server:
            self.server.stop_server()
            self.server = None  # Đặt server về None
        if self.client:
            self.client.disconnect()  # Ngắt kết nối client
            self.client = None  # Đặt client về None
        self.reset_to_menu()  # Trở lại menu ban đầu

    def disconnect(self):
        """Ngắt kết nối client"""
        if self.client:
            self.client.disconnect()  # Ngắt kết nối client
            self.client = None  # Đặt client về None
        self.reset_to_menu()  # Trở lại menu ban đầu

    def reset_to_menu(self):
        """Khôi phục giao diện về trạng thái menu ban đầu"""
        if hasattr(self, 'stop_frame'):
            self.stop_frame.pack_forget()  # Ẩn nút Stop Server
        if hasattr(self, 'copy_btn'):
            self.copy_btn.pack_forget()  # Ẩn nút sao chép IP và Port
        if hasattr(self, 'message_display'):
            self.message_display.pack_forget()  # Ẩn phần chat
        if hasattr(self, 'message_entry'):
            self.message_entry.pack_forget()  # Ẩn phần nhập tin nhắn

        # Hiển thị lại các nút New Meeting và Join
        self.new_meeting_btn.grid(row=0, column=0, padx=20, pady=10)
        self.join_btn.grid(row=0, column=1, padx=20, pady=10)
        self.disconnect_btn.grid_forget()  # Ẩn nút Disconnect

        # Xóa danh sách người tham gia
        self.participants_list.delete(0, tk.END)

    def send_message(self):
        message = self.message_entry.get()
        if self.client and message:
            self.client.send_message(f"{self.username}: {message}")
            self.message_entry.delete(0, tk.END)  # Xóa nội dung sau khi gửi

    def display_message(self, message):
        self.message_display.config(state='normal')
        self.message_display.insert(tk.END, f"{message}\n")
        self.message_display.config(state='disabled')

    def update_participants_list(self, participants):
        self.participants_list.delete(0, tk.END)  # Xóa danh sách hiện tại
        for participant in participants:
            ip, username, join_time = participant
            self.participants_list.insert(tk.END,
                                          f"{ip} - {username} - Joined at {join_time}")  # Hiển thị IP, tên, và thời gian

if __name__ == "__main__":
    root = tk.Tk()
    username = simpledialog.askstring("Username", "Enter your username:")
    if username:
        app = Menu(root, username)
        root.mainloop()
