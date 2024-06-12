def word_pattern(pattern: str, s: str) -> bool:
    words = s.split()
    occupied = set()

    if len(words) != len(pattern):
        return False

    mappings = {}

    for char, word in zip(pattern, words):
        if char in mappings:
            if word != mappings[char]:
                return False
        else:
            if word in occupied:
                return False
            mappings[char] = word
            occupied.add(word)

    return True


tests = [
    ("abba", "dog cat cat dog"),
    ("abba", "dog cat cat fish"),
    ("aaaa", "dog cat cat dog"),
    ("abcd", "dog cat cat dog"),
]
for pat, s in tests:
    print(word_pattern(pat, s))
