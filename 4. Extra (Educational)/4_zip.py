# Using a for loop to manually combine elements from multiple lists without using zip.
people_list = ['Jenny', 'Alice', 'Nafis', 'Lily', 'Thomas', 'Danny']  # List of 6 names.
ages = [20, 23, 25, 21, 23]  # List of 5 ages.
gender = ['Female', 'Female', 'Male', 'Female']  # List of 4 genders.

# Using the smallest list length to avoid IndexError for uneven lists.
print('Using a for loop to manually combine elements from multiple lists without using zip.')
for idx in range(min(len(people_list), len(ages), len(gender))):  
    people = people_list[idx]  # Get the name from people_list.
    age = ages[idx]  # Get the corresponding age.
    gen = gender[idx]  # Get the corresponding gender.
    # Print information combining all three lists.
    print(f'{people} is {age} years old and is {gen}')




# Using the zip function to combine elements from multiple  lists.
combined = list(zip(people_list, ages, gender))  # Combines the lists into a list of tuples.
print(f'\nPrinting the combined list of tuples: {combined}')  # Prints the combined list of tuples.

# Iterating through the zipped list and printing each person's details.
print('\nUsing the zip function to combine elements from multiple  lists.')
for people, age, gen in combined:  
    # Prints information for each tuple in the zipped list.
    print(f'{people} is {age} years old and is {gen}')