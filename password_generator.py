"""
====================================================
Password Generator
Author : Mili
Description:
Generate secure random passwords.
====================================================
"""

import secrets
import string


# ----------------------------------------
# Check Password Strength
# ----------------------------------------

def check_strength(password):

    strength = 0

    if any(c.islower() for c in password):
        strength += 1

    if any(c.isupper() for c in password):
        strength += 1

    if any(c.isdigit() for c in password):
        strength += 1

    if any(c in string.punctuation for c in password):
        strength += 1

    if len(password) >= 12:
        strength += 1

    if strength <= 2:
        return "Weak"

    elif strength <= 4:
        return "Medium"

    else:
        return "Strong"


# ----------------------------------------
# Generate Password
# ----------------------------------------

def generate_password():

    try:

        length = int(input("Enter Password Length : "))

        if length < 4:
            print("Password should be at least 4 characters.")
            return

        use_letters = input("Include Letters? (y/n): ").lower()
        use_numbers = input("Include Numbers? (y/n): ").lower()
        use_symbols = input("Include Symbols? (y/n): ").lower()

        pool = ""

        if use_letters == "y":
            pool += string.ascii_letters

        if use_numbers == "y":
            pool += string.digits

        if use_symbols == "y":
            pool += string.punctuation

        if pool == "":
            print("Select at least one option.")
            return

        password = ""

        for i in range(length):
            password += secrets.choice(pool)

        print("\nGenerated Password")
        print("-------------------------")
        print(password)

        print("\nStrength :", check_strength(password))

    except ValueError:
        print("Please enter a valid number.")


# ----------------------------------------
# Generate Multiple Passwords
# ----------------------------------------

def multiple_passwords():

    try:

        count = int(input("How many passwords? : "))
        length = int(input("Password Length : "))

        pool = (
            string.ascii_letters
            + string.digits
            + string.punctuation
        )

        print()

        for i in range(count):

            password = ""

            for j in range(length):
                password += secrets.choice(pool)

            print(f"{i+1}. {password}")

    except ValueError:
        print("Invalid Input.")


# ----------------------------------------
# Password Menu
# ----------------------------------------

def password_menu():

    while True:

        print("\n" + "=" * 40)
        print("PASSWORD GENERATOR")
        print("=" * 40)
        print("1. Generate Password")
        print("2. Generate Multiple Passwords")
        print("3. Back to Main Menu")
        print("=" * 40)

        choice = input("Enter Choice : ")

        if choice == "1":

            generate_password()

        elif choice == "2":

            multiple_passwords()

        elif choice == "3":

            break

        else:

            print("Invalid Choice.")