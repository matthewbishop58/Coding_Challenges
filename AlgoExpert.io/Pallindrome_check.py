# Solution 1
# O(n^2) time | O(n) space

def isPalindrome(string):
    reversed_string = ""
    for i in reversed(range(len(string))):
        reversed_string += string[i]
    return string == reversed_string


# Solution 2
# O(n) time | O(n) space

def isPalindrome(string):
    reversed_chars = []
    for i in reversed(range(len(string))):
        reversed_chars.append(string[i])

    return string == "".join(reversed_chars)


# Solution 3
# O(n) time | O(n) space

def isPalindrome(string, i = 0):
    j = len(string) - 1 - i
    return True if i >= j else string[i] == string[j] and isPalindrome(string, i + 1)

# Solution 4
def isPalindrome(string):
    left = 0
    right = len(string)-1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right += 1
    return True