"""
:Example pass throughs

:ar = [3 1 2]
1st call: ar = [3 1 2]; left subar = [3 1], right subar = [2]
    2nd call: ar = [3 1]; left = [3], right = [1]
        3rd call (reccur left): ar = [3] -> returns 
        4th call (reccur right): ar = [1] -> returns
        - merging stage begins with left = [3], right = [1]
            at the end of merging stage ar gets resetteled as [1 3]
    5th call: ar = [2] -> returns
    - final merging stage begins with left = [1 3] and right = [2]
            at the end of merging stage ar gets resetteled as [1 2 3]

:ar = [2 7 8 3 6]
1st call: ar = [2 7 8 3 6]; left = [2 7], right = [8 3 6]
    2nd call: ar = [2 7]; left = [2], right = [7]
        3rd call (reccur left): ar = [2] -> returns
        4th call (reccur right): ar = [7] -> returns
        - merging stage begins with left = [2], right = [7]
            at the end of merging stage ar remains [2 7]
    5th call: ar = [8 3 6], left = [8], right = [3 6]
        6th call (reccur left): ar = [8] -> returns
        7th call (reccur right): ar = [3 6]; left = [3], right = [6]
            8th call (reccur left): ar = [3] -> returns
            9th call (reccur right): ar = [6] -> returns
        - merging stage begins with left = [8], right = [3 6]
            at the end of the merging stage ar gets resetteled as [3 6 8]
    - final merging stage begins with left = [2 7], right = [3 6 8]
        at the end of the merging stage ar gets resettled as [2 3 6 7 8]


:ar = [4 3 2 1 0]
1st call: ar = [4 3 2 1 0]; left = [4 3], right = [2 1 0]
    2nd call (reccur left): ar = [4 3]; left = [4], right[3]
        3rd call (reccur left): ar = [4] -> returns
        4th call (reccur right): ar = [3] -> returns
        - merging stage begins with left = [4], right = [3]
            at the end of the merging stage ar gets resetteled as [3 4]
    5th call (recurr right): ar = [2 1 0]; left = [2], right = [1 0]
        6th call (recurr left): ar = [2] -> returns;
        7th call (recurr right): ar = [1 0]; left = [1], right = [0]
            8th call (recurr left): ar = [1] -> returns
            9th call (recurr right): ar = [0] -> returns
            - merging stage begins with left = [1], right = [0]
                at the end of the merging stage ar gets resetteled as [0 1]
        - merging stage begins with left = [2], right = [0 1]
            at the end of the merging stage ar gets resetteled as [0 1 2]
    - merging stage begins with left = [3 4], right = [0 1 2]
        at the end of the merging stage ar gets resetteled as [0 1 2 3 4] 
"""


def merge_sort[T](arr: list[T]) -> None:
    if len(arr) < 2:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

    i = j = k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

a = [4, 3, 2, 1, 0]
a = [2]
merge_sort(a)
print(a)