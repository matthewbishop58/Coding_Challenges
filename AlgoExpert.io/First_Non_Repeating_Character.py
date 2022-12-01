# Solution 1
# O(n^2) time | O(1) space

def firstNonRepeatingCharacter(string):
    for idx in range(len(string)):
        found_duplicate = False
        for idx2 in range(len(string)):
            if string[idx] == string[idx2] and idx != idx2:
                found_duplicate = True

        if not found_duplicate:
            return idx

    return -1


# Solution 2
# O(n) time | O(1) space

def firstNonRepeatingCharacter(string):
    character_frequencies = {}
    for character in string:
        character_frequencies[character] = character_frequencies.get(character, 0) + 1

    for idx in range(len(string)):
        character = string[idx]
        if character_frequencies[character] == 1:
            return idx

    return -1