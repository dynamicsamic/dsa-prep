def can_jump(nums: list[int]) -> bool:
    """
    Leetcode. 55. Jump Game
    https://leetcode.com/problems/jump-game/description

    -----------------------------Description-----------------------------------
    You are given an integer array nums. You are initially positioned at the
    array's first index, and each element in the array represents your maximum
    jump length at that position.
    Return true if you can reach the last index, or false otherwise.

    -----------------------------Constraints-----------------------------------
    : 1 <= nums.length <= 10**4
    : 0 <= nums[i] <= 10**5

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: nums = [2,3,1,1,4]
    Output: true
    Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

    Example 2:
    Input: nums = [3,2,1,0,4]
    Output: false
    Explanation: You will always arrive at index 3 no matter what. Its maximum
    jump length is 0, which makes it impossible to reach the last index.

    ------------------------------Algorithm------------------------------------
    First initialize a variable `step_cost` that will track the cost to make
    the next successfull step. We start iterating the nums array from the rear,
    at the second to last index. On each step we chek the number on a given
    index. If the number is less than our cost, that means we can't make a
    jump, so we increment the cost for the next position. If we number
    is greater or equal to step cost, that means we can make a jump, so we
    set the possible flag to True and set the step cost back to 1.
    """
    i = len(nums) - 2
    step_cost = 1
    possible = True

    while i >= 0:
        if nums[i] >= step_cost:
            possible = True
            step_cost = 1
        else:
            possible = False
            step_cost += 1
        i -= 1

    return possible


assert can_jump([1, 3, 0, 2, 0, 4])
assert can_jump([2, 3, 1, 1, 4])
assert can_jump([1])
assert can_jump([7, 0, 0, 0, 0, 0, 0, 4])
assert not can_jump([7, 0, 0, 0, 0, 0, 0, 0, 4])
assert not can_jump([2, 3, 3, 0, 0, 0, 4])
assert not can_jump([3, 2, 1, 0, 4])
assert not can_jump([0, 2])

print("\nAll tests passed\n")
