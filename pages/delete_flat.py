import tkinter as tk, tools, database, pages.dashboard

def page(root: tk.Tk):
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    
    tools.insert_bgimage(frame, "./assets/delete.png")
    flat_number = tools.create_entry(frame, 210, 280)
    
    tools.create_button(
        frame, text="Submit", 
        command=lambda: check_delete(root, frame, flat_number.get())
    ).place(x=670, y=525)
    tools.create_button(
        frame, text="Quit", 
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=525, y=525)

def check_delete(root, frame, flat_number):
    flat = database.get_flat(flat_number)
    if flat is None: 
        tk.messagebox.showerror("Flat doesn't exist", f"Flat {flat_number} doesn't exist")
        return

    tools.switch_frame(root, frame, delete, flat)

def delete(root, flat):
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    
    tools.insert_bgimage(frame, "./assets/delete.png")
    tk.Label(frame, text=f"{flat[0]}").place(x=250, y=280)
    tk.Label(frame, text=f"{bool(flat[1])}").place(x=250, y=340)
    tk.Label(frame, text=f"{bool(flat[2])}").place(x=250, y=405)
    tk.Label(frame, text=f"{flat[3]}").place(x=550, y=340)
    tk.Label(frame, text=f"{flat[4]}").place(x=550, y=405)
    
    tools.create_button(
        frame, text="Delete", 
        command=lambda: perf_delete(root, frame, flat)
    ).place(x=670, y=525)
    tools.create_button(
        frame, text="Quit", 
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=525, y=525)

def perf_delete(root, frame, flat):
    choice = tk.messagebox.askyesno(
        "Confirmation", "Are you sure you want to sell the flat?\nThis is an irreserable change")
    if not choice: return

    deleted_owner = database.delete_flat(flat)
    if deleted_owner is not None: 
        tk.messagebox.showinfo("Deleted Owner Information", f"Deleted {deleted_owner[0]}'s information'")

    tk.messagebox.showinfo("Deleted flat", f"Deleted flat {flat[0]}")
    tools.switch_frame(root, frame, pages.dashboard.page)
