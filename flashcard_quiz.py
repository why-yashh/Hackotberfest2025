 
questions = {
    "What is the capital of France?": "Paris",
    "Who developed Python?": "Guido van Rossum",
    "What is 9 * 8?": "72",
}

score = 0
for q, a in questions.items():
    ans = input(q + " ")
    if ans.strip().lower() == a.lower():
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! Correct answer: {a}")

print(f"\nFinal Score: {score}/{len(questions)}")
