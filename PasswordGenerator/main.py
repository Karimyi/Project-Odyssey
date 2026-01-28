#Simple Password Generator

import random

def generate_password(length):
    i, password = 1, ""
    while (i <= length):
        password = password + chr(random.randint(33,126))
        i = i + 1
    return password

if __name__ == "__main__":
    print("Password generator. Enter the desired password length:\n")
    try:
        length = int(input())
        print(generate_password(length))
    except Exception: print("An unexpected error occurred")