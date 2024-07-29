import tkinter as tk
from theme_manager import set_theme
from note_manager import load_template, browse_folder, list_existing_folders, new_note_command, save_note_with_path

def create_menubar(root, title_entry, content_text, tree, folder_entry, convert_var, style):
    menubar = tk.Menu(root)

    # File Menu
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New Note", command=lambda: new_note_command(title_entry, content_text))
    file_menu.add_command(label="Save Note", command=lambda: save_note_with_path(None, title_entry, content_text, convert_var))
    file_menu.add_command(label="Load Note", command=lambda: list_existing_folders(tree))
    file_menu.add_command(label="Load Template", command=lambda: load_template(title_entry, content_text))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=file_menu)

    # Settings Menu
    settings_menu = tk.Menu(menubar, tearoff=0)
    settings_menu.add_command(label="Preferences", command=lambda: show_preferences_dialog(root))
    
    # Theme submenu under Settings
    theme_menu = tk.Menu(settings_menu, tearoff=0)
    theme_menu.add_command(label="Light Mode", command=lambda: set_theme("light", root, style))
    theme_menu.add_command(label="Dark Mode", command=lambda: set_theme("dark", root, style))
    settings_menu.add_cascade(label="Theme", menu=theme_menu)

    menubar.add_cascade(label="Settings", menu=settings_menu)

    root.config(menu=menubar)

def show_preferences_dialog(root):
    preferences_window = tk.Toplevel(root)
    preferences_window.title("Preferences")
    tk.Label(preferences_window, text="Settings will be added here.").pack(padx=20, pady=20)
