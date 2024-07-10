def merge_sorted_array(
    nums1: list[int], m: int, nums2: list[int], n: int
) -> None:
    """
    Leetcode. 88. Merge Sorted Array
    https://leetcode.com/problems/merge-sorted-array/description

    -----------------------------Description-----------------------------------
    You are given two integer arrays nums1 and nums2, sorted in non-decreasing
    order, and two integers m and n, representing the number of elements in
    nums1 and nums2 respectively. Merge nums1 and nums2 into a single array
    sorted in non-decreasing order. The final sorted array should not be
    returned by the function, but instead be stored inside the array nums1.
    To accommodate this, nums1 has a length of m + n, where the first m
    elements denote the elements that should be merged, and the last n
    elements are set to 0 and should be ignored. nums2 has a length of n.

    -----------------------------Constraints-----------------------------------
    : nums1.length == m + n
    : nums2.length == n
    : 0 <= m, n <= 200
    : 1 <= m + n <= 200
    : -10**9 <= nums1[i], nums2[j] <= 10**9

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
    The result of the merge is [1,2,2,3,5,6] with the underlined elements
    coming from nums1.

    Example 2:
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]
    Explanation: The arrays we are merging are [1] and [].
    The result of the merge is [1].

    Example 3:
    Input: nums1 = [0], m = 0, nums2 = [1], n = 1
    Output: [1]
    Explanation: The arrays we are merging are [] and [1].
    The result of the merge is [1].
    Note that because m = 0, there are no elements in nums1. The 0 is only
    there to ensure the merge result can fit in nums1.

    ------------------------------Algorithm------------------------------------
    We iterate over both arrays from the end. On each step we choose the
    greates number of the two arrays, decrementing its pointer respectively.
    We place the greates number at the end of the final array and decrement
    our pointer. At the end of the iteration there may be a situation
    where haven't fully traverse the second array. This may happen if value in
    that array are lower, than in the final array. In this case we place those
    numbers at the start of the final array.
    """
    if n == 0:
        return

    last_idx = len(nums1) - 1
    i = m - 1
    j = n - 1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            shift_end = nums1[i]
            i -= 1
        else:
            shift_end = nums2[j]
            j -= 1

        nums1[last_idx] = shift_end
        last_idx -= 1

    if j >= 0:
        nums1[0 : j + 1] = nums2[0 : j + 1]


nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]
merge_sorted_array(nums1, 3, nums2, len(nums2))
assert nums1 == [1, 2, 2, 3, 5, 6]

nums1 = [2, 3, 7, 0, 0]
nums2 = [1, 4]
merge_sorted_array(nums1, 3, nums2, len(nums2))
assert nums1 == [1, 2, 3, 4, 7]

nums1 = []
nums2 = [1]
merge_sorted_array(nums1, 0, nums2, len(nums2))
assert nums1 == [1]

print("\nAll tests passed\n")
