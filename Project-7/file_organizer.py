import os
import shutil

def organize_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Folder does not exist!")
        return

    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
        "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
        "Music": [".mp3", ".wav", ".aac", ".flac"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Archives": [".zip", ".rar", ".7z", ".tar"],
        "Python": [".py"]
    }

    for folder_name in categories:
        new_folder=os.path.join(folder_path, folder_name)
        os.makedirs(new_folder, exist_ok=True)

    for item in os.listdir(folder_path):
        file_path=os.path.join(folder_path, item)

        if not os.path.isfile(file_path):
            continue

        extension=os.path.splitext(item)[1].lower()
        destination_folder=None

        for folder_name,extensions in categories.items():
            if extension in extensions:
                destination_folder=os.path.join(folder_path,folder_name)
                break

        if destination_folder is None:
            destination_folder = os.path.join(folder_path, "Others")
            os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(destination_folder, item)

        if os.path.exists(destination_path):
            print("Skipped duplicate:", item)
            continue

        try:
            shutil.move(file_path, destination_path)
            print("Moved:", item, "->", os.path.basename(destination_folder))
        except OSError as error:
            print("Could not move", item, ":", error)

    print("File organization completed!")


folder_path = input("Enter the folder path to organize: ").strip().strip('"')
organize_files(folder_path)
