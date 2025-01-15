# #Day 4 Challenge
# #By Liz Gonzales, Cristal Jimenez, Jazmin Martinez, Sofia Barrios, and Lesly Saldana
import random
user_name = input("What's your name? ") # Ask for the user's name
# Generate a random number between 1 and 100
random_num = random.randint(1, 100)

# Initial values of variables (must start with 0 because the game has not started yet.)
num_trials = 0
guess = None

# adding 1 after every trial to the num_trials variable if number is guessed wrong
while num_trials < 8 and guess != random_num:
    guess = int(input(f"Well {user_name}, I've thought of a number between 1 and 100. You have 8 tries to guess it. What number do you think it is? "))
    num_trials += 1

    if guess == random_num: # It is part you are going to be inputing a number and once you find the number 
        print(f"Congratulations, {user_name}! You found the number in {num_trials} trials.") # it is going to give you a congratulations  
    elif guess < random_num:
        print("Wrong, the number is higher.") #if the guess is low, print higher
    else:
        print("Wrong, the number is lower.") #if guess is high, print lower

# If the user doesn't guess correctly after 8 tries, the program ends
if guess != random_num:
    print("Sorry, " + user_name + "you have exceeded 8 trials. The correct number was " + random_num + ".")
#end of programs once max amount of trials is reached
    print("Game Over...")




# ---------------------------------------------------------------------------------------------

# improved code

 
import random

# Ask for the user's name
user_name = input("What's your name? ")

# Generate a random number between 1 and 100
random_num = random.randint(1, 100)

# Initial values of variables
num_trials = 0
guess = None

# Game loop
while num_trials < 8 and guess != random_num:
   
        guess = int(input(f"Well {user_name}, I've thought of a number between 1 and 100. You have {8 - num_trials} tries left. What number do you think it is? "))
        
        # Check if the guess is within range
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
            continue
        
        num_trials += 1

        if guess == random_num:
            print(f"Congratulations, {user_name}! You found the number in {num_trials} trials.")
        elif guess < random_num:
            print("Wrong, the number is higher.")
        else:
            print("Wrong, the number is lower.")
    
        print("Invalid input. Please enter a valid number.")

# If the user doesn't guess correctly after 8 tries
if guess != random_num:
    print(f"Sorry, {user_name}, you have exceeded 8 trials. The correct number was {random_num}.")
    print("Game Over...")




 





