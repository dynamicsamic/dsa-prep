def is_subsequence(s: str, t: str) -> bool:
    """
    Leetcode. 392. Is Subsequence
    https://leetcode.com/problems/is-subsequence//description

    -----------------------------Description-----------------------------------
    Given two strings s and t, return true if s is a subsequence of t,
    or false otherwise.

    A subsequence of a string is a new string that is formed from the original
    string by deleting some (can be none) of the characters without disturbing
    the relative positions of the remaining characters.
    (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

    -----------------------------Constraints-----------------------------------
    : 0 <= s.length <= 100
    : 0 <= t.length <= 104
    : s and t consist only of lowercase English letters.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: s = "abc", t = "ahbgdc"
    Output: true

    Example 2:
    Input: s = "axc", t = "ahbgdc"
    Output: false

    ------------------------------Algorithm------------------------------------
    Declare two pointers `fast` and `slow`.
    Traverse the string incrementing fast pointer on every step.
    Increment slow pointer only if chars of pointers equal.
    If the slow pointer reached the end of its contents, that means we found
    the longest substring.
    If we dont't reached the end of our subsequence, that means that it is not
    a valid subsuquence and we return False.
    """
    if not s:
        return True

    slen = len(s)
    i = 0

    for j in range(len(t)):
        if t[j] == s[i]:
            i += 1

        if i == slen:
            return True

    return False


assert is_subsequence("abc", "adebyhcq")
assert is_subsequence("elo", "hello")
assert not is_subsequence("abx", "adebyhcq")
