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
all_students = ["Alex", "Briana", "Cheri", "Daniele", "Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)
  
print(students_in_poetry)