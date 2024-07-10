import time

"""
Leetcode. 27. Remove Element
https://leetcode.com/problems/remove-element/description

-----------------------------Description-----------------------------------
Given an integer array nums and an integer val, remove all occurrences of val 
in nums in-place. The order of the elements may be changed. Then return the 
number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:
  - Change the array nums such that the first k elements of nums contain 
  the elements which are not equal to val. The remaining elements of nums 
  are not important as well as the size of nums.
  - Return k.

-----------------------------Constraints-----------------------------------
: 0 <= nums.length <= 100
: 0 <= nums[i] <= 50
: 0 <= val <= 100

------------------------------Examples-------------------------------------
Input: nums = [1,1,2]
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements 
of nums being 2. It does not matter what you leave beyond the returned 
k (hence they are underscores).

Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements 
of nums containing 0, 0, 1, 3, and 4. Note that the five elements can be returned 
in any order.It does not matter what you leave beyond the returned k 
(hence they are underscores).
"""


def remove_element(nums: list[int], val: int) -> int:
    """
    ------------------------------Algorithm------------------------------------
    Set a pointer i, which will point to the index, where a valid number
    should be placed. Start a loop in which compare current number with `val`.
    If current number is a valid number we place in it the current index which
    i points to and increment i.
    """
    i = 0

    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1

    return i


def remove_element_two_pointers(nums: list[int], val: int) -> int:
    """
    ------------------------------Algorithm------------------------------------
    Set two pointers which will traverse array from both sides. Left pointer
    moves only if it finds a value that is not equal to val. Right pointer
    moves only if the left pointer found number eqaul to val and performed a
    swap. At the end we return left pointer.
    """
    l = 0
    r = len(nums) - 1

    while l <= r:
        if nums[l] == val:
            nums[l], nums[r] = nums[r], nums[l]
            r -= 1
        else:
            l += 1

    return l


def remove_element_hacky(nums: list[int], val: int) -> int:
    """
    ------------------------------Algorithm------------------------------------
    Create an additional array of consisting only from valid numbers. Put all
    these numbers in the original array.
    """
    valid = [num for num in nums if num != val]

    for i in range(len(valid)):
        nums[i] = valid[i]

    return len(valid)


start = time.perf_counter()
nums = [3, 2, 2, 3]
assert remove_element(nums, 3) == 2
assert nums[:2] == [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
assert remove_element(nums2, 2) == 5
assert nums2[:5] == [0, 1, 3, 0, 4]

nums3 = [3, 3]
assert remove_element(nums3, 3) == 0

nums4 = [3, 3]
assert remove_element(nums4, 5) == 2
assert nums4[:2] == [3, 3]
end = time.perf_counter()
print(
    f"It took {(end-start)*1000:.5f} miliseconds for one pointer remove element"
)

start = time.perf_counter()
nums = [3, 2, 2, 3]
assert remove_element_hacky(nums, 3) == 2
assert nums[:2] == [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
assert remove_element_hacky(nums2, 2) == 5
assert nums2[:5] == [0, 1, 3, 0, 4]

nums3 = [3, 3]
assert remove_element_hacky(nums3, 3) == 0

nums4 = [3, 3]
assert remove_element_hacky(nums4, 5) == 2
assert nums4[:2] == [3, 3]
end = time.perf_counter()
print(f"It took {(end-start)*1000:.5f} miliseconds for hacky remove element")


start = time.perf_counter()
nums = [3, 2, 2, 3]
assert remove_element_two_pointers(nums, 3) == 2
assert nums[:2] == [2, 2]

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
assert remove_element_two_pointers(nums2, 2) == 5
assert nums2[:5] == [0, 1, 4, 0, 3]

nums3 = [3, 3]
assert remove_element_two_pointers(nums3, 3) == 0

nums4 = [3, 3]
assert remove_element_two_pointers(nums4, 5) == 2
assert nums4[:2] == [3, 3]
end = time.perf_counter()
print(
    f"It took {(end-start)*1000:.5f} miliseconds for two pointers remove element"
)

print("\nAll tests passed\n")
