import tkinter as tk
from tkinter import messagebox

from constants import *
import functions
from functions import database
from classes import FlatInfo, OwnerInfo


def page1(root: tk.Frame, table_one: dict, table_two: dict):
    modify_flat_frame = tk.Frame(
        root,
        bg=BACKGROUND_COLOUR,
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT,
    )
    modify_flat_frame.place(x=0, y=0)

    heading = tk.Label(
        modify_flat_frame,
        text="Modify flat",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("boulder", 32),
    )
    heading.place(x=310, y=25)

    flat_number_label = tk.Label(
        modify_flat_frame,
        text="Enter flat number",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    flat_number_label.place(x=200, y=100)

    flat_number_entry = tk.Entry(modify_flat_frame, width=35)
    flat_number_entry.place(x=400, y=105)

    submit_button = tk.Button(
        modify_flat_frame,
        text="Submit",
        relief="groove",
        command=lambda: _page2(
            root,
            modify_flat_frame,
            flat_number_entry.get().strip(),
            table_one,
            table_two,
        ),
    )
    submit_button.bind("<Return>", lambda _: submit_button.invoke())
    submit_button.place(x=350, y=450)

    quit_button = tk.Button(
        modify_flat_frame,
        text="Quit",
        relief="groove",
        command=lambda: functions.delete_frame(modify_flat_frame),
    )
    quit_button.bind("<Return>", lambda _: quit_button.invoke())
    quit_button.place(x=425, y=450)


def _page2(
    root: tk.Frame,
    modify_flat_frame: tk.Frame,
    flat_number: str,
    table_one: dict,
    table_two: dict,
):
    if flat_number not in table_one:
        messagebox.showerror(
            "Flat doesn't exist", f"Flat no. {flat_number} doesn't exist"
        )
        return

    functions.delete_frame(modify_flat_frame)

    old_flat_info = table_one[flat_number]
    old_owner_info = (
        table_two[old_flat_info.owner_name] if old_flat_info.owner_name else None
    )

    modify_flat_frame = tk.Frame(
        root,
        bg=BACKGROUND_COLOUR,
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT,
    )
    modify_flat_frame.place(x=0, y=0)

    heading = tk.Label(
        modify_flat_frame,
        text="Enter flat details",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("boulder", 32),
    )
    heading.place(x=260, y=25)

    flat_number_label = tk.Label(
        modify_flat_frame,
        text="Flat number",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    flat_number_label.place(x=25, y=150)

    flat_number_entry = tk.Entry(modify_flat_frame, width=15)
    flat_number_entry.insert(0, flat_number)
    flat_number_entry.place(x=250, y=155)

    availability_label = tk.Label(
        modify_flat_frame,
        text="Availability",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    availability_label.place(x=25, y=200)

    availability_option = tk.BooleanVar()
    availability_checkbox = tk.Checkbutton(
        modify_flat_frame,
        variable=availability_option,
        onvalue=True,
        offvalue=False,
        bg=BACKGROUND_COLOUR,
        activebackground=BACKGROUND_COLOUR,
    )
    availability_checkbox.place(x=250, y=205)

    if old_flat_info.availability:
        availability_checkbox.toggle()

    on_rent_label = tk.Label(
        modify_flat_frame,
        text="For rent",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    on_rent_label.place(x=25, y=250)

    on_rent_option = tk.BooleanVar()
    on_rent_checkbox = tk.Checkbutton(
        modify_flat_frame,
        variable=on_rent_option,
        onvalue=True,
        offvalue=False,
        bg=BACKGROUND_COLOUR,
        activebackground=BACKGROUND_COLOUR,
    )
    on_rent_checkbox.place(x=250, y=255)

    if old_flat_info.on_rent:
        on_rent_checkbox.toggle()

    owner_name_label = tk.Label(
        modify_flat_frame,
        text="Owner's Name",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    owner_name_label.place(x=25, y=300)

    owner_name_entry = tk.Entry(modify_flat_frame, width=15)
    owner_name_entry.insert(
        0, old_flat_info.owner_name if old_flat_info.owner_name else ""
    )
    owner_name_entry.place(x=250, y=305)

    tenant_name_label = tk.Label(
        modify_flat_frame,
        text="Tenant's Name",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    tenant_name_label.place(x=25, y=350)

    tenant_name_entry = tk.Entry(modify_flat_frame, width=15)
    tenant_name_entry.insert(
        0, old_flat_info.tenant_name if old_flat_info.tenant_name else ""
    )
    tenant_name_entry.place(x=250, y=355)

    phone_number_label = tk.Label(
        modify_flat_frame,
        text="Phone no.",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    phone_number_label.place(x=425, y=150)

    phone_number_entry = tk.Entry(modify_flat_frame, width=15)
    phone_number_entry.insert(0, old_owner_info.phone_number if old_owner_info else "")
    phone_number_entry.place(x=600, y=155)

    email_label = tk.Label(
        modify_flat_frame,
        text="Email",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    email_label.place(x=425, y=200)

    email_entry = tk.Entry(modify_flat_frame, width=15)
    email_entry.insert(0, old_owner_info.email if old_owner_info else "")
    email_entry.place(x=600, y=205)

    quit_button = tk.Button(
        modify_flat_frame,
        text="Quit",
        relief="groove",
        command=lambda: functions.delete_frame(modify_flat_frame),
    )
    quit_button.bind("<Return>", lambda _: quit_button.invoke())
    quit_button.place(x=400, y=400)

    submit_button = tk.Button(
        modify_flat_frame,
        text="Submit",
        relief="groove",
        command=lambda: _update_details(
            modify_flat_frame,
            table_one,
            table_two,
            flat_number,
            old_flat_info,
            old_owner_info,
            flat_number_entry.get().strip(),
            availability_option.get(),
            on_rent_option.get(),
            owner_name_entry.get().strip(),
            tenant_name_entry.get().strip(),
            phone_number_entry.get().strip(),
            email_entry.get().strip(),
        ),
    )
    submit_button.bind("<Return>", lambda _: submit_button.invoke())
    submit_button.place(x=500, y=400)


def _update_details(
    modify_flat_frame: tk.Frame,
    table_one: dict,
    table_two: dict,
    old_flat_number: str,
    old_flat_info: FlatInfo,
    old_owner_info: OwnerInfo,
    new_flat_number: str,
    new_availability: bool,
    new_on_rent: bool,
    new_owner_name: str,
    new_tenant_name: str,
    new_phone_number: str,
    new_email: str,
):
    owned = new_on_rent or (not new_availability)
    rented = new_on_rent and (not new_availability)

    if new_flat_number == "":
        messagebox.showerror("Invalid flat number", "Please enter a flat number")
        return

    new_flat_info = FlatInfo(
        new_availability, new_on_rent, new_owner_name, new_tenant_name
    )
    new_owner_info = OwnerInfo(new_phone_number, new_email, [new_flat_number])

    if new_flat_number == "":
        messagebox.showerror("Invalid flat number", "Please enter a flat number")
        return

    if new_flat_number in table_one and new_flat_number != old_flat_number:
        if not messagebox.askyesno(
            "Flat number already exists",
            f"Flat number already exists. Are you sure you editing the flat details of {new_flat_number}?",
        ):
            return

    if new_owner_name == "" and owned:
        messagebox.showerror(
            "Invalid name",
            "Owner name cannot be empty for an owned house",
        )
        return

    if not functions.is_valid_phone_number(new_phone_number) and owned:
        messagebox.showerror(
            "Invalid phone number",
            "Phone number must contain 10 numeric character only",
        )
        return

    if not functions.is_valid_email(new_email) and owned:
        messagebox.showerror(
            "Invalid email address",
            "The email address must contain a username and domain separated with '@'",
        )
        return

    if new_tenant_name == "" and rented:
        messagebox.showerror(
            "Invalid name",
            "Tenant name cannot be empty for a rented house that is not available",
        )

    del table_one[old_flat_number]
    if old_flat_info.owner_name:
        del table_two[old_flat_info.owner_name]

    if old_owner_info and owned:
        if old_flat_number == new_flat_number:
            new_owner_info.flats_owned = old_owner_info.flats_owned
        else:
            other_flats = old_owner_info.flats_owned
            other_flats.remove(old_flat_number)
            new_owner_info.flats_owned.extend(other_flats)

    new_owner_info.flats_owned = list(set(new_owner_info.flats_owned))

    table_one[new_flat_number] = new_flat_info

    if owned:
        table_two[new_owner_name.upper()] = new_owner_info

    database.write_tables(table_one, table_two)
    messagebox.showinfo(
        "Flat modified successfully",
        f"Flat no. {new_flat_number} has been modified successfully",
    )
    functions.delete_frame(modify_flat_frame)
