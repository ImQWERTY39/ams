import tkinter as tk
from tkinter import messagebox

from constants import *
import functions
from functions import database
from classes import FlatInfo, OwnerInfo


def add_flat_page(
    root: tk.Frame,
    table_one: dict[str, FlatInfo],
    table_two: dict[str, OwnerInfo],
):
    add_flat_frame = tk.Frame(
        root,
        bg=BACKGROUND_COLOUR,
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT,
    )
    add_flat_frame.place(x=0, y=0)

    heading = tk.Label(
        add_flat_frame,
        text="Enter flat details",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("boulder", 32),
    )
    heading.place(x=260, y=25)

    flat_number_label = tk.Label(
        add_flat_frame,
        text="Flat number",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    flat_number_label.place(x=25, y=150)

    flat_number_entry = tk.Entry(add_flat_frame, width=15)
    flat_number_entry.place(x=250, y=155)

    availability_label = tk.Label(
        add_flat_frame,
        text="Availability",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    availability_label.place(x=25, y=200)

    availability_option = tk.BooleanVar()
    availability_checkbox = tk.Checkbutton(
        add_flat_frame,
        variable=availability_option,
        onvalue=True,
        offvalue=False,
        bg=BACKGROUND_COLOUR,
        activebackground=BACKGROUND_COLOUR,
    )
    availability_checkbox.place(x=250, y=205)

    on_rent_label = tk.Label(
        add_flat_frame,
        text="For rent",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    on_rent_label.place(x=25, y=250)

    on_rent_option = tk.BooleanVar()
    on_rent_checkbox = tk.Checkbutton(
        add_flat_frame,
        variable=on_rent_option,
        onvalue=True,
        offvalue=False,
        bg=BACKGROUND_COLOUR,
        activebackground=BACKGROUND_COLOUR,
    )
    on_rent_checkbox.place(x=250, y=255)

    owner_name_label = tk.Label(
        add_flat_frame,
        text="Owner's Name",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    owner_name_label.place(x=25, y=300)

    owner_name_entry = tk.Entry(add_flat_frame, width=15)
    owner_name_entry.place(x=250, y=305)

    tenant_name_label = tk.Label(
        add_flat_frame,
        text="Tenant's Name",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    tenant_name_label.place(x=25, y=350)

    tenant_name_entry = tk.Entry(add_flat_frame, width=15)
    tenant_name_entry.place(x=250, y=355)

    phone_number_label = tk.Label(
        add_flat_frame,
        text="Phone no.",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    phone_number_label.place(x=425, y=150)

    phone_number_entry = tk.Entry(add_flat_frame, width=15)
    phone_number_entry.place(x=600, y=155)

    email_label = tk.Label(
        add_flat_frame,
        text="Email",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    email_label.place(x=425, y=200)

    email_entry = tk.Entry(add_flat_frame, width=15)
    email_entry.place(x=600, y=205)

    quit_button = tk.Button(
        add_flat_frame,
        text="Quit",
        relief="groove",
        command=lambda: functions.delete_frame(add_flat_frame),
    )
    quit_button.place(x=400, y=400)

    submit_button = tk.Button(
        add_flat_frame,
        text="Submit",
        relief="groove",
        command=lambda: submit_details(
            add_flat_frame,
            table_one,
            table_two,
            flat_number_entry.get().strip(),
            availability_option.get(),
            on_rent_option.get(),
            owner_name_entry.get(),
            tenant_name_entry.get(),
            phone_number_entry.get(),
            email_entry.get().strip(),
        ),
    )
    submit_button.place(x=500, y=400)


def submit_details(
    add_flat_frame: tk.Frame,
    table_one: dict[str, FlatInfo],
    table_two: dict[str, OwnerInfo],
    flat_number: str,
    availability: bool,
    on_rent: bool,
    owner_name: str,
    tenant_name: str,
    phone_number: str,
    email: str,
):
    owned = on_rent or (not availability)
    rented = on_rent and (not availability)

    if not is_valid_phone_number(phone_number) and owned:
        messagebox.showerror(
            "Invalid phone number",
            "Phone number must contain 10 numeric character only",
        )
        return

    if not is_valid_email(email) and owned:
        messagebox.showerror(
            "Invalid email address",
            "The email address must contain a username and domain separated with '@'",
        )
        return

    if flat_number == "":
        messagebox.showerror("Invalid flat number", "Please enter a flat number")
        return

    if flat_number in table_one:
        messagebox.showerror(
            "Flat number already exists",
            "Flat number already exists. If you want to edit the information, go to 'Modify Flat Information' menu",
        )
        return

    table_one[flat_number] = FlatInfo(availability, on_rent, owner_name, tenant_name)

    if owner_name in table_two:
        table_two[owner_name].flats_owned.append(flat_number)
    elif owner_name:
        table_two[owner_name] = OwnerInfo(phone_number, email, [flat_number])

    database.write_tables(table_one, table_two)
    messagebox.showinfo(
        "Flat added successfully", f"Flat no. {flat_number} has been added successfully"
    )
    functions.delete_frame(add_flat_frame)


def is_valid_phone_number(phone_number: str) -> bool:
    for i in phone_number:
        if not (48 <= ord(i) <= 57):
            return False

    return len(phone_number) == 10


def is_valid_email(email: str) -> bool:
    email_split = email.split("@")
    return len(email_split) == 2
