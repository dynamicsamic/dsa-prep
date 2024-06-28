def search_range(nums: list[int], target: int) -> list[int]:
    """
    Leetcode. 34. Find First and Last Position of Element in Sorted Array
    https://leetcode.com/problems/
    find-first-and-last-position-of-element-in-sorted-array

    -----------------------------Description-----------------------------------
    Given an array of integers nums sorted in non-decreasing order,
    find the starting and ending position of a given target value.
    If target is not found in the array, return [-1, -1].
    You must write an algorithm with O(log n) runtime complexity.

    -----------------------------Constraints-----------------------------------
    : 0 <= nums.length <= 105
    : -109 <= nums[i] <= 109
    : nums is a non-decreasing array.
    : -109 <= target <= 109

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

    Example 2:
    Input: nums = [5,7,7,8,8,10], target = 6
    Output: [-1,-1]

    Example 3:
    Input: nums = [], target = 0
    Output: [-1,-1]

    ------------------------------Algorithm------------------------------------
    We basically just do two binarys searches on each half of the array by
    running two helper functions `search_left` and `search_right`.
    After that we combine the result in a list.
    """
    left = search_left(nums, target)
    right = search_right(nums, target)
    return [left, right]


def search_left(nums: list[int], target: int) -> int:
    """
    Do a binary search. When the target is found, place the right border on the
    mid's place and repeat the search on the left half of the array.
    Return the found result.
    """
    left = 0
    right = len(nums)
    found = -1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            right = mid
            found = mid

        elif target < nums[mid]:
            right = mid

        else:
            left = mid + 1

    return found


def search_right(nums: list[int], target: int) -> int:
    """
    Do a binary search. When the target is found, place the left border on the
    mid's place and repeat the search on the right half of the array.
    Return the found result.
    """
    left = 0
    right = len(nums)
    found = -1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] == target:
            left = mid + 1
            found = mid

        elif target < nums[mid]:
            right = mid

        else:
            left = mid + 1

    return found


assert search_range([5, 7, 7, 8, 8, 10], 7) == [1, 2]
assert search_range([5, 7, 7, 8, 8, 10], 8) == [3, 4]
assert search_range([1], 1) == [0, 0]
assert search_range([5, 7, 7, 8, 8, 10], 11) == [-1, -1]
assert search_range([1, 1], 1) == [0, 1]
assert search_range([], 0) == [-1, -1]
assert search_range([5, 7, 7, 8, 8, 10], 6) == [-1, -1]
