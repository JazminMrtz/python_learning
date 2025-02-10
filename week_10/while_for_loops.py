------------------------WHILE LOOPS-------------------------------------
# while loop = execute some code WHILE some condition remains true

name = input("Enter your name:")
# iteration (noun version) = loop over something (verb form)
while name == "":
    print("You did not enter your name")
    name = input("Enter your name")
# infinite loops are bad
print(f"Hello {name}")

age = int(input("Enter your age: "))

while age < 0:
    print("Age can't be negative:")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")

food = input("Enter a food you like (q to quit): ")

while not food == "q":
    print(f"You like {food}")
    food = input("Enter another you like(q to quit): ")
print("Bye!")

num = input("Enter a # between 1-10: ")

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))

print(f"Your number is {num}")

# -----------------------FOR LOOPS-----------------------------------
# for loops = execute a block of code a fixed numger of times
#             you can iterate over a range, string, sequence, etc.
# iterable = more than one thing / multiple
# ------------------range-----------------------------
for x in range(1, 11, 3):
    print(x)

# ------------------string------------------------------
credit_card = "1234-5678-9012-3456"
for x in credit_card:
    print(x) #prints one number each time you print

# -------------------range------------------------------
for x in range(1, 21):
    if x == 13:
        continue #skips over
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break #stops
    else: 
        print(x)
# ----------------------------------------------------------------------------------------------
# create a list of famous movie characters
horror_characters = ["Freddy Krueger","Jason Voorhees","Micheal Myers", "Pennywise", "Chucky"]
# iterate through the list and print each character

for character in horror_characters:
    # print(character)
    # if character == "Jason Voorhees":
    #     continue
    # print(character)
    # if character == "Micheal Myers":
    #     character = "Dracula" #swaps values
    #     continue
    # print(character)
    if character == "Pennywise":
        character = "Reeper"
        print(character)

# ------------------------------------------------------------------------------------------------
# create a list of famous horror movies or your 
horror_movies = ["The Shining, The Nun, Chucky, The Exorcist, Halloween"]
# favorite horror movies
favorite_movies = "Halloween"
# iterate through the list and if a cartain movie is found
for movies in horror_movies:
        print(movies)
# is your least favorite movie, break out of the loop
        if movies == "The Exorcist":
            break
        print(movies)
# print out the rest of the movies
for movies in "horror_movies":
# next replace one of the movies that you like
    if movies == "Halloween":
            movies == "The Conjuring"
            print(movies)