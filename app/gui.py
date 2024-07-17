import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from fpdf import FPDF
import markdown2

def create_note():
    def browse_folder():
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            folder_entry.delete(0, tk.END)
            folder_entry.insert(0, folder_selected)
            list_existing_folders()

    def save_note():
        li_notes_dir = os.path.join(os.path.dirname(__file__), "..", "LiNotes")
        images_dir = os.path.join(li_notes_dir, "images")

        if not os.path.exists(li_notes_dir):
            os.makedirs(li_notes_dir)
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)

        selected_folder = tree.focus()
        if selected_folder:
            folder_name = tree.item(selected_folder, 'text')
            folder_path = os.path.join(li_notes_dir, folder_name)
        else:
            folder_path = li_notes_dir

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        title = title_entry.get()
        content = content_text.get("1.0", tk.END)

        note_content = f"# {title}\n\n{content}"
        file_name = f"{title.replace(' ', '_')}.md"
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, 'w') as file:
            file.write(note_content)

        messagebox.showinfo("Success", f"Note '{title}' created successfully as {file_path}.")

        if convert_var.get():
            pdf_filename = f"{title.replace(' ', '_')}.pdf"
            pdf_file_path = os.path.join(folder_path, pdf_filename)
            markdown_to_pdf(note_content, pdf_file_path)
            messagebox.showinfo("Success", f"Note '{title}' also saved as {pdf_file_path}.")

        list_existing_folders()

    def add_image():
        image_path = filedialog.askopenfilename()
        if image_path:
            image_name = os.path.basename(image_path)
            new_image_path = os.path.join("..", "LiNotes", "images", image_name)
            os.makedirs(os.path.dirname(new_image_path), exist_ok=True)
            with open(image_path, 'rb') as source_file:
                with open(new_image_path, 'wb') as dest_file:
                    dest_file.write(source_file.read())
            content_text.insert(tk.END, f"\n\n![Image]({new_image_path})")

    def markdown_to_pdf(md_content, pdf_filename):
        html_content = markdown2.markdown(md_content)
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for line in html_content.split('\n'):
            pdf.cell(200, 10, txt=line, ln=True)

        pdf.output(pdf_filename)

    def list_existing_folders():
        li_notes_dir = os.path.join(os.path.dirname(__file__), "..", "LiNotes")
        for i in tree.get_children():
            tree.delete(i)
        for folder in os.listdir(li_notes_dir):
            folder_path = os.path.join(li_notes_dir, folder)
            if os.path.isdir(folder_path):
                folder_id = tree.insert("", "end", text=folder, open=False)
                for file in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file)
                    if os.path.isfile(file_path):
                        tree.insert(folder_id, "end", text=file)

    def insert_markdown(markdown_text):
        content_text.insert(tk.INSERT, markdown_text)

    def on_note_select(event):
        selected_item = tree.selection()[0]
        item_text = tree.item(selected_item, 'text')
        parent_item = tree.parent(selected_item)
        parent_text = tree.item(parent_item, 'text')

        if parent_text:
            note_path = os.path.join(os.path.dirname(__file__), "..", "LiNotes", parent_text, item_text)
            with open(note_path, 'r') as file:
                note_content = file.read()
            title_entry.delete(0, tk.END)
            title_entry.insert(0, item_text.replace('_', ' ').replace('.md', ''))
            content_text.delete('1.0', tk.END)
            content_text.insert(tk.END, note_content)

    def new_note():
        title_entry.delete(0, tk.END)
        content_text.delete('1.0', tk.END)
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, "LiNotes")

    def exit_app():
        root.quit()

    def set_theme(theme):
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

    root = tk.Tk()
    root.title("Note Creator")

    # Menü erstellen
    menubar = tk.Menu(root)
    file_menu = tk.Menu(menubar, tearoff=0)
    file_menu.add_command(label="New Note", command=new_note)
    file_menu.add_command(label="Save Note", command=save_note)
    file_menu.add_command(label="Load Note", command=list_existing_folders)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=exit_app)
    menubar.add_cascade(label="File", menu=file_menu)

    # Theme-Menü erstellen
    theme_menu = tk.Menu(menubar, tearoff=0)
    theme_menu.add_command(label="Light Mode", command=lambda: set_theme("light"))
    theme_menu.add_command(label="Dark Mode", command=lambda: set_theme("dark"))
    menubar.add_cascade(label="Theme", menu=theme_menu)

    root.config(menu=menubar)

    # Style für die Buttons festlegen
    style = ttk.Style()
    style.configure("TButton", padding=3, relief="flat")

    # PanedWindow erstellen
    paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
    paned_window.pack(fill=tk.BOTH, expand=1)

    # Linker Frame für Ordnerauswahl und Notizen
    left_frame = ttk.Frame(paned_window, width=200)
    paned_window.add(left_frame)

    # Rechter Frame für die Notizerstellung
    right_frame = ttk.Frame(paned_window)
    paned_window.add(right_frame)

    # Ordnerauswahl und Notizen im linken Frame
    tk.Label(left_frame, text="Folder Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    folder_entry = tk.Entry(left_frame, width=50)
    folder_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    ttk.Button(left_frame, text="Browse", command=browse_folder).grid(row=1, column=1, padx=5, pady=5)

    tk.Label(left_frame, text="Existing Folders and Notes:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    tree = ttk.Treeview(left_frame, height=20)
    tree.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    list_existing_folders()
    tree.bind("<Double-1>", on_note_select)

    left_frame.grid_rowconfigure(3, weight=1)
    left_frame.grid_columnconfigure(0, weight=1)

    # Notizerstellung im rechten Frame
    tk.Label(right_frame, text="Markdown Tools:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    toolbar_frame = ttk.Frame(right_frame)
    toolbar_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="w")

    bold_button = ttk.Button(toolbar_frame, text="B", command=lambda: insert_markdown("**bold**"))
    bold_button.grid(row=0, column=0, padx=2)
    bold_button.config(style="Bold.TButton")

    italic_button = ttk.Button(toolbar_frame, text="I", command=lambda: insert_markdown("_italic_"))
    italic_button.grid(row=0, column=1, padx=2)
    italic_button.config(style="Italic.TButton")

    h1_button = ttk.Button(toolbar_frame, text="H1", command=lambda: insert_markdown("# "))
    h1_button.grid(row=0, column=2, padx=2)
    h1_button.config(style="H1.TButton")

    h2_button = ttk.Button(toolbar_frame, text="H2", command=lambda: insert_markdown("## "))
    h2_button.grid(row=0, column=3, padx=2)
    h2_button.config(style="H2.TButton")

    h3_button = ttk.Button(toolbar_frame, text="H3", command=lambda: insert_markdown("### "))
    h3_button.grid(row=0, column=4, padx=2)
    h3_button.config(style="H3.TButton")

    list_button = ttk.Button(toolbar_frame, text="List", command=lambda: insert_markdown("- item"))
    list_button.grid(row=0, column=5, padx=2)
    list_button.config(style="List.TButton")

    link_button = ttk.Button(toolbar_frame, text="Link", command=lambda: insert_markdown("[title](http://)"))
    link_button.grid(row=0, column=6, padx=2)
    link_button.config(style="Link.TButton")

    tk.Label(right_frame, text="Note Title:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    title_entry = tk.Entry(right_frame, width=50)
    title_entry.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    tk.Label(right_frame, text="Note Content:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
    content_text = tk.Text(right_frame, width=60, height=20)
    content_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")

    ttk.Button(right_frame, text="Add Image", command=add_image).grid(row=6, column=0, padx=5, pady=5, sticky="w")

    convert_var = tk.BooleanVar()
    ttk.Checkbutton(right_frame, text="Convert to PDF", variable=convert_var).grid(row=7, column=0, padx=5, pady=5, sticky="w")

    ttk.Button(right_frame, text="Save Note", command=save_note).grid(row=8, column=0, padx=5, pady=20, sticky="e")
    ttk.Button(right_frame, text="New Note", command=new_note).grid(row=8, column=1, padx=5, pady=20, sticky="e")

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

    root.mainloop()

if __name__ == "__main__":
    create_note()
