from Ciphar_Ascii_Art import ascii_art
# my_list = [chr(i) for i in range(97, 123)]
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(switch_mode, message, caesar_value):
        encrypted_text = []
        for char in message:
            if char.isalpha():
                pos = my_list.index(char) # pos = mylist(e) | pos = 5
                if switch_mode == "encode":
                    new_pos = pos + caesar_value # new_pos = 5 + 3 = 8
                else:
                    new_pos = pos - caesar_value # new_pos = 5 - 3 = 2
                new_text = my_list[new_pos] # new_text = mylist[8] = h
                encrypted_text.append(new_text) # encrypted_text = h... and so on
            else:
                encrypted_text.append(char) # encrypted_text = h... and so on
        print(f'The {switch_mode}d message is',''.join(encrypted_text))

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