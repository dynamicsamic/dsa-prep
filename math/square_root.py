def sqrt(x: int) -> int:
    """
    Leetcode. 136. Sqrt(x)
    https://leetcode.com/problems/sqrtx/description

    -----------------------------Description-----------------------------------
    Given a non-negative integer x, return the square root of x rounded down to
    the nearest integer. The returned integer should be non-negative as well.
    You must not use any built-in exponent function or operator.
    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

    -----------------------------Constraints-----------------------------------
    : 0 <= x <= 2**31 - 1

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: x = 4
    Output: 2
    Explanation: The square root of 4 is 2, so we return 2.

    Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we round it down
    to the nearest integer, 2 is returned.

    ------------------------------Algorithm------------------------------------
    First, the square root of 0 is always 0. Square root of numbers less than 4
    rounded to nearest integer is 1. If we have numbers greater or equal to 4,
    we start a loop in which we check if squares of subsquent digits are equal
    or greater than x. E.g. if our number if 4, and we stopped at 2, well that
    means the square root of 4 is 2.
    """
    if x == 0:
        return 0
    elif x < 4:
        return 1

    for i in range(2, x // 2 + 1):
        if i * i > x:
            return i - 1
    return i


assert sqrt(2) == 1
assert sqrt(4) == 2
assert sqrt(6) == 2
assert sqrt(25) == 5
assert sqrt(11) == 3

print("\nAll tests passed\n")
