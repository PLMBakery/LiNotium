# -----------------------------------------------------------------------------
# main.py
# Author: Marc Weidner
# Date: 26. Juni 2024
# Version: 1.0
# License: MIT
import os
import markdown2
from fpdf import FPDF

def create_note():
    li_notes_dir = os.path.join(os.path.dirname(__file__), "..", "LiNotes")
    images_dir = os.path.join(li_notes_dir, "images")

    # Hauptordner und Bilderordner erstellen, falls nicht vorhanden
    if not os.path.exists(li_notes_dir):
        os.makedirs(li_notes_dir)
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    title = input("Enter the title of the note: ")
    content = input("Enter the content of the note: ")

    note_content = f"# {title}\n\n{content}"
    file_name = f"{title.replace(' ', '_')}.md"
    file_path = os.path.join(li_notes_dir, file_name)

    with open(file_path, 'w') as file:
        file.write(note_content)

    print(f"Note '{title}' created successfully as {file_path}.")

    convert_to_pdf = input("Do you want to convert this note to PDF? (y/n): ").lower()
    if convert_to_pdf == 'y':
        pdf_filename = f"{title.replace(' ', '_')}.pdf"
        pdf_file_path = os.path.join(li_notes_dir, pdf_filename)
        markdown_to_pdf(note_content, pdf_file_path)
        print(f"Note '{title}' also saved as {pdf_file_path}.")

def markdown_to_pdf(md_content, pdf_filename):
    html_content = markdown2.markdown(md_content)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in html_content.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(pdf_filename)

if __name__ == "__main__":
    create_note()
