import game_data       # Custom module containing the dataset and ASCII art
import random          # For picking random choices
import os              # To clear the console 

#Global Variables
score = 0              # Player's starting score
high = ''              # Stores the correct answer for the round ('A' or 'B')
user_choice = ''       # Stores the player's guess

# Pick the first random option (Choice A)
choice_A=random.choice(game_data.data)


# game keeps running while the player guesses correctly
while(user_choice == high):

    # Display the game logo
    print(game_data.logo)        

    # Show current score
    print(f"Your Score:{score}")  
    
    # Show Choice A details
    print(f"Compare A: {choice_A['name']}, {choice_A['description']}, {choice_A["country"]}")
    
    print(game_data.vs) 

    # Pick a different random option for Choice B
    choice_B = random.choice(game_data.data) 
    # Show Choice B details
    print(f"Against B: {choice_B['name']}, {choice_B["description"]}, {choice_B["country"]}")
    
    # find out which one has more followers
    followers_A = int(choice_A["follower_count"])
    followers_B = int(choice_B["follower_count"])

    if(followers_A>=followers_B):
        high = "A"
    else:
        high = "B"

    # ask player for their guess
    user_choice = (input("Who has more followers: Type 'A' or 'B': ")).upper()
    
    # check if guess is right
    if(user_choice == high):
        score+=1                 # add to score
        choice_A=choice_B        # make B the new A for next round
        os.system("cls")         # clear screen (Windows) - for Mac/Linux use 'clear'
    else:
        # game over
        print("You Lost!")
        print(f"Your final score:{score}")
        break