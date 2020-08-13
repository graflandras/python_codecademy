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