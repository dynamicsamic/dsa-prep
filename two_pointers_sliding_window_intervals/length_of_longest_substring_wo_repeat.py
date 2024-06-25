def length_of_longest_non_repeat_substring(s: str) -> int:
    """
    Leetcode. 3. Longest Substring Without Repeating Characters
    https://leetcode.com/problems/longest-substring-without-repeating-characters

    -----------------------------Description-----------------------------------
    Given a string s, find the length of the longest substring without
    repeating characters.

    -----------------------------Constraints-----------------------------------
    : 0 <= s.length <= 5 * 104
    : s consists of English letters, digits, symbols and spaces.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

    Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

    Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a subsequence
    and not a substring.

    ------------------------------Algorithm------------------------------------
    Use two ponters `fast` and `slow`. Fast pointer moves one step forvard
    on each iteration and traverses the string sequentially.
    For every unique char we add it to `seen` set and update the
    `subst_length` variable with substring length seen so far.
    Current substring length is the difference between pointers.
    Slow pointer moves only when a duplicate is detected.
    If a duplicate detected we remove all the characters added to seen before
    the duplicate was first added. After that we add current char
    (which previously was a duplicate) to seen.
    """
    string_length = len(s)
    subst_length = 0
    seen = set()
    j = 0

    for i in range(string_length):
        char = s[i]
        if char not in seen:
            seen.add(char)
            subst_length = max(subst_length, i - j + 1)
        else:
            while char in seen:
                seen.remove(s[j])
                j += 1
            seen.add(char)

    return subst_length


assert length_of_longest_non_repeat_substring("abcabcbb") == 3
assert length_of_longest_non_repeat_substring("dvdf") == 3
assert length_of_longest_non_repeat_substring("bbbb") == 1
assert length_of_longest_non_repeat_substring("pwwkew") == 3
assert length_of_longest_non_repeat_substring(" ") == 1
