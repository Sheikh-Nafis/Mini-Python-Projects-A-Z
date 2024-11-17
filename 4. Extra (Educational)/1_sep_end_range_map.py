'''
# Instead of the default space between arguments in print, 
# you can use the 'sep' parameter to set a custom separator.
'''
print("Hey", "I'm", "seperated", "by \'&\'!", sep=" & ")  # Custom separator '&' between words.



'''
# The 'end' parameter in print allows you to specify what should be printed at the end of a line.
# By default, it adds a newline character ('\n'). Here, it is overridden to prevent a new line.
'''
print("Hey there! My name is first line.", end=" ")  # Prevents a newline after this statement.
print("Hello, I am second line but we do look like a combined line isn' it?\n")   # Continues on the same line as the previous print statement.



# Demonstrating the range function
random_num = range(20)  # Creates a range object from 0 to 19.
print(list(random_num))  # Converts the range to a list and prints the numbers from 0 to 19.
print(f'Printing the range object itself: {random_num}\n')        # Prints the range object itself (not the actual numbers).



# Using the map function to apply operations to all elements in a list
animal_list = ['cat', 'dog', 'chicken', 'tiger', 'turtle']

# Maps the `len` function to each element of the list to get their lengths.
length = map(len, animal_list)  
print(f'Printing the length of the words: {list(length)}')  # Converts the map object to a list and prints the lengths of the words.

# Using a lambda function in map to modify each element in the list.
length = map(lambda x: x + 's', animal_list)  # Adds an 's' to each word in the list.
print(f'Updated the names of the list by using the lambda funtion: {list(length)}')  # Prints the updated list with 's' added to each word.

# Manually applying the same operation as the lambda function using a custom function
def word_s(mylist):  # Defines a function that appends 's' to a given string.
    return mylist + 's'

length = map(word_s, animal_list)  # Applies the custom function to each element in the list.
print(f'Updated the names of the list by using the user defined funtion: {list(length)}')  # Prints the updated list with 's' added to each word.