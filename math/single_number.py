def single_number(nums: list[int]) -> int:
    """
    Leetcode. 136. Single Number.
    https://leetcode.com/problems/add-binary/description

    -----------------------------Description-----------------------------------
    Given a non-empty array of integers nums, every element appears twice
    except for one. Find that single one. You must implement a solution
    with a linear runtime complexity and use only constant extra space.

    -----------------------------Constraints-----------------------------------
    : 1 <= nums.length <= 3 * 104
    : -3 * 104 <= nums[i] <= 3 * 104
    : Each element in the array appears twice except for one element which appears only once.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: nums = [2,2,1]
    Output: 1

    Example 2:
    Input: nums = [4,1,2,1,2]
    Output: 4

    Example 3:
    Input: nums = [1]
    Output: 1

    ------------------------------Algorithm------------------------------------
    The result of an XOR operation on a number with inself returns zero.
    Since we know that every value except one has a duplicate constantly
    applying XOR operation will eliminate all duplicates. And the remaining
    value will be the single one we were looking for.
    """
    single = nums[0]

    for i in range(1, len(nums)):
        single ^= nums[i]

    return single


assert single_number([4, 2, 1, 2, 1, 4, 5, 9, 3, 5, 9]) == 3
assert single_number([4, 2, 1, 2, 1]) == 4
assert single_number([2, 2, 1]) == 1
assert single_number([1]) == 1

print("\nAll tests passed\n")
