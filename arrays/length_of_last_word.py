"""
Leetcode. 58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/description

-----------------------------Description-----------------------------------
Given a string s consisting of words and spaces, return the length of the 
last word in the string. A word is a maximal substring consisting of 
non-space characters only.

-----------------------------Constraints-----------------------------------
: 1 <= s.length <= 10**4
: s consists of only English letters and spaces ' '.
: There will be at least one word in s.

------------------------------Examples-------------------------------------
Example 1:
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.

Example 2:
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Example 3:
Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
"""


def length_of_last_word(sentence: str) -> int:
    """
    ------------------------------Algorithm------------------------------------
    Iterate the sentence from the end. Skip any space. If a non-space character
    found - traverse it until the next space or the end of the string and count
    its length.
    """
    i = len(sentence) - 1
    count = 0

    while i >= 0:
        if sentence[i] != " ":
            while sentence[i] != " ":
                if i < 0:
                    break
                count += 1
                i -= 1
            return count
        i -= 1


def length_of_last_word_builtin(sentence: str) -> int:
    """Split the string by any space and return the last string in list."""
    return len(sentence.split()[-1])


assert length_of_last_word("hello world") == 5
assert length_of_last_word("   fly me   to   the moon  ") == 4
assert length_of_last_word("luffy is still joyboy") == 6

assert length_of_last_word_builtin("hello world") == 5
assert length_of_last_word_builtin("   fly me   to   the moon  ") == 4
assert length_of_last_word_builtin("luffy is still joyboy") == 6

print("\nAll tests passed\n")
