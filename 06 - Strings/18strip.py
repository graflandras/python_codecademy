# Python provides a great method for cleaning strings: .strip().
# Stripping a string removes all whitespace characters from the beginning and end.
# You can also use .strip() with a character argument,
# which will strip that character from either end of the string.

love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms',
                    '           like flowering mines    ', '\n', '   to conquer me home.    ']

# First, use .strip() on each line in the list to remove the
# unnecessary whitespace and save it as a new list love_maybe_lines_stripped.

love_maybe_lines_stripped = []
for line in love_maybe_lines:
    love_maybe_lines_stripped.append(line.strip())

# .join() the lines in love_maybe_lines_stripped together into one large multi-line string, 
# love_maybe_full, that can be printed to display the poem. Each line of the poem should show up on its own line.

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)
