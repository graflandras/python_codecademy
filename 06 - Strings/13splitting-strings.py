# .split() is performed on a string, takes one argument, and returns a list of substrings
# found between the given argument (which in the case of .split() is known as the delimiter).
# The following syntax should be used:

# string_name.split(delimiter)

man_its_a_hot_one = "Like seven inches from the midday sun"
print(man_its_a_hot_one.split())
# ['Like', 'seven', 'inches', 'from', 'the', 'midday', 'sun']

commas = "Like, seven, inches, from the midday sun"
print(commas.split(','))