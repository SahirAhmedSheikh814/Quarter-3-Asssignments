import random
import string
import pyperclip  # To copy password to clipboard

# Constants for different character types
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits
SYMBOLS = string.punctuation
ALL_CHARACTERS = LOWERCASE + UPPERCASE + DIGITS + SYMBOLS

def generate_password(length=12, use_upper=True, use_digits=True, use_symbols=True):
    """
    Generates a random password based on user preferences.

    Parameters:
    - length (int): Desired length of the password (default: 12)
    - use_upper (bool): Include uppercase letters
    - use_digits (bool): Include numbers
    - use_symbols (bool): Include special characters

    Returns:
    - str: Generated password
    """
    characters = LOWERCASE  # Start with lowercase letters
    if use_upper:
        characters += UPPERCASE
    if use_digits:
        characters += DIGITS
    if use_symbols:
        characters += SYMBOLS

    if length < 4:
        print("⚠️ Password length must be at least 4 characters.")
        return None

    password = "".join(random.sample(characters, length))
    return password

def main():
    print("🔐 Welcome to the Secure Random Password Generator 🔐")

    try:
        length = int(input("📏 Enter password length (min 4): "))
        use_upper = input("🔠 Include uppercase letters? (y/n): ").strip().lower() == 'y'
        use_digits = input("🔢 Include numbers? (y/n): ").strip().lower() == 'y'
        use_symbols = input("🔣 Include special characters? (y/n): ").strip().lower() == 'y'

        password = generate_password(length, use_upper, use_digits, use_symbols)

        if password:
            print(f"\n✅ Your Secure Password: {password}")
            pyperclip.copy(password)
            print("📋 Password copied to clipboard!")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()