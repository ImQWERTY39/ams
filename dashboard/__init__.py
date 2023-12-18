import tkinter as tk

import home
import constants
import functions
from functions import database

from dashboard import (
    add_flat_page,
    modify_flat_page,
    delete_flat_page,
    display_flats_page,
    buy_flat_page,
    sell_flat_page,
)


def page(root: tk.Tk):
    table_one, table_two = database.load_tables()

    dashboard_frame = tk.Frame(
        root,
        width=constants.SCREEN_WIDTH,
        height=constants.SCREEN_HEIGHT,
        bg=constants.BACKGROUND_COLOUR,
    )
    dashboard_frame.place(x=0, y=0)

    heading = tk.Label(
        dashboard_frame,
        text="Dashboard",
        bg=constants.BACKGROUND_COLOUR,
        fg=constants.FOREGROUND_COLOUR,
        font=("palatino", 32),
    )
    heading.place(x=280, y=25)

    add_flat_button = tk.Button(
        dashboard_frame,
        text="Add flat",
        relief="groove",
        width=20,
        command=lambda: add_flat_page.add_flat_page(
            dashboard_frame, table_one, table_two
        ),
    )
    add_flat_button.bind("<Return>", lambda _: add_flat_button.invoke())
    add_flat_button.place(x=150, y=150)

    modify_flat_info_button = tk.Button(
        dashboard_frame,
        text="Modify flat information",
        relief="groove",
        width=20,
        command=lambda: modify_flat_page.page1(dashboard_frame, table_one, table_two),
    )
    modify_flat_info_button.bind("<Return>", lambda _: modify_flat_info_button.invoke())
    modify_flat_info_button.place(x=150, y=200)

    display_flat_button = tk.Button(
        dashboard_frame,
        text="Display flats",
        relief="groove",
        width=20,
        command=lambda: display_flats_page.display_flats(dashboard_frame, table_one),
    )
    display_flat_button.bind("<Return>", lambda _: display_flat_button.invoke())
    display_flat_button.place(x=150, y=250)

    delete_flat_button = tk.Button(
        dashboard_frame,
        text="Delete flat",
        relief="groove",
        width=20,
        command=lambda: delete_flat_page.delete_flat_page(
            dashboard_frame, table_one, table_two
        ),
    )
    delete_flat_button.bind("<Return>", lambda _: delete_flat_button.invoke())
    delete_flat_button.place(x=150, y=300)

    buy_flat_button = tk.Button(
        dashboard_frame,
        text="Buy flat",
        relief="groove",
        width=20,
        command=lambda: buy_flat_page.page1(dashboard_frame, table_one, table_two),
    )
    buy_flat_button.bind("<Return>", lambda _: buy_flat_button.invoke())
    buy_flat_button.place(x=450, y=150)

    sell_flat_button = tk.Button(
        dashboard_frame,
        text="Sell flat",
        relief="groove",
        width=20,
        command=lambda: sell_flat_page.page1(dashboard_frame, table_one, table_two),
    )
    sell_flat_button.bind("<Return>", lambda _: sell_flat_button.invoke())
    sell_flat_button.place(x=450, y=200)

    quit_button = tk.Button(
        dashboard_frame,
        text="Quit",
        relief="groove",
        width=20,
        command=root.destroy,
    )
    quit_button.bind("<Return>", lambda _: quit_button.invoke())
    quit_button.place(x=200, y=400)

    logout_button = tk.Button(
        dashboard_frame,
        text="Log Out",
        relief="groove",
        width=20,
        command=lambda: _logout(root, dashboard_frame, table_one, table_two),
    )
    logout_button.bind("<Return>", lambda _: logout_button.invoke())
    logout_button.place(x=400, y=400)


def _logout(root: tk.Tk, dashboard_frame: tk.Frame, table_one: dict, table_two: dict):
    functions.delete_frame(dashboard_frame)
    home.home_page(root)
