set1 = {1, 2, 4, 5}
set2 = {3, 1, 6, 8}
print(set1)
print(set2)

# Adding element in the set
set1.add(9) #only one element can be added
print(set1)
set1.update([10, 11, 12, 14]) # Multiple elements can be added
print(set1)

# Removing elements fromt the set
set1.remove(10)
print(set1)
set1.pop() #Any random element can be removed
print(set1)
# set1.clear() # Clear all elements form the set
# print(set1) 

#Set operations
print("Union of set1 and set2:" , set1 | set2)  
print("Union of set1 and set2:" , set1.union(set2)) # Another method
print("Intersection of set1 and set2:" , set1 & set2)  
print("Intersection of set1 and set2:" , set1.intersection(set2)) # Another method
print("Difference between set1 - set2 :", set1 - set2)

# Set Functions
print(len(set1))
print(max(set1))
print(min(set1))
print(sum(set1))
