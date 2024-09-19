import tkinter
import tkinter as tk  # Sử dụng thư viện tkinter gốc
from tkinter import mainloop
import pyrebase
import customtkinter
from windows.menu.Menu import Menu


# Sử dụng customtkinter để tạo giao diện đăng nhập
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")

# Cấu hình Firebase
firebaseConfig = {
    'apiKey': "AIzaSyCTvWEv-raCwRbFsrr6_EBIxiWITGyNS8c",
    'authDomain': "zoom-6168e.firebaseapp.com",
    'databaseURL': "https://zoom-6168e-default-rtdb.firebaseio.com",
    'projectId': "zoom-6168e",
    'storageBucket': "zoom-6168e.appspot.com",
    'messagingSenderId': "696910928874",
    'appId': "1:696910928874:web:ead4f53ee7d12e94a83093",
    'measurementId': "G-W61LY98BH9"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Lớp Menu để hiển thị sau khi đăng nhập thành công
# class Menu:
#     def __init__(self, root, username):
#         self.root = root
#         self.username = username
#         self.root.title(self.username)  # Đặt tiêu đề là tên người dùng
#         self.root.geometry("600x400")  # Kích thước cửa sổ
#         self.create_menu()
#
#     def create_menu(self):
#         # Tạo frame cho các nút
#         button_frame = tk.Frame(self.root)
#         button_frame.pack(pady=50)
#
#         # Nút New Meeting
#         new_meeting_btn = tk.Button(button_frame, text="New Meeting", width=20)
#         new_meeting_btn.grid(row=0, column=0, padx=20, pady=10)
#
#         # Nút Join
#         join_btn = tk.Button(button_frame, text="Join", width=20)
#         join_btn.grid(row=0, column=1, padx=20, pady=10)
#
#         # Nút Schedule
#         schedule_btn = tk.Button(button_frame, text="Schedule", width=20)
#         schedule_btn.grid(row=1, column=0, padx=20, pady=10)
#
#         # Nút Share screen
#         share_btn = tk.Button(button_frame, text="Share screen", width=20)
#         share_btn.grid(row=1, column=1, padx=20, pady=10)
#
#         # Hiển thị lịch và đồng hồ (tuỳ chọn, chỉ để trang trí)
#         calendar_label = tk.Label(self.root, text="6:24 PM\nThursday, September 19", font=("Arial", 16))
#         calendar_label.pack(pady=20)

# Hàm đăng ký người dùng
def registerDB():
    email = username_entry.get()
    password = password_entry.get()
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print(user)
    except Exception as e:
        print(f"Error: {e}")
    return

# Hàm đăng nhập người dùng
def loginDB():
    email = username_entry.get()
    password = password_entry.get()
    try:
        # Đăng nhập thành công
        user = auth.sign_in_with_email_and_password(email, password)
        print(user)

        # Lấy tên người dùng từ email
        username = email.split('@')[0]  # Lấy phần trước dấu @ làm username

        # Đóng giao diện đăng nhập hiện tại
        app.destroy()

        # Mở giao diện menu với tên người dùng
        root = tk.Tk()
        Menu(root, username)
        mainloop()

    except Exception as e:
        print(f"Error: {e}")
    return

# Giao diện đăng nhập
username = customtkinter.CTkLabel(
    master=app,
    text="Username",
    width=80,
    height=25,
    text_color="black",
    fg_color=("black", "white"),
    corner_radius=8
)
username.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)

password = customtkinter.CTkLabel(
    master=app,
    text="Password",
    width=80,
    height=25,
    text_color="black",
    fg_color=("black", "white"),
    corner_radius=8
)
password.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)

username_entry = customtkinter.CTkEntry(
    master=app,
    placeholder_text="Enter your username",
    width=180,
    height=25,
    border_width=2,
    corner_radius=10
)
username_entry.place(relx=0.65, rely=0.3, anchor=tkinter.CENTER)

password_entry = customtkinter.CTkEntry(
    master=app,
    placeholder_text="Enter your password",
    width=180,
    height=25,
    border_width=2,
    corner_radius=10
)
password_entry.place(relx=0.65, rely=0.5, anchor=tkinter.CENTER)

login_button = customtkinter.CTkButton(
    master=app,
    width=80,
    height=32,
    border_width=0,
    corner_radius=8,
    text="Login",
    command=loginDB
)
login_button.place(relx=0.71, rely=0.7, anchor=tkinter.CENTER)

signup_button = customtkinter.CTkButton(
    master=app,
    width=80,
    height=32,
    border_width=0,
    corner_radius=8,
    text="Sign Up",
    command=registerDB
)
signup_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

result = customtkinter.CTkLabel(
    master=app,
    text="",
    width=120,
    height=25,
    text_color="black",
    fg_color=("black", "white"),
    corner_radius=8
)
result.place(relx=0.62, rely=0.85, anchor=tkinter.CENTER)

app.mainloop()
