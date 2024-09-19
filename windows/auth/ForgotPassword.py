from tkinter import *


class ForgotPassword:

    def __init__(self):
        self.windown = Toplevel()
        self.window_width = 350
        self.window_height = 350
        self.screen_width = self.windown.winfo_screenwidth()
        self.screen_height = self.windown.winfo_screenheight()
        self.position_top = int(self.screen_height / 4 - self.window_height / 4)
        self.position_right = int(self.screen_width / 2 - self.window_width / 2)
        self.windown.geometry(f'{self.window_width}x{self.window_height}+{self.position_right}+{self.position_top}')

        self.windown.title('Forgot Password')
        # windown.iconbitmap('images\\aa.ico')
        self.windown.configure(background='#272A37')
        self.windown.resizable(False, False)

        # ====== Email ====================
        self.email_entry3 = Entry(self.windown, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                                  bd=0)
        self.email_entry3.place(x=40, y=80, width=256, height=50)
        self.email_entry3.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        self.email_label3 = Label(self.windown, text='• Email', fg="#FFFFFF", bg='#272A37',
                                  font=("yu gothic ui", 11, 'bold'))
        self.email_label3.place(x=40, y=50)

        # ====  New Password ==================
        self.new_password_entry = Entry(self.windown, bg="#3D404B", font=("yu gothic ui semibold", 12), show='•',
                                        highlightthickness=1,
                                        bd=0)
        self.new_password_entry.place(x=40, y=180, width=256, height=50)
        self.new_password_entry.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
        self.new_password_label = Label(self.windown, text='• New Password', fg="#FFFFFF", bg='#272A37',
                                        font=("yu gothic ui", 11, 'bold'))
        self.new_password_label.place(x=40, y=150)

        # ======= Update password Button ============
        self.update_pass = Button(self.windown, fg='#f8f8f8', text='Update Password', bg='#1D90F5',
                                  font=("yu gothic ui", 12, "bold"),
                                  cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5")
        self.update_pass.place(x=40, y=260, width=256, height=45)
