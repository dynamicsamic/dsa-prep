# exmaples
nums1 = [1, 2, 3, 0, 0, 0]
nums2 = [2, 5, 6]

# nums1 = [2, 3, 7, 0, 0]
# nums2 = [1, 4]
nums1 = [0]
m = 0
nums2 = [1]
n = 1


def merge_sorterd_array(
    nums1: list[int], m: int, nums2: list[int], n: int
) -> None:
    """
    Given two arrays both sorted in non-decreasing order
    merge both of them into the first array `nums1` preserving the order.
    The merging must happen in-place.

    Args:
        nums1 (list[int]): the first array.

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
