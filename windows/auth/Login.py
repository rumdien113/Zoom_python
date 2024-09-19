from tkinter import *
from ForgotPassword import ForgotPassword
# from database.DbHelpers import loginDB


def forgot_password():
    ForgotPassword()


class Login:

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
        self.window.title('Login Page')

        # ================== Background Image =================
        self.Login_backgroundImage = PhotoImage(file="../../assets/image_1.png")
        self.bg_imageLogin = Label(
            window,
            image=self.Login_backgroundImage,
            bg="#525561"
        )
        self.bg_imageLogin.place(x=120, y=28)
        self.Login_backgroundImage.image = self.Login_backgroundImage

        # ================ Header Text Left ====================
        self.Login_headerText_image_left = PhotoImage(file="../../assets/headerText_image.png")
        self.Login_headerText_image_label1 = Label(
            self.bg_imageLogin,
            image=self.Login_headerText_image_left,
            bg="#272A37"
        )
        self.Login_headerText_image_left.image = self.Login_headerText_image_left
        self.Login_headerText_image_label1.place(x=60, y=45)

        self.Login_headerText1 = Label(
            self.bg_imageLogin,
            text="Zoom          ",
            fg="#FFFFFF",
            font=("yu gothic ui bold", 20 * -1),
            bg="#272A37"
        )
        self.Login_headerText1.place(x=110, y=45)

        # ================ Header Text Right ====================
        self.Login_headerText_image_right = PhotoImage(file="../../assets/headerText_image.png")
        self.Login_headerText_image_label2 = Label(
            self.bg_imageLogin,
            image=self.Login_headerText_image_right,
            bg="#272A37"
        )
        self.Login_headerText_image_right.image = self.Login_headerText_image_right
        self.Login_headerText_image_label2.place(x=400, y=45)

        self.Login_headerText2 = Label(
            self.bg_imageLogin,
            anchor="nw",
            text="Some Extra Text",
            fg="#FFFFFF",
            font=("yu gothic ui Bold", 20 * -1),
            bg="#272A37"
        )
        self.Login_headerText2.place(x=450, y=45)

        # ================ LOGIN TO ACCOUNT HEADER ====================
        self.loginAccount_header = Label(
            self.bg_imageLogin,
            text="Login to continue",
            fg="#FFFFFF",
            font=("yu gothic ui Bold", 28 * -1),
            bg="#272A37"
        )
        self.loginAccount_header.place(x=75, y=121)

        # ================ NOT A MEMBER TEXT ====================
        self.loginText = Label(
            self.bg_imageLogin,
            text="Not a member?",
            fg="#FFFFFF",
            font=("yu gothic ui Regular", 15 * -1),
            bg="#272A37"
        )
        self.loginText.place(x=75, y=187)

        # ================ GO TO SIGN UP ====================
        self.switchSignup = Button(
            self.bg_imageLogin,
            text="Sign Up",
            fg="#206DB4",
            font=("yu gothic ui Bold", 15 * -1),
            bg="#272A37",
            bd=0,
            cursor="hand2",
            highlightthickness=0,
            activebackground="#272A37",
            activeforeground="#ffffff",
            command=self.switch_register
        )
        self.switchSignup.place(x=220, y=185, width=70, height=35)

        # ================ Email Name Section ====================
        self.Login_emailName_image = PhotoImage(file="../../assets/email.png")
        self.Login_emailName_image_Label = Label(
            self.bg_imageLogin,
            image=self.Login_emailName_image,
            bg="#272A37"
        )
        self.Login_emailName_image.image = self.Login_emailName_image
        self.Login_emailName_image_Label.place(x=76, y=242)

        self.Login_emailName_text = Label(
            self.Login_emailName_image_Label,
            text="Email account",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.Login_emailName_text.place(x=25, y=0)

        self.Login_emailName_icon = PhotoImage(file="../../assets/email-icon.png")
        self.Login_emailName_icon_Label = Label(
            self.Login_emailName_image_Label,
            image=self.Login_emailName_icon,
            bg="#3D404B"
        )
        self.Login_emailName_icon.image = self.Login_emailName_icon
        self.Login_emailName_icon_Label.place(x=370, y=15)

        self.Login_emailName_entry = Entry(
            self.Login_emailName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.Login_emailName_entry.place(x=8, y=17, width=354, height=27)

        # ================ Password Name Section ====================
        self.Login_passwordName_image = PhotoImage(file="../../assets/email.png")
        self.Login_passwordName_image_Label = Label(
            self.bg_imageLogin,
            image=self.Login_passwordName_image,
            bg="#272A37"
        )
        self.Login_passwordName_image.image = self.Login_passwordName_image
        self.Login_passwordName_image_Label.place(x=80, y=330)

        self.Login_passwordName_text = Label(
            self.Login_passwordName_image_Label,
            text="Password",
            fg="#FFFFFF",
            font=("yu gothic ui SemiBold", 13 * -1),
            bg="#3D404B"
        )
        self.Login_passwordName_text.place(x=25, y=0)

        self.Login_passwordName_icon = PhotoImage(file="../../assets/pass-icon.png")
        self.Login_passwordName_icon_Label = Label(
            self.Login_passwordName_image_Label,
            image=self.Login_passwordName_icon,
            bg="#3D404B"
        )
        self.Login_passwordName_icon.image = self.Login_passwordName_icon
        self.Login_passwordName_icon_Label.place(x=370, y=15)

        self.Login_passwordName_entry = Entry(
            self.Login_passwordName_image_Label,
            bd=0,
            bg="#3D404B",
            highlightthickness=0,
            font=("yu gothic ui SemiBold", 16 * -1),
        )
        self.Login_passwordName_entry.place(x=8, y=17, width=354, height=27)

        # =============== Submit Button ====================
        self.Login_button_image_1 = PhotoImage(
            file="../../assets/button_1.png")
        self.Login_button_1 = Button(
            self.bg_imageLogin,
            image=self.Login_button_image_1,
            borderwidth=0,
            highlightthickness=0,
            relief="flat",
            activebackground="#272A37",
            cursor="hand2",
            # command=lambda: login(self.Login_emailName_entry.get(), self.Login_passwordName_entry.get())
        )
        self.Login_button_image_1.image = self.Login_button_image_1
        self.Login_button_1.place(x=120, y=445, width=333, height=65)

        # ================ Forgot Password ====================
        self.forgotPassword = Button(
            self.bg_imageLogin,
            text="Forgot Password",
            fg="#206DB4",
            font=("yu gothic ui Bold", 15 * -1),
            bg="#272A37",
            bd=0,
            highlightthickness=0,
            activebackground="#272A37",
            activeforeground="#ffffff",
            cursor="hand2",
            command=lambda: forgot_password(),
        )
        self.forgotPassword.place(x=210, y=400, width=150, height=35)

        # ================ Header Text Down ====================
        self.Login_headerText_image_down = PhotoImage(file="../../assets/headerText_image.png")
        self.Login_headerText_image_label3 = Label(
            self.bg_imageLogin,
            image=self.Login_headerText_image_down,
            bg="#272A37"
        )
        self.Login_headerText_image_down.image = self.Login_headerText_image_down
        self.Login_headerText_image_label3.place(x=650, y=530)

        self.Login_headerText3 = Label(
            self.bg_imageLogin,
            text="Powered by Tieens DDatj",
            fg="#FFFFFF",
            font=("yu gothic ui bold", 20 * -1),
            bg="#272A37"
        )
        self.Login_headerText3.place(x=700, y=530)

    def switch_register(self):
        from WindowHelpers import open_register_window
        self.window.destroy()
        open_register_window()


def page():
    window = Tk()
    Login(window)
    window.mainloop()


if __name__ == '__main__':
    page()
