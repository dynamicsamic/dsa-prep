def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    """
    Leetcode. 219. Contains Duplicate II
    https://leetcode.com/problems/contains-duplicate-ii/description

    -----------------------------Description-----------------------------------
    Given an integer array nums and an integer k, return true if there are two
    distinct indices i and j in the array such that nums[i] == nums[j]
    and abs(i - j) <= k.

    -----------------------------Constraints-----------------------------------
    : 1 <= nums.length <= 10**5
    : -10**9 <= nums[i] <= 10**9
    : 0 <= k <= 10**5

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: nums = [1,2,3,1], k = 3
    Output: true

    Example 2:
    Input: nums = [1,0,1,1], k = 1
    Output: true

    Example 3:
    Input: nums = [1,2,3,1,2,3], k = 2
    Output: false

    ------------------------------Algorithm------------------------------------
    Define an empty seen dict. Iterate through the array. On each step check if
    we haven't seen the number - add the number to seen with its index as value.
    If we've already seen this number check if the difference between
    current index and index of the added number are less or equal to k. If so -
    we return true. If the iteration ended without returning, in means
    there is no such pair.
    """
    seen = {}

    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    return False


tests = [
    ([1, 2, 2, 1], 3, True),
    ([1, 2, 3, 1], 1, False),
    ([1, 2, 3, 1, 1], 1, True),
    ([1, 0, 1, 1], 1, True),
    ([1, 2, 3, 1, 2, 3], 2, False),
    ([1, 2, 3, 1], 3, True),
]

for nums, k, res in tests:
    assert contains_nearby_duplicate(nums, k) is res

print("\nAll tests passed\n")
