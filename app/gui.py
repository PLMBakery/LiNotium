import os
import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF
import markdown2

def create_note():
    def save_note():
        li_notes_dir = os.path.join(os.path.dirname(__file__), "..", "LiNotes")
        images_dir = os.path.join(li_notes_dir, "images")

        # Hauptordner und Bilderordner erstellen, falls nicht vorhanden
        if not os.path.exists(li_notes_dir):
            os.makedirs(li_notes_dir)
        if not os.path.exists(images_dir):
            os.makedirs(images_dir)

        folder_name = os.path.join(li_notes_dir, folder_entry.get()) if folder_entry.get() else li_notes_dir
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        title = title_entry.get()
        content = content_text.get("1.0", tk.END)

        note_content = f"# {title}\n\n{content}"
        file_name = f"{title.replace(' ', '_')}.md"
        file_path = os.path.join(folder_name, file_name)

        with open(file_path, 'w') as file:
            file.write(note_content)

        messagebox.showinfo("Success", f"Note '{title}' created successfully as {file_path}.")

        if convert_var.get():
            pdf_filename = f"{title.replace(' ', '_')}.pdf"
            pdf_file_path = os.path.join(folder_name, pdf_filename)
            markdown_to_pdf(note_content, pdf_file_path)
            messagebox.showinfo("Success", f"Note '{title}' also saved as {pdf_file_path}.")

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

    root = tk.Tk()
    root.title("Note Creator")

    # Label and Entry for Folder Name
    tk.Label(root, text="Folder Name:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    folder_entry = tk.Entry(root, width=50)
    folder_entry.grid(row=1, column=0, padx=5, pady=5, sticky="w")

    # Label and Entry for Note Title
    tk.Label(root, text="Note Title:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    title_entry = tk.Entry(root, width=50)
    title_entry.grid(row=3, column=0, padx=5, pady=5, sticky="w")

    # Label and Text for Note Content
    tk.Label(root, text="Note Content:").grid(row=4, column=0, padx=5, pady=5, sticky="w")
    content_text = tk.Text(root, width=60, height=20)
    content_text.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    # Buttons for Adding Image and Saving Note
    tk.Button(root, text="Add Image", command=add_image).grid(row=6, column=0, padx=5, pady=5, sticky="w")
    
    convert_var = tk.BooleanVar()
    tk.Checkbutton(root, text="Convert to PDF", variable=convert_var).grid(row=7, column=0, padx=5, pady=5, sticky="w")

    tk.Button(root, text="Save Note", command=save_note).grid(row=8, column=0, padx=5, pady=20, sticky="e")

    root.mainloop()

if __name__ == "__main__":
    create_note()
