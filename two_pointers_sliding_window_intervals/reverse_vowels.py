def reverse_vowels(s: str) -> str:
    """
    Leetcode. 345. Reverse Vowels of a String
    https://leetcode.com/problems/reverse-vowels-of-a-string/description

    -----------------------------Description-----------------------------------
    Given a string s, reverse only all the vowels in the string and return it.
    The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both
    lower and upper cases, more than once.

    -----------------------------Constraints-----------------------------------
    : 1 <= s.length <= 3 * 105
    : s consist of printable ASCII characters.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: s = "hello"
    Output: "holle"

    Example 2:
    Input: s = "leetcode"
    Output: "leotcede"

    ------------------------------Algorithm------------------------------------
    Declare two pointers to track front and rear chars. Traverse the array
    until theese pointers meet. On each pass check if both pointers point at
    vowel and if so swap the chars and increment both pointers.
    Otherwise increment one of the pointers that currently points to consonant.
    """
    string_length = len(s)

    if string_length < 2:
        return s

    left = 0
    right = string_length - 1
    res = list(s)
    vowels = {"A", "E", "I", "O", "U", "a", "e", "i", "o", "u"}

    while left < right:
        if res[left] not in vowels:
            left += 1
        elif res[right] not in vowels:
            right -= 1
        else:
            res[left], res[right] = res[right], res[left]
            left += 1
            right -= 1

    return "".join(res)


assert reverse_vowels("hello") == "holle"
assert reverse_vowels("leetcode") == "leotcede"
assert reverse_vowels("a") == "a"
assert reverse_vowels("ae") == "ea"
assert reverse_vowels("spAmeggs") == "spemAggs"
