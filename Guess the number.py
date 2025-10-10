import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 100.")
    print("Can you guess what it is?")

    while True:
        # Ask the player for a guess
        player_guess = input("Enter your guess: ")
        
        try:
            # Convert the guess to an integer
            player_guess = int(player_guess)
        except ValueError:
            print("Please enter a valid number.")
            continue
# Start the game
number_guessing_game()
