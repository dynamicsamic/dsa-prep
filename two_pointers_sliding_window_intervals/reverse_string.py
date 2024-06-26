def reverse_string(s: list[str])-> None:
    """
    Leetcode. 344. Reverse String
    https://leetcode.com/problems/reverse-string/description

    -----------------------------Description-----------------------------------
    Write a function that reverses a string. The input string is given as 
    an array of characters s. You must do this by modifying the input array 
    in-place with O(1) extra memory.

    -----------------------------Constraints-----------------------------------
    : 1 <= s.length <= 105
    : s[i] is a printable ascii character.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: s = ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]

    Example 2:
    Input: s = ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]

    ------------------------------Algorithm------------------------------------
    Declare two pointers to track front and rear chars. Traverse the array
    until theese pointers meet. On each pass swap the chars and increment 
    both pointers.
    """
    i = 0
    j = len(s) - 1

    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1

def reverse_string_builtin(s: list[str])-> None:
    s.reverse()

s1 = ["h","e","l","l","o"]
reverse_string(s1)
assert s1 == ["o","l","l","e","h"]

s2 = ["H","a","n","n","a","h"]
reverse_string(s2)
assert s2 == ["h","a","n","n","a","H"]

s3 = ["b"]
reverse_string(s3)
assert s3 == ["b"]