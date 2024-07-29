import tkinter as tk
from tkinter import ttk

def set_theme(theme, root, left_frame, right_frame, folder_entry, title_entry, content_text, style, tree):
    if theme == "light":
        root.config(bg="white")
        left_frame.config(bg="white")
        right_frame.config(bg="white")
        for widget in [folder_entry, title_entry, content_text]:
            widget.config(bg="white", fg="black")
        style.configure('TButton', background='white', foreground='black')
        style.configure('TLabel', background='white', foreground='black')
        style.configure('TEntry', background='white', foreground='black')
        style.configure('TCheckbutton', background='white', foreground='black')
        tree.tag_configure('light', background='white', foreground='black')
    elif theme == "dark":
        root.config(bg="black")
        left_frame.config(bg="black")
        right_frame.config(bg="black")
        for widget in [folder_entry, title_entry, content_text]:
            widget.config(bg="black", fg="white", insertbackground='white')
        style.configure('TButton', background='black', foreground='white')
        style.configure('TLabel', background='black', foreground='white')
        style.configure('TEntry', background='black', foreground='white')
        style.configure('TCheckbutton', background='black', foreground='white')
        tree.tag_configure('dark', background='black', foreground='white')
