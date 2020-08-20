# Previously with .format(), you had to make sure that your variables appeared
# as arguments in the same order that you wanted them to appear in the string,
# which just added unnecessary complications when writing code. By including
# keywords in the string and in the arguments, you can remove that ambiguity.
# Let’s look at an example.

def favorite_song_statement(song, artist):
    return "My favorite song is {song} by {artist}.".format(song=song, artist=artist)


# The function poem_description is supposed to use .format() to print out
# some quick information about a poem, but it seems to be causing some
# errors currently. Fix the function by using keywords in the .format() method.

def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(
        publishing_date=publishing_date, author=author, title=title, original_work=original_work)
    return poem_desc


# Run poem_description with the following arguments and save the results to the variable my_beard_description:
author = "Shel Silverstein"
title = "My Beard"
original_work = "Where the Sidewalk Ends"
publishing_date = "1974"

my_beard_description = poem_description(
    publishing_date, author, title, original_work)
print(my_beard_description)
