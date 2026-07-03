"""
====================================================
JSON Student Management System
Author : Mili
====================================================
"""

import json
import os

FILE_NAME = "student.json"


# ----------------------------------------
# Load Student Data
# ----------------------------------------

def load_students():

    if not os.path.exists(FILE_NAME):

        with open(FILE_NAME, "w") as file:
            json.dump([], file)

    with open(FILE_NAME, "r") as file:
        return json.load(file)


# ----------------------------------------
# Save Student Data
# ----------------------------------------

def save_students(students):

    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# ----------------------------------------
# Add Student
# ----------------------------------------

def add_student():

    students = load_students()

    student = {

        "id": int(input("Enter ID : ")),

        "name": input("Enter Name : "),

        "age": int(input("Enter Age : "))
    }

    students.append(student)

    save_students(students)

    print("\nStudent Added Successfully!")


# ----------------------------------------
# View Students
# ----------------------------------------

def view_students():

    students = load_students()

    if len(students) == 0:

        print("\nNo Students Found.")

        return

    print("\nStudent List")

    print("-" * 35)

    for student in students:

        print(f"ID   : {student['id']}")
        print(f"Name : {student['name']}")
        print(f"Age  : {student['age']}")
        print("-" * 35)


# ----------------------------------------
# Search Student
# ----------------------------------------

def search_student():

    students = load_students()

    search_id = int(input("Enter Student ID : "))

    for student in students:

        if student["id"] == search_id:

            print("\nStudent Found")

            print(student)

            return

    print("\nStudent Not Found.")


# ----------------------------------------
# Update Student
# ----------------------------------------

def update_student():

    students = load_students()

    student_id = int(input("Enter Student ID : "))

    for student in students:

        if student["id"] == student_id:

            student["name"] = input("New Name : ")

            student["age"] = int(input("New Age : "))

            save_students(students)

            print("\nStudent Updated.")

            return

    print("\nStudent Not Found.")


# ----------------------------------------
# Delete Student
# ----------------------------------------

def delete_student():

    students = load_students()

    student_id = int(input("Enter Student ID : "))

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            save_students(students)

            print("\nStudent Deleted.")

            return

    print("\nStudent Not Found.")


# ----------------------------------------
# Menu
# ----------------------------------------

def json_menu():

    while True:

        print("\n" + "=" * 40)

        print("JSON STUDENT MANAGEMENT")

        print("=" * 40)

        print("1. Add Student")

        print("2. View Students")

        print("3. Search Student")

        print("4. Update Student")

        print("5. Delete Student")

        print("6. Back to Main Menu")

        print("=" * 40)

        choice = input("Enter Choice : ")

        if choice == "1":

            add_student()

        elif choice == "2":

            view_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            break

        else:

            print("\nInvalid Choice.")