import tkinter as tk
from tkinter import ttk

def set_theme(theme, root, style):
    if theme == "light":
        root.config(bg="white")
        for widget in root.winfo_children():
            widget.config(bg="white", fg="black")
        style.configure('TButton', background='white', foreground='black')
        style.configure('TLabel', background='white', foreground='black')
        style.configure('TEntry', background='white', foreground='black')
        style.configure('TCheckbutton', background='white', foreground='black')
    elif theme == "dark":
        root.config(bg="black")
        for widget in root.winfo_children():
            widget.config(bg="black", fg="white", insertbackground='white')
        style.configure('TButton', background='black', foreground='white')
        style.configure('TLabel', background='black', foreground='white')
        style.configure('TEntry', background='black', foreground='white')
        style.configure('TCheckbutton', background='black', foreground='white')
