def sort_colors_counting(nums: list[int]) -> None:
    """
    Leetcode. 75. Sort Colors
    https://leetcode.com/problems/sort-colors/description

    -----------------------------Description-----------------------------------
    Given an array nums with n objects colored red, white, or blue, sort them
    in-place so that objects of the same color are adjacent, with the colors
    in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white,
    and blue, respectively.

    You must solve this problem without using the library's sort function.

    -----------------------------Constraints-----------------------------------
    : n == nums.length
    : 1 <= n <= 300
    : nums[i] is either 0, 1, or 2.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]

    Example 2:
    Input: nums = [2,0,1]
    Output: [0,1,2]

    ------------------------------Algorithm------------------------------------
    Since the range of numbers is low we can use counting sort. Set up
    additional `counts` array to count every occurance of each num.
    After counting place indexes from counts to their corresponding places
    in nums array.
    """
    counts = [0, 0, 0]

    for num in nums:
        counts[num] += 1

    i = j = 0
    for i in range(len(counts)):
        while counts[i]:
            nums[j] = i
            counts[i] -= 1
            j += 1


def sort_colors_pointers(nums: list[int]) -> None:
    """
    ------------------------------Algorithm------------------------------------
    Declare three pointers: `left` and `right` will track front and rear parts
    of the array, and `i` will traverse the array and check each item.
    Traverse the array i meet the right pointers meet.
    On each pass follow rules:
        - if encounter 2, swap it with the right pointer and increment it.
        - if encounter 1, increment i pointer since we need all ones
            to be in the middle .
        - if encounter 0: swap it with the left pointer and increment both
            left and i pointers.
    """
    left = 0
    right = len(nums) - 1
    i = 0

    while i <= right:
        if nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        elif nums[i] == 1:
            i += 1
        elif nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
            i += 1


a = [2, 1, 1, 2, 0, 0]
sort_colors_counting(a)
assert a == [0, 0, 1, 1, 2, 2]

b = [2, 0, 1]
sort_colors_counting(b)
assert b == [0, 1, 2]

c = [2]
sort_colors_counting(c)
assert c == [2]

d = [2, 1, 1, 2, 0, 0]
sort_colors_pointers(d)
assert d == [0, 0, 1, 1, 2, 2]

e = [2, 0, 1]
sort_colors_pointers(e)
assert e == [0, 1, 2]

f = [2]
sort_colors_pointers(f)
assert f == [2]