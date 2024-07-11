"""
Leetcode. 383. Ransom Note
https://leetcode.com/problems/ransom-note/description

-----------------------------Description---------------------------------------
Given two strings ransomNote and magazine, return true if ransomNote can be 
constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

-----------------------------Constraints---------------------------------------
: 1 <= ransomNote.length, magazine.length <= 105
: ransomNote and magazine consist of lowercase English letters.

------------------------------Examples-----------------------------------------
Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""

import time
from collections import Counter


def ransome_note_collections(note: str, magazine: str) -> bool:
    """
    ------------------------------Algorithm------------------------------------
    Use builtin Counter class from collections module. Transform both strings
    into counters and compare them.
    """
    if len(magazine) < len(note):
        return False

    c1 = Counter(note)
    c2 = Counter(magazine)

    return c2 >= c1


def ransome_note_two_lists(note: str, magazine: str) -> bool:
    """
    ------------------------------Algorithm------------------------------------
    Since we dealing with lowercase ascii characters we can take advantage of
    their fixed size. Set two lists to be a counter for each string. First
    iterate over note string. Shift all letters by 97 and place them by their
    respective index in the array. E.g. if we have an `a` char which have
    ascii number of 97, it wiil take 0-th index; `z` will take 25-th index.
    Repeat the same process for the magazine string. After that iterate over
    two counters and check if any count in note string is greater than its
    counterpart in magazine counter. If so, there is no way to build a note
    from magazie. If all comparisons passed successfully, return true.
    """
    if len(magazine) < len(note):
        return False

    mask = ord("a")

    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(note)):
        c1[ord(note[i]) - mask] += 1

    for i in range(len(magazine)):
        c2[ord(magazine[i]) - mask] += 1

    for i in range(len(c1)):
        if c1[i] > c2[i]:
            return False

    return True


def ransome_note_one_list(note: str, magazine: str) -> bool:
    """
    ------------------------------Algorithm------------------------------------
    This algorithm is derived from the previous one. But here we use only one
    counter array, and decrease number of traversals. First we iterate over
    magazine string and count how many items we have at our disposal. Next we
    iterate over note and check if any of notes characters has a 0 on its index
    in the counter. If it does, that means we can't build a note from that
    string, and should return false. If counter is OK, we decrement the counter,
    thus noting we have visisted this char once.
    """
    note_length = len(note)
    mag_length = len(magazine)

    if note_length > mag_length:
        return False

    mask = ord("a")
    counter = [0] * 26

    for i in range(mag_length):
        counter[ord(magazine[i]) - mask] += 1

    for i in range(note_length):
        if counter[ord(note[i]) - mask] == 0:
            return False

        counter[ord(note[i]) - mask] -= 1

    return True


start = time.perf_counter_ns()
assert ransome_note_collections("aa", "aab")
assert not ransome_note_collections("a", "b")
assert not ransome_note_collections("aa", "b")
assert ransome_note_collections(
    "fihjei",
    "hjfasdgasqereopptoklreikjxcvnkjalieirtiuqweribagacbhadfaefdjaeaebgi",
)
assert not ransome_note_collections("fihjjjjei", "hjibagacbhadfaefdjaeaebgi")
end = time.perf_counter_ns()
print(f"Collections.Counter approach takes {end-start} nanosec (w/o import)")


start = time.perf_counter_ns()
assert ransome_note_two_lists("aa", "aab")
assert not ransome_note_two_lists("a", "b")
assert not ransome_note_two_lists("aa", "b")
assert ransome_note_two_lists(
    "fihjei",
    "hjfasdgasqereopptoklreikjxcvnkjalieirtiuqweribagacbhadfaefdjaeaebgi",
)
assert not ransome_note_two_lists("fihjjjjei", "hjibagacbhadfaefdjaeaebgi")
end = time.perf_counter_ns()
print(f"Two list approach takes {end-start} nanosec")


start = time.perf_counter_ns()
assert ransome_note_one_list("aa", "aab")
assert not ransome_note_one_list("a", "b")
assert not ransome_note_one_list("aa", "b")
assert ransome_note_one_list(
    "fihjei",
    "hjfasdgasqereopptoklreikjxcvnkjalieirtiuqweribagacbhadfaefdjaeaebgi",
)
assert not ransome_note_one_list("fihjjjjei", "hjibagacbhadfaefdjaeaebgi")
end = time.perf_counter_ns()
print(f"One list approach takes {end-start} nanosec")

print("\nAll tests passed")
