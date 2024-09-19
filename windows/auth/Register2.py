import pyrebase
import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")

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


def registerDB():
    email = username_entry.get()
    password = password_entry.get()
    try:
        user = auth.create_user_with_email_and_password(email, password)
        print(user)
    except Exception as e:
        print(f"Error: {e}")
    return


def loginDB():
    email = username_entry.get()
    password = password_entry.get()
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        print(user)
    except Exception as e:
        print(f"Error: {e}")
    return


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
