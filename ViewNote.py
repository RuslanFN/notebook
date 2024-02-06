from tkinter import *
from tkinter import ttk

class ViewNote():
    def create_note(title, text, date, rootFrame) -> type(Frame):
        frame = Frame(rootFrame, borderwidth=1, relief=SOLID)
        title = Label(frame, text = title, font=("Arial", 14, "bold"), anchor=NW, justify=CENTER).pack(fill=X, anchor=NW)
        text = Label(frame, text = text, font=("Arial", 11), anchor=NW, justify=CENTER).pack(fill=BOTH)
        date = Label(frame, text = date, font=("Courier New", 8), foreground = "#808080").pack(anchor=SE)
        return frame
