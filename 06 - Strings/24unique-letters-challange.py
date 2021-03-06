# Write a function called unique_english_letters that takes the string word as a parameter.
# The function should return the total number of unique letters in the string.
# Uppercase and lowercase letters should be counted as different letters.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:

def unique_english_letters(word):
    unique_letters_final = []
    for letter in word:
        if not letter in unique_letters_final:
          unique_letters_final.append(letter)
    return len(unique_letters_final)

# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4
