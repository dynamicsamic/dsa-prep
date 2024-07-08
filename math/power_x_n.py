def power(x: float, n: int) -> float:
    """
    Leetcode. 50. Pow(x,n)
    https://leetcode.com/problems/powx-n/description

    -----------------------------Description-----------------------------------
    Implement pow(x, n), which calculates x raised to the power n (i.e., x**n).

    -----------------------------Constraints-----------------------------------
    : -100.0 < x < 100.0
    : -2**31 <= n <= 2**31-1
    : n is an integer.
    : Either x is not zero or n > 0.
    : -10**4 <= xn <= 10**4

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000

    Example 2:
    Input: x = 2.10000, n = 3
    Output: 9.26100

    Example 3:
    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2**-2 = 1/2**2 = 1/4 = 0.25

    ------------------------------Algorithm------------------------------------
    First we handle some corner cases. Then check if n is a negative power,
    we need to adjust our x and p. In the loop we check if power is odd, if so
    we decrement p and multiply accumulator by x. There always will be at least
    one operation of multiplying accumulator - when the power is 1. That's why
    we can safely return it as the final result. Almost all operations will be
    with even p, and we will multiply the x by itself and divide p by 2.
    """
    if n == 0:
        return 1.0

    if x == 0 or x == 1.0:
        return x

    p = n
    if p < 0:
        x = 1 / x
        p = -p

    acc = 1
    while p > 0:
        if p % 2 == 0:
            x *= x
            p //= 2
        else:
            acc *= x
            p -= 1

    return acc


assert power(1, 23232323322323) == 1
assert power(0, 23232323322323) == 0
assert power(2, 2) == 4
assert power(2, -2) == 0.25
assert power(5, 3) == 125
assert power(2, 10) == 1024
assert round(power(2.1, 3), 3) == 9.261

print("\nAll tests passed\n")
