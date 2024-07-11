def is_happy_number(n: int) -> bool:
    """
    Leetcode. 202. Happy Number
    https://leetcode.com/problems/happy-number/description

    -----------------------------Description-----------------------------------
    Write an algorithm to determine if a number n is happy. A happy number is
    a number defined by the following process:
      - Starting with any positive integer, replace the number by the sum of
        the squares of its digits.
      - Repeat the process until the number equals 1 (where it will stay), or
        it loops endlessly in a cycle which does not include 1.
      - Those numbers for which this process ends in 1 are happy.
    Return true if n is a happy number, and false if not.

    -----------------------------Constraints-----------------------------------
    : 1 <= n <= 2**31 - 1

    ------------------------------Examples-------------------------------------
    Example 1:
    Output: true
    Explanation:
    12 + 92 = 82
    82 + 22 = 68
    62 + 82 = 100
    12 + 02 + 02 = 1

    Example 2:
    Input: n = 2
    Output: false

    ------------------------------Algorithm------------------------------------
    Define an empty seen dict. While n is not equal to 1 we calculate the sum
    of squares of its digits. If we have already seen this sum, it means we
    hit a cycle, and can go in cycles forewer, so we return false. Otherwise
    we add this sum to seen dict. We end up reaching 1 and returning true.
    """
    seen = set()

    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])
        if n in seen:
            return False

        seen.add(n)

    return True


tests = [(19, True), (2, False), (6, False), (1111111, True)]
for num, res in tests:
    assert is_happy_number(num) is res

print("\nAll tests passed\n")
