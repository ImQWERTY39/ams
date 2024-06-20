import tkinter as tk, tools, database, pages.dashboard

def page(root: tk.Tk):
    frame = tk.Frame(root, width=800, height=600, bg="#0000ff")
    frame.place(x=0, y=0)
    
    tools.create_button(frame, text="Quit", command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)).place(x=0, y=0)
