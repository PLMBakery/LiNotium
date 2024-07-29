import os
import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
import markdown2

def save_note_with_path(current_file_path, title_entry, content_text, convert_var):
    if current_file_path:
        save_note_to_path(current_file_path, title_entry, content_text, convert_var)
    else:
        save_note_new(title_entry, content_text, convert_var)

def save_note_to_path(file_path, title_entry, content_text, convert_var):
    with open(file_path, 'w') as file:
        file.write(content_text.get("1.0", tk.END))
    messagebox.showinfo("Info", f"Note saved at {file_path}")

def save_note_new(title_entry, content_text, convert_var):
    li_notes_dir = os.path.join(os.path.dirname(__file__), "..", "LiNotes")
    images_dir = os.path.join(li_notes_dir, "images")

    if not os.path.exists(li_notes_dir):
        os.makedirs(li_notes_dir)
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    title = title_entry.get()
    content = content_text.get("1.0", tk.END)

    note_content = f"# {title}\n\n{content}"
    file_name = f"{title.replace(' ', '_')}.md"
    file_path = os.path.join(li_notes_dir, file_name)

    with open(file_path, 'w') as file:
        file.write(note_content)

    messagebox.showinfo("Success", f"Note '{title}' created successfully as {file_path}.")

    if convert_var.get():
        pdf_filename = f"{title.replace(' ', '_')}.pdf"
        pdf_file_path = os.path.join(li_notes_dir, pdf_filename)
        markdown_to_pdf(note_content, pdf_file_path)
        messagebox.showinfo("Success", f"Note '{title}' also saved as {pdf_file_path}.")

    return file_path

def add_image(content_text):
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

def list_existing_folders(tree):
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
                    tree.insert(folder_id, "end", text=file, values=[file_path])

def on_note_select(event, tree, title_entry, content_text):
    selected_item = tree.selection()[0]
    values = tree.item(selected_item, 'values')
    if values:
        note_path = values[0]
        with open(note_path, 'r') as file:
            note_content = file.read()
        title_entry.delete(0, tk.END)
        title_entry.insert(0, os.path.basename(note_path).replace('_', ' ').replace('.md', ''))
        content_text.delete('1.0', tk.END)
        content_text.insert(tk.END, note_content)
        return note_path
    return None

def new_note_command(title_entry, content_text):
    title_entry.delete(0, tk.END)
    content_text.delete('1.0', tk.END)

def load_template(title_entry, content_text):
    template_path = os.path.join(os.path.dirname(__file__), "templates", "support_case_template.md")
    with open(template_path, 'r') as file:
        template_content = file.read()
    title_entry.delete(0, tk.END)
    title_entry.insert(0, "Support Case")
    content_text.delete('1.0', tk.END)
    content_text.insert('1.0', template_content)

def browse_folder(folder_entry, tree):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        folder_entry.delete(0, tk.END)
        folder_entry.insert(0, folder_selected)
        list_existing_folders(tree)
