def subsets(nums: list[int]) -> list[list[int]]:
    """
    Leetcode. 78. Subsets
    https://leetcode.com/problems/subsets/description

    -----------------------------Description-----------------------------------
    Given an integer array nums of unique elements, return all possible subsets
    (the power set). The solution set must not contain duplicate subsets.
    Return the solution in any order.

    -----------------------------Constraints-----------------------------------
    : 1 <= nums.length <= 10
    : -10 <= nums[i] <= 10
    : All the numbers of nums are unique.

    ------------------------------Examples-------------------------------------
    Input: nums = [1,2,3]
    Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    Example 2:
    Input: nums = [0]
    Output: [[],[0]]

    ------------------------------Algorithm------------------------------------
    The outer function is a setup for the inner function to properly work. In
    the inner function before each successive function call we add a subset
    to the resulting array. We start a recursive loop which at every step spins
    out one or several `subloops`. On every subloop start we append the number
    from subloop to the temporary container named `subs` which may already
    contain a value from one or many of the previous outer loops. When loop
    reaches its end, the last added value gets pop out. Doing so we can pick
    next value and form a new unique combination.
    """

    res = []

    def backtrack(i: int, subs: list[int]) -> None:
        res.append(subs[:])

        for j in range(i, len(nums)):
            subs.append(nums[j])
            backtrack(j + 1, subs)
            subs.pop()

    backtrack(0, [])
    return res


assert subsets([1, 2, 3]) == [
    [],
    [1],
    [1, 2],
    [1, 2, 3],
    [1, 3],
    [2],
    [2, 3],
    [3],
]
assert subsets([0]) == [[], [0]]
