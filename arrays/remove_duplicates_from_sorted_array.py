"""
Leetcode. 26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description

-----------------------------Description-----------------------------------
Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the
number of unique elements in nums. Consider the number of unique elements
of nums to be k, to get accepted, you need to do the following things:
    - Change the array nums such that the first k elements of nums contain
    the unique elements in the order they were present in nums initially.
    The remaining elements of nums are not important as well as the size
    of nums.
    - Return k.

-----------------------------Constraints-----------------------------------
: 1 <= nums.length <= 3 * 10**4
: -100 <= nums[i] <= 100
: nums is sorted in non-decreasing order.

------------------------------Examples-------------------------------------
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements
of nums being 1 and 2 respectively. It does not matter what you leave
beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five
elements of nums being 0, 1, 2, 3, and 4 respectively. It does not matter
what you leave beyond the returned k (hence they are underscores).
"""


def remove_duplicates_with_seen(nums: list[int]) -> int:
    """
    ------------------------------Algorithm------------------------------------
    Initialize a seen array to store numbers we've encountered so far. Set
    the first number as our current number and store it in seen. Iterate through
    nums array, check each number against our current number. If it's a new
    number - update our current number variable and store this new number
    in seen. After the iteration the number of unique elements is the length of
    seen array. But before we return the number of unique elements we need to
    satisfy leetcode judge, so we place all unique elements on their respective
    places in the original array.
    """
    current = nums[0]
    seen = [current]

    for i in range(1, len(nums)):
        if nums[i] != current:
            current = nums[i]
            seen.append(current)

    for i in range(len(seen)):
        nums[i] = seen[i]

    return len(seen)


def remove_duplicates(nums: list[int]) -> int:
    """
    ------------------------------Algorithm------------------------------------
    Set a pointer j, which will point to the index, where a unique number
    should be placed. Start a loop in which compare current number with a
    previous one. If numbers are equal, place the current number to where
    j points to and increment j.
    """
    j = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[j] = nums[i]
            j += 1

    return j


assert remove_duplicates_with_seen([0, 1, 2, 3, 4]) == 5
assert remove_duplicates_with_seen([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
assert remove_duplicates_with_seen([0, 0, 1, 1, 1, 2, 2, 3, 4, 8, 8, 9]) == 7
assert remove_duplicates_with_seen([1, 1, 2]) == 2
assert remove_duplicates_with_seen([1, 1]) == 1

assert remove_duplicates([0, 1, 2, 3, 4]) == 5
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
assert remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 4, 8, 8, 9]) == 7
assert remove_duplicates([1, 1, 2]) == 2
assert remove_duplicates([1, 1]) == 1


print("\nAll tests passed\n")
