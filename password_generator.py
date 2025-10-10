import random
import string

class PasswordGenerator:
    def __init__(self, length=8):
        self.length = length
        self.characters = string.ascii_letters + string.digits + string.punctuation

    def set_length(self, length):
        """Set the desired password length."""
        self.length = length

    def generate_password(self):
        """Generate and return a random password."""
        password = ''.join(random.choice(self.characters) for _ in range(self.length))
        return password

def main():
    print("🔐 Simple Password Generator 🔐")
    
    # Create an object of PasswordGenerator
    generator = PasswordGenerator()

if __name__ == "__main__":
    main()
