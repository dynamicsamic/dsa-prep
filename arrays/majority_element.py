"""
Leetcode. 169. Majority Element
https://leetcode.com/problems/majority-element/description

-----------------------------Description-----------------------------------
Given an array nums of size n, return the majority element. The majority 
element is the element that appears more than ⌊n / 2⌋ times. You may 
assume that the majority element always exists in the array.

-----------------------------Constraints-----------------------------------
: n == nums.length
: 1 <= n <= 5 * 10**4
: -10**9 <= nums[i] <= 10**9

------------------------------Examples-------------------------------------
Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""


def majority_element_iter(nums: list[int]) -> int:
    """
    ------------------------------Algorithm------------------------------------
    First sort the array to place all elements next to each oother. Iterate
    through the array. For each number start a loop and count equal subsequent
    numbers. Check if current count is greater than the array's length. At some
    point we should hit the majority element.
    """
    nums.sort()

    length = len(nums)
    i = 0
    counter = 0

    while i < length:
        majority_el = nums[i]
        while nums[i] == majority_el:
            counter += 1
            i += 1
            if i == length:
                break
        if counter > length // 2:
            return majority_el

        counter = 0


def majority_element_moore(nums: list[int]) -> int:
    """
    ------------------------------Algorithm------------------------------------
    This solution uses Moore voting algorithm. The idea is that if the presence
    of the majority element is guaranteed, its count will always be greater
    than sum of other element's count. E.g. if we have nums=[1,2,1,3,2,3,2,2,2]
    the count of majority element (2) will be 5, while sum of counts of other
    elements will be 4. So we iterate through the array, if we have a 0 count,
    it means we are not sure about the majority element, and can pick up next
    one in the array. On every occurance of this element we increment the count,
    on every occurance we decrement it. If the count came to 0, we pick another
    element and repeat the proccess. By the end of the traversal the majority
    element will show up.
    """
    count = 0
    major_el = None

    for num in nums:
        if count == 0:
            major_el = num

        if num == major_el:
            count += 1

        else:
            count -= 1

    return major_el


def majority_element_median(nums: list[int]) -> int:
    """
    Sort the arrays and pick its median. This choice will always
    be true, because the number of majority element's copies is greater than
    half of the array.
    """
    nums.sort()
    return nums[len(nums) // 2]


assert majority_element_iter([1, 1, 1, 2, 2, 2, 2]) == 2
assert majority_element_iter([2, 2, 1, 1, 1, 2, 1]) == 1
assert majority_element_iter([1, 1, 2, 3, 3, 2, 2, 2, 2]) == 2
assert majority_element_iter([3, 2, 3]) == 3

assert majority_element_moore([1, 1, 1, 2, 2, 2, 2]) == 2
assert majority_element_moore([2, 2, 1, 1, 1, 2, 1]) == 1
assert majority_element_moore([1, 1, 2, 3, 3, 2, 2, 2, 2]) == 2
assert majority_element_moore([3, 2, 3]) == 3

assert majority_element_median([1, 1, 1, 2, 2, 2, 2]) == 2
assert majority_element_median([2, 2, 1, 1, 1, 2, 1]) == 1
assert majority_element_median([1, 1, 2, 3, 3, 2, 2, 2, 2]) == 2
assert majority_element_median([3, 2, 3]) == 3

print("\nAll tests passed\n")
