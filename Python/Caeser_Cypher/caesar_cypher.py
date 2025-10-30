# List of lowercase alphabets for reference
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
             'h', 'i', 'j', 'k', 'l', 'm', 'n',
             'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']


# Function to encrypt the given text using Caesar cipher logic
def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        # Encrypt only alphabetic characters
        if letter.isalpha():
            lower_letter = letter.lower()  # Convert to lowercase for uniform processing
            shifted_index = (alphabet.index(lower_letter) + shift_amount) % 26  # Shift index within 26 letters
            new_letter = alphabet[shifted_index]
            
            # Preserve the original case (upper/lower)
            cipher_text += new_letter.upper() if letter.isupper() else new_letter
        else:
            # Non-alphabetic characters remain unchanged (like space, punctuation, etc.)
            cipher_text += letter  
    print(f"Here is the encoded result: {cipher_text}")


# Function to decrypt the given text using Caesar cipher logic
def decrypt(original_text, shift_amount):
    output_text = ""
    for letter in original_text:
        # Decrypt only alphabetic characters
        if letter.isalpha():
            lower_letter = letter.lower()
            shifted_index = (alphabet.index(lower_letter) - shift_amount) % 26  # Reverse the shift
            new_letter = alphabet[shifted_index]
            
            # Preserve the original case
            output_text += new_letter.upper() if letter.isupper() else new_letter
        else:
            # Keep symbols and numbers as they are
            output_text += letter
    print(f"Here is the decoded result: {output_text}")


# Main program loop to allow multiple encryptions/decryptions
run = "Y"
while run.upper() == "Y":
    # Ask user whether they want to encode or decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
    text = input("Type your message:\n")
    shift = int(input("Type the shift number:\n"))

    # Perform the appropriate operation
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("Invalid direction!")

    # Ask if user wants to continue
    run = input("Do you want to convert more...? Y/N: ").upper()
