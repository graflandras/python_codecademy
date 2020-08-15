# List Comprehensions
# Let’s say we have scraped a certain website and gotten these words:

words = ["@coolguy35", "#nofilter", "@kewldawg54",
         "reply", "timestamp", "@matchamom", "follow", "#updog"]

# We want to make a new list, called usernames, that has all of the strings
# in words with an '@' as the first character. We know we can do this with a for loop:
# usernames = []
# for word in words:
#    if word[0] == '@':
#        usernames.append(word)
# Python has a convenient shorthand to create lists like this with one line, This is called a list comprehension:

usernames = [word for word in words if word[0] == '@']

# This list comprehension:
# Takes an element in words
# Assigns that element to a variable called word
# Checks if word[0] == '@', and if so, it adds word to the new list, usernames. If not, nothing happens.
# Repeats steps 1-3 for all of the strings in words

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if (height > 161)]
print(can_ride_coaster)

# Being able to create lists with modified values is especially useful when working with numbers. Let’s say we have this list:

my_upvotes = [192, 34, 22, 175, 75, 101, 97]

# We want to add 100 to each value. We can accomplish this goal in one line:

updated_upvotes = [vote_value + 100 for vote_value in my_upvotes]

# This list comprehension:
# Takes a number in my_upvotes
# Assigns that number to a variable called vote_value
# Adds 100 to vote_value
# Appends that sum to the new list updated_upvotes
# Repeats steps 1-4 for all of the numbers in my_upvotes

celsius = [0, 10, 15, 32, -5, 27, 3]
# Using a list comprehension, create a new list called fahrenheit that converts each element in the celsius list to fahrenheit.
fahrenheit = [(celsius_value * 9/5 + 32) for celsius_value in celsius]
print(fahrenheit)
