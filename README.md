# LiNotium
 Note Taking App for VSCodium

# LiNotium Note-Taking Application

This guide will walk you through testing the LiNotium note-taking application using VSCodium.

## Prerequisites

- **VSCodium** installed
- **Python** installed
- **Virtual environment** already created

## Steps to Test the Application

### 1. Open VSCodium

Launch VSCodium on your system.

### 2. Open the Project Folder

Open the folder where your project is located (e.g., `G:\My Drive\Gitea\LiNotium`).

### 3. Open Terminal in VSCodium

Press `Ctrl + Shift + Ö` to open the terminal in VSCodium.

### 4. Activate the Virtual Environment

Navigate to the `app` directory and activate the virtual environment:

cd app
.\env\Scripts\activate

#### 5. Run the Note Creation Script
Run the main.py script to create a note:

python main.py
Follow the instructions in the terminal to enter the title and content of the note.

### 6. Run the GUI Script
Run the gui.py script to start the graphical user interface:


python gui.py
Use the GUI to create notes, add images, and save notes as PDFs.

### Additional Notes
Ensure that all dependencies are installed in the virtual environment. If not, you can install them using:


pip install -r requirements.txt

### Structure: Your project should have the following structure:

bash
Code kopieren
LiNotium (WORKSPACE)
├── app
│   ├── env
│   ├── main.py
│   └── gui.py
├── LiNotes
│   └── images
├── .gitattributes
├── LICENSE
├── LiNotium.code-workspace
└── README.md

### Troubleshooting
If you encounter any issues, ensure that:

The virtual environment is activated.
All required dependencies are installed.
The file paths in your scripts are correct.
For further assistance, feel free to reach out to the project maintainers.