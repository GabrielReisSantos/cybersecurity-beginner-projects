import re

def check_password_strength(password):
    length = len(password) >= 8
    digit = re.search(r"\d", password)
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if all([length, digit, upper, lower, symbol]):
        return "Strong password"
    else:
        return "Weak password"

pwd = input("Enter a password: ")
print(check_password_strength(pwd))
