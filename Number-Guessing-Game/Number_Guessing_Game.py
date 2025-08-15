import random      #Importing random module to generate a random number

#Declaring Global Variables
number_to_guess = random.randint(1,100)     #Randomly generates a number between 1 and 100
number_of_attempts = 0                      #Will be Set later based on difficulty

#Game Introduction
print("Welcome to the Number Guessing Game.")
print("I'm Thinking of a number between 1 and 100.")
choice=(input("Choose Difficulty. Type 'EASY' or 'HARD':")).upper()

#Setting Attempts based on difficulty
if choice == "EASY":
    number_of_attempts = 10      #Easy Mode
elif choice == "HARD":
    number_of_attempts = 5       #Hard Mode
else:
    print("INVALID CHOICE!")
    exit(0)

#Main Game Logic
while (number_of_attempts > 0):
    print(f"\nYou have {number_of_attempts} attempts to guess the number.")
    user_guess=int(input("Enter Your Guess:"))
    number_of_attempts-=1

    #Logic for Guessing Number
    if user_guess == number_to_guess:
        print("You Guessed the correct number.")
        exit(0)

    elif user_guess > number_to_guess:
        print("Too HIGH, Guess Again.")
    
    elif user_guess < number_to_guess:
        print("Too LOW, Guess Again.")
    # print("\n")

print("You LOST! Unable to Guess.")