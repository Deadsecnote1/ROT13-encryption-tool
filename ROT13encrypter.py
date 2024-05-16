print("ROT13 encrypter")
print(" ")

# Prompt user for input text
text = input("Enter your text: ")

# Define alphabets
alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Initialize variable to save encoded text
encoded_text = ""

# Function for encoding a single character
def encryption(item):
    if item in alphabet_lower:
        # Calculate new index with wrap-around using modulo operation
        index = (alphabet_lower.index(item) + 13) % 26
        encoded_item = alphabet_lower[index]
    elif item in alphabet_upper:
        # Calculate new index with wrap-around using modulo operation
        index = (alphabet_upper.index(item) + 13) % 26
        encoded_item = alphabet_upper[index]
    else:
        # Non-alphabet characters remain unchanged
        encoded_item = item
    return encoded_item

# Loop through each character in the input text
for item in text:
    encoded_text += encryption(item)

# Print the encoded text
print(encoded_text)
