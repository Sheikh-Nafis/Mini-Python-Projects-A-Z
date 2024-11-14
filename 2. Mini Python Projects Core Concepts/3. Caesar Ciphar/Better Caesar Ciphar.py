from Ciphar_Ascii_Art import ascii_art
def caesar(switch_mode, message, caesar_value):
    encrypt_or_decrypt_text = []

    for char in message:
        if char.isalpha(): # Only encrypt alphabetic characters
            if switch_mode == 'encode': # Shift the character by 'shift' positions within the alphabet, wrapping around if needed
                new_char = chr((ord(char) - ord('a') + caesar_value) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('a') - caesar_value) % 26 + ord('a'))
            encrypt_or_decrypt_text.append(new_char)
        else: # Non-alphabetic characters remain unchanged
            encrypt_or_decrypt_text.append(char)
    print("".join(encrypt_or_decrypt_text))


print(ascii_art)
while True:
    set_fuction = input("Type 'encode' to encrypt or type 'decode' to decrypt:\n")
    if set_fuction == 'encode' or set_fuction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the desired shift number:\n"))
        caesar(switch_mode = set_fuction, message = text, caesar_value = shift)
    else:
        print("Wrong input! Please try again.")

    x = input("Do you want to encode/decode again? Type 'yes' or 'no'\n").lower()

    if x == 'no':
        print("See you!")
        break
    elif x == 'yes':
        pass
    else:
        print("Wrong input! Please try again.")
        pass