import tkinter as tk, tools, database, pages.dashboard, math
from tkinter import filedialog
import csv

def page(root: tk.Tk):
    global minf, maxf, total_pages, cur_page, flats
    
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    display_frame = tk.Frame(root, width=600, height=300, bg="white")
    display_frame.place(x=100, y=210)

    flats = database.get_flats()

    if len(flats) == 0:
        tk.messagebox.showwarning("No information found", "No information found in the database")

    minf = 0
    maxf = min(len(flats), 4)
    total_pages = math.ceil(len(flats) / 4)
    cur_page = 1

    tools.insert_bgimage(frame, "./assets/display_flat.png")
    show_flats(flats[minf:maxf], display_frame)
    page_number_label = tk.Label(frame, text=f"Page: {cur_page}/{total_pages}", bg="white")
    page_number_label.place(x=355, y=550)

    tools.create_button(
        frame, text="Export",
        width=15, height=2,
        command=lambda: export_csv(flats)
    ).place(x=110, y=160)
    tools.create_button(
        frame, text="<", width=4, height=2,
        command=lambda: change_view(flats, display_frame, False, page_number_label)
    ).place(x=50, y=345)
    tools.create_button(
        frame, text=">", width=4, height=2,
        command=lambda: change_view(flats, display_frame, True, page_number_label)
    ).place(x=728, y=346)
    tools.create_button(
        frame, text="Quit", 
        width=15, height=2,
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=645, y=526)

def fmt_flat(root, i):
    frame = tk.Frame(root, width=200, height=100, bg="white")
    tk.Label(frame, text=f"Flat Number:\t{i[0]}", bg="white").place(x=0, y=0)
    tk.Label(frame, text=f"Availability:\t{bool(i[1])}", bg="white").place(x=0, y=20)
    tk.Label(frame, text=f"For Rent:\t\t{bool(i[2])}", bg="white").place(x=0, y=40)
    tk.Label(frame, text=f"Owner name:\t{i[3]}", bg="white").place(x=0, y=60)
    tk.Label(frame, text=f"Tenant name:\t{i[4]}", bg="white").place(x=0, y=80)

    return frame

def show_flats(flats, display_frame):
    position = [(50, 25), (350, 25), (50, 175), (350, 175)]

    for pos, flat in zip(position, flats):
        fmt_flat(display_frame, flat).place(x=pos[0], y=pos[1])

def change_view(flats, frame: tk.Frame, next, page_number_label):
    global minf, maxf, total_pages, cur_page
    
    if (minf == 0 and not next) or (maxf == len(flats) and next): 
        return

    if next:
        minf = min(minf + 4, len(flats) - 4)
        cur_page += 1
    else:
        minf = max(minf - 4, 0)
        cur_page -= 1
    maxf = minf + 4

    for i in frame.winfo_children():
        i.place(x=-100, y=-100)

    show_flats(flats[minf:maxf], frame)
    page_number_label.config(text=f"Page: {cur_page}/{total_pages}")

def export_csv(flats):
    path = tk.filedialog.askdirectory(initialdir='./', title='Select a folder') + '/flat_info.csv'
    with open(path, 'w', newline='') as f:
        wo = csv.writer(f)
        wo.writerow(["Flat Number", "Availibility", "For Rent",
                     "Owner Name", "Phone Number", "Email", "Tenant Name"])

        for flat in flats:
            info = []
            info.append(flat[0])
            info.append("Yes" if flat[1] else "No")
            info.append("Yes" if flat[2] else "No")
            info.append(flat[3] if flat[3] else "NIL")
            
            if flat[3] is not None:
                owner = database.get_owner(flat[3])
                info.extend(owner[1:3])
            else:
                info.extend(["NIL", "NIL"])
                
            info.append(flat[4] if flat[4] else "NIL")
            wo.writerow(info)

    tk.messagebox.showinfo("Success", "Exported Data to " + path)
