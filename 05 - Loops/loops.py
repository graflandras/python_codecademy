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
