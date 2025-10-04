```java
import java.util.Random;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Hangman game = new Hangman();
        game.start();
    }
}

class Hangman {
    private static final String ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    private static final int WORD_LENGTH = 6;
    private final Random random = new Random();
    private final Scanner scanner = new Scanner(System.in);
    private final char[] word = new char[WORD_LENGTH];
    private final char[] display = new char[WORD_LENGTH];
    private int attemptsRemaining = 6;

    public void start() {
        generateWord();
        System.out.println("Guess the " + WORD_LENGTH + "-letter word:");
        displayWord();
        play();
    }

    private void generateWord() {
        for (int i = 0; i < WORD_LENGTH; i++) {
            word[i] = ALPHABET.charAt(random.nextInt(ALPHABET.length()));
            display[i] = '_';
        }
    }

    private void displayWord() {
        for (int i = 0; i < WORD_LENGTH; i++) {
            System.out.print(display[i] + " ");
        }
        System.out.println();
    }
```
