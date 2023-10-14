import re

def main():
    email = input("What's your email: ").strip()
    
    if email:
        print("VALID email format")
    else:
        print("INVALID email format")

def validate_email(email):
    valid_email = False
    if re.search(r"^\w+@(\w|\w+\.)+\.(com|ar)$", email, re.IGNORECASE):
        valid_email = True

    return valid_email


if __name__ == "__main__":
    main()
