# my_string[length-4:]
# Write a function called password_generator that takes two inputs, first_name
# and last_name and then concatenate the last three letters of each and returns them as a string.

first_name = "Reiko"
last_name = "Matsuki"


def password_generator(first_name, last_name):
    first_name_length = len(first_name)
    last_name_length = len(last_name)
    password = first_name[first_name_length-3:] + \
        last_name[last_name_length-3:]
    return password


temp_password = password_generator(first_name, last_name)
print(temp_password)
