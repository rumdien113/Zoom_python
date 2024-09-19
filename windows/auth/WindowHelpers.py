from tkinter import Tk
from Register import Register
from Login import Login


def open_register_window():
    register_window = Tk()
    Register(register_window)
    register_window.mainloop()


def open_login_window():
    login_window = Tk()
    Login(login_window)
    login_window.mainloop()
