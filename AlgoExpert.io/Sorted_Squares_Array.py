# Solution 1
# O(nlog(n)) time | O(n) space

def isValidSubsequence(array, sequence):
    seq_idx = 0
    for value in array:
        if seq_idx == len(sequence):
            break
        if sequence[seq_idx] == value:
            seq_idx += 1
    return seq_idx == len(sequence)

# Solution 2
# O(n) time | O(n) space
def sortedSquaredArray(array):
    sorted_squares = [0 for _ in array]
    small_val_idx = 0
    large_val_idx = len(array) - 1

    for idx in reversed(range(len(array))):
        smaller_value = array[small_val_idx]
        larger_value = array[large_val_idx]

        if abs(smaller_value) > abs(larger_value):
            sorted_squares[idx] = smaller_value ** 2
            small_val_idx += 1
        else:
            sorted_squares[idx] = larger_value ** 2
            large_val_idx -= 1 

    return sorted_squares