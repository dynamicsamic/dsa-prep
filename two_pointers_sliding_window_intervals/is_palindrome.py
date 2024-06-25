def is_palindrome(s: str) -> bool:
    """
    Leetcode. 125. Valid Palindrome
    https://leetcode.com/problems/valid-palindrome//description

    -----------------------------Description-----------------------------------
    A phrase is a palindrome if, after converting all uppercase letters into
    lowercase letters and removing all non-alphanumeric characters,
    it reads the same forward and backward.
    Alphanumeric characters include letters and numbers.

    Given a string s, return true if it is a palindrome, or false otherwise.

    -----------------------------Constraints-----------------------------------
    : 1 <= s.length <= 2 * 105
    : s consists only of printable ASCII characters.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

    Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

    Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing non-alphanumeric characters.
    Since an empty string reads the same forward and backward, it is a palindrome.

    ------------------------------Algorithm------------------------------------
    Firstly normalize the palindrome.
    Traverse the valid palindrome from both sides.
    Retrun False if chars from both sides are different.
    Return True if we make til the end.
    """
    if s == " ":
        return True

    valid = [char.lower() for char in s if char.isalnum()]
    size = len(valid)

    if size == 1:
        return True

    start = 0
    end = size - 1

    while end > start:
        if valid[start] != valid[end]:
            return False

        start += 1
        end -= 1

    return True


assert is_palindrome("racecar")
assert is_palindrome("A man, a plan, a canal: Panama")
assert is_palindrome(" ")
assert not is_palindrome("Not a palindrome")
