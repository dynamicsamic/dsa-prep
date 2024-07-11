"""
Leetcode. 49. Group Anagrams
https://leetcode.com/problems/group-anagrams/description

-----------------------------Description---------------------------------------
Given an array of strings strs, group the anagrams together. You can return the
answer in any order. An Anagram is a word or phrase formed by rearranging the 
letters of a different word or phrase, typically using all the original 
letters exactly once.

-----------------------------Constraints---------------------------------------
: 1 <= strs.length <= 10**4
: 0 <= strs[i].length <= 100
: strs[i] consists of lowercase English letters.

------------------------------Examples-----------------------------------------
Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]
"""


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """
    ------------------------------Algorithm------------------------------------
    We define a grouped array to hold our results. Since groups of anagrams are
    stored in this array, we will need to be able to find any anagram group by
    its index. Otherwise we would need iterate through the array each time we
    need to store new anagram. To overcome this store all anagram's subarray
    indexes in the seen dictionary.
    When we iterate through the strs array we first `normalize` every word,
    that is, we sort its characters to make anagrams look like identical words.
    If this is the first time we see an anagram we store its normalized version
    in the seen dict and assign a pointer to it. We then place this word in an
    array and append it to resulting array. We increment the index, to place
    next unique word on next index. If we've already seen this anagram, we
    get its index (stored in seen dictionary), find its anagram subarray
    in resulting array by this index and append this word to found subarray.
    """
    seen = {}
    grouped = []
    index = 0

    for s in strs:
        normalized = "".join(sorted(s))
        if normalized not in seen:
            seen[normalized] = index
            grouped.append([s])
            index += 1
        else:
            idx = seen[normalized]
            grouped[idx].append(s)

    return grouped


def group_anagrams_defaultdict(strs: list[str]) -> list[list[str]]:
    """
    This algorithm repeats previous one, but here instead of doing manual
    storing and retrieving of subarrays, we use the defaultdict with
    list factory function.
    """

    from collections import defaultdict

    grouped = defaultdict(list)
    for word in strs:
        grouped["".join(sorted(word))].append(word)

    return list(grouped.values())


tests = [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
    ),
    ([""], [[""]]),
    (["a"], [["a"]]),
]

for words, res in tests:
    assert group_anagrams(words) == res
    assert group_anagrams_defaultdict(words) == res

print("\nAll tests passed\n")
