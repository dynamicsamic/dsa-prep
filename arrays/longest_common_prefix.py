def longest_common_prefix(words: list[str]) -> str:
    """
    Leetcode. 14. Longest Common Prefix
    https://leetcode.com/problems/longest-common-prefix/description

    -----------------------------Description-----------------------------------
    Write a function to find the longest common prefix string amongst an array
    of strings. If there is no common prefix, return an empty string "".

    -----------------------------Constraints-----------------------------------
    : 1 <= words.length <= 200
    : 0 <= words[i].length <= 200
    : words[i] consists of only lowercase English letters.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: words = ["flower","flow","flight"]
    Output: "fl"

    Example 2:
    Input: words = ["dog","racecar","car"]
    Output: ""
    Explanation: There is no common prefix among the input strings.

    ------------------------------Algorithm------------------------------------
    Set the first word from the array as the longest prefix for other words.
    Iterate through the array and for every word match letters with the prefix,
    for every matching letter increment counter. If we found no matching
    letters it means that at least two words in the array don't have a common
    prefix, that's why we return early. If we have any matching letters cut
    our longest prefix by the amount of counter. Return the resulting prefix.
    """

    prefix = words[0]

    for word in words[1:]:
        i = 0
        long_count = 0
        while i < len(prefix) and i < len(word):
            if prefix[i] == word[i]:
                long_count += 1
                i += 1

            else:
                break

        if long_count == 0:
            return ""

        prefix = prefix[:long_count]

    return prefix


assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"
assert (
    longest_common_prefix(["crowd", "crow", "crowsource", "crown"]) == "crow"
)
assert longest_common_prefix(["dog", "racecar", "car"]) == ""

print("\nAll tests passed\n")
