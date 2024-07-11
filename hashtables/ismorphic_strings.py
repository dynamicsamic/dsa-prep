"""
Leetcode. 205. Isomorphic Strings
https://leetcode.com/problems/isomorphic-strings/description

-----------------------------Description---------------------------------------
Given two strings s and t, determine if they are isomorphic.Two strings s and t
are isomorphic if the characters in s can be replaced to get t. All occurrences
of a character must be replaced with another character while preserving the 
order of characters. No two characters may map to the same character, but a 
character may map to itself

-----------------------------Constraints---------------------------------------
: 1 <= s.length <= 5 * 10**4
: t.length == s.length
: s and t consist of any valid ascii character.

------------------------------Examples-----------------------------------------
Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
"""

import time


def is_isomorphic_set_dict(s: str, t: str) -> bool:
    """
    ------------------------------Algorithm------------------------------------
    Define a dict mappings and a set mappings occupied. Traverse both strings
    simultaneously. For every new combination of two characters we add their
    combination to mapping and also add the second character to occupied set
    to prevent it from being used in other combinations. If the second
    char is already in occupied set, it means it has been already used in
    some other combination, therefore we return false. If a letter from s
    is not new to us we check if its mapping fits current combination of two
    letters. If it is not, we return false. If the loop ends without violating
    the conditions, we return true.
    """
    mappings = {}
    mappings_occupied = set()

    for i in range(len(s)):
        if s[i] not in mappings:
            if t[i] not in mappings_occupied:
                mappings[s[i]] = t[i]
                mappings_occupied.add(t[i])
            else:
                return False
        else:
            if mappings[s[i]] != t[i]:
                return False

    return True


def is_isomorphic_dict(s: str, t: str) -> bool:
    """
    ------------------------------Algorithm------------------------------------
    A little optimized form of the previous algorithm.
    Define a dict mappings. Traverse both strings simultaneously. For every new
    combination of two characters we check if the second char is already in
    mappings values. If it's not, we add this combination to mapping. If it is
    the condition was violated and we can return false. If a letter from s
    is not new to us we check if its mapping fits current combination of two
    letters. If it is not, we return false. If the loop ends without violating
    the conditions, we return true.
    """
    mappings = {}

    for val, mapper in zip(s, t):
        if val in mappings:
            if mapper != mappings[val]:
                return False
        else:
            if mapper in mappings.values():
                return False
            mappings[val] = mapper

    return True


def is_isomorphic_list(s: str, t: str) -> bool:
    """
    ------------------------------Algorithm------------------------------------
    This algorithm utilizes that fact that by the definition of the problem
    we are dealing only with ASCII characters, each of which fits in one byte.
    We use ordinal number for each character as an index for a list.
    We Set two arrays of size 256 with only zeros in them. We iterate over the
    two strings and for every new combination of characters we store the
    current counter `i` as a value that can be found by indexes of that
    characters' ordinal values. This works like a sort of a time stamp.
    If we have two chars `a` and `m` from two strings with their ascii numbers
    as 97 and 109, it means that seen_s[97] == i and seen_t[109] == i. Since
    counter increases on every step, values assigned to the indexes become
    unique. If we chech two chars and their values are not the same, it means
    this values was set not in the same time, that violates the condition.
    """

    seen_s = [0] * 256
    seen_t = [0] * 256

    for i in range(len(s)):
        if seen_s[ord(s[i])] != seen_t[ord(t[i])]:
            return False

        seen_s[ord(s[i])] = i + 1
        seen_t[ord(t[i])] = i + 1

    return True


start = time.perf_counter_ns()
assert is_isomorphic_set_dict("egg", "add")
assert is_isomorphic_set_dict("paper", "title")
assert not is_isomorphic_set_dict("foo", "bar")
assert not is_isomorphic_set_dict("badc", "baba")
end = time.perf_counter_ns()
print(f"Set and dict approach takes {end - start} nanosec")


start = time.perf_counter_ns()
assert is_isomorphic_dict("egg", "add")
assert is_isomorphic_dict("paper", "title")
assert not is_isomorphic_dict("foo", "bar")
assert not is_isomorphic_dict("badc", "baba")
end = time.perf_counter_ns()
print(f"One dict approach takes {end - start} nanosec")

start = time.perf_counter_ns()
assert is_isomorphic_list("egg", "add")
assert is_isomorphic_list("paper", "title")
assert not is_isomorphic_list("foo", "bar")
assert not is_isomorphic_list("badc", "baba")
end = time.perf_counter_ns()
print(f"List approach takes {end - start} nanosec")

print("\nAll tests passed")
