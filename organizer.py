"""
====================================================
File Organizer
Author : Mili
Description:
Automatically organize files into folders based
on their extensions.
====================================================
"""

import os
import shutil

# ---------------------------------------
# File Categories
# ---------------------------------------

FILE_TYPES = {

    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"
    ],

    "Documents": [
        ".pdf", ".docx", ".doc", ".txt", ".xlsx",
        ".csv", ".pptx"
    ],

    "Videos": [
        ".mp4", ".avi", ".mov", ".mkv"
    ],

    "Music": [
        ".mp3", ".wav", ".aac"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar", ".gz"
    ]

}


# ---------------------------------------
# Organize Function
# ---------------------------------------

def organize_files(folder_path):

    if not os.path.exists(folder_path):
        print("\nFolder does not exist!")
        return

    moved_files = 0

    summary = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Music": 0,
        "Archives": 0,
        "Others": 0
    }

    files = os.listdir(folder_path)

    if len(files) == 0:
        print("\nFolder is Empty.")
        return

    print("\nOrganizing Files...\n")

    for file in files:

        source_path = os.path.join(folder_path, file)

        # Skip folders
        if os.path.isdir(source_path):
            continue

        extension = os.path.splitext(file)[1].lower()

        moved = False

        # Search category
        for category, extensions in FILE_TYPES.items():

            if extension in extensions:

                destination_folder = os.path.join(folder_path, category)

                os.makedirs(destination_folder, exist_ok=True)

                destination = os.path.join(destination_folder, file)

                shutil.move(source_path, destination)

                print(f"Moved : {file}  --->  {category}")

                summary[category] += 1

                moved_files += 1

                moved = True

                break

        # Unknown files
        if not moved:

            other_folder = os.path.join(folder_path, "Others")

            os.makedirs(other_folder, exist_ok=True)

            destination = os.path.join(other_folder, file)

            shutil.move(source_path, destination)

            print(f"Moved : {file} ---> Others")

            summary["Others"] += 1

            moved_files += 1

    print("\n" + "=" * 40)

    print("Organization Completed")

    print("=" * 40)

    print(f"Total Files : {moved_files}")

    print()

    for category, count in summary.items():

        print(f"{category:<12}: {count}")

    print("=" * 40)