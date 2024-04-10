#aradhanahegde
def encode_password(password):
    encoded_password = ""
    for digit in password:
        # Convert digit to integer, add 3, take modulo 10 to wrap around if needed
        encoded_digit = (int(digit) + 3) % 10
        encoded_password += str(encoded_digit)
    return encoded_password

def decode_password(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        digit = int(digit) - 3
        decoded_password = f"{decoded_password}{digit}"
    return decoded_password

def main():

    while True:
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit")

        option = input("Please enter an option: ")

        if option == '1':
            password = input("Please enter your password to encode: ")
            if len(password) != 8 or not password.isdigit():
                print("Invalid password format. Please enter 8 digits.")
                continue
            print("Your password has been encoded and stored!")

        elif option == '2':
            print(f"The encoded password is {encode_password(password)}, and the original password is {decode_password(encode_password(password))}.")

        elif option == '3':
            break


        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()