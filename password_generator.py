# Password Generator
import string as s
import secrets

def get_length():
    try:
        length = int(input("Enter the length of the password: "))
        return length
    except:
        print("Error: You must enter the length correctly")
        return get_length() 

def get_chars():
    chars = ""
    x = input("Include letters(y/n): ").lower() == "y"
    y = input("Include numbers(y/n): ").lower() == "y"
    z = input("Include symbols(y/n): ").lower() == "y"
    if x:
        chars += s.ascii_letters
    if y:
        chars += s.digits
    if z:
        chars += s.punctuation
    if not chars:
        print("Error: You must include at least one type of character")
        return get_chars()
    return chars    

def generate_password(length, char):
    password = "".join(secrets.choice(char) for _ in range(length))
    return password    

def main():
    length = get_length()
    char = get_chars()
    password = generate_password(length, char)
    print(f"The password is: {password}")

if __name__ == "__main__":
    main()