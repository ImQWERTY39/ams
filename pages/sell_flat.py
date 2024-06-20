import tkinter as tk, tools, database, pages.dashboard

def page(root: tk.Tk):
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    tools.insert_bgimage(frame, "./assets/buy_sell.png")
    flat_number = tools.create_entry(frame, 210, 280)
    tools.create_button(frame, text="Submit", command=lambda: switch(root, frame, flat_number.get())).place(x=670, y=525)
    tools.create_button(frame, text="Quit", command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)).place(x=525, y=525)

def switch(root, frame, flat_number):
    flat = database.get_flat(flat_number)
    if flat is None: tk.messagebox.showerror("Flat doesn't exist", f"Flat {flat_number} doesn't exist"); return
    if flat[1]: tk.messagebox.showerror("Flat not available", f"Flat {flat_number} is for sale"); return
    tools.switch_frame(root, frame, sell_flat, flat)

def sell_flat(root, flat):
    owner = None
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)

    if flat[2]:
        tools.insert_bgimage(frame, "./assets/buy_sell_rented.png")
        tk.Label(frame, text=f"{flat[4]}", bg="white").place(x=220, y=335)
    else:
        owner = database.get_owner(flat[3])
        tools.insert_bgimage(frame, "./assets/buy_sell_owned.png")
        tk.Label(frame, text=f"{owner[0]}", bg="white").place(x=220, y=330)
        tk.Label(frame, text=f"{owner[1]}", bg="white").place(x=220, y=380)
        tk.Label(frame, text=f"{owner[2]}", bg="white").place(x=220, y=440)
    tk.Label(frame, text=f"{flat[0]}", bg="white").place(x=250, y=280)
    tools.create_button(frame, text="Sell", command=lambda: sell(root, frame, flat, owner)).place(x=670, y=525)
    tools.create_button(frame, text="Quit", command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)).place(x=525, y=525)

def sell(root, frame, flat, owner):
    if not tk.messagebox.askyesno("Confirmation", "Are you sure you want to sell the flat?\nThis is an irreverseable change"): return
    if database.sell_flat(flat, owner): tk.messagebox.showinfo("Deleted Owner Information", f"Deleted {owner[0]}'s information'")
    tk.messagebox.showinfo("Sold Flat", f"Flat {flat[0]} sold successfully")
    tools.switch_frame(root, frame, pages.dashboard.page)
