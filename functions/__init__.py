from tkinter import Frame


def delete_frame(frame: Frame):
    for i in frame.winfo_children():
        i.destroy()

    frame.destroy()


def is_valid_phone_number(phone_number: str) -> bool:
    for i in phone_number:
        if not (48 <= ord(i) <= 57):
            return False

    return len(phone_number) == 10


def is_valid_email(email: str) -> bool:
    email_split = email.split("@")
    return len(email_split) == 2
