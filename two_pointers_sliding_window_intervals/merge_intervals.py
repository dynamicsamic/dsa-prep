def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    """
    Leetcode. 56. Merge Intervals
    https://leetcode.com/problems/merge-intervals/description

    -----------------------------Description-----------------------------------
    Given an array of intervals where intervals[i] = [starti, endi],
    merge all overlapping intervals, and return an array of the non-overlapping
    intervals that cover all the intervals in the input.

    -----------------------------Constraints-----------------------------------
    : 1 <= intervals.length <= 104
    : intervals[i].length == 2
    : 0 <= starti <= endi <= 104

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

    Example 2:
    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.

    ------------------------------Algorithm------------------------------------
    Sort the intervals first to be able to make comparisons between
    subsuquent intervals. Iterate over intervals.
    If the resulting array is empty add current interval.
    Also if current interval's left border greater than the right border
    of the interval that we added to result latest it means we encountered
    non-overlapping intervals. Simply add to the result.
    Otherwise it means that find an overlapping interval.
    Determine which of the right borders is greater and update the last
    interval's right border if needed.
    """

    if len(intervals) == 1:
        return intervals

    intervals.sort(key=lambda x: x[0])

    result = []

    for i in intervals:
        if not result or result[-1][1] < i[0]:
            result.append(i)
        else:
            result[-1][1] = max(result[-1][1], i[1])

    return result


assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
    [1, 6],
    [8, 10],
    [15, 18],
]
assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]
assert merge_intervals([[0, 0], [0, 0]]) == [[0, 0]]
assert merge_intervals([[1, 4], [0, 4]]) == [[0, 4]]
assert merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]
