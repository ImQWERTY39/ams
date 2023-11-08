import tkinter as tk
from tkinter import ttk

from constants import *
import functions


def display_flats(root: tk.Frame, table_one: dict, conditions: list = None):
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

    tree = ttk.Treeview(
        display_flat_frame,
        columns=("col1", "col2", "col3", "col4", "col5"),
        show="headings",
        height=15,
    )

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

    if conditions is None:
        flats_info = _get_all_flats(table_one)
    else:
        flats_info = _get_all_flats(table_one, *conditions)

    for flats in flats_info:
        tree.insert("", tk.END, values=flats)

    tree.place(x=0, y=100)

    filter_button = tk.Button(
        display_flat_frame,
        text="Filters",
        relief="groove",
        command=lambda: _get_filters(display_flat_frame, root, table_one),
    )
    filter_button.bind("<Return>", lambda _: filter_button.invoke())
    filter_button.place(x=300, y=450)

    quit_button = tk.Button(
        display_flat_frame,
        text="Quit",
        relief="groove",
        command=lambda: functions.delete_frame(display_flat_frame),
    )
    quit_button.bind("<Return>", lambda _: quit_button.invoke())
    quit_button.place(x=370, y=450)


def _get_all_flats(
    table_one: dict,
    check_owned_flats: bool = False,
    check_rented_flats: bool = False,
    check_all_available_flats: bool = False,
    check_non_rented_available_flats: bool = False,
    check_rented_available_flats: bool = False,
) -> list:
    flats_info = list()

    for flat_number, flat_info in table_one.items():
        owner_name = flat_info.owner_name
        tenant_name = flat_info.tenant_name

        owned = flat_info.on_rent or (not flat_info.availability)
        rented = flat_info.on_rent and (not flat_info.availability)

        if (
            (check_owned_flats and not owned)
            or (check_rented_flats and not rented)
            or (check_all_available_flats and not flat_info.availability)
            or (
                check_non_rented_available_flats
                and (flat_info.on_rent or not flat_info.availability)
            )
            or (
                check_rented_available_flats
                and not (flat_info.on_rent and flat_info.availability)
            )
        ):
            continue

        flats_info.append(
            (
                flat_number,
                flat_info.availability,
                flat_info.on_rent,
                owner_name if owner_name is not None else "NONE",
                tenant_name if tenant_name is not None else "NONE",
            )
        )

    return flats_info


def _get_filters(display_flat_frame: tk.Frame, root: tk.Frame, table_one: dict):
    check_owned_flats = tk.BooleanVar()
    check_rented_flats = tk.BooleanVar()
    check_all_available_flats = tk.BooleanVar()
    check_non_rented_available_flats = tk.BooleanVar()
    check_rented_available_flats = tk.BooleanVar()

    filters_frame = tk.Frame(
        display_flat_frame, bg=BACKGROUND_COLOUR, width=500, height=250
    )
    filters_frame.place(x=50, y=200)

    filter_option1_label = tk.Label(
        filters_frame,
        text="Owned flats: ",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    filter_option1_label.place(x=5, y=5)

    filter_option1_checkbox = tk.Checkbutton(
        filters_frame,
        variable=check_owned_flats,
        onvalue=True,
        offvalue=False,
        bg=BACKGROUND_COLOUR,
        activebackground=BACKGROUND_COLOUR,
    )
    filter_option1_checkbox.place(x=350, y=5)

    filter_option2_label = tk.Label(
        filters_frame,
        text="Rented flats: ",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    filter_option2_label.place(x=5, y=45)

    filter_option2_checkbox = tk.Checkbutton(
        filters_frame,
        variable=check_rented_flats,
        onvalue=True,
        offvalue=False,
        bg=BACKGROUND_COLOUR,
        activebackground=BACKGROUND_COLOUR,
    )
    filter_option2_checkbox.place(x=350, y=45)

    filter_option3_label = tk.Label(
        filters_frame,
        text="Available Flats (all): ",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    filter_option3_label.place(x=5, y=85)

    filter_option3_checkbox = tk.Checkbutton(
        filters_frame,
        variable=check_all_available_flats,
        onvalue=True,
        offvalue=False,
        bg=BACKGROUND_COLOUR,
        activebackground=BACKGROUND_COLOUR,
    )
    filter_option3_checkbox.place(x=350, y=85)

    filter_option4_label = tk.Label(
        filters_frame,
        text="Available Flats (not rented): ",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    filter_option4_label.place(x=5, y=125)

    filter_option4_checkbox = tk.Checkbutton(
        filters_frame,
        variable=check_non_rented_available_flats,
        onvalue=True,
        offvalue=False,
        bg=BACKGROUND_COLOUR,
        activebackground=BACKGROUND_COLOUR,
    )
    filter_option4_checkbox.place(x=350, y=125)

    filter_option5_label = tk.Label(
        filters_frame,
        text="Available Flats (rented): ",
        bg=BACKGROUND_COLOUR,
        fg=FOREGROUND_COLOUR,
        font=("monospace", 18),
    )
    filter_option5_label.place(x=5, y=165)

    filter_option5_checkbox = tk.Checkbutton(
        filters_frame,
        variable=check_rented_available_flats,
        onvalue=True,
        offvalue=False,
        bg=BACKGROUND_COLOUR,
        activebackground=BACKGROUND_COLOUR,
    )
    filter_option5_checkbox.place(x=350, y=165)

    refresh_button = tk.Button(
        filters_frame,
        text="Refresh",
        relief="groove",
        command=lambda: _refresh_search(
            filters_frame,
            display_flat_frame,
            root,
            table_one,
            check_owned_flats.get(),
            check_rented_flats.get(),
            check_all_available_flats.get(),
            check_non_rented_available_flats.get(),
            check_rented_available_flats.get(),
        ),
    )
    refresh_button.bind("<Return>", lambda _: refresh_button.invoke())
    refresh_button.place(x=400, y=100)


def _refresh_search(
    filters_frame: tk.Frame,
    display_flat_frame: tk.Frame,
    root: tk.Frame,
    table_one: dict,
    check_owned_flats: bool,
    check_rented_flats: bool,
    check_all_available_flats: bool,
    check_non_rented_available_flats: bool,
    check_rented_available_flats: bool,
):
    functions.delete_frame(filters_frame)
    functions.delete_frame(display_flat_frame)

    display_flats(
        root,
        table_one,
        [
            check_owned_flats,
            check_rented_flats,
            check_all_available_flats,
            check_non_rented_available_flats,
            check_rented_available_flats,
        ],
    )
