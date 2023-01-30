# Solution 1
# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    new_letters = []
    new_key = key % 26
    for letter in string:
        new_letters.append(get_new_letter(letter, new_key))

    return ''.join(new_letters)

def get_new_letter(letter, key):
    new_letter_code = ord(letter) + key
    return chr(new_letter_code) if new_letter_code <= 122 else chr(96 + new_letter_code % 122)
    

# Solution 2
# O(n) time | O(n) space
def caesarCipherEncryptor(string, key):
    new_letters = []
    new_key = key % 26
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for letter in string:
        new_letters.append(get_new_letter(letter, new_key, alphabet))

    return ''.join(new_letters)

def get_new_letter(letter, key, alphabet):
    new_letter_code = alphabet.index(letter) + key
    return alphabet[new_letter_code % 26]
