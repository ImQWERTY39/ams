import tkinter as tk, tools, database, pages.dashboard

def page(root: tk.Tk):
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    
    tools.insert_bgimage(frame, "./assets/buy_sell.png")
    flat_number = tools.create_entry(frame, 210, 280)
    
    tools.create_button(
        frame, text="Submit",
        width=15, height=2,
        command=lambda: try_modify(root, frame, flat_number.get())
    ).place(x=630, y=520)
    tools.create_button(
        frame, text="Quit", 
        width=15, height=2,
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=480, y=520)

def try_modify(root, frame, flat_number):
    flat = database.get_flat(flat_number)
    
    if flat is None: 
        tk.messagebox.showerror("Flat doesn't exist", f"Flat {flat_number} doesn't exist")
        return
    
    tools.switch_frame(root, frame, modify, flat)

def modify(root, flat):
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)

    tools.insert_bgimage(frame, "./assets/modify.png")
    tk.Label(frame, text=f"{flat[0]}", bg="white").place(x=250, y=280)
    availability = tools.create_checkbox(frame, 250, 340, flat[1])
    for_rent = tools.create_checkbox(frame, 250, 405, flat[2])
    tenant_name = tools.create_entry(frame, x=250, y=475)

    if flat[4] is not None:
        tenant_name.insert(0, flat[4])

    tools.create_button(
        frame, text="Submit",
        width=15, height=2,
        command=lambda: perf_modify(root, frame, flat, availability.get(), for_rent.get(), tenant_name.get())
    ).place(x=630, y=520)
    tools.create_button(
        frame, text="Quit", 
        width=15, height=2,
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=480, y=520)

def perf_modify(root, frame, flat, new_availability, new_for_rent, new_tenant):
    choice = tk.messagebox.askyesno(
        "Confirmation", "Are you sure you want to sell the flat?\nThis is an irreserable change")
    if not choice: return

    success = database.modify_flat(flat, new_availability, new_for_rent, new_tenant)
    if success == 1: tk.messagebox.showerror("Invalid detail", "Tenant name is empty")
    elif success == 2: tk.messagebox.showerror("Invalid detail", "Current options are for selling flat, consider going to 'Sell Flat' or recheck the selected options")
    else:
        tk.messagebox.showinfo("Information Updated", "Flat modified successfully")
        tools.switch_frame(root, frame, pages.dashboard.page)
