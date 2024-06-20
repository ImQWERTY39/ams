import tkinter as tk, tools, database
from pages import home, add_flat, modify_flat, delete_flat, display_flats, buy_flat, sell_flat, edit_owner, display_owner

def page(root: tk.Tk):
    frame = tk.Frame(root, width=800, height=600, bg="#0000ff")
    frame.place(x=0, y=0)

    tools.insert_bgimage(frame, "./assets/dashboard.png")
    tools.create_button(frame, text="Add Flat", command=lambda: tools.switch_frame(root, frame, add_flat.page)).place(x=50, y=150)
    tools.create_button(frame, text="Delete Flat", command=lambda: tools.switch_frame(root, frame, delete_flat.page)).place(x=50, y=210)
    # tools.create_button(frame, text="Modify Flat", command=lambda: tools.switch_frame(root, frame, modify_flat.page)).place(x=50, y=275)
    tools.create_button(frame, text="Display Flats", command=lambda: tools.switch_frame(root, frame, display_flats.page)).place(x=50, y=330)
    tools.create_button(frame, text="Buy Flat", command=lambda: tools.switch_frame(root, frame, buy_flat.page)).place(x=50, y=390)
    tools.create_button(frame, text="Sell Flat", command=lambda: tools.switch_frame(root, frame, sell_flat.page)).place(x=50, y=450)
    tools.create_button(frame, text="Edit Owner", command=lambda: tools.switch_frame(root, frame, edit_owner.page)).place(x=50, y=510)
    tools.create_button(frame, text="View Owner", command=lambda: tools.switch_frame(root, frame, display_owner.page)).place(x=600, y=185)
    tools.create_button(frame, text="Logout", command=lambda: (database.close(), tools.switch_frame(root, frame, home.page))).place(x=400, y=500)
    tools.create_button(frame, text="Quit", command=lambda: (database.close(), root.destroy())).place(x=600, y=500)

    tk.Label(frame, text=f"{database.get_flats_count()}", bg="white").place(x=400, y=195)
    tk.Label(frame, text=f"{database.get_flats_for_sale_count()}", bg="white").place(x=500, y=300)
    tk.Label(frame, text=f"{database.get_flat_for_rent_count()}", bg="white").place(x=675, y=300)
    tk.Label(frame, text=f"{database.get_occupied_flat_count()}", bg="white").place(x=500, y=360)
