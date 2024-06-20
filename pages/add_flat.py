import tkinter as tk, tools, database, pages.dashboard

def page(root: tk.Tk) -> None:
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)

    tools.insert_bgimage(frame, "./assets/add.png")

    flat_number = tools.create_entry(frame, 180, 280)
    availability = tools.create_checkbox(frame, 220, 340)
    for_rent = tools.create_checkbox(frame, 200, 400)
    tenant_name = tools.create_entry(frame, 230, 460)
    owner_name = tools.create_entry(frame, 500, 280)
    phone_number = tools.create_entry(frame, 500, 340)
    email = tools.create_entry(frame, 500, 400)
    
    tools.create_button(frame, text="Submit", command=lambda: submit(root, frame, flat_number.get().strip(), availability.get(), for_rent.get(), owner_name.get().strip(), tenant_name.get().strip(), phone_number.get().strip(), email.get().strip())).place(x=670, y=525)
    tools.create_button(frame, text="Quit", command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)).place(x=525, y=525)

def submit(root, frame, *args) -> None:
    success = database.add_flat(*args)
    if success == 1: tk.messagebox.showerror("Invalid data", "Flat number cannot be empty")
    elif success == 2: tk.messagebox.showerror("Invalid data", f"Flat {args[0]} already exists")
    elif success == 3: tk.messagebox.showerror("Invalid data", "Empty owner name for owned house")
    elif success == 4: tk.messagebox.showerror("Invalid data", "Invalid phone number")
    elif success == 5: tk.messagebox.showerror("Invalid data", "Invalid email")
    elif success == 6: tk.messagebox.showerror("Invalid data", "Empty tenant name for rented house")
    else: tk.messagebox.showinfo("Success", f"Flat {args[0]} added successfully"); tools.switch_frame(root, frame, pages.dashboard.page)
