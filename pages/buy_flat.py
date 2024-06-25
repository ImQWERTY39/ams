import tkinter as tk, tools, database, pages.dashboard

def page(root: tk.Tk):
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    
    tools.insert_bgimage(frame, "./assets/buy_sell.png")
    flat_number = tools.create_entry(frame, 210, 280)
    
    tools.create_button(
        frame, text="Submit", command=lambda: own_flat(root, frame, flat_number.get())
    ).place(x=670, y=525)
    tools.create_button(
        frame, text="Quit", 
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=525, y=525)

def own_flat(root, frame, flat_number):
    flat = database.get_flat(flat_number)
    
    if flat is None: 
        tk.messagebox.showerror("Flat doesn't exist", f"Flat {flat_number} doesn't exist")
        return
    
    if not flat[1]: 
        tk.messagebox.showerror("Flat not available", f"Flat {flat_number} is not for sale")
        return
    
    if flat[2]: tools.switch_frame(root, frame, rent_out, flat)
    else: tools.switch_frame(root, frame, for_buy, flat)

def rent_out(root, flat):
    frame = tk.Frame(root, width=800, height=600, bg="#0000ff")
    frame.place(x=0, y=0)
    
    tools.insert_bgimage(frame, "./assets/buy_sell_rented.png")
    tk.Label(frame, text=f"{flat[0]}", bg="white").place(x=250, y=280)
    tenant_name = tools.create_entry(frame, 220, 330)
    
    tools.create_button(
        frame, text="Submit", 
        command=lambda: rent(root, frame, flat[0], tenant_name.get())
    ).place(x=670, y=525)
    tools.create_button(
        frame, text="Quit", 
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=525, y=525)

def for_buy(root, flat):
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    
    tools.insert_bgimage(frame, "./assets/buy_sell_owned.png")
    tk.Label(frame, text=f"{flat[0]}", bg="white").place(x=250, y=280)
    owner_name = tools.create_entry(frame, 220, 330)
    phno = tools.create_entry(frame, 220, 385)
    email = tools.create_entry(frame, 220, 440)
    
    tools.create_button(
        frame, text="Submit", 
        command=lambda: buy(root, frame, flat[0], owner_name.get(), phno.get(), email.get())
    ).place(x=670, y=525)
    tools.create_button(
        frame, text="Quit", 
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=525, y=525)

def rent(root, frame, flat_number, tenant_name):
    if database.rent_out_flat(flat_number, tenant_name) == 1: 
        tk.messagebox.showerror("Invalid detail", "Tenant name is empty")
    else:
        tk.messagebox.showinfo("Information Updated", "Tenant added successfully")
        tools.switch_frame(root, frame, pages.dashboard.page)

def buy(root, frame, flat_number, owner_name, phno, email): 
    success = database.buy_flat(flat_number, owner_name, phno, email)
    
    if success == 1: tk.messagebox.showerror("Invalid detail", "Owner name is empty")
    elif success == 2: tk.messagebox.showerror("Invalid detail", "Invalid phone number")
    elif success == 3: tk.messagebox.showerror("Invalid detail", "Invalid email")
    else:
        tk.messagebox.showinfo("Information Updated", "Owner added successfully")
        tools.switch_frame(root, frame, pages.dashboard.page)
