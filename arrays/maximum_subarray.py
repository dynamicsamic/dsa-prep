def max_subarray(nums: list[int]) -> int:
    """
    Leetcode. 55. Maximum Subarray.
    https://leetcode.com/problems/add-binary/description

    -----------------------------Description-----------------------------------
    Given an integer array nums, find the subarray with the largest sum, and
    return its sum.

    -----------------------------Constraints-----------------------------------
    : 1 <= nums.length <= 10**5
    : -10**4 <= nums[i] <= 10**4

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

    Example 2:
    Input: nums = [1]
    Output: 1
    Explanation: The subarray [1] has the largest sum 1.

    Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23
    Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

    ------------------------------Algorithm------------------------------------
    We iterate over the array. On each step we add current number to the
    current sum and check it against max_sum. If current sum turned negative
    we kind of invalidate to zero. We do this because negative current sum will
    surely decrease any of potential subarray sum. Since we don't want this to
    happen, we simply get rid of this dead weight.
    """
    max_sum = float("-inf")
    current_sum = 0

    for i in range(len(nums)):
        current_sum += nums[i]
        max_sum = max(max_sum, current_sum)

        if current_sum <= 0:
            current_sum = 0

    return max_sum


assert max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
assert max_subarray([5, 4, -1, 7, 8]) == 23
assert max_subarray([1]) == 1
assert max_subarray([-1]) == -1
assert max_subarray([-3, -1]) == -1

print("\nAll tests passed\n")
