def min_subarray_len3(nums: list[int], target: int) -> int:
    """
    Leetcode. 209. Minimum Size Subarray Sum
    https://leetcode.com/problems/sort-colors/description

    -----------------------------Description-----------------------------------
    Given an array of positive integers nums and a positive integer target,
    return the minimal length of a subarray whose sum is greater than or equal
    to target. If there is no such subarray, return 0 instead.

    -----------------------------Constraints-----------------------------------
    : 1 <= target <= 109
    : 1 <= nums.length <= 105
    : 1 <= nums[i] <= 104

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: target = 7, nums = [2,3,1,2,4,3]
    Output: 2
    Explanation: The subarray [4,3] has the minimal length under the problem
    constraint.

    Example 2:
    Input: target = 4, nums = [1,4,4]
    Output: 1

    Example 3:
    Input: target = 11, nums = [1,1,1,1,1,1,1,1]
    Output: 0

    ------------------------------Algorithm------------------------------------
    Set up two pointers - left and right. Start loop and on each step check if
    current sum greater or equals target. If it's less than target it means we
    need to expand our window, so we increment right pointer and add right
    pointers sum to our current sum. If our current sum is greater or equals
    to target, it means we found a caindidate combination of values, so we
    save this combination in `addends` var, then we can shrink our window
    until it gets less than target and triggers the right pointer to start
    moving. Doing so we are able to make search in other parts of array and
    find other candidates. We also decrement our right pointer's value from
    current sum.
    """
    length = len(nums)
    addends = float("inf")
    current_sum = nums[0]
    left = right = 0

    while left < length:
        if current_sum < target:
            right += 1
            if right >= length:  # check right pointer does not go too far.
                break
            current_sum += nums[right]

        else:
            addends = min(addends, right - left + 1)
            current_sum -= nums[left]
            left += 1

    return addends if addends != float("inf") else 0


assert min_subarray_len3([3, 2, 1, 2, 4, 3, 2, 4, 1], 7) == 2
assert min_subarray_len3([3, 2, 1, 2, 4, 3, 2, 4, 1, 7], 7) == 1
assert min_subarray_len3([2, 3, 1, 2, 4, 3], 7) == 2
assert min_subarray_len3([1, 4, 4], 4) == 1
assert min_subarray_len3([1], 1) == 1
assert min_subarray_len3([1, 1, 1, 1, 1, 1, 1], 11) == 0
assert min_subarray_len3([1, 2, 3, 4, 5], 11) == 3
assert min_subarray_len3([1, 2, 3, 4, 5], 15) == 5

print("\nAll tests passed\n")
