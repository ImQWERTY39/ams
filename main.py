import sys
import tkinter as tk
import home
import dashboard
import constants


root = tk.Tk()

root.geometry(f"{constants.SCREEN_WIDTH}x{constants.SCREEN_HEIGHT}+300+100")
root.configure(bg=constants.BACKGROUND_COLOUR)
root.resizable(False, False)
root.title(constants.TITLE)

if sys.argv.pop() == "notest":
    home.home_page(root)
else:
    dashboard.page(root)

root.mainloop()
