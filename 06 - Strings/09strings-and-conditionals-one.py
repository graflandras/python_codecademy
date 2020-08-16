# Write a function called letter_check that takes two inputs, word and letter.
# This function should return True if the word contains the letter and False if it does not.

def letter_check(word, letter):
    for character in word:
        if character == letter:
            return True
    return False
