from tkinter import Frame


def delete_frame(frame: Frame):
    for i in frame.winfo_children():
        i.destroy()

    frame.destroy()
