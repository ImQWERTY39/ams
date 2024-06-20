from tkinter import Tk, Frame, Button, Entry, Label, Checkbutton, BooleanVar, PhotoImage

def switch_frame(root: Tk, old_frame: Frame, new_page, *args) -> None:
    old_frame.destroy()
    new_page(root, *args)

def create_button(frame: Frame, **kwargs) -> Button:
    button = Button(frame, relief="groove", **kwargs)
    button.bind("<Return>", lambda _: button.invoke())
    return button

def create_entry(frame: Frame, x: int, y: int, **kwargs) -> Entry:
    entry = Entry(frame, **kwargs)
    entry.place(x=x, y=y)
    return entry

def create_checkbox(frame: Frame, x: int, y: int, **kwargs) -> BooleanVar:
    var = BooleanVar()
    Checkbutton(frame, variable=var, onvalue=True, offvalue=False).place(x=x, y=y)
    return var

def insert_bgimage(frame: Frame, image: str):
    bg = Label(frame, compound="top")
    frame.image = PhotoImage(file=image)
    bg['image'] = frame.image
    bg.place(x=-1, y=-1)
