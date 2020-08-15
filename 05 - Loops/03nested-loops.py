# Nested Loops
# What if we have a list made up of multiple lists? How can we loop through all of the individual elements?
# Suppose we are in charge of a science class, that is split into three project teams:

project_teams = [["Ava", "Samantha", "James"],
                 ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

# If we want to go through each student, we have to put one loop inside another:
for team in project_teams:
    for student in team:
        print(student)

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0
for location in sales_data:
    print(location)
    for number in location:
        scoops_sold += number

print(scoops_sold)
