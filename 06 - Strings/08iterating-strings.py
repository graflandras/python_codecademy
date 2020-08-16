# def print_each_letter(word):
# for letter in word:
#   print(letter)

# Write a new function called get_length() that takes a string as an input and returns the number
# of characters in that string. Do this by iterating through the string, don’t cheat and use len()!

def get_length(string):
    sum_of_chars = 0
    for letter in string:
        sum_of_chars += 1
    return sum_of_chars


print(get_length("four"))
