import tkinter as tk
from tkinter import messagebox

from classes import *
from constants import *
import functions
from functions import database


def page1(
    root: tk.Frame,
    table_one: dict[str, FlatInfo],
    table_two: dict[str, OwnerInfo],
):
    buy_flat_frame = tk.Frame(
        root,
        bg=BACKGROUND_COLOUR,
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT,
    )
    buy_flat_frame.place(x=0, y=0)

    heading = tk.Label(
        buy_flat_frame,
        text="Buy flat",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("boulder", 32),
    )
    heading.place(x=325, y=25)

    flat_number_label = tk.Label(
        buy_flat_frame,
        text="Enter flat number",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    flat_number_label.place(x=175, y=100)

    flat_number_entry = tk.Entry(buy_flat_frame, width=35)
    flat_number_entry.place(x=400, y=105)

    submit_button = tk.Button(
        buy_flat_frame,
        text="Submit",
        relief="groove",
        command=lambda: _page2(
            buy_flat_frame, table_one, table_two, flat_number_entry.get()
        ),
    )
    submit_button.place(x=350, y=450)

    quit_button = tk.Button(
        buy_flat_frame,
        text="Quit",
        relief="groove",
        command=lambda: functions.delete_frame(buy_flat_frame),
    )
    quit_button.place(x=425, y=450)


def _page2(
    buy_flat_frame: tk.Frame,
    table_one: dict[str, FlatInfo],
    table_two: dict[str, OwnerInfo],
    flat_number: str,
):
    if flat_number not in table_one:
        messagebox.showerror(
            "Flat doesn't exist", f"Flat no. {flat_number} doesn't exist"
        )
        return

    flat = table_one[flat_number]

    if not flat.availability:
        messagebox.showerror(
            "Flat not for sale", f"Flat no. {flat_number} is already owned"
        )
        return

    if flat.on_rent:
        tenant_name_label = tk.Label(
            buy_flat_frame,
            text="Tenant's Name",
            bg=BACKGROUND_COLOUR,
            fg=FOREGROUND_COLOUR,
            font=("monospace", 18),
        )
        tenant_name_label.place(x=275, y=75)

        tenant_name_entry = tk.Entry(buy_flat_frame, width=15)
        tenant_name_entry.place(x=250, y=355)

        delete_button = tk.Button(
            buy_flat_frame,
            text="Delete",
            relief="groove",
            command=lambda: add_tenant(
                buy_flat_frame,
                table_one,
                table_two,
                flat_number,
                tenant_name_entry.get(),
            ),
        )
        delete_button.place(x=225, y=450)
    else:
        owner_name_label = tk.Label(
            buy_flat_frame,
            text="Owner's Name",
            bg=BACKGROUND_COLOUR,
            fg=FOREGROUND_COLOUR,
            font=("monospace", 18),
        )
        owner_name_label.place(x=30, y=150)

        owner_name_entry = tk.Entry(buy_flat_frame, width=15)
        owner_name_entry.place(x=250, y=155)

        phone_number_label = tk.Label(
            buy_flat_frame,
            text="Phone no.",
            bg=BACKGROUND_COLOUR,
            fg=FOREGROUND_COLOUR,
            font=("monospace", 18),
        )
        phone_number_label.place(x=425, y=150)

        phone_number_entry = tk.Entry(buy_flat_frame, width=15)
        phone_number_entry.place(x=600, y=155)

        email_label = tk.Label(
            buy_flat_frame,
            text="Email",
            bg=BACKGROUND_COLOUR,
            fg=FOREGROUND_COLOUR,
            font=("monospace", 18),
        )
        email_label.place(x=425, y=200)

        email_entry = tk.Entry(buy_flat_frame, width=15)
        email_entry.place(x=600, y=205)

        delete_button = tk.Button(
            buy_flat_frame,
            text="Buy",
            relief="groove",
            command=lambda: add_owner_info(
                buy_flat_frame,
                table_one,
                table_two,
                flat_number,
                owner_name_entry.get(),
                phone_number_entry.get(),
                email_entry.get(),
            ),
        )
        delete_button.place(x=225, y=450)


def add_tenant(
    buy_flat_frame: tk.Tk,
    table_one: dict[str, FlatInfo],
    table_two: dict[str, OwnerInfo],
    flat_number: str,
    tenant_name: str,
):
    if not tenant_name:
        messagebox.showerror("No Name", "Enter a name")
        return

    table_one[flat_number].availability = False
    table_one[flat_number].tenant_name = tenant_name

    messagebox.showinfo("Flat on rent", f"Flat {flat_number} is now on rent")
    functions.delete_frame(buy_flat_frame)
    database.write_tables(table_one, table_two)


def add_owner_info(
    buy_flat_frame: tk.Tk,
    table_one: dict[str, FlatInfo],
    table_two: dict[str, OwnerInfo],
    flat_number: str,
    owner_name: str,
    phone_number: str,
    email: str,
):
    if not owner_name:
        messagebox.showerror("No Name", "Enter a name")
        return

    if not functions.is_valid_email(email):
        messagebox.showerror("Invalid Email", "")
        return

    if not functions.is_valid_phone_number(phone_number):
        messagebox.showerror("Invalid no.", "")
        return

    table_one[flat_number].availability = False
    table_one[flat_number].owner_name = owner_name

    owner_name = table_one[flat_number].owner_name

    if owner_name in table_two:
        table_two[owner_name].flats_owned.append(flat_number)
    else:
        table_two[owner_name] = OwnerInfo(phone_number, email, [flat_number])

    messagebox.showinfo("Flat on rent", f"Flat {flat_number} is bought")
    functions.delete_frame(buy_flat_frame)
    database.write_tables(table_one, table_two)
