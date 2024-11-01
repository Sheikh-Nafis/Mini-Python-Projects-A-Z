import random

# Get user input
store = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissor: "))

# Generate computer's choice
random_choice = random.randint(0, 2)

# Display user choice
if store == 0:
    print("You chose: Rock.")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif store == 1:
    print("You chose: Paper.")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
elif store == 2:
    print("You chose: Scissor.")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")
else:
    print("Invalid choice. Please choose 0, 1, or 2.")
    exit()

# Display computer's choice
if random_choice == 0:
    print("Computer chose: Rock.")
    print("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
elif random_choice == 1:
    print("Computer chose: Paper.")
    print("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
else:
    print("Computer chose: Scissor.")
    print("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

# Determine the outcome
if store == random_choice:
    print("Draw!")
elif (store == 0 and random_choice == 2) or (store == 1 and random_choice == 0) or (store == 2 and random_choice == 1):
    print("You win!")
else:
    print("You lose!")
