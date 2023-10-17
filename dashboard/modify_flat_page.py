import tkinter as tk
from tkinter import messagebox

import constants
import functions
from functions import database
from classes import FlatInfo, OwnerInfo


def page1(
    root: tk.Frame, table_one: dict[str, FlatInfo], table_two: dict[str, OwnerInfo]
):
    modify_flat_frame = tk.Frame(
        root,
        bg=constants.BACKGROUND_COLOUR,
        width=constants.SCREEN_WIDTH,
        height=constants.SCREEN_HEIGHT,
    )
    modify_flat_frame.place(x=0, y=0)

    heading = tk.Label(
        modify_flat_frame,
        text="Modify flat",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("boulder", 32),
    )
    heading.place(x=280, y=25)

    flat_number_label = tk.Label(
        modify_flat_frame,
        text="Enter flat number",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    flat_number_label.place(x=200, y=100)

    flat_number_entry = tk.Entry(modify_flat_frame, width=35)
    flat_number_entry.place(x=400, y=105)

    submit_button = tk.Button(
        modify_flat_frame,
        text="Submit",
        relief="groove",
        command=lambda: page2(
            root,
            modify_flat_frame,
            flat_number_entry.get().strip(),
            table_one,
            table_two,
        ),
    )
    submit_button.place(x=350, y=145)

    quit_button = tk.Button(
        modify_flat_frame,
        text="Quit",
        relief="groove",
        command=lambda: functions.delete_frame(modify_flat_frame),
    )
    quit_button.place(x=425, y=450)


def page2(
    root: tk.Frame,
    modify_flat_frame: tk.Frame,
    flat_number: str,
    table_one: dict[str, FlatInfo],
    table_two: dict[str, OwnerInfo],
):
    if not table_one.__contains__(flat_number):
        messagebox.showerror(
            "Flat doesn't exist", f"Flat no. {flat_number} doesn't exist"
        )
        return

    functions.delete_frame(modify_flat_frame)

    modify_flat_frame = tk.Frame(
        root,
        bg=constants.BACKGROUND_COLOUR,
        width=constants.SCREEN_WIDTH,
        height=constants.SCREEN_HEIGHT,
    )
    modify_flat_frame.place(x=0, y=0)

    heading = tk.Label(
        modify_flat_frame,
        text="Change flat details",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("boulder", 32),
    )
    heading.place(x=260, y=25)

    flat_number_label = tk.Label(
        modify_flat_frame,
        text="Flat number",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    flat_number_label.place(x=25, y=150)

    flat_number_entry = tk.Entry(modify_flat_frame, width=15)
    flat_number_entry.insert(0, flat_number)
    flat_number_entry.place(x=250, y=155)

    availability_label = tk.Label(
        modify_flat_frame,
        text="Availability",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    availability_label.place(x=25, y=200)

    availability_option = tk.BooleanVar()
    availability_checkbox = tk.Checkbutton(
        modify_flat_frame,
        variable=availability_option,
        onvalue=True,
        offvalue=False,
        bg=constants.BACKGROUND_COLOUR,
        activebackground=constants.BACKGROUND_COLOUR,
    )
    availability_checkbox.place(x=250, y=205)

    if table_one[flat_number].availability:
        availability_checkbox.toggle()

    on_rent_label = tk.Label(
        modify_flat_frame,
        text="For rent",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    on_rent_label.place(x=25, y=250)

    on_rent_option = tk.BooleanVar()
    on_rent_checkbox = tk.Checkbutton(
        modify_flat_frame,
        variable=on_rent_option,
        onvalue=True,
        offvalue=False,
        bg=constants.BACKGROUND_COLOUR,
        activebackground=constants.BACKGROUND_COLOUR,
    )
    on_rent_checkbox.place(x=250, y=255)

    if table_one[flat_number].on_rent:
        on_rent_checkbox.toggle()

    owner_name = table_one[flat_number].owner_name
    tenant_name = table_one[flat_number].tenant_name

    owner_name_label = tk.Label(
        modify_flat_frame,
        text="Owner's Name",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    owner_name_label.place(x=25, y=300)

    owner_name_entry = tk.Entry(modify_flat_frame, width=15)
    owner_name_entry.insert(0, owner_name if owner_name is not None else "")
    owner_name_entry.place(x=250, y=305)

    tenant_name_label = tk.Label(
        modify_flat_frame,
        text="Tenant's Name",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    tenant_name_label.place(x=25, y=350)

    tenant_name_entry = tk.Entry(modify_flat_frame, width=15)
    tenant_name_entry.insert(0, tenant_name if tenant_name is not None else "")
    tenant_name_entry.place(x=250, y=355)

    if tenant_name is not None:
        pass

    phone_number_label = tk.Label(
        modify_flat_frame,
        text="Phone no.",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    phone_number_label.place(x=425, y=150)

    phone_number_entry = tk.Entry(modify_flat_frame, width=15)
    phone_number_entry.insert(0, table_two[owner_name].phone_number)
    phone_number_entry.place(x=600, y=155)

    email_label = tk.Label(
        modify_flat_frame,
        text="Email",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    email_label.place(x=425, y=200)

    email_entry = tk.Entry(modify_flat_frame, width=15)
    email_entry.insert(0, table_two[owner_name].email)
    email_entry.place(x=600, y=205)

    quit_button = tk.Button(
        modify_flat_frame,
        text="Quit",
        relief="groove",
        command=lambda: functions.delete_frame(modify_flat_frame),
    )
    quit_button.place(x=400, y=400)

    submit_button = tk.Button(
        modify_flat_frame,
        text="Submit",
        relief="groove",
        command=lambda: submit_details(
            modify_flat_frame,
            table_one,
            table_two,
            flat_number,
            flat_number_entry.get().strip(),
            availability_option.get(),
            on_rent_option.get(),
            owner_name,
            owner_name_entry.get().strip().upper(),
            tenant_name_entry.get().strip().upper(),
            phone_number_entry.get().strip(),
            email_entry.get().strip(),
        ),
    )
    submit_button.place(x=500, y=400)


def submit_details(
    modify_flat_frame: tk.Frame,
    table_one: dict[str, FlatInfo],
    table_two: dict[str, OwnerInfo],
    flat_number_old: str,
    flat_number_new: str,
    availability: bool,
    on_rent: bool,
    owner_name_old: str,
    owner_name_new: str,
    tenant_name: str,
    phone_number: str,
    email: str,
):
    if not is_valid_phone_number(phone_number):
        messagebox.showerror(
            "Invalid phone number",
            "Phone number must contain 10 numeric character only",
        )
        return

    if not is_valid_email(email):
        messagebox.showerror(
            "Invalid email address",
            "The email address must contain a username and domain separated with '@'",
        )
        return

    if flat_number_new == "":
        messagebox.showerror("Invalid flat number", "Please enter a flat number")
        return

    flat_info = FlatInfo(availability, on_rent, owner_name_new, tenant_name)
    owner_info = OwnerInfo(phone_number, email, table_two[owner_name_old].flats_owned)

    if flat_number_old != flat_number_new:
        del table_one[flat_number_old]
        owner_info.flats_owned.remove(flat_number_old)
        owner_info.flats_owned.append(flat_number_new)

    if owner_name_old != owner_name_new:
        del table_two[owner_name_old]

    table_one[flat_number_new] = flat_info
    table_two[owner_name_new] = owner_info

    database.write_tables(table_one, table_two)
    messagebox.showinfo(
        "Flat added successfully",
        f"Flat no. {flat_number_new} has been modified successfully",
    )
    functions.delete_frame(modify_flat_frame)


def is_valid_phone_number(phone_number: str) -> bool:
    for i in phone_number:
        if not (48 <= ord(i) <= 57):
            return False

    return len(phone_number) == 10


def is_valid_email(email: str) -> bool:
    email_split = email.split("@")
    return len(email_split) == 2
