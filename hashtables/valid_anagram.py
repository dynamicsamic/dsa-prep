"""
Leetcode. 242. Valid Anagram
https://leetcode.com/problems/valid-anagram/description

-----------------------------Description---------------------------------------
Given two strings s and t, return true if t is an anagram of s, and false 
otherwise. An Anagram is a word or phrase formed by rearranging the letters of 
a different word or phrase, typically using all the original letters exactly
once.

-----------------------------Constraints---------------------------------------
1 <= s.length, t.length <= 5 * 10**4
s and t consist of lowercase English letters.

------------------------------Examples-----------------------------------------
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false
"""

import time
from collections import Counter


def is_anagram_counter(s: str, t: str) -> bool:
    """
    ------------------------------Algorithm------------------------------------
    Use builtin Counter class from collections module. Transform both strings
    into counters and compare them.
    """
    return Counter(s) == Counter(t)


def is_anagram_sorted(s: str, t: str) -> bool:
    """
    ------------------------------Algorithm------------------------------------
    Since anagrams are virtually just shuffled versions of the same string,
    sorting lets you normalize them. Thats why we sort them and compare.
    """
    return sorted(s) == sorted(t)


def is_anagram_dict(s: str, t: str) -> bool:
    """
    ------------------------------Algorithm------------------------------------
    Iterate over s and count occurances of its chars in count dict. Iterate
    over t and subtract from count all occurances of its chars. Iterate over
    values in count, if strings are anagrams every value should be equal
    to zero.
    """
    if len(s) != len(t):
        return False

    count = {}

    for char in s:
        count[char] = count.get(char, 0) + 1

    for char in t:
        count[char] = count.get(char, 0) - 1

    for char in count.values():
        if char != 0:
            return False

    return True


def is_anagram_list(s: str, t: str) -> bool:
    """
    ------------------------------Algorithm------------------------------------
    Here we will use ascii values for our characters, since all characters in
    a problem are lowercase english letters. Define a count array to store all
    26 lowercase egnlish letters. At the start of the loop it is filled with
    zeroes. Iterate over s a t simulatneoulsy, on each char of s increment
    value sitiing by its index, on each char of t - vice versa (decrement).
    After that iterate over count to make sure all values are set to zero.

    """
    s_length, t_length = len(s), len(t)

    if s_length != t_length:
        return False

    count = [0] * 26
    mask = ord("a")

    for i in range(s_length):
        count[ord(s[i]) - mask] += 1
        count[ord(t[i]) - mask] -= 1

    for i in count:
        if i != 0:
            return False

    return True


start = time.perf_counter_ns()
assert is_anagram_counter("anagram", "nagaram")
assert is_anagram_counter("rat", "tar")
assert is_anagram_counter(
    "dnyxijlfhskgoeprubwamtcqzvdnyxijlfhskgoeprubwamtcqzv",
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
)
assert not is_anagram_counter("rat", "car")
end = time.perf_counter_ns()
print(f"Collections.Counter approach takes {end-start} nanosec (w/o import)")

start = time.perf_counter_ns()
assert is_anagram_sorted("anagram", "nagaram")
assert is_anagram_sorted("rat", "tar")
assert is_anagram_sorted(
    "dnyxijlfhskgoeprubwamtcqzvdnyxijlfhskgoeprubwamtcqzv",
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
)
assert not is_anagram_sorted("rat", "car")
end = time.perf_counter_ns()
print(f"Sorted approach takes {end-start} nanosec")

start = time.perf_counter_ns()
assert is_anagram_dict("anagram", "nagaram")
assert is_anagram_dict("rat", "tar")
assert is_anagram_dict(
    "dnyxijlfhskgoeprubwamtcqzvdnyxijlfhskgoeprubwamtcqzv",
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
)
assert not is_anagram_dict("rat", "car")
end = time.perf_counter_ns()
print(f"Dict approach takes {end-start} nanosec")

start = time.perf_counter_ns()
assert is_anagram_list("anagram", "nagaram")
assert is_anagram_list("rat", "tar")
assert is_anagram_list(
    "dnyxijlfhskgoeprubwamtcqzvdnyxijlfhskgoeprubwamtcqzv",
    "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
)
assert not is_anagram_list("rat", "car")
end = time.perf_counter_ns()
print(f"List approach takes {end-start} nanosec")

print("\nAll tests passed")
