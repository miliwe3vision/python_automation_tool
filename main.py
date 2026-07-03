from organizer import organize_files
from json_manager import json_menu
from password_generator import password_menu


def display_menu():
    print("\n" + "=" * 45)
    print("      PYTHON AUTOMATION TOOLKIT")
    print("=" * 45)
    print("1. File Organizer")
    print("2. JSON Manager")
    print("3. Password Generator")
    print("4. Exit")
    print("=" * 45)


def main():

    while True:

        display_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            folder = input("Enter folder path: ")
            organize_files(folder)

        elif choice == "2":

            json_menu()

        elif choice == "3":

            password_menu()

        elif choice == "4":

            print("\nThank you for using Python Automation Toolkit.")
            break

        else:

            print("\nInvalid Choice!")


if __name__ == "__main__":
    main()