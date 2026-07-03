"""
=========================================
Simple CLI Calculator
Author : Mili
=========================================
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):

    if b == 0:
        return "Error! Division by zero."

    return a / b


def calculator_menu():

    while True:

        print("\n" + "=" * 40)
        print("        SIMPLE CLI CALCULATOR")
        print("=" * 40)
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter your choice: ")

        if choice == "5":
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice!")
            continue

        try:

            num1 = float(input("Enter First Number : "))
            num2 = float(input("Enter Second Number : "))

        except ValueError:

            print("Please enter valid numbers.")
            continue

        if choice == "1":
            answer = add(num1, num2)
            operation = "+"

        elif choice == "2":
            answer = subtract(num1, num2)
            operation = "-"

        elif choice == "3":
            answer = multiply(num1, num2)
            operation = "*"

        else:
            answer = divide(num1, num2)
            operation = "/"

        print("\nResult")
        print("-" * 30)
        print(f"{num1} {operation} {num2} = {answer}")