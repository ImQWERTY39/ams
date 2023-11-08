import tkinter as tk
from tkinter import messagebox

import constants
import functions
import dashboard


def home_page(root: tk.Tk):
    home_page_frame = tk.Frame(
        root,
        width=constants.SCREEN_WIDTH,
        height=constants.SCREEN_HEIGHT,
        bg=constants.BACKGROUND_COLOUR,
    )
    home_page_frame.place(x=0, y=0)

    background_canvas = tk.Canvas(home_page_frame, width=500, height=500)
    background_canvas.place(x=0, y=0)
    background_canvas.image = tk.PhotoImage(file="./assets/background.png")
    background_canvas.create_image(0, 0, anchor=tk.NW, image=background_canvas.image)

    heading = tk.Label(
        home_page_frame,
        text="Apartment\nManagement\nSystem",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("boulder", 32),
    )
    heading.place(x=510, y=25)

    login_button = tk.Button(
        home_page_frame,
        text="Login",
        relief="groove",
        width=10,
        height=1,
        font=("", 12),
        command=lambda: _goto_login_screen(root, home_page_frame),
    )
    login_button.bind("<Return>", lambda _: login_button.invoke())
    login_button.place(x=600, y=300)


def _goto_login_screen(root: tk.Tk, home_page_frame: tk.Frame):
    functions.delete_frame(home_page_frame)
    _login_page(root)


def _login_page(root: tk.Tk):
    root.title(constants.TITLE + " (Login)")

    login_frame = tk.Frame(
        root,
        width=constants.SCREEN_WIDTH,
        height=constants.SCREEN_HEIGHT,
        bg=constants.BACKGROUND_COLOUR,
    )
    login_frame.place(x=0, y=0)

    heading = tk.Label(
        login_frame,
        text="Apartment Management System",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("palatino", 24),
    )
    heading.place(x=195, y=50)

    username_label = tk.Label(
        login_frame,
        text="Username: ",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    username_label.place(x=190, y=165)

    username_entry = tk.Entry(login_frame, width=35)
    username_entry.place(x=390, y=170)

    password_label = tk.Label(
        login_frame,
        text="Password: ",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    password_label.place(x=190, y=245)

    password_entry = tk.Entry(login_frame, width=35, show="*")
    password_entry.place(x=390, y=250)

    login_button = tk.Button(
        login_frame,
        text="Login",
        relief="groove",
        width=10,
        height=1,
        font=("", 12),
        command=lambda: _check_username_and_password(
            username_entry, password_entry, login_frame, root
        ),
    )
    login_button.bind("<Return>", lambda _: login_button.invoke())
    login_button.place(x=325, y=350)

    quit_button = tk.Button(
        login_frame,
        text="Quit",
        relief="groove",
        width=10,
        height=1,
        font=("", 12),
        command=root.destroy,
    )
    quit_button.bind("<Return>", lambda _: quit_button.invoke())
    quit_button.place(x=325, y=390)

    root.mainloop()


def _check_username_and_password(
    username_entry: tk.Entry,
    password_entry: tk.Entry,
    login_frame: tk.Frame,
    root: tk.Tk,
):
    username_string = username_entry.get().strip()
    password_string = password_entry.get().strip()

    if username_string != "admin":
        messagebox.showerror(
            "Incorrect Username",
            "The username you have entered is not correct.\nPlease check the username and try again",
        )
        return

    if password_string != "admin_password":
        messagebox.showerror(
            "Incorrect Password",
            "The password you have entered is not correct.\nPlease check the password and try again",
        )
        return

    messagebox.showinfo("Login Successful", "You have been logged in successfully")

    functions.delete_frame(login_frame)
    root.title(constants.TITLE)

    dashboard.page(root)
