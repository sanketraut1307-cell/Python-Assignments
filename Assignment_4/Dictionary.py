dict = {"Name" : "Parth",
        "Marks" : 100,
        "age" : 19}
print(dict)

# Accesing Dictionary
print(dict["Name"])
print(dict.get("Name")) #Another method

#Adding new key value pair in dictionary
dict["city"] = "Pune"
print("updated Dictionary:" , dict)

#Updating dictionary
dict["Marks"] = 101
print("Updated Dictionary:", dict)

# Removing elements from Dictionary
dict.pop("age")
print("After deleting age :", dict)
dict.popitem() # It will remove last incerted key value pair
print(dict)
del dict["Name"]
print("After del name:", dict)
dict.clear() #clear all values in dict
print(dict)

#new
dict1 = {1, 2, 3, 4}
dict2 = {4, 5, 6, 8}
print(dict1, dict2)

# Dictionary function
print(len(dict1))

#Nested Dictionary
s1 = {"name": "parth", "marks": 100}
s2 = {"name": "Neha", "marks": 90}


students = {"s1" : s1,  #Here we nested the dictionary other wise error getting
            "s2" : s2
            }
print(students["s1"]["marks"])   

#Merging the dictionary
merg = s1 | s2
print(merg)
