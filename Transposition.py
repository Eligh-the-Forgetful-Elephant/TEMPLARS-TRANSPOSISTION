
transposition_cipher = {
    'A': ['N', 'C', 'Q', 'A', '!'],
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
    'T': ['1', 'Y', '9', 'F', '0'],
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

# Function to encrypt a message
def encrypt(message):
    encrypted_message = []
    for char in message:
        if char in transposition_cipher:
            options = transposition_cipher[char]
            encrypted_char = options[0]  # Take the first option
            encrypted_message.append(encrypted_char)
        else:
            encrypted_message.append(char)
    return ''.join(encrypted_message)

# Prompt the user for input
message = input("Enter a message: ")

# Encrypt the message and print it
encrypted_message = encrypt(message)
print("Encrypted Message: " + encrypted_message)
