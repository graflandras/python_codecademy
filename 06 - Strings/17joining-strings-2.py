# We could join this list together with ANY string. One often used string is
# a comma , because then we can create a string of comma separated variables, or CSV.

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!',
                      'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds',
                      'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

# You’ve been asked to join together the strings in the list together
# into a single string that can be used to display the full poem. Name this string winter_trees_full.

winter_trees_full = '\n'.join(winter_trees_lines)
print(winter_trees_full)
