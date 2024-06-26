# -----------------------------------------------------------------------------
# main.py
# Author: Marc Weidner
# Date: 26. Juni 2024
# Version: 1.0
# License: MIT
# -----------------------------------------------------------------------------
import os
import markdown2
from fpdf import FPDF

def create_note():
    # Ordner abfragen oder erstellen
    folder_name = input("Enter the folder name (or press Enter to create in the root directory): ")
    if folder_name:
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"Folder '{folder_name}' created.")
    else:
        folder_name = "."

    title = input("Enter the title of the note: ")
    content = input("Enter the content of the note: ")

    note_content = f"# {title}\n\n{content}"
    file_name = f"{title.replace(' ', '_')}.md"
    file_path = os.path.join(folder_name, file_name)

    with open(file_path, 'w') as file:
        file.write(note_content)

    print(f"Note '{title}' created successfully as {file_path}.")

    # Option to convert to PDF
    convert_to_pdf = input("Do you want to convert this note to PDF? (y/n): ").lower()
    if convert_to_pdf == 'y':
        pdf_filename = f"{title.replace(' ', '_')}.pdf"
        pdf_file_path = os.path.join(folder_name, pdf_filename)
        markdown_to_pdf(note_content, pdf_file_path)
        print(f"Note '{title}' also saved as {pdf_file_path}.")

def markdown_to_pdf(md_content, pdf_filename):
    html_content = markdown2.markdown(md_content)
    
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Fügen Sie HTML-Inhalt hinzu
    for line in html_content.split('\n'):
        pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(pdf_filename)

if __name__ == "__main__":
    create_note()
