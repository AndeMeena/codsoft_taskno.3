import random
import string

def generate_password(length, include_uppercase, include_digits, include_symbols):
    # Define character pools
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    digits = string.digits if include_digits else ""
    symbols = string.punctuation if include_symbols else ""
    
    # Combine selected character pools
    all_characters = lowercase + uppercase + digits + symbols
    
    if not all_characters:
        return "Error: No character types selected!"
    
    # Generate the password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        # User input
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Error: Password length must be greater than 0!")
            return
        
        # Complexity options
        include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        include_digits = input("Include digits? (y/n): ").lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        
        # Generate and display password
        password = generate_password(length, include_uppercase, include_digits, include_symbols)
        print("\nGenerated Password:", password)
    except ValueError:
        print("Error: Please enter a valid number for the password length.")

if _name_ == "_main_":
    main()