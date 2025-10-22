
import re

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Make it at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include digits.")

    if re.search(r"[@$!%*?&]", password):
        score += 1
    else:
        feedback.append("Include special symbols like @$!%*?&.")

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    else:
        strength = "Weak"

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print("-", f)


if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    check_strength(pwd)
