import tkinter as tk
import home

import constants


def create_window() -> tk.Tk:
    root = tk.Tk()

    root.geometry(f"{constants.SCREEN_WIDTH}x{constants.SCREEN_HEIGHT}+300+100")
    root.configure(bg=constants.BACKGROUND_COLOUR)
    root.resizable(False, False)
    root.title(constants.TITLE)

    return root


root = create_window()

home.home_page(root)
root.mainloop()
