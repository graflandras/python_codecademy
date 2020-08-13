# Length of a list
list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)

#Selecting List Elements I
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 = employees[4]
print(len(employees))
print(employees[1])

#Selecting List Elements II (Last element)
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = shopping_list[-1]

#Slicing Lists
#list[start:end]
#start is the index of the first element that we want to include in our selection. 
#end is the index of !!!>>one more than the last index that we want to include!!!. 
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]
print(beginning) #>>['shirt', 'shirt', 'pants', 'pants']
middle = suitcase[2:4]
print(middle) #>>['pants', 'pants']

testList = [1, 2, 3, 4, 5, 6, 7, 8]
#Slicing Lists II
#When starting at the beginning of the list, it is also valid to omit the 0:
print(testList[:3]) #>>[1, 2, 3]

#We can do something similar when selecting the last few items of a list:
print(testList[2:]) #>>[3, 4, 5, 6, 7, 8]

#If we want to select the last 3 elements of fruits, we can also use this syntax:
print(testList[-3:]) #>>[6, 7, 8]

#Counting elements in a list
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count('Jake')
print(jake_votes) #>>9

#Sorting Lists I
#Sometimes, we want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.
#We can sort a list in place using .sort(). Sort modifies the original list. 
#sort does not return anything. So, if we try to assign names.sort() to a variable, our new variable would be None. 
#votes.sort()

#Sorting Lists II
#A second way of sorting a list is to use sorted. 
#It comes before a list, instead of after. It generates a new list and does not modifies the original list. 
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games) #>>['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
print(games_sorted) #>>['Minecraft', 'Pacman', 'Pokemon', 'Portal', 'Tetris', 'The Sims']

#Recap
inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']
#inventory is a list of items that are in the warehouse for Bob’s Furniture. How many items are in the warehouse?

#Save your answer to inventory_len.
inventory_len = len(inventory)

#Select the first element in inventory. Save it to the variable first.
first = inventory[0]

#Select the last item from inventory and save it to the variable last.
last = inventory[-1]

#Select items from the inventory starting at index 2 and up to, but not including, index 6. Save your answer to inventory_2_6.
inventory_2_6 = inventory[2:6]

#Select the first 3 items of inventory and save it to the variable first_3.
first_3 = inventory[:3]

#How many 'twin bed's are in inventory? Save your answer to twin_beds.
twin_beds = inventory.count('twin bed')

#Sort inventory using .sort().
inventory.sort()