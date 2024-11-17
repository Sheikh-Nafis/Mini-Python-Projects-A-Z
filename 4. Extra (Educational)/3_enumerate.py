# Using the enumerate function to get index-value pairs from a list
animal_list = ['cat', 'dog', 'chicken', 'tiger', 'turtle']  # Sample list of animals.

# Convert the enumerated object into a list of tuples where each tuple contains (index, value).
print(f'Printing index-value pairs for each element in the list: {list(enumerate(animal_list))}\n')  # Prints index-value pairs for each element in the list.

# Enumerate in a for loop to get both index and value while iterating over a list.
print("Printing the index (starting from 1) and the corresponding element")
for index, element in enumerate(animal_list):  
    # Prints the index (starting from 1) and the corresponding element.
    print(f'{index + 1}. {element}')  