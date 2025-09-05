"""This program that reads the text file "raw_text.txt", encrypts its contents using a
simple encryption method, and writes the encrypted text to a new file
"encrypted_text.txt". Then create a function to decrypt the content and a function to
verify the decryption was successful."""


def shift_character_forward(character, shift_value, range_start, range_end): 
    ascii_value = ord(character) + shift_value # change character to num and add shift
    if ascii_value > ord(range_end): # wrap around
        ascii_value = ord(range_start) + (ascii_value - ord(range_end) - 1)
    return chr(ascii_value) # change num back to character

def shift_character_backward(character, shift_value, range_start, range_end):
    ascii_value = ord(character) - shift_value # change character to num and subtract shift
    if ascii_value < ord(range_start): # wrap around
        ascii_value = ord(range_end) - (ord(range_start) - ascii_value - 1)
    return chr(ascii_value) # change num back to character

#+++++++++++++++++++++++#
#   Encrypt character   #
#+++++++++++++++++++++++#
def encrypt_letter(character, shift1, shift2): 
    if 'a' <= character <= 'm': #lowercase character a-m
        return shift_character_forward(character, shift1 * shift2, 'a', 'z') #shift forward
    elif 'n' <= character <= 'z': #lowercase character n-z
        return shift_character_backward(character, shift1 + shift2, 'a', 'z') #shift backward
    elif 'A' <= character <= 'M': #uppercase character A-M
        return shift_character_backward(character, shift1, 'A', 'Z') #shift backward
    elif 'N' <= character <= 'Z': #uppercase character N-Z
        return shift_character_forward(character, shift2 ** 2, 'A', 'Z') #shift forward 
    else: #numbers, symbols and punctuations characteracters remain unchanged
        return character

#++++++++++++++++++++++++#
#    Decrypt character   #
#++++++++++++++++++++++++#

def decrypt_letter(character, shift1, shift2, original_character):
    if 'a' <= original_character <= 'm': # original lowercase character a-m
        return shift_character_backward(character, shift1 * shift2, 'a', 'z')
    elif 'n' <= original_character <= 'z': #original lowercase character n-z
        return shift_character_forward(character, shift1 + shift2, 'a', 'z')
    elif 'A' <= original_character <= 'M': #originaluppercase character A-M
        return shift_character_forward(character, shift1, 'A', 'Z')
    elif 'N' <= original_character <= 'Z': #originaluppercase character N-Z
        return shift_character_backward(character, shift2 ** 2, 'A', 'Z')
    else: #numbers, symbols and punctuations characteracters remain unchanged
        return character

def encrypt(text, shift1, shift2):
    return "".join(encrypt_letter(c, shift1, shift2) for c in text) # Encrypt the character

def decrypt(encrypted_text, raw_text, shift1, shift2):
    return "".join(decrypt_letter(enc, shift1, shift2, orig)  # Decrypt the character
                   for enc, orig in zip(encrypted_text, raw_text))

def verify(original_text, decrypted_text):
    if original_text == decrypted_text:
        print("Original and decrypted texts match. Decryption successful!")
    else:
        print("Original and decrypted texts do not match. Decryption failed!")

def get_integer_input(prompt):
    while True:
        value = input(prompt) # Get user input
        if value.isdigit(): # Check if input is a digit
            return int(value) # change to integer and return
        print("Please enter a valid number.") # Repeat the Prompt again if invalid

def main():
    shift1 = get_integer_input("please enter a number for shift1 (number): ") # Get shift1
    shift2 = get_integer_input("please enter a number for shift2 (number): ") # Get shift2

    with open("question1/raw_text.txt", "r", encoding="utf-8") as file: # Read raw text characteracter
        raw_text = file.read() # Read entire content

    encrypted_text = encrypt(raw_text, shift1, shift2) # Encrypt text
    with open("question1/encrypted_text.txt", "w", encoding="utf-8") as file: # Save encrypted text
        file.write(encrypted_text)

    decrypted_text = decrypt(encrypted_text, raw_text, shift1, shift2) # Decrypt text
    with open("question1/decrypted_text.txt", "w", encoding="utf-8") as file: # Save decrypted text
        file.write(decrypted_text)

    verify(raw_text, decrypted_text) # Verify decryption with original text

# Run the main function
main()