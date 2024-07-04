def add_binary(a: str, b: str) -> str:
    """
    Leetcode. 67. Add Binary
    https://leetcode.com/problems/add-binary/description

    -----------------------------Description-----------------------------------
    Given two binary strings a and b, return their sum as a binary string.

    -----------------------------Constraints-----------------------------------
    : 1 <= a.length, b.length <= 104
    : a and b consist only of '0' or '1' characters.
    : Each string does not contain leading zeros except for the zero itself.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: a = "11", b = "1"
    Output: "100"

    Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

    ------------------------------Algorithm------------------------------------
    Define two helper functions. One for converting binary string to integer.
    Second for making the reverse conversion.
    Convert two strings to integers, add them together, convert back to string.
    """

    def bin2int(num: str) -> int:
        """Convert binary string to integer."""
        power = 0
        result = 0
        i = len(num) - 1

        while i >= 0:
            result += int(num[i]) * (2**power)
            i -= 1
            power += 1

        return result

    def int2bin(num: int) -> str:
        """Convert integer to binary string."""
        result = ""

        while num:
            num, rem = divmod(num, 2)
            result = str(rem) + result

        return result or "0"

    a = bin2int(a)
    b = bin2int(b)

    res = a + b

    return int2bin(res)


assert add_binary("11", "1") == "100"
assert add_binary("0", "1") == "1"
assert add_binary("110", "1") == "111"
assert add_binary("1010", "1011") == "10101"


def add_binary_builtin(a: str, b: str) -> str:
    """Use builtin functionality to accomplish the same task."""
    num = int(a, base=2) + int(b, base=2)
    return f"{num:b}"


assert add_binary_builtin("11", "1") == "100"
assert add_binary_builtin("0", "1") == "1"
assert add_binary_builtin("110", "1") == "111"
assert add_binary_builtin("1010", "1011") == "10101"
