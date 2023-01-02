# Solution 1
# O(m * (m + n)) time | O(1) space
def generateDocument(characters, document):
    for character in document:
        document_frequency = count_character_frequency(character, document)
        character_frequency = count_character_frequency(character, characters)
        if document_frequency > character_frequency:
            return False
    return True

def count_character_frequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1
    return frequency


# Solution 2
# O(c * (n + m)) time | O(c) space
def generateDocument(characters, document):
    already_counted = set()
    for character in document:
        document_frequency = count_character_frequency(character, document)
        character_frequency = count_character_frequency(character, characters)
        if document_frequency > character_frequency:
            return False
        already_counted.add(character)
    return True

def count_character_frequency(character, target):
    frequency = 0
    for char in target:
        if char == character:
            frequency += 1
    return frequency

# Solution 3
# 0(n + m) time | O(c) space
def generateDocument(characters, document):
    character_counts = {}

    for character in characters:
        if character not in character_counts:
            character_counts[character] = 0

        character_counts[character] += 1

    for character in document:
        if character not in character_counts or character_counts[character] == 0:
            return False
        character_counts[character] -= 1

    return True