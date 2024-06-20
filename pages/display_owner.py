import tkinter as tk, tools, database, pages.dashboard

minf, maxf, total_pages, cur_page = 0, 0, 0, 1

def page(root: tk.Tk):
    global minf, maxf, total_pages
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    display_frame = tk.Frame(root, width=600, height=300, bg="white")
    display_frame.place(x=100, y=210)

    owners = fmt_owner(display_frame, database.get_owners())
    minf, maxf, total_pages = 0, min(len(owners), 4), len(owners) // 4 + 1
    tools.insert_bgimage(frame, "./assets/display.png")
    show_owners(owners[minf:maxf])

    page_number_label = tk.Label(frame, text=f"Page: {cur_page}/{total_pages}")
    page_number_label.place(x=0, y=0)
    tools.create_button(frame, text="<", command=lambda: change_view(owners, display_frame, False, page_number_label)).place(x=50, y=350)
    tools.create_button(frame, text=">", command=lambda: change_view(owners, display_frame, True, page_number_label)).place(x=720, y=350)
    tools.create_button(frame, text="Quit", command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)).place(x=675, y=530)

def fmt_owner(root, owners):
    ret = []
    for i in owners:
        frame = tk.Frame(root, width=200, height=100, bg="white")
        tk.Label(frame, text=f"Name:   {i[0]}", bg="white").place(x=0, y=0)
        tk.Label(frame, text=f"Ph No:  {i[1]}", bg="white").place(x=0, y=20)
        tk.Label(frame, text=f"Email:  {i[2]}", bg="white").place(x=0, y=40)
        tk.Label(frame, text=f"Houses\nowned: {i[3]}", bg="white").place(x=0, y=60)
        ret.append(frame)
    return ret

def show_owners(owners):
    try:
        owners[0].place(x=50, y=25)
        owners[1].place(x=350, y=25)
        owners[2].place(x=50, y=175)
        owners[3].place(x=350, y=175)
    except: pass

def change_view(owners, frame, next, page_number_label):
    global minf, maxf, total_pages, cur_page
    if (minf == 0 and not next) or (maxf == len(owners) and next): return
    if next: minf, maxf = min(minf + 4, len(owners) - 4), min(maxf + 4, len(owners))
    else: minf, maxf = max(0, minf - 4), max(4, maxf - 4)
    for i in frame.winfo_children(): i.place(x=-100, y=-100)
    show_owners(owners[minf:maxf])
    page_number_label.config(text=f"Page: {cur_page}/{total_pages}")
