import tkinter as tk, tools, database
from pages import home, add_flat, modify_flat, delete_flat, display_flats, buy_flat, sell_flat, edit_owner, display_owner

def page(root: tk.Tk):
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    tools.insert_bgimage(frame, "./assets/dashboard.png")

    button_values = [
        ("Add Flat", lambda: tools.switch_frame(root, frame, add_flat.page), 14, 2, 53, 148),
        ("Delete Flat", lambda: tools.switch_frame(root, frame, delete_flat.page), 14, 2, 53, 208),
        ("Modify Flat", lambda: tools.switch_frame(root, frame, modify_flat.page), 14, 2, 53, 268),
        ("Display Flats", lambda: tools.switch_frame(root, frame, display_flats.page), 14, 2, 53, 325),
        ("Buy Flat", lambda: tools.switch_frame(root, frame, buy_flat.page), 14, 2, 53, 385),
        ("Sell Flat", lambda: tools.switch_frame(root, frame, sell_flat.page), 14, 2, 53, 445),
        ("Edit Owner", lambda: tools.switch_frame(root, frame, edit_owner.page), 14, 2, 54, 503),
        ("View Owners", lambda: tools.switch_frame(root, frame, display_owner.page), 16, 1, 611, 188),
        ("Logout", lambda: (database.close(), tools.switch_frame(root, frame, home.page)), 15, 2, 375, 500),
        ("Quit", lambda: (database.close(), root.destroy()), 15, 2, 575, 500),
    ]

    information_values = [
        (database.get_flats_count(), 400, 195), 
        (database.get_flats_for_sale_count(), 500, 300), 
        (database.get_flat_for_rent_count(), 675, 300), 
        (database.get_occupied_flat_count(), 500, 360),
    ]

    for text, fn, w, h, x, y in button_values:
        tools.create_button(frame, text=text, width=w, height=h, command=fn).place(x=x, y=y)

    for value, x, y in information_values:
        tk.Label(frame, text=f"{value}", bg="white").place(x=x, y=y)
   
