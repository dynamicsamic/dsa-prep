"""
Leetcode. 28. Find the Index of the First Occurrence in a String
https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

-----------------------------Description-----------------------------------
Given two strings needle and haystack, return the index of the first 
occurrence of needle in haystack, or -1 if needle is not part of haystack.

-----------------------------Constraints-----------------------------------
: 1 <= haystack.length, needle.length <= 10**4
: haystack and needle consist of only lowercase English characters.

------------------------------Examples-------------------------------------
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.

Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


def find_index_pointers(haystack: str, needle: str) -> int:
    """
    ------------------------------Algorithm------------------------------------
    Set three pointers `i`, `j` and `k`. i pointer will control the main while
    loop and point to current character in haystack. j and k pointers used to
    make comparisons between characters in haystack and needle. If j and k
    point to the same character we increment them to check next two
    characcters. We do this until the characters don't match or one of the
    two pointers reaches the end of its string. After that we check k pointer
    reached the length of needle. If so, it means we found a complete match
    and return the i index. We repeat this process until the end of the
    haystack. On each iteration of the main while loop we reset j to point
    to the current character in haystack and reset k pointer to point to
    the first character in needle. If the loop has reached its end, it means
    we haven't found a match and return -1.
    """
    needle_length, haystack_length = len(needle), len(haystack)

    if needle_length > haystack_length:
        return -1

    i = j = k = 0
    while i < haystack_length:
        while (
            k < needle_length
            and j < haystack_length
            and haystack[j] == needle[k]
        ):
            j += 1
            k += 1
        if k == needle_length:
            return i
        i += 1
        j = i
        k = 0

    return -1


def find_index_slice(haystack: str, needle: str) -> int:
    """
    ------------------------------Algorithm------------------------------------
    We start a for loop and on each step we check a string slice from haystakc
    starting from current character with length of needle matches the needle.
    """
    needle_length, haystack_length = len(needle), len(haystack)

    if needle_length > haystack_length:
        return -1

    for i in range(haystack_length - needle_length + 1):
        if haystack[i : i + needle_length] == needle:
            return i
    return -1


def find_index_builtin(haystack: str, needle: str) -> int:
    """Use the builtin string method."""
    return haystack.find(needle)


def find_index_re(haystack: str, needle: str) -> int:
    """Use re module to search a pattern."""
    import re

    if m := re.search(needle, haystack):
        return m.start()

    return -1


assert find_index_pointers("sadbutsad", "sad") == 0
assert find_index_pointers("leetcode", "leeto") == -1
assert find_index_pointers("mississippi", "issippi") == 4

assert find_index_slice("sadbutsad", "sad") == 0
assert find_index_slice("leetcode", "leeto") == -1
assert find_index_slice("mississippi", "issippi") == 4

assert find_index_builtin("sadbutsad", "sad") == 0
assert find_index_builtin("leetcode", "leeto") == -1
assert find_index_builtin("mississippi", "issippi") == 4

assert find_index_re("sadbutsad", "sad") == 0
assert find_index_re("leetcode", "leeto") == -1
assert find_index_re("mississippi", "issippi") == 4

print("\nAll tests passed\n")
