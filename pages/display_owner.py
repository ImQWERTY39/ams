import tkinter as tk, tools, database, pages.dashboard, math

def page(root: tk.Tk):
    global mino, maxo, total_pages, cur_page
    
    frame = tk.Frame(root, width=800, height=600)
    frame.place(x=0, y=0)
    display_frame = tk.Frame(root, width=600, height=300, bg="white")
    display_frame.place(x=100, y=210)

    owners = fmt_owner(display_frame, database.get_owners())
    mino = 0
    maxo = min(len(owners), 4)
    total_pages = math.ceil(len(owners) / 4)
    cur_page = 1

    tools.insert_bgimage(frame, "./assets/display.png")
    show_owners(owners[mino:maxo])
    page_number_label = tk.Label(frame, text=f"Page: {cur_page}/{total_pages}", bg="white")
    page_number_label.place(x=355, y=550)
    
    tools.create_button(
        frame, text="<", width=4, height=2,
        command=lambda: change_view(owners, display_frame, False, page_number_label)
    ).place(x=30, y=340)
    tools.create_button(
        frame, text=">", width=4, height=2,
        command=lambda: change_view(owners, display_frame, True, page_number_label)
    ).place(x=710, y=340)
    tools.create_button(
        frame, text="Quit", width=15, height=2,
        command=lambda: tools.switch_frame(root, frame, pages.dashboard.page)
    ).place(x=620, y=520)

def fmt_owner(root, owners):
    ret = []
    
    for i in owners:
        frame = tk.Frame(root, width=200, height=100, bg="white")
        tk.Label(frame, text=f"Name:   {i[0]}", bg="white").place(x=0, y=0)
        tk.Label(frame, text=f"Ph No:  {i[1]}", bg="white").place(x=0, y=20)
        tk.Label(frame, text=f"Email:  {i[2]}", bg="white").place(x=0, y=40)
        tk.Label(frame, text=f"Houses owned: {i[3]}", bg="white").place(x=0, y=60)
    
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
    global mino, maxo, total_pages, cur_page
    
    if (mino == 0 and not next) or (maxo == len(flats) and next): 
        return

    if next:
        mino = min(mino + 4, len(flats) - 4)
        cur_page += 1
    else:
        mino = max(mino - 4, 0)
        cur_page -= 1
    maxo = mino + 4

    for i in frame.winfo_children():
        i.place(x=-100, y=-100)

    show_flats(flats[mino:maxo])
    page_number_label.config(text=f"Page: {cur_page}/{total_pages}")
