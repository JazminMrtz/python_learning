# collection = single "variable" used to store multiple values
#    List = [] ordered and changeable. Duplicates OK
#    Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#    Table = () ordered and unchangeable. Duplicates OK. FASTER

fruits = ["apple", "orange", "banana", "coconut", "strawberry", "grape"]
# print(dir(fruits)) #attributes for the lists

# print(help(fruits))

# print(len(fruits)) #counts how many words there are

# print("apple" in fruits) #find if value is in a list... true or false

# fruits[0] = "pineapple" #reassign value
# fruits.append("pineapple") #adds
# fruits.remove("apple") #removes a value
# fruits.insert(0, "pineapple") #adds a value
# fruits.sort() #sorts it
# fruits.reverse() #reverses the order
# fruits.clear() #clears it out

# print(fruits[0])

# for fruit in fruits:
#     print(fruit)