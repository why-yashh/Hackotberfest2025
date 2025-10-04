import random

class AIDetective:
    def __init__(self):
        self.case_solved = False
        self.clues = []
        self.suspects = ["Mr. Green", "Mrs. White", "Colonel Mustard", "Miss Scarlet"]
        self.weapons = ["Candlestick", "Knife", "Lead Pipe", "Revolver"]
        self.rooms = ["Library", "Kitchen", "Ballroom", "Conservatory"]
        self.solution = {
            "culprit": random.choice(self.suspects),
            "weapon": random.choice(self.weapons),
            "room": random.choice(self.rooms)
        }

   //bad logic 
import java.util.*;

class Main {
    public static void main(String args[]) {
        Hang hm = new Hang();
        hm.Generate();
    }
}

class Hang {
    Random rd = new Random();
    Scanner sc = new Scanner(System.in);
    String s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int n = s.length();
    char[] c = new char[6]; // Array for random letters
    char[] c1 = {'_', '_', '_', '_', '_', '_'}; // Array to display guessed letters
    int maxAttempts = 6; // Maximum allowed attempts

    void Generate() {
        // Generate a random 6-letter word
        for (int i = 0; i < 6; i++) {
            c[i] = s.charAt(rd.nextInt(n));
        }

        System.out.println("Guess the 6-letter word:");
        displayWord();
        Function();
    }

    void displayWord() {
        // Display the current state of the guessed word
        for (int i = 0; i < 6; i++) {
            System.out.print(c1[i] + " ");
        }
        System.out.println();
    }

    void Function() {
        int attempts = 0;

        // Loop until the word is guessed or attempts are exhausted
        while (attempts < maxAttempts && !isWordGuessed()) {
            System.out.println("Enter your guess (a single letter): ");
            char guess = sc.nextLine().toUpperCase().charAt(0);

            boolean correctGuess = false;

            // Check if the guessed letter is in the word
            for (int i = 0; i < 6; i++) {
                if (c[i] == guess && c1[i] == '_') {
                    c1[i] = guess;
                    correctGuess = true;
                }
            }

            // If the guess was incorrect, increment attempts
            if (!correctGuess) {
                attempts++;
                System.out.println("Wrong guess! Attempts left: " + (maxAttempts - attempts));
            }

            // Display the current state of the word
            displayWord();
        }

        // Check if the word was fully guessed
        if (isWordGuessed()) {
            System.out.println("You've guessed the word correctly.");
        } else {
            System.out.println("You've run out of attempts. The word was: " + Arrays.toString(c));
        }
    }

    boolean isWordGuessed() {
        for (char ch : c1) {
            if (ch == '_') {
                return false;
            }
        }
        return true;
    }
}

    def get_clue(self):
        if len(self.clues) < 5:
            new_clue = random.choice([
                f"I found traces of {self.solution['weapon'].lower()} in the {self.solution['room'].lower()}.",
                f"{self.solution['culprit']} was seen near the {self.solution['room'].lower()} earlier.",
                f"A witness heard a commotion in the {self.solution['room'].lower()}.",
                f"{self.solution['culprit']} had a motive for the crime.",
                f"The {self.solution['weapon'].lower()} seems to be missing from its usual place."
            ])
            if new_clue not in self.clues:
                self.clues.append(new_clue)
                return new_clue
            else:
                return self.get_clue()
        else:
            return random.choice(self.clues)

    def solve_case(self, culprit, weapon, room):
        if (culprit == self.solution["culprit"] and
            weapon == self.solution["weapon"] and
            room == self.solution["room"]):
            self.case_solved = True
            return "Congratulations! You've solved the case!"
        else:
            return "I'm afraid that's not correct. Let's continue our investigation."

    def play(self):
        self.introduce_game()
        while not self.case_solved:
            user_input = input("What would you like to do? ").strip().lower()
            if user_input == "solve":
                culprit = input("Who is the culprit? ")
                weapon = input("What is the murder weapon? ")
                room = input("In which room did the murder occur? ")
                print(self.solve_case(culprit, weapon, room))
            elif user_input == "quit":
                print("Thank you for playing. The case remains unsolved.")
                break
            else:
                print(self.get_clue())

if __name__ == "__main__":
    game = AIDetective()
    game.play()
