
import secrets
import string

def generate_password(length, use_numbers, use_symbols):
    letters=string.ascii_letters
    characters=letters
    required=[]

    if use_numbers:
        characters+=string.digits
        required.append(secrets.choice(string.digits))

    if use_symbols:
        characters+=string.punctuation
        required.append(secrets.choice(string.punctuation))

    password=required[:]

    for _ in range(length-len(password)):
        password.append(secrets.choice(characters))

    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

try:
    length=int(input("Enter password length (minimum 8): "))

    if length<8:
        print("Password length must be at least 8.")
    else:
        numbers=input("Include numbers?(yes/no): ").lower()
        symbols=input("Include special characters?(yes/no): ").lower()

        if numbers not in ("yes", "no") or symbols not in ("yes","no"):
            print("Please enter yes or no.")
        else:
            password=generate_password(length,numbers=="yes",symbols=="yes")
            print("Generated Password:",password)

except ValueError:
    print("Invalid input! Please enter a valid number.")
