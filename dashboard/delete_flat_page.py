import tkinter as tk
from tkinter import messagebox
import constants
import functions
from functions import database
from classes import FlatInfo, OwnerInfo


def delete_flat_page(
    root: tk.Frame, table_one: dict[str, FlatInfo], table_two: dict[str, OwnerInfo]
):
    delete_flat_frame = tk.Frame(
        root,
        bg=constants.BACKGROUND_COLOUR,
        width=constants.SCREEN_WIDTH,
        height=constants.SCREEN_HEIGHT,
    )
    delete_flat_frame.place(x=0, y=0)

    heading = tk.Label(
        delete_flat_frame,
        text="Delete flat",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("boulder", 32),
    )
    heading.place(x=280, y=25)

    flat_number_label = tk.Label(
        delete_flat_frame,
        text="Enter flat number",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    flat_number_label.place(x=200, y=100)

    flat_number_entry = tk.Entry(delete_flat_frame, width=35)
    flat_number_entry.place(x=400, y=105)

    submit_button = tk.Button(
        delete_flat_frame,
        text="Submit",
        relief="groove",
        command=lambda: show_flat_and_owner_details(
            flat_number_entry.get().strip(), table_one, table_two, delete_flat_frame
        ),
    )
    submit_button.place(x=350, y=145)

    quit_button = tk.Button(
        delete_flat_frame,
        text="Quit",
        relief="groove",
        command=lambda: functions.delete_frame(delete_flat_frame),
    )
    quit_button.place(x=425, y=450)


def show_flat_and_owner_details(
    flat_number: str,
    table_one: dict[str, FlatInfo],
    table_two: dict[str, OwnerInfo],
    delete_flat_frame: tk.Frame,
):
    if not table_one.__contains__(flat_number):
        messagebox.showerror(
            "Flat doesn't exist", f"Flat no. {flat_number} doesn't exist"
        )
        return

    flat_info = table_one[flat_number]
    owner_info = table_two[flat_info.owner_name]

    info_label = tk.Label(
        delete_flat_frame,
        text=f"""\
Flat number: {flat_number}\t\tOwner name: {flat_info.owner_name}
Availability: {flat_info.availability}\t\tPhone number: {owner_info.phone_number}
On Rent: {flat_info.on_rent}\t\tEmail: {owner_info.email}
Tenant name: {flat_info.tenant_name}\t\tFlat's owned: {owner_info.flats_owned}""",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("monospace", 12),
        anchor=tk.W,
        justify="left",
    )
    info_label.place(x=50, y=250)

    delete_button = tk.Button(
        delete_flat_frame,
        text="Delete",
        relief="groove",
        command=lambda: delete_flat(
            flat_number, table_one, table_two, delete_flat_frame
        ),
    )
    delete_button.place(x=225, y=450)


def delete_flat(
    flat_number: str,
    table_one: dict[str, FlatInfo],
    table_two: dict[str, OwnerInfo],
    delete_flat_frame: tk.Frame,
):
    if not messagebox.askyesno(
        "Deleting flat", "This is an irreversible change, are you sure?"
    ):
        return

    owner_name = table_one[flat_number].owner_name
    del table_one[flat_number]

    if owner_name is not None:
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
