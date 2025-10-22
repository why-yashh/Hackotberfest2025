import random
import time
import os

def clear_screen():
    # Works for both Windows and Unix-based systems
    os.system('cls' if os.name == 'nt' else 'clear')

def number_memory_game():
    level = 1
    print("🔢 Welcome to the Number Memory Game!")
    print("You’ll see a number for a few seconds. Try to remember it!\n")
    
    while True:
        number = ''.join(str(random.randint(0, 9)) for _ in range(level))
        print(f"Level {level}: Remember this number → {number}")
        time.sleep(3)
        clear_screen()

        guess = input("Enter the number you remember: ")

        if guess == number:
            print("✅ Correct! Moving to the next level...\n")
            level += 1
            time.sleep(1.5)
            clear_screen()
        else:
            print(f"❌ Wrong! The correct number was {number}.")
            print(f"You reached Level {level}.")
            break

if __name__ == "__main__":
    number_memory_game()
