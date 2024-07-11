def word_pattern(pattern: str, s: str) -> bool:
    """
    Leetcode. 290. Word Pattern
    https://leetcode.com/problems/word-pattern/description

    -----------------------------Description-----------------------------------
    Given a pattern and a string s, find if s follows the same pattern. Here
    follow means a full match, such that there is a bijection between a letter
    in pattern and a non-empty word in s.

    -----------------------------Constraints-----------------------------------
    : 1 <= pattern.length <= 300
    : pattern contains only lower-case English letters.
    : 1 <= s.length <= 3000
    : s contains only lowercase English letters and spaces ' '.
    : s does not contain any leading or trailing spaces.
    : All the words in s are separated by a single space.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: pattern = "abba", s = "dog cat cat dog"
    Output: true

    Example 2:
    Input: pattern = "abba", s = "dog cat cat fish"
    Output: false

    Example 3:
    Input: pattern = "aaaa", s = "dog cat cat dog"
    Output: false

    ------------------------------Algorithm------------------------------------
    We split a string of space separated words into an array of strings to our
    convinience. We define a dict and a mapping to check cross-reference of
    words and chars. We start a loop over pattern and string simultaneously.
    If we encounter a word and a char the first time, we add a char: word
    combination to dict. We also add the word to set, to prevent another char
    in pattern from occupying this word. If we found a char in our mappings we
    check if its bound word is the same as current word. If it is not, it means
    this pattern char already has another word bound to it, whick violates the
    conditions. Additionally before adding a char:word pair we check if a word
    is already occupied. If it is, this violates the condition.
    """
    words = s.split()

    if len(words) != len(pattern):
        return False

    mappings = {}
    occupied = set()

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


assert word_pattern("abba", "dog cat cat dog")
assert word_pattern("abcd", "dog cat horse fish")
assert not word_pattern("abba", "dog cat cat fish")
assert not word_pattern("aaaa", "dog cat cat dog")
assert not word_pattern("abcd", "dog cat cat dog")

print("\nAll tests passed")
