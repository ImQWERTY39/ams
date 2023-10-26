import tkinter as tk
from tkinter import ttk
from constants import *
import functions
from classes import FlatInfo


def display_flats(root: tk.Frame, table_one: dict):
    display_flat_frame = tk.Frame(
        root,
        bg=BACKGROUND_COLOUR,
        width=SCREEN_WIDTH,
        height=SCREEN_HEIGHT,
    )
    display_flat_frame.place(x=0, y=0)

    heading = tk.Label(
        display_flat_frame,
        text="Display flats",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("boulder", 32),
    )
    heading.place(x=280, y=25)

    columns = ("col1", "col2", "col3", "col4", "col5")
    tree = ttk.Treeview(display_flat_frame, columns=columns, show="headings", height=15)

    tree.column("col1", anchor=tk.CENTER, width=SCREEN_WIDTH // 5)
    tree.heading("col1", text="Flat No.")

    tree.column("col2", anchor=tk.CENTER, width=SCREEN_WIDTH // 5)
    tree.heading("col2", text="Availability")

    tree.column("col3", anchor=tk.CENTER, width=SCREEN_WIDTH // 5)
    tree.heading("col3", text="On Rent")

    tree.column("col4", width=SCREEN_WIDTH // 5)
    tree.heading("col4", text="Owner Name")

    tree.column("col5", width=SCREEN_WIDTH // 5)
    tree.heading("col5", text="Tenant Name")

    flats_info: list[tuple] = list()

    for flat_number, flat_info in table_one.items():
        owner_name = flat_info.owner_name
        tenant_name = flat_info.tenant_name
        flats_info.append(
            (
                flat_number,
                flat_info.availability,
                flat_info.on_rent,
                owner_name if owner_name is not None else "NONE",
                tenant_name if tenant_name is not None else "NONE",
            )
        )

    for flats in flats_info:
        tree.insert("", tk.END, values=flats)

    tree.place(x=0, y=100)

    quit_button = tk.Button(
        display_flat_frame,
        text="Quit",
        relief="groove",
        command=lambda: functions.delete_frame(display_flat_frame),
    )
    quit_button.place(x=370, y=450)
