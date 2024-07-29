import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter import PhotoImage  # Importieren der PhotoImage-Klasse für das Logo
from note_manager import save_note_with_path, add_image, list_existing_folders, on_note_select, new_note_command, load_template, browse_folder
from theme_manager import set_theme
from menu_manager import create_menubar

# Globale Variable für den aktuellen Dateipfad
current_file_path = None

def insert_markdown(markdown_text, content_text):
    try:
        start = content_text.index("sel.first")
        end = content_text.index("sel.last")
        selected_text = content_text.get(start, end)
        formatted_text = f"{markdown_text}{selected_text}{markdown_text}"
        content_text.delete(start, end)
        content_text.insert(start, formatted_text)
    except tk.TclError:
        messagebox.showinfo("Info", "Please select text to format")

def create_note():
    global current_file_path

    root = tk.Tk()
    root.title("LiNotium")

    # Setze das Logo
    logo_path = os.path.join(os.path.dirname(__file__), "logo.png")
    if os.path.exists(logo_path):
        logo = PhotoImage(file=logo_path)
        root.iconphoto(False, logo)

    # Style für die Buttons festlegen
    style = ttk.Style()
    style.configure("TButton", padding=3, relief="flat")

    # Define font for bold labels
    bold_font = ("Arial", 12, "bold")

    # Create PanedWindow
    paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
    paned_window.pack(fill=tk.BOTH, expand=1)

    # Left frame for folder selection and notes
    left_frame = ttk.Frame(paned_window, width=200)
    paned_window.add(left_frame)

    # Right frame for note creation
    right_frame = ttk.Frame(paned_window)
    paned_window.add(right_frame)

    # Folder selection and notes in the left frame
    tk.Label(left_frame, text="Folder Name:", font=bold_font).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    folder_entry = tk.Entry(left_frame, width=50)
    folder_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    ttk.Button(left_frame, text="Browse", command=lambda: browse_folder(folder_entry, tree)).grid(row=1, column=1, padx=5, pady=5)

    tk.Label(left_frame, text="Existing Folders and Notes:", font=bold_font).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    tree = ttk.Treeview(left_frame, height=20)
    tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    list_existing_folders(tree)
    tree.bind("<Double-1>", lambda event: update_current_file_path(on_note_select(event, tree, title_entry, content_text)))

    left_frame.grid_rowconfigure(3, weight=1)
    left_frame.grid_columnconfigure(0, weight=1)

    # Note creation in the right frame
    tk.Label(right_frame, text="Markdown Tools:", font=bold_font).grid(row=0, column=0, padx=5, pady=5, sticky="w")
    toolbar_frame = ttk.Frame(right_frame)
    toolbar_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

    bold_button = ttk.Button(toolbar_frame, text="B", command=lambda: insert_markdown("**", content_text))
    bold_button.grid(row=0, column=0, padx=2)
    bold_button.config(style="Bold.TButton")

    italic_button = ttk.Button(toolbar_frame, text="I", command=lambda: insert_markdown("_", content_text))
    italic_button.grid(row=0, column=1, padx=2)
    italic_button.config(style="Italic.TButton")

    h1_button = ttk.Button(toolbar_frame, text="H1", command=lambda: insert_markdown("# ", content_text))
    h1_button.grid(row=0, column=2, padx=2)
    h1_button.config(style="H1.TButton")

    h2_button = ttk.Button(toolbar_frame, text="H2", command=lambda: insert_markdown("## ", content_text))
    h2_button.grid(row=0, column=3, padx=2)
    h2_button.config(style="H2.TButton")

    h3_button = ttk.Button(toolbar_frame, text="H3", command=lambda: insert_markdown("### ", content_text))
    h3_button.grid(row=0, column=4, padx=2)
    h3_button.config(style="H3.TButton")

    list_button = ttk.Button(toolbar_frame, text="List", command=lambda: insert_markdown("- ", content_text))
    list_button.grid(row=0, column=5, padx=2)
    list_button.config(style="List.TButton")

    link_button = ttk.Button(toolbar_frame, text="Link", command=lambda: insert_markdown("[title](http://)", content_text))
    link_button.grid(row=0, column=6, padx=2)
    link_button.config(style="Link.TButton")

    tk.Label(right_frame, text="Note Title:", font=bold_font).grid(row=2, column=0, padx=5, pady=5, sticky="w")
    title_entry = tk.Entry(right_frame, width=50)
    title_entry.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    tk.Label(right_frame, text="Note Content:", font=bold_font).grid(row=4, column=0, padx=5, pady=5, sticky="w")
    content_text = tk.Text(right_frame, width=60, height=20)
    content_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    ttk.Button(right_frame, text="Add Image", command=lambda: add_image(content_text)).grid(row=6, column=0, padx=5, pady=5, sticky="w")

    convert_var = tk.BooleanVar()
    ttk.Checkbutton(right_frame, text="Convert to PDF", variable=convert_var).grid(row=7, column=0, padx=5, pady=5, sticky="w")

    ttk.Button(right_frame, text="Save Note", command=lambda: save_note_with_path(current_file_path, title_entry, content_text, convert_var)).grid(row=8, column=0, padx=5, pady=20, sticky="e")
    ttk.Button(right_frame, text="New Note", command=lambda: new_note_command(title_entry, content_text)).grid(row=8, column=1, padx=5, pady=20, sticky="e")

    style.configure("Bold.TButton", font=("Arial", 10, "bold"))
    style.configure("Italic.TButton", font=("Arial", 10, "italic"))
    style.configure("H1.TButton", font=("Arial", 10, "bold"))
    style.configure("H2.TButton", font=("Arial", 10, "bold"))
    style.configure("H3.TButton", font=("Arial", 10, "bold"))
    style.configure("List.TButton", font=("Arial", 10))
    style.configure("Link.TButton", font=("Arial", 10))
    style.configure("Image.TButton", font=("Arial", 10))

    right_frame.grid_rowconfigure(5, weight=1)
    right_frame.grid_columnconfigure(0, weight=1)

    # Create menubar
    create_menubar(root, title_entry, content_text, tree, folder_entry, convert_var, style)

    root.mainloop()

def update_current_file_path(file_path):
    global current_file_path
    current_file_path = file_path

if __name__ == "__main__":
    create_note()
