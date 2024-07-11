def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Leetcode. 1. Two Sum
    https://leetcode.com/problems/two-sum/description

    -----------------------------Description-----------------------------------
    Given an array of integers nums and an integer target, return indices of
    the two numbers such that they add up to target. You may assume that each
    input would have exactly one solution, and you may not use the same element
    twice. You can return the answer in any order.

    -----------------------------Constraints-----------------------------------
    : 2 <= nums.length <= 104
    : -10**9 <= nums[i] <= 10**9
    : -10**9 <= target <= 10**9
    : Only one valid answer exists.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

    ------------------------------Algorithm------------------------------------
    The main idea here is if we have a target number and some other number, we
    can check if subtracting
    Define a compliments dict to store numbers and indexes there. Iterate over
    the nums array. For every new number we store the result of its subtraction
    from target thus we store the complements of this number and can conduct a
    fast search in the future. We also store its index as a dict value. If we
    find a number that is already in complements it means we have already seen
    its conterpart, therefore we should find it the complements dict and return
    along with current index.
    """
    complements = {}

    for i in range(len(nums)):
        if nums[i] in complements:
            return [complements[nums[i]], i]
        complements[target - nums[i]] = i


assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([3, 3], 6) == [0, 1]

print("\nAll tests passed")
