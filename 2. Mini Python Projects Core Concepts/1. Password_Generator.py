import random

# List 1: Create a list of letters from a-z and A-Z

# Start with lowercase letters
'''
ord('a') gives the Unicode number for 'a' (97)
ord('z') gives the Unicode number for 'z' (122)
range(ord('a'), ord('z') + 1) creates a range from 97 to 122
The +1 includes 'z' in the range
'''
lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
# The list comprehension [chr(i) for i in ...] converts each number back to a letter

# Now do the same for uppercase letters
uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# Combine the lowercase and uppercase lists into one list
list_letters = lowercase_letters + uppercase_letters

# List 2: Create a list of symbols
list_symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', 
         '+', '{', '}', '[', ']', '|', ':', ';', '"', "'", '<', '>', 
         ',', '.', '?', '/']

# List 3: Create a list of numbers from 0 to 9
list_numbers = [str(i) for i in range(10)]
# The list comprehension [str(i) for i in ...] converts each number to a string

print("Welcome to Password Generator!\n")
new_letter = int(input("How many letters would you like in your password: ")) #14
new_symbol = int(input("How many symbols would you like: ")) #5
new_numbers = int(input("How many numbers would you like:")) #6

password  = []
for let in range(1, new_letter + 1): #1-14
    password.append(random.choice(list_letters))
    # print(password)

for sym in range(1, new_symbol + 1): #1-5
    password.append(random.choice(list_symbols))
    # print(password)

for num in range(1, new_numbers + 1): #1-6
    password.append(random.choice(list_numbers))
    # print(password)

random.shuffle(password)

final_pass = ""

for i in password:
    final_pass += i
print(f'Feel free to copy the new password you generated: {final_pass}')