"""
Leetcode. 50. Plus One
https://leetcode.com/problems/plus-one/description

-----------------------------Description---------------------------------------
You are given a large integer represented as an integer array digits, where 
each digits[i] is the ith digit of the integer. The digits are ordered from 
most significant to least significant in left-to-right order. The large integer 
does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.

-----------------------------Constraints---------------------------------------
: 1 <= digits.length <= 100
: 0 <= digits[i] <= 9
: digits does not contain any leading 0's.

------------------------------Examples-----------------------------------------
Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""


def plus_one(digits: list[int]) -> list[int]:
    """
    ------------------------------Algorithm------------------------------------
    First increment the last digit of the array and find if it' less than 10.
    If it is greater than 10, that mean we have a carry and need to handle it.
    Carry can potitially cause all our subsequent digits to shift to 10 and
    thus have their own carries. To handle this properly we start a loop and
    iterate while we have a carry. At the end we add the carry as the first
    digit.
    """
    i = len(digits) - 1
    carry, r = divmod(digits[i] + 1, 10)
    digits[i] = r

    while i > 0 and carry:
        i -= 1
        carry, r = divmod(digits[i] + carry, 10)
        digits[i] = r

    if carry:
        return [1] + digits

    return digits


def plus_one2(digits: list[int]) -> list[int]:
    """
    We glue all the digits in a string, then covert it to integer.
    After that we increment the resulting number and collect separate
    digits into a list.
    """
    num = int("".join((str(d) for d in digits)))
    return [int(d) for d in str(num + 1)]


assert plus_one([9, 9, 9]) == [1, 0, 0, 0]
assert plus_one([9, 8]) == [9, 9]
assert plus_one([3, 4]) == [3, 5]


assert plus_one2([9, 9, 9]) == [1, 0, 0, 0]
assert plus_one2([9, 8]) == [9, 9]
assert plus_one2([3, 4]) == [3, 5]

print("\nAll tests passed\n")
