import tkinter as tk, tools, database, pages.dashboard

def page(root: tk.Tk):
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    
    tools.insert_bgimage(frame, "./assets/edit_owner.png")
    owner_name = tools.create_entry(frame, 220, 280)
    
    tools.create_button(
        frame, text="Submit", width=15, height=2,
        command=lambda: check(root, frame, owner_name.get().strip())
    ).place(x=645, y=526)
    tools.create_button(
        frame, text="Quit", width=15, height=2,
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=500, y=526)

def check(root, frame, owner_name):
    owner = database.get_owner(owner_name)
    if owner is None: 
        tk.messagebox.showerror("Owner doesn't exist", f"Owner {owner_name} not found")
    else:
        tools.switch_frame(root, frame, edit_information, owner)
    
def edit_information(root, owner):
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    
    tools.insert_bgimage(frame, "./assets/edit_owner2.png")
    owner_name = tools.create_entry(frame, 220, 280)
    owner_name.insert(tk.END, owner[0])
    
    phno = tools.create_entry(frame, 220, 335)
    phno.insert(tk.END, owner[1])
    
    email = tools.create_entry(frame, 220, 388)
    email.insert(tk.END, owner[2])
    
    tools.create_button(
        frame, text="Submit", 
        width=15, height=2,
        command=lambda: update(
            root, frame, 
            (owner_name.get().strip(), phno.get().strip(), email.get().strip()), 
            owner
        )
    ).place(x=645, y=526)
    tools.create_button(
        frame, text="Quit", width=15, height=2,
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=500, y=526)

def update(root, frame, new_owner_info, old_owner_info):
    success = database.update_owner(old_owner_info, new_owner_info)
    if success == 1: tk.messagebox.showerror("Invalid detail", "Invalid phone number")
    elif success == 2: tk.messagebox.showerror("Invalid detail", "Invalid email")
    elif success == 3: tk.messagebox.showerror("Invalid data", "Phone number already exists")
    elif success == 4: tk.messagebox.showerror("Invalid data", "Email already exists")
    else:
        tk.messagebox.showinfo("Updated information", "Information Updated successfully")
        tools.switch_frame(root, frame, pages.dashboard.page)
