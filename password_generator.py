import secrets
import string
import pyperclip

def generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "Error: No character types selected."

    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def copy_to_clipboard(password):
    pyperclip.copy(password)
    print("Password copied to clipboard.")

def main():
    while True:
        print("\nPassword Generator Menu")
        try:
            length = int(input("Enter the desired password length: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        if length < 1:
            print("Error: Password length must be at least 1.")
            continue
        
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
        
        if "Error" in password:
            print(password)
        else:
            print(f"Generated password: {password}")
            
            if input("Copy password to clipboard? (y/n): ").lower() == 'y':
                copy_to_clipboard(password)

        if input("Generate another password? (y/n): ").lower() != 'y':
            print("Thank you for using the Password Generator. Goodbye!")
            break

if __name__ == "__main__":
    main()
