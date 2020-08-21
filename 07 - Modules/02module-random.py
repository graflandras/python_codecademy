# With random, we’ll be using more than one piece of the module’s functionality, so the import syntax will look like:

import random

# random.choice() which takes a list as an argument and returns a number from the list
# random.randint() which takes two numbers as arguments and generates a random number between the two numbers you passed in

# Import random below:
import random

# Create random_list below:
# Remember: Python list comprehensions look like this:
# [what_will_replace_i for i in some_list_or_range]

random_list = [random.randint(1, 101) for i in range(101)]

# Create randomer_number below:
randomer_number = random.choice(random_list)

# Print randomer_number below:
print(randomer_number)
