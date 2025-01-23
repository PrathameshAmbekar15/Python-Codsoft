import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    # Define possible characters for each category
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation

    # Build the character pool based on the user's preferences
    char_pool = lowercase_chars
    if use_uppercase:
        char_pool += uppercase_chars
    if use_digits:
        char_pool += digits
    if use_special_chars:
        char_pool += special_chars

    # Generate a random password from the selected character pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")

    # Get user input
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input! Please enter a number for the length.")
        return
    
    # Ask about password complexity preferences
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)

    # Display the generated password
    print("\nGenerated Password:", password)

if __name__ == "__main__":
    main()
