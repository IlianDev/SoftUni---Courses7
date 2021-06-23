from gui_shop_live_demo.canvas import tk
from tkinter import Button


def render_main_enter_screen():
    Button(tk, text="Login", bg="green", fg="black", command=).grid(row=0, column=0)
    Button(tk, text="Registration", bg="yellow", fg="black").grid(row=0, column=1)

