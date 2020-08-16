# Create a function named reversed_list() that takes two lists of the same size as parameters
# named lst1 and lst2. The function should return True if lst1 is the same as lst2 reversed.
# The function should return False otherwise. For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

def reversed_list(lst1, lst2):
    lst2.reverse()
    if (lst2 == lst1):
        return True
    else:
        return False


# Uncomment the lines below when your function is done
print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))
