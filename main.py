import random
import string

def generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars):
    characters = ''

    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase
    if include_numbers:
        characters += string.digits
    if include_special_chars:
        characters += string.punctuation

    if not characters:
        print("Please include at least one character type.")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
length = int(input("Enter the length of the password: "))
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
include_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
include_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

password = generate_password(length, include_uppercase, include_lowercase, include_numbers, include_special_chars)

if password:
    print(f"Generated Password: {password}")

