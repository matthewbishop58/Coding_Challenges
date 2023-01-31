# O(n * m) time | O(n * m) space
def semordnilap(words):
    words_set = set(words)
    semordnilap_pairs = []

    for word in words:
        reverse = word[::-1]
        if reverse in words_set and reverse != word:
            semordnilap_pairs.append([word, reverse])
            words_set.remove(word)
            words_set.remove(reverse)
            
    return semordnilap_pairs
