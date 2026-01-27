lst = [ 30, 20, 50, 40, 10]
print(lst)

# Accesing elements in list
print(lst[0])
print(lst[-1])

# Slicing elemints in list
print(lst[0:4])
print(lst[3:5])

# Updating or Modifing list
lst[0] = 80
print(lst)

# Adding elements in list
lst.append(100) #It will at end of list
print(lst)
lst.insert(1, 100) #It will add where we give index 
print(lst)

# Removing elements from List
lst.remove(100) #Remove specific element in the list we gave to remove
print(lst)
lst.pop()
print(lst) #Remove last element from the list
lst.pop(1)
print(lst) #Remove specific index which we gave 
# lst.clear() #Clear or remove or empty the list
# print(lst)

# List Functions
print(len(lst)) #length of list
print(max(lst)) #Maximum number in list
print(min(lst)) #Minimum number in list
print(sum(lst)) # Sum of all elements present in the list

#Searching and Sorting in List
lst.sort() #print the element in ascending order
print(lst)
lst.reverse() # print the elements in decending or reverse order
print(lst)
print(lst[::-1]) #reversing the list another method

# Searching elements in the List
print(lst.index(80)) #Show which index the element present
print(lst.count(10)) #Number of times specific element repeated in list
