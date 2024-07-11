import os

def print_directory_structure(root_dir, file_handle, padding=""):
    if not os.path.isdir(root_dir):
        file_handle.write(f"{root_dir} ist kein gültiges Verzeichnis.\n")
        return

    file_handle.write(padding[:-1] + "+--" + os.path.basename(root_dir) + "/\n")
    padding = padding + "   "
    files = []
    dirs = []
    for item in os.listdir(root_dir):
        if os.path.isdir(os.path.join(root_dir, item)):
            dirs.append(item)
        else:
            files.append(item)
    for dir in dirs:
        print_directory_structure(os.path.join(root_dir, dir), file_handle, padding + "|  ")
    for file in files:
        file_handle.write(padding + "+--" + file + "\n")

root_directory = "G:\\My Drive\\Gitea\\LiNotium"
output_file_path = os.path.join(os.path.dirname(__file__), "directory_structure.txt")

with open(output_file_path, "w", encoding="utf-8") as file_handle:
    print_directory_structure(root_directory, file_handle)

print(f"Die Verzeichnisstruktur wurde in {output_file_path} gespeichert.")
