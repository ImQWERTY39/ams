import tkinter as tk, tools, database, pages.dashboard

def page(root: tk.Tk) -> None:
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)

    tools.insert_bgimage(frame, "./assets/add.png")
    flat_number = tools.create_entry(frame, 180, 280)
    (a_cb, availability) = tools.create_checkbox(frame, 220, 340, False)
    (fr_cb, for_rent) = tools.create_checkbox(frame, 220, 400, False)
    tenant_name = tools.create_entry(frame, 230, 460)
    owner_name = tools.create_entry(frame, 500, 280)
    phone_number = tools.create_entry(frame, 500, 340)
    email = tools.create_entry(frame, 500, 400)

    change_state(availability.get(), for_rent.get(), tenant_name, owner_name, phone_number, email)
    a_cb.config(command=lambda: change_state(availability.get(), for_rent.get(), tenant_name, owner_name, phone_number, email))
    fr_cb.config(command=lambda: change_state(availability.get(), for_rent.get(), tenant_name, owner_name, phone_number, email))
    
    tools.create_button(
        frame, text="Submit",
        width=15, height=2,
        command=lambda: submit(
            root, frame, flat_number.get().strip(), 
            availability.get(), for_rent.get(), 
            owner_name.get().strip(), tenant_name.get().strip(),
            phone_number.get().strip(), email.get().strip()
        )
    ).place(x=645, y=526)
    tools.create_button(
        frame, text="Quit", 
        width=15, height=2,
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=500, y=526)

def change_state(availability, for_rent, tenant_name, owner_name, phone_number, email):
    owner_state = "normal" if for_rent or (not availability) else "disabled"
    rent_state = "normal" if for_rent and (not availability) else "disabled"

    tenant_name.config(state=rent_state)
    owner_name.config(state=owner_state)
    phone_number.config(state=owner_state)
    email.config(state=owner_state)

def submit(root, frame, *args) -> None:
    success = database.add_flat(*args)
    if success == 1: tk.messagebox.showerror("Invalid data", "Flat number cannot be empty")
    elif success == 2: tk.messagebox.showerror("Invalid data", f"Flat {args[0]} already exists")
    elif success == 3: tk.messagebox.showerror("Invalid data", "Empty owner name for owned house")
    elif success == 4: tk.messagebox.showerror("Invalid data", "Invalid phone number")
    elif success == 5: tk.messagebox.showerror("Invalid data", "Invalid email")
    elif success == 6: tk.messagebox.showerror("Invalid data", "Empty tenant name for rented house")
    elif success == 7: tk.messagebox.showerror("Invalid data", "Phone number already exists")
    elif success == 8: tk.messagebox.showerror("Invalid data", "Email already exists")
    else: 
        tk.messagebox.showinfo("Success", f"Flat {args[0]} added successfully")
        tools.switch_frame(root, frame, pages.dashboard.page)
