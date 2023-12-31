import tkinter as tk
from tkinter import messagebox

from constants import *
from classes import *
import functions
from functions import database


def page1(
    root: tk.Frame,
    table_one: dict,
    table_two: dict,
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
        text="Sell flat",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("boulder", 32),
    )
    heading.place(x=310, y=25)

    flat_number_label = tk.Label(
        buy_flat_frame,
        text="Enter flat number",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    flat_number_label.place(x=200, y=100)

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
    submit_button.bind("<Return>", lambda _: submit_button.invoke())
    submit_button.place(x=350, y=450)

    quit_button = tk.Button(
        buy_flat_frame,
        text="Quit",
        relief="groove",
        command=lambda: functions.delete_frame(buy_flat_frame),
    )
    quit_button.bind("<Return>", lambda _: quit_button.invoke())
    quit_button.place(x=425, y=450)


def _page2(
    buy_flat_frame: tk.Frame,
    table_one: dict,
    table_two: dict,
    flat_number: str,
):
    if flat_number not in table_one:
        messagebox.showerror(
            "Flat doesn't exist", f"Flat no. {flat_number} doesn't exist"
        )
        return

    flat_info = table_one[flat_number]
    owner_info = table_two[flat_info.owner_name]
    owned = flat_info.on_rent or (not flat_info.availability)

    if not owned:
        messagebox.showerror("Flat for sale", f"Flat no. {flat_number} is not owned")
        return

    info_label = tk.Label(
        buy_flat_frame,
        text=f"""\
Flat number: {flat_number}\t\tOwner name: {flat_info.owner_name}
Availability: {flat_info.availability}\t\tPhone number: {owner_info.phone_number}
On Rent: {flat_info.on_rent}\t\tEmail: {owner_info.email}
Tenant name: {flat_info.tenant_name}\t\tFlat's owned: {owner_info.flats_owned}""",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 12),
        anchor=tk.W,
        justify="left",
    )
    info_label.place(x=50, y=250)

    delete_button = tk.Button(
        buy_flat_frame,
        text="Sell",
        relief="groove",
        command=lambda: _sell_flat(buy_flat_frame, table_one, table_two, flat_number),
    )
    delete_button.bind("<Return>", lambda _: delete_button.invoke())
    delete_button.place(x=300, y=450)


def _sell_flat(
    buy_flat_frame: tk.Frame,
    table_one: dict,
    table_two: dict,
    flat_number: str,
):
    if not messagebox.askyesno(
        "Selling flat", "This is an irreversible change, are you sure?"
    ):
        return

    flat_info = table_one[flat_number]
    owner_name = flat_info.owner_name
    table_two[owner_name].flats_owned.remove(flat_number)

    if len(table_two[owner_name].flats_owned) == 0:
        del table_two[owner_name]

        messagebox.showinfo(
            "Owner name removed successfully",
            f"Owner name {owner_name} has been removed due to them owning 0 flats",
        )

    table_one[flat_number] = FlatInfo(flat_info.availability, False, None, None)

    database.write_tables(table_one, table_two)
    messagebox.showinfo(
        "Flat no. sold successfully", f"Flat no. {flat_number} has been sold"
    )
    functions.delete_frame(buy_flat_frame)
