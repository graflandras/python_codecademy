# Python also provides a handy string method for including variables in strings.
# This method is .format(). .format() takes variables as an argument and includes
# them in the string that it is run on. You include {} marks as placeholders
# for where those variables will be imported.

def favorite_song_statement(song, artist):
    return "My favorite song is {} by {}.".format(song, artist)


favorite_song_statement("Smooth", "Santana")
# "My favorite song is Smooth by Santana"

# Write a function called poem_title_card that takes two inputs:
# the first input should be poet and the second title.
# The function should use .format() to return the following string:
# The poem "[TITLE]" is written by [POET].

def poem_title_card(poet, title):
    poem_desc = "The poem \"{}\" is written by {}.".format(title, poet)
    return poem_desc


print(poem_title_card("Walt Whitman", "I Hear America Singing"))
