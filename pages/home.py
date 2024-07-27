import tkinter as tk, tools, database, pages.dashboard
from tkinter import messagebox

def page(root: tk.Tk) -> None:
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)

    tools.insert_bgimage(frame, "./assets/home_screen.png")
    tools.create_button(
        frame, text="Login", width=13, height=2,
        command=lambda: tools.switch_frame(root, frame, login)
    ).place(x=335, y=352)
    
def login(root: tk.Tk) -> None:
    frame = tk.Frame(root, width=800, height=600, bg="#00ff00")
    frame.place(x=0, y=0)

    tools.insert_bgimage(frame, "./assets/login_screen.png")
    username = tools.create_entry(frame, 350, 270)
    password = tools.create_entry(frame, 350, 310, show='*')
    
    tools.create_button(
        frame, text="Submit", width=13, height=2, 
        command=lambda: validate(root, username.get(), password.get(), frame)
    ).place(x=410, y=356)
    
    tools.create_button(
        frame, text="Exit", width=13, height=2, 
        command=lambda: tools.switch_frame(root, frame, page)
    ).place(x=250, y=356)

def validate(root: tk.Tk, username: str, password: str, frame: tk.Frame) -> None:
    if not database.init(username.strip(), password.strip()): 
        messagebox.showerror("Invalid details", "Incorrect username/password")
        return

    messagebox.showinfo("Login successful", f"Login successful ({username})")
    tools.switch_frame(root, frame, pages.dashboard.page)
