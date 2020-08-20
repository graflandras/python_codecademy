# We can do this type of check more efficiently using with for .. in:
# >>>letter in word. Here, letter in word is a boolean expression that
# is True if the string letter is in the string word.
# It works not only with letters, but with entire strings as well.
# >>> "blue" in "blueberry"
# True

# Write a function called contains that takes two arguments, big_string and little_string and returns True if big_string contains little_string.
# For example contains("watermelon", "melon") should return True and contains("watermelon", "berry") should return False.

def contains(big_string, little_string):
    return little_string in big_string

# Write a function called common_letters that takes two arguments,
# string_one and string_two and then returns a list with all of the letters they have in common.

def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common

#for the temporary password, they want the function to take the input user name and 
# shift all of the letters by one to the right, so the last letter of the username 
# ends up as the first letter and so forth. For example, if the username is AbeSimp, 
# then the temporary password generated should be pAbeSim. Start by defining the 
# function password_generator so that it takes one input, username and in it define 
# an empty string named password.

