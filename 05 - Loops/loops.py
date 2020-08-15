dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
    print(breed)

# For example, if we wanted to print out a "WARNING!" message three times, we would want to say something like:
for i in range(3):
    print("WARNING!")


dog_breeds_available_for_adoption = [
    'french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for dog in dog_breeds_available_for_adoption:
    print(dog)
    if (dog == dog_breed_I_want):
        print("They have the dog I want!")
        break


# When we’re iterating through lists, we may want to skip some values.
# Let’s say we want to print out all of the numbers in a list, unless they’re negative.
# We can use continue to move to the next i in the list:
big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

for i in big_number_list:
    if i < 0:
        continue
    print(i)


# While loops
# You are adding students to a Poetry class, the size of which is capped at 6.
# While the length of the students_in_poetry list is less than 6, use .pop()
# to take a student off the all_students list and add it to the students_in_poetry list.
all_students = ["Alex", "Briana", "Cheri", "Daniele",
                "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
    student = all_students.pop()
    students_in_poetry.append(student)

print(students_in_poetry)


# Nested Loops
# What if we have a list made up of multiple lists? How can we loop through all of the individual elements?
# Suppose we are in charge of a science class, that is split into three project teams:

project_teams = [["Ava", "Samantha", "James"],
                 ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

# If we want to go through each student, we have to put one loop inside another:
for team in project_teams:
    for student in team:
        print(student)

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0
for location in sales_data:
    print(location)
    for number in location:
        scoops_sold += number

print(scoops_sold)


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
