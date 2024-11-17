# Using the filter function to filter elements of a list based on a condition
animal_list = ['cat', 'dog', 'chicken', 'tiger', 'turtle']

def more_than_three(string):  # Defines a function that checks if the length of a string is greater than 3.
    return len(string) > 3

# Filters the list to include only words with more than 3 letters using a predefined function.
print(f'Showing the filtered words with more than 3 letters using a predefined function: {list(filter(more_than_three, animal_list))}')  # Prints the filtered list.

# Filters the list to include only words with more than 3 letters using a lambda function.
print(f'Showing the filtered words with more than 3 letters using the lambda function: {list(filter(lambda x: len(x) > 3, animal_list))}\n')  # Prints the filtered list.

# Using the sum function to calculate the total of a set of numbers.
numbers = {8, 6, 4, 10, 2}  # A set of numbers (order doesn't matter in sets).
print(f'Sum after using the start function (+20): {sum(numbers, start=20)}')  # Adds 20 to the sum of numbers in the set (30 + 20 = 50).
print(f'Sum after using the start function (-20): {sum(numbers, start=-20)}\n')  # Adds -20 to the sum of numbers in the set (30 - 20 = 10).

# Using the sorted function to sort a set of numbers.
print(f'Ascending order: {sorted(numbers)}')  # Sorts the numbers in ascending order and prints the sorted list.
print(f'Descending order: {sorted(numbers, reverse=True)}\n')  # Sorts the numbers in descending order and prints the sorted list.

# Sorting a list of dictionaries (students) based on a specific key.
print('Sorting a list of dictionaries (students) based on a specific key (number).')
student = [
    {"name": "Nafis", "number": 74},  # Each student is represented as a dictionary.
    {"name": "Alex", "number": 67},
    {"name": "Ben", "number": 80},
    {"name": "Jenyy", "number": 70},
]

# Sorting students by their 'number' in ascending order using a lambda function as the key.
print(f'Ascending order: {sorted(student, key=lambda name: name["number"])}')

# Sorting students by their 'number' in descending order using a lambda function as the key.
print(f'Descending order: {sorted(student, key=lambda name: name["number"], reverse=True)}')