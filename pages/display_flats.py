import tkinter as tk, tools, database, pages.dashboard, math

minf, maxf, total_pages, cur_page = 0, 0, 0, 1

def page(root: tk.Tk):
    global minf, maxf, total_pages
    
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    display_frame = tk.Frame(root, width=600, height=300, bg="white")
    display_frame.place(x=100, y=210)

    flats = fmt_flats(display_frame, database.get_flats())
    maxf = min(len(flats), 4)
    total_pages = math.ceil(len(flats) / 4)

    tools.insert_bgimage(frame, "./assets/display.png")
    show_flats(flats[minf:maxf])
    page_number_label = tk.Label(frame, text=f"Page: {cur_page}/{total_pages}", bg="white")
    page_number_label.place(x=355, y=550)

    tools.create_button(
        frame, text="<", width=4, height=2,
        command=lambda: change_view(flats, display_frame, False, page_number_label)
    ).place(x=30, y=340)
    tools.create_button(
        frame, text=">", width=4, height=2,
        command=lambda: change_view(flats, display_frame, True, page_number_label)
    ).place(x=710, y=340)
    tools.create_button(
        frame, text="Quit", 
        width=15, height=2,
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=620, y=520)

def fmt_flats(root, flats):
    ret = []
    
    for i in flats:
        frame = tk.Frame(root, width=200, height=100, bg="white")
        tk.Label(frame, text=f"Flat Number:\t{i[0]}", bg="white").place(x=0, y=0)
        tk.Label(frame, text=f"Availability:\t{bool(i[1])}", bg="white").place(x=0, y=20)
        tk.Label(frame, text=f"For Rent:\t\t{bool(i[2])}", bg="white").place(x=0, y=40)
        tk.Label(frame, text=f"Owner name:\t{i[3]}", bg="white").place(x=0, y=60)
        tk.Label(frame, text=f"Tenant name:\t{i[4]}", bg="white").place(x=0, y=80)

        ret.append(frame)
    
    return ret

def show_flats(flats):
    try:
        flats[0].place(x=50, y=25)
        flats[1].place(x=350, y=25)
        flats[2].place(x=50, y=175)
        flats[3].place(x=350, y=175)
    except: pass

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

    show_flats(flats[minf:maxf])
    page_number_label.config(text=f"Page: {cur_page}/{total_pages}")
