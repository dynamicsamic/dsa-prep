def longest_consecutive(nums: list[int]) -> int:
    """
    Leetcode. 128. Longest Consecutive Sequence
    https://leetcode.com/problems/longest-consecutive-sequence/description

    -----------------------------Description-----------------------------------
    Given an unsorted array of integers nums, return the length of the longest
    consecutive elements sequence.
    You must write an algorithm that runs in O(n) time.

    -----------------------------Constraints-----------------------------------
    : 0 <= nums.length <= 105
    : -109 <= nums[i] <= 109

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: nums = [100,4,200,1,3,2]
    Output: 4
    Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
    Therefore its length is 4.

    Example 2:
    Input: nums = [0,3,7,2,5,8,4,6,0,1]
    Output: 9

    ------------------------------Algorithm------------------------------------
    From the conext of the problem we can see that duplicate values such as
    0,...0,...0 don't affect the final count, so we can eliminate them in
    order to not accidentally count them more than once.
    That's why firstly create a set with nums values. Next we iterate through
    the set and find a number that does not have a preceding value. Such a
    number would be the start of a sequence. E.g. if there is a 1 and no 0,
    it means that 1 may be the start of a new suquence. If we found the start
    of a sequence we iterate the set again and increment our counter each time
    we found a value that is greater than our number by 1.
    After the loop we choose the maximum between our current count and the
    maximum count so far.
    """
    if (length := len(nums)) < 2:
        return length

    longest = 0
    unique = set(nums)

    for num in unique:
        if num - 1 not in unique:
            count = 1
            next_num = num + 1
            while next_num in unique:
                count += 1
                next_num += 1
            longest = max(longest, count)

    return longest


assert longest_consecutive([4, 2, 5, 1, 3, 5, 0]) == 6
assert longest_consecutive([1, 10, 2]) == 2
assert longest_consecutive([1, 10]) == 1
assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
assert longest_consecutive([0, 5, 9]) == 1
assert longest_consecutive([2]) == 1
assert longest_consecutive([]) == 0
assert longest_consecutive([1, 2, 8, 9, 10]) == 3
assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9

print("\nAll tests passed\n")
