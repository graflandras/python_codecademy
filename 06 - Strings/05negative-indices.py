# There’s a much easier way to do this, we can use negative indices!
# >>> favorite_fruit = 'blueberry`
# >>> favorite_fruit[-1]
# 'y'
# >>> favorite_fruit[-2]
# 'r'
# >>> favorite_fruit[-3:]
# 'rry'

company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

# Use negative indices to find the the second to last character in company_motto. Save this to the variable second_to_last.

second_to_last = company_motto[-2]

# Use negative indices to create a slice of the last 4 characters in company_motto. Save this to the variable final_word.

final_word = company_motto[-4:]
