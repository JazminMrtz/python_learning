#    collection = single "variable" used to store multiple values
#    List = [] ordered and changeable. Duplicates OK
#    Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#    Table = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = {"apple", "orange", "banana", "coconut", "strawberry", "grape"}
# print(dir(fruits)) #attributes for the lists
# print(help(fruits))
# print(len(fruits)) #counts how many words there are

# fruits = ("apple", "orange", "banana", "coconut", "strawberry", "grape")
# print(dir(fruits)) #attributes for the lists
# print(help(fruits))
# print(help(fruits))
# print(len(fruits)) #counts how many words there are



# print("pineapple" in fruits) #find if value is in a list... true or false
# print(fruits[0]) #going to get you an error

# fruits.add("pineapple") #adds to the list
# fruits.remove("apple") #removes from the list
# fruits.pop() #removes an element at the end
# fruits.clear() #clears it out

# fruits[0] = "pineapple" #reassign value
# fruits.append("pineapple") #adds
# fruits.remove("apple") #removes a value
# fruits.insert(0, "pineapple") #adds a value
# fruits.sort() #sorts it
# fruits.reverse() #reverses the order

# # print(fruits.index("apple"))
# print(fruits.count("coconut"))

# # print(fruits)

# for fruit in fruits:
#     print(fruit)


# -----------------------------------------------------------------------

# cars = ["bmw", "maserati", "audi","mercedes", "ferrari"]
# # print(f"these are lists of {cars}")
# # print(f"the first car is {cars[0]}")

# # # changing the value of the list
# # cars[0] = "toyota"
# # print(f"the first car is {cars[0]}")

# # print(f"the last car is {cars[-1]}")
# # cars[-1] = "lamborghini"
# # print(f"the last car is {cars[-1]}")

# # # adding a new value to the lists
# # cars.append("bugatti")
# # print(cars)
# # cars.remove("maserati")
# # print(cars)

# # looping through the list
# # otherwise called iterating through the list
# for car in cars:
# #   print(len(car))
# #   print(car)
# #   carRequest = input("add a new car please: ")
# #   cars.append(carRequest)
# #   print(cars)
#     print(len(cars))
#     print(cars.upper())
#     print(cars)
#     if len(cars) > 10:
#         break

# -------------------------------------------------------

# # challenge
# # create a list of friends
# friends = []
# # make sure the initial list is none
# # add a new friend to the list, add at least 5 friends
# friends = ["Zayla", "Leo", "Jacky", "Cristal", "Lesly"]
# # remove a friend
# friends.remove("Jacky")
# # insert a friend at a specific index maybe 2
# friends.apprend("Lucy", [2])
# # print the list of friends
# print(friends)
# # loop through the list and print the friends name
# print(friends)
# # if the list is greater than 10 break the loop
# for friend in friends:
#     print(friends)
#     if len(friends) > 10:
#      break

# ------------------ DICTIONARIES ------------------------

# dictionary = collection of {key:value} pairs
#               ordered and changeable. No duplicates

capitals = {"USA": "Washington, D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
# if capitals.get("China"):
#     print("That capital exists.")
# else:
#     print("That capital doesn't exist.")

# capitals.update({"Germany": "Berlin",
#                  "Mexico": "Cuidad de Mexico"
#                  "Chile": "Santiago"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China") #removes last element
# capitals.popitem() #pop offs certian element
# # capitals.clear() #clears
# print(capitals)

# keys = capitals.keys()
# for key in capital.keys():
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capital.items() #returns keys and values
# for key, value in capitals.items()
#     print(f"{key}: {value}")