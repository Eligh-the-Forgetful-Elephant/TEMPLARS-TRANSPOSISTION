# Define a dictionary to store the rotation values for each character
rotation_values = {
    'A': ['N', 'C', 'Q', 'A'],
    'B': ['Y', 'K', 'S', 'X', '-'],
    'C': ['O', 'B', '.', '0', 'A'],
    'D': ['M', 'R', '2', '9', 'S'],
    'E': ['0', 'J', '0', 'Z', '!'],
    'F': ['A', '1', 'P', 'B', 'B'],
    'G': ['L', '!', 'A', 'J', 'T'],
    'H': ['Z', 'A', 'R', 'Y', '?'],
    'I': ['P', '7', 'O', '1', 'C'],
    'J': ['K', 'S', '1', '6', '8'],
    'K': ['5', '.', 'N', 'C', 'Q'],
    'L': ['Q', 'D', 'B', 'K', '9'],
    'M': ['J', '0', '5', '.', 'D'],
    'N': ['!', 'L', '3', '2', '7'],
    'O': ['B', 'Z', '4', '7', 'P'],
    'P': ['9', 'T', 'M', 'D', '5'],
    'Q': ['I', '2', '7', 'L', 'E'],
    'R': ['4', 'I', '6', '8', '6'],
    'S': ['F', '8', '8', '3', '3'],
    'T': ['1', 'Y', '9', 'F'],
    'U': ['?', '5', 'L', 'E', 'O'],
    'V': ['C', 'M', 'C', 'M', '4'],
    'W': ['6', '9', '!', '!', 'G'],
    'X': ['H', 'W', 'J', '4', '1'],
    'Y': ['D', '6', 'Z', '?', 'N'],
    'Z': ['7', 'H', 'D', 'F', 'Z'],
    '1': ['U', 'Q', 'V', 'N', 'H'],
    '2': ['G', '4', 'K', 'W', 'W'],
    '3': ['.', 'N', 'Y', '5', 'Y'],
    '4': ['8', 'X', 'E', 'S', 'X'],
    '5': ['R', 'E', 'X', 'G', 'M'],
    '6': ['E', '?', '?', 'O', 'I'],
    '7': ['2', '3', 'I', 'T', 'V'],
    '8': ['V', 'O', 'U', 'V', 'U'],
    '9': ['S', 'V', 'W', 'R', 'L'],
    '0': ['X', 'U', 'F', 'H', 'J'],
    '.': ['W', 'F', 'H', 'P', '2'],
    '!': ['3', 'P', 'T', 'U', '0'],
    '?': ['T', 'G', 'G', 'Q', 'K']
}

def encrypt(text):
    encrypted_text = ""
    for char in text:
        if char in rotation_values:
            row = int(input("Enter the row for character '{}': ".format(char))
            encrypted_text += rotation_values[char][row - 1]
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text):
    decrypted_text = ""
    for char in text:
        if char in rotation_values:
            row = rotation_values[char].index(input("Enter the character in row {} for '{}': ".format(char, row)))
            decrypted_text += char
        else:
            decrypted_text += char
    return decrypted_text

# Example usage:
text = "HELLO, WORLD!"
encrypted_text = encrypt(text)
print("Encrypted text: ", encrypted_text)

decrypted_text = decrypt(encrypted_text)
print("Decrypted text: ", decrypted_text)
