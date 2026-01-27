tuple = (10, 20, 30, 50, 60)
print(tuple)

# single tuple
tup = (30,) # for single tuple comma important
print(tup)

# Accesing elements
print(tuple[0])
print(tuple[-1])

# Slicing a tuple
print(tuple[0:4])

# Tuple Functions
print(len(tuple))
print(max(tuple))
print(min(tuple))
print(sum(tuple))

# Tuple Methods
print(tuple.count(20))
print(tuple.index(30))

#Nested Tuple
t = (1, 3, 5), (6,7,8)
print(t[1][0])
print(t[0][0])
