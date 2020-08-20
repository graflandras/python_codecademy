highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)
# Start by splitting highlighted_poems at the commas and saving it to highlighted_poems_list.

highlighted_poems_list = highlighted_poems.split(',')

# print(highlighted_poems_list)

# Iterate through highlighted_poems_list using a for loop and for each poem strip away the whitespace and append it to your new list, highlighted_poems_stripped.

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
    highlighted_poems_stripped.append(poem.strip())

# print(highlighted_poems_stripped)

# Iterate through highlighted_poems_stripped and split each string around the : characters and append the new lists into highlighted_poems_details

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
    highlighted_poems_details.append(poem.split(':'))

# Iterate through highlighted_poems_details and for each list in the list append the appropriate elements into the lists titles, poets, and dates.

titles = []
poets = []
dates = []

for poem in highlighted_poems_details:
    titles.append(poem[0])
    poets.append(poem[1])
    dates.append(poem[2])

# Finally, write a for loop that uses either f-strings or .format() to prints out the following string for each poem:
# The poem TITLE was published by POET in DATE.

for i in range(0, len(highlighted_poems_details)):
    print('The poem {} was published by {} in {}'.format(
        titles[i], poets[i], dates[i]))
