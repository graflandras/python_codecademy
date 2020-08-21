# Let’s say we have two lists that we want to combine into a dictionary, like a list of students and a list of their heights, in inches:

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# Python allows you to create a dictionary using a list comprehension, with this syntax:
#dictionary = {key:value for key, value in zip(list1, list2)}


# You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First, create a variable called zipped_drinks that is a zipped list of pairs between the drinks list and the caffeine list.

zipped_drinks = zip(drinks, caffeine)

# Create a dictionary called drinks_to_caffeine by using a list comprehension that goes through the zipped_drinks list and turns each pair into a key:value item.
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(drinks_to_caffeine)
