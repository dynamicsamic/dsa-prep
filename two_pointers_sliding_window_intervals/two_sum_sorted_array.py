def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    Leetcode. 167. Two Sum II - Input Array Is Sorted
    https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description

    -----------------------------Description-----------------------------------
    Given a 1-indexed array of integers numbers that is already sorted
    in non-decreasing order, find two numbers such that they add up to a
    specific target number. Let these two numbers be numbers[index1] and
    numbers[index2] where 1 <= index1 < index2 <= numbers.length.

    Return the indices of the two numbers, index1 and index2, added by one as
    an integer array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution. You may
    not use the same element twice.

    Your solution must use only constant extra space.
    
    -----------------------------Constraints-----------------------------------
    : 2 <= numbers.length <= 3 * 104
    : -1000 <= numbers[i] <= 1000
    : numbers is sorted in non-decreasing order.
    : -1000 <= target <= 1000

    -------------------------------Examples------------------------------------
    Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9.
    Therefore, index1 = 1, index2 = 2. We return [1, 2].

    Example 2:
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6.
    Therefore index1 = 1, index2 = 3. We return [1, 3].

    Example 3:
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1.
    Therefore index1 = 1, index2 = 2. We return [1, 2].

    ------------------------------Algorithm------------------------------------
    Since the presence of `target` is guaranteed by the defifnition
    we traverse `numbers` from both sides until we find the matching pair.
    If sum of the pair is less than target - increment the lesser left pointer.
    Otherwise decrement the greater right pointer.
    """
    i = 0
    j = len(numbers) - 1

    while i < j:
        if numbers[i] + numbers[j] == target:
            # Here we could just return the list of indexes,
            # but to fit in leetcode's requirements, we need
            # to increment idexes to match 1-based index count.
            return [
                i + 1,
                j + 1,
            ]
        elif numbers[i] + numbers[j] > target:
            j -= 1
        else:
            i += 1


assert two_sum([1, 2, 4, 5, 6, 7, 8, 9], 15) == [5, 8]
assert two_sum([2, 7, 11, 15], 9) == [1, 2]
assert two_sum([2, 3, 4], 6) == [1, 3]
assert two_sum([-1, 0], -1) == [1, 2]
