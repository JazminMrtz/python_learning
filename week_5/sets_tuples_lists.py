#    collection = single "variable" used to store multiple values
#    List = [] ordered and changeable. Duplicates OK
#    Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#    Table = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "orange", "banana", "coconut", "strawberry", "grape"]
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
cars = ["bmw", "maserati", "audi","mercedes", "ferrari"]
# print(f"these are lists of {cars}")
# print(f"the first car is {cars[0]}")

# # changing the value of the list
# cars[0] = "toyota"
# print(f"the first car is {cars[0]}")

# print(f"the last car is {cars[-1]}")
# cars[-1] = "lamborghini"
# print(f"the last car is {cars[-1]}")

# # adding a new value to the lists
# cars.append("bugatti")
# print(cars)
# cars.remove("maserati")
# print(cars)

# looping through the list
# otherwise called iterating through the list
for car in cars:
#   print(len(car))
#   print(car)
#   carRequest = input("add a new car please: ")
#   cars.append(carRequest)
#   print(cars)
    print(len(cars))
    print(cars.upper())
    print(cars)
    if len(cars) > 10:
        break

# challenge
# create a list of friends
friends = []
# make sure the initial list is none
# add a new friend to the list, add at least 5 friends
friends = ["Zayla", "Leo", "Jacky", "Cristal", "Lesly"]
# remove a friend
friends.remove("Jacky")
# insert a friend at a specific index maybe 2
friends.apprend("Lucy", [2])
# print the list of friends
print(friends)
# loop through the list and print the friends name
print(friends)
# if the list is greater than 10 break the loop
for friend in friends:
    print(friends)
    if len(friends) > 10:
     break