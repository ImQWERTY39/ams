import tkinter as tk
from tkinter import messagebox

from constants import *
import functions
from functions import database


def delete_flat_page(root: tk.Frame, table_one: dict, table_two: dict):
    delete_flat_frame = tk.Frame(
        root,
        bg=BACKGROUND_COLOUR,
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT,
    )
    delete_flat_frame.place(x=0, y=0)

    heading = tk.Label(
        delete_flat_frame,
        text="Delete flat",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("boulder", 32),
    )
    heading.place(x=280, y=25)

    flat_number_label = tk.Label(
        delete_flat_frame,
        text="Enter flat number",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    flat_number_label.place(x=200, y=100)

    flat_number_entry = tk.Entry(delete_flat_frame, width=35)
    flat_number_entry.place(x=400, y=105)

    submit_button = tk.Button(
        delete_flat_frame,
        text="Submit",
        relief="groove",
        command=lambda: _show_flat_and_owner_details(
            flat_number_entry.get().strip(), table_one, table_two, delete_flat_frame
        ),
    )
    submit_button.bind("<Return>", lambda _: submit_button.invoke())
    submit_button.place(x=350, y=145)

    quit_button = tk.Button(
        delete_flat_frame,
        text="Quit",
        relief="groove",
        command=lambda: functions.delete_frame(delete_flat_frame),
    )
    quit_button.bind("<Return>", lambda _: quit_button.invoke())
    quit_button.place(x=425, y=450)


def _show_flat_and_owner_details(
    flat_number: str,
    table_one: dict,
    table_two: dict,
    delete_flat_frame: tk.Frame,
):
    if flat_number not in table_one:
        messagebox.showerror(
            "Flat doesn't exist", f"Flat no. {flat_number} doesn't exist"
        )
        return

    flat_info = table_one[flat_number]
    owner_info = table_two[flat_info.owner_name] if flat_info.owner_name else None

    details = tk.Label(
        delete_flat_frame,
        text=f"""\
Flat Number: {flat_number}\t\tOwner Name: {flat_info.owner_name}
Availability: {flat_info.availability}\t\tPhone Number: {owner_info.phone_number if owner_info else None}
On Rent: {flat_info.on_rent}\t\tEmail: {owner_info.email if owner_info else None}
Tenant Name: {flat_info.tenant_name}""",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
        anchor="w",
        justify="left",
    )

    details.place(x=50, y=250)

    delete_button = tk.Button(
        delete_flat_frame,
        text="Delete",
        relief="groove",
        command=lambda: delete_flat(
            flat_number, table_one, table_two, delete_flat_frame
        ),
    )
    delete_button.bind("<Return>", lambda _: delete_button.invoke())
    delete_button.place(x=225, y=450)


def delete_flat(
    flat_number: str,
    table_one: dict,
    table_two: dict,
    delete_flat_frame: tk.Frame,
):
    if not messagebox.askyesno(
        "Deleting flat", "This is an irreversible change, are you sure?"
    ):
        return

    owner_name = table_one[flat_number].owner_name
    del table_one[flat_number]

    if owner_name:
        table_two[owner_name].flats_owned.remove(flat_number)

        if len(table_two[owner_name].flats_owned) == 0:
            del table_two[owner_name]

            messagebox.showinfo(
                "Owner name removed successfully",
                f"Owner name {owner_name} has been removed due to them owning 0 flats",
            )

    database.write_tables(table_one, table_two)

    messagebox.showinfo(
        "Flat no. removed successfully", f"Flat no. {flat_number} have been removed"
    )

    functions.delete_frame(delete_flat_frame)
