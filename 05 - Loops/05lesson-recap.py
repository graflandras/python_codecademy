# Lesson recap
# Create a list called single_digits that consists of the numbers 0-9 (inclusive).
single_digits = range(10)

# Create a for loop that goes through single_digits and prints out each one.
squares = []
for number in single_digits:
    print(number)
    squares.append(number**2)
print(squares)
# Before the loop, create a list called squares. Assign it to be an empty list to begin with.

# Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.

# Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.
cubes = [number**3 for number in single_digits]
print(cubes)
