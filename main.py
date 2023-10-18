import tkinter as tk
import home
import dashboard
import constants


root = tk.Tk()

root.geometry(f"{constants.SCREEN_WIDTH}x{constants.SCREEN_HEIGHT}+300+100")
root.configure(bg=constants.BACKGROUND_COLOUR)
root.resizable(False, False)
root.title(constants.TITLE)

# swap comments for testing
# delete import dashboard and dashboard page function when finished

home.home_page(root)
# dashboard.page(root)

root.mainloop()
