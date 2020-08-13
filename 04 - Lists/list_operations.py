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