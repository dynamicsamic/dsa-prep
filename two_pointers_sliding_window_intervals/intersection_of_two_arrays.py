def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    """
    Leetcode. 349. Intersection of Two Arrays
    https://leetcode.com/problems/intersection-of-two-arrays/description

    -----------------------------Description-----------------------------------
    Given two integer arrays nums1 and nums2, return an array of their
    intersection. Each element in the result must be unique and you may return
    the result in any order.

    -----------------------------Constraints-----------------------------------
    : 1 <= nums1.length, nums2.length <= 1000
    : 0 <= nums1[i], nums2[i] <= 1000

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2]

    Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [9,4]
    Explanation: [4,9] is also accepted.

    ------------------------------Algorithm------------------------------------
    Firstly sort both arrays to be able to track which value of the arrays
    comes next. Next we set two pointers to track values for each array.
    If values from both arrays equal we store the value in the resulting
    array unless this value is not already in it. For equal values we increment
    both pointers. Otherwise we increment pointer which points to the
    lowest value.
    """
    result = []
    nums1.sort()
    nums2.sort()

    l1 = len(nums1)
    l2 = len(nums2)

    i = j = 0

    while i < l1 and j < l2:
        if nums1[i] == nums2[j]:
            if not result or nums1[i] != result[-1]:
                result.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1

    return result


def intersection_one_line(nums1: list[int], nums2: list[int]) -> list[int]:
    return list(set(nums1).intersection(nums2))


assert intersection([1, 2, 2, 1], [2, 1]) == [1, 2]
assert intersection([1, 2, 2, 1], [2, 2]) == [2]
assert intersection([4, 9, 5], [9, 4, 9, 8, 4]) == [4, 9]
assert intersection([3, 5], [1, 6, 7]) == []
assert intersection([1], [1]) == [1]

assert intersection_one_line([1, 2, 2, 1], [2, 1]) == [1, 2]
assert intersection_one_line([1, 2, 2, 1], [2, 2]) == [2]
assert intersection_one_line([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]
assert intersection_one_line([3, 5], [1, 6, 7]) == []
assert intersection_one_line([1], [1]) == [1]