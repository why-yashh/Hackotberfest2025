import time
import random

def typing_speed_test():
    sentences = [
        "The quick brown fox jumps over the lazy dog.",
        "Python makes programming fun and efficient.",
        "Artificial Intelligence is transforming the world.",
        "Practice makes a person perfect in coding.",
        "Always write clean and readable code."
    ]
    
    sentence = random.choice(sentences)
    print("\nType the following sentence as quickly and accurately as you can:\n")
    print(f"👉 {sentence}\n")

    input("Press Enter when you're ready to start...")
    start_time = time.time()
    
    typed_sentence = input("\nStart typing here:\n")
    end_time = time.time()
    
    time_taken = round(end_time - start_time, 2)
    words = len(sentence.split())
    wpm = round((words / time_taken) * 60, 2)
    
    # Calculate accuracy
    correct_chars = 0
    for i in range(min(len(sentence), len(typed_sentence))):
        if sentence[i] == typed_sentence[i]:
            correct_chars += 1
    
    accuracy = round((correct_chars / len(sentence)) * 100, 2)
    
    print("\n--- Results ---")
    print(f"Time Taken: {time_taken} seconds")
    print(f"Words Per Minute: {wpm}")
    print(f"Accuracy: {accuracy}%")

if __name__ == "__main__":
    typing_speed_test()
