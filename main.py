import tkinter as tk, pages.home, database

root = tk.Tk()
root.resizable(False, False)
root.configure(width=800, height=600)
root.title("Apartment Management System")
root.protocol("WM_DELETE_WINDOW", lambda: (database.close(), root.destroy()))

# pages.home.page(root)
database.init("admin", "password")
import pages.dashboard
pages.dashboard.page(root)
root.mainloop()
