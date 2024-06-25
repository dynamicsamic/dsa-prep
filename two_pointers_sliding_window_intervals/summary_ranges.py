def summary_ranges(nums: list[int]) -> list[str]:
    """
    Leetcode. 228. Summary Ranges
    https://leetcode.com/problems/summary-ranges/description/

    -----------------------------Description-----------------------------------
    You are given a sorted unique integer array nums.
    A range [a,b] is the set of all integers from a to b (inclusive).

    Return the smallest sorted list of ranges that cover all the numbers
    in the array exactly. That is, each element of nums is covered by exactly
    one of the ranges, and there is no integer x such that x is in one of
    the ranges but not in nums.

    Each range [a,b] in the list should be output as:
        "a->b" if a != b
        "a" if a == b

    -----------------------------Constraints-----------------------------------
    : 0 <= nums.length <= 20
    : -231 <= nums[i] <= 231 - 1
    : All the values of nums are unique.
    : nums is sorted in ascending order.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: nums = [0,1,2,4,5,7]
    Output: ["0->2","4->5","7"]
    Explanation: The ranges are:
    [0,2] --> "0->2"
    [4,5] --> "4->5"
    [7,7] --> "7"

    Example 2:
    Input: nums = [0,2,3,4,6,8,9]
    Output: ["0","2->4","6","8->9"]
    Explanation: The ranges are:
    [0,0] --> "0"
    [2,4] --> "2->4"
    [6,6] --> "6"
    [8,9] --> "8->9"

    ------------------------------Algorithm------------------------------------
    Use two pointers `left` and `right` to track sequential ranges.
    Increment right pointer on every iteration. Increment left pointer
    if a range break found.
    If a break is found (i.e. next number is greater than previous number more
    than by 2) draw the range and append it to the resulting array.
    At the end of the iteration there will be unhandled range
    because we stop earlier than `nums` end. Append this range too.
    """
    ranges = []
    size = len(nums)

    if not size:
        pass
    elif size == 1:
        ranges.append(draw_range(nums[0], nums[0]))
    else:
        left = 0
        for right in range(size - 1):
            if nums[right + 1] - nums[right] > 1:
                ranges.append(draw_range(nums[left], nums[right]))
                left = right + 1

        ranges.append(draw_range(nums[left], nums[right + 1]))

    return ranges


def draw_range(num1: int, num2: int) -> str:
    return f"{num1}->{num2}" if num1 != num2 else str(num1)


assert summary_ranges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
assert summary_ranges([0, 1, 2, 3, 4, 5]) == ["0->5"]
assert summary_ranges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
assert summary_ranges([0, 1]) == ["0->1"]
assert summary_ranges([0]) == ["0"]
assert summary_ranges([1]) == ["1"]
assert summary_ranges([]) == []
