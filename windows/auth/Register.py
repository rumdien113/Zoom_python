from tkinter import *
from tkinter import messagebox
import pyrebase
import threading

from database.DBHelpers import registerDB


def registerHandle(email, password):
    pass
    # registerDB(email, password)
    # Register.switch_login()

class Register:


    #      _       _
    #   __| | __ _| |_ __ _
    #  / _` |/ _` | __/ _` |
    # | (_| | (_| | || (_| |
    #  \__,_|\__,_|\__\__,_|
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

    def registerDB(self):
        email = self.emailName_entry.get()
        password = self.passwordName_entry.get()
        if len(password) < 6:
            messagebox.showerror("Error", "Password should be at least 6 characters.")
            return False

        try:
            user = Register.auth.create_user_with_email_and_password(email, password)
            print(user)
            return True
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
            return False



    def __init__(self, window):
        self.window = window

        height = 650
        width = 1240
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 4) - (height // 4)
        self.window.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.window.configure(bg="#525561")
        self.window.resizable(0, 0)
        self.window.attributes('-fullscreen', False)  # This works on Linux
        # self.window.attributes('-zoomed', True)  # This works on Windows
        self.window.title('Register Page')

        # ================== Background Image =================
        self.Login_backgroundImage = PhotoImage(file="../../assets/image_1.png")
        self.bg_image = Label(
            window,
            image=self.Login_backgroundImage,
            bg="#525561"
        )
        self.bg_image.place(x=120, y=28)
        self.Login_backgroundImage.image = self.Login_backgroundImage

        # ================ Header Text Left ====================
        self.Login_headerText_image_left = PhotoImage(file="../../assets/headerText_image.png")
        self.Login_headerText_image_label1 = Label(
            self.bg_image,
            image=self.Login_headerText_image_left,
            bg="#272A37"
        )
        self.Login_headerText_image_left.image = self.Login_headerText_image_left
        self.Login_headerText_image_label1.place(x=60, y=45)

        self.Login_headerText1 = Label(
            self.bg_image,
            text="Zoom          ",
            fg="#FFFFFF",
            font=("yu gothic ui bold", 20 * -1),
            bg="#272A37"
        )
        self.Login_headerText1.place(x=110, y=45)

        # ================ Header Text Right ====================
        self.Login_headerText_image_right = PhotoImage(file="../../assets/headerText_image.png")
        self.Login_headerText_image_label2 = Label(
            self.bg_image,
            image=self.Login_headerText_image_right,
            bg="#272A37"
        )
        self.Login_headerText_image_right.image = self.Login_headerText_image_right
        self.Login_headerText_image_label2.place(x=400, y=45)

        self.Login_headerText2 = Label(
            self.bg_image,
            anchor="nw",
            text="Some Extra Text",
            fg="#FFFFFF",
            font=("yu gothic ui Bold", 20 * -1),
            bg="#272A37"
        )
        self.Login_headerText2.place(x=450, y=45)

        # ================ CREATE ACCOUNT HEADER ====================
        self.createAccount_header = Label(
            self.bg_image,
            text="Create new account",
            fg="#FFFFFF",
            font=("yu gothic ui Bold", 28 * -1),
            bg="#272A37"
        )
        self.createAccount_header.place(x=75, y=121)

        # ================ ALREADY HAVE AN ACCOUNT TEXT ====================
        self.text = Label(
            self.bg_image,
            text="Already a member?",
            fg="#FFFFFF",
            font=("yu gothic ui Regular", 15 * -1),
            bg="#272A37"
        )
        self.text.place(x=75, y=187)

        # ================ GO TO LOGIN ====================
        self.switchLogin = Button(
            self.bg_image,
            text="Login",
            fg="#206DB4",
            font=("yu gothic ui Bold", 15 * -1),
            bg="#272A37",
            bd=0,
            highlightthickness=0,
            cursor="hand2",
            activebackground="#272A37",
            activeforeground="#ffffff",
            command=self.switch_login
        )
        self.switchLogin.place(x=230, y=185, width=50, height=35)

        # ================ First Name Section ====================
        self.firstName_image = PhotoImage(file="../../assets/input_img.png")
        self.firstName_image_Label = Label(
            self.bg_image,
            image=self.firstName_image,
            bg="#272A37"
        )
        self.firstName_image.image = self.firstName_image
        self.firstName_image_Label.place(x=80, y=242)

        self.firstName_text = Label(
            self.firstName_image_Label,
            text="First name",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.firstName_text.place(x=25, y=0)

        self.firstName_icon = PhotoImage(file="../../assets/name_icon.png")
        self.firstName_icon_Label = Label(
            self.firstName_image_Label,
            image=self.firstName_icon,
            bg="#3D404B"
        )
        self.firstName_icon.image = self.firstName_icon
        self.firstName_icon_Label.place(x=159, y=15)

        self.firstName_entry = Entry(
            self.firstName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.firstName_entry.place(x=8, y=17, width=140, height=27)

        # ================ Last Name Section ====================
        self.lastName_image = PhotoImage(file="../../assets/input_img.png")
        self.lastName_image_Label = Label(
            self.bg_image,
            image=self.lastName_image,
            bg="#272A37"
        )
        self.lastName_image.image = self.lastName_image
        self.lastName_image_Label.place(x=293, y=242)

        self.lastName_text = Label(
            self.lastName_image_Label,
            text="Last name",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.lastName_text.place(x=25, y=0)

        self.lastName_icon = PhotoImage(file="../../assets/name_icon.png")
        self.lastName_icon_Label = Label(
            self.lastName_image_Label,
            image=self.lastName_icon,
            bg="#3D404B"
        )
        self.lastName_icon.image = self.lastName_icon
        self.lastName_icon_Label.place(x=159, y=15)

        self.lastName_entry = Entry(
            self.lastName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.lastName_entry.place(x=8, y=17, width=140, height=27)

        # ================ Email Name Section ====================
        self.emailName_image = PhotoImage(file="../../assets/email.png")
        self.emailName_image_Label = Label(
            self.bg_image,
            image=self.emailName_image,
            bg="#272A37"
        )
        self.emailName_image.image = self.emailName_image
        self.emailName_image_Label.place(x=80, y=311)

        self.emailName_text = Label(
            self.emailName_image_Label,
            text="Email account",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.emailName_text.place(x=25, y=0)

        self.emailName_icon = PhotoImage(file="../../assets/email-icon.png")
        self.emailName_icon_Label = Label(
            self.emailName_image_Label,
            image=self.emailName_icon,
            bg="#3D404B"
        )
        self.emailName_icon.image = self.emailName_icon
        self.emailName_icon_Label.place(x=370, y=15)

        self.emailName_entry = Entry(
            self.emailName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.emailName_entry.place(x=8, y=17, width=354, height=27)

        # ================ Password Name Section ====================
        self.passwordName_image = PhotoImage(file="../../assets/input_img.png")
        self.passwordName_image_Label = Label(
            self.bg_image,
            image=self.passwordName_image,
            bg="#272A37"
        )
        self.passwordName_image.image = self.passwordName_image
        self.passwordName_image_Label.place(x=80, y=380)

        self.passwordName_text = Label(
            self.passwordName_image_Label,
            text="Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.passwordName_text.place(x=25, y=0)

        self.passwordName_icon = PhotoImage(file="../../assets/pass-icon.png")
        self.passwordName_icon_Label = Label(
            self.passwordName_image_Label,
            image=self.passwordName_icon,
            bg="#3D404B"
        )
        self.passwordName_icon.image = self.passwordName_icon
        self.passwordName_icon_Label.place(x=159, y=15)

        self.passwordName_entry = Entry(
            self.passwordName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.passwordName_entry.place(x=8, y=17, width=140, height=27)

        # ================ Confirm Password Name Section ====================
        self.confirm_passwordName_image = PhotoImage(file="../../assets/input_img.png")
        self.confirm_passwordName_image_Label = Label(
            self.bg_image,
            image=self.confirm_passwordName_image,
            bg="#272A37"
        )
        self.confirm_passwordName_image.image = self.confirm_passwordName_image
        self.confirm_passwordName_image_Label.place(x=293, y=380)

        self.confirm_passwordName_text = Label(
            self.confirm_passwordName_image_Label,
            text="Confirm Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.confirm_passwordName_text.place(x=25, y=0)

        self.confirm_passwordName_icon = PhotoImage(file="../../assets/pass-icon.png")
        self.confirm_passwordName_icon_Label = Label(
            self.confirm_passwordName_image_Label,
            image=self.confirm_passwordName_icon,
            bg="#3D404B"
        )
        self.confirm_passwordName_icon.image = self.confirm_passwordName_icon
        self.confirm_passwordName_icon_Label.place(x=159, y=15)

        self.confirm_passwordName_entry = Entry(
            self.confirm_passwordName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.confirm_passwordName_entry.place(x=8, y=17, width=140, height=27)

        # =============== Submit Button ====================
        self.submit_buttonImage = PhotoImage(file="../../assets/button_1.png")
        self.submit_button = Button(
            self.bg_image,
            image=self.submit_buttonImage,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#272A37",
            cursor="hand2",
            command=lambda: self.registerDB()
        )
        self.submit_buttonImage.image = self.submit_buttonImage
        self.submit_button.place(x=130, y=460, width=333, height=65)

        # ================ Header Text Down ====================
        self.headerText_image_down = PhotoImage(file="../../assets/headerText_image.png")
        self.headerText_image_label3 = Label(
            self.bg_image,
            image=self.headerText_image_down,
            bg="#272A37"
        )
        self.headerText_image_down.image = self.headerText_image_down
        self.headerText_image_label3.place(x=650, y=530)

        self.headerText3 = Label(
            self.bg_image,
            text="Powered by Tieens DDatj",
            fg="#FFFFFF",
            font=("yu gothic ui bold", 20 * -1),
            bg="#272A37"
        )
        self.headerText3.place(x=700, y=530)

    def switch_login(self):
        from WindowHelpers import open_login_window
        self.window.destroy()
        open_login_window()

    def registerHandle(self):
        def run_registration():
            try:
                register = self.registerDB()
                if register:
                    self.switch_login()
            except KeyboardInterrupt:
                messagebox.showerror("Error", "Operation interrupted by user")
            except Exception as e:
                messagebox.showerror("Error", f"An unexpected error occurred: {e}")

        # Run the registration in a separate thread
        threading.Thread(target=run_registration).start()

def page():
    window = Tk()
    Register(window)
    window.mainloop()


if __name__ == '__main__':
    page()
