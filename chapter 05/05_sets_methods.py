#  Creating an empty set.
b = set()
print(type(b))

#  Adding values to an empty sets.
b.add(4) 
b.add(5)
# b.add(5) # Adding a value repeatedly does not changes a set. 
b.add((4,5,6))
# b.add({4,5,6,}) #Cannot add list or dictionary to sets.

print(b) 

# Length of the set.
print(len(b)) # Prints the length of this sets.

# Removalof an item.
b.remove(4) # Removes 5 from set b.
# b.removr(12) # Throws an error while trying to remove 12 (which is not present in a set.)
print(b)

print(b.pop())




