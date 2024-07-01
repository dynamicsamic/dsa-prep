def three_consecutive_odds(arr: list[int]) -> bool:
    """
    Leetcode. 1550. Three Consecutive Odds
    https://leetcode.com/problems/three-consecutive-odds/description

    -----------------------------Description-----------------------------------
    Given an integer array arr, return true if there are three consecutive odd
    numbers in the array. Otherwise, return false.

    -----------------------------Constraints-----------------------------------
    : 1 <= arr.length <= 1000
    : 1 <= arr[i] <= 1000

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: arr = [2,6,4,1]
    Output: false
    Explanation: There are no three consecutive odds.

    Example 2:
    Input: arr = [1,2,34,3,4,5,7,23,12]
    Output: true
    Explanation: [5,7,23] are three consecutive odds.

    ------------------------------Algorithm------------------------------------
    Traverse the array and count the number of consecutive odds. If encounter
    an even number the counter is set to zero. The traversal goes until the
    counter becomes equal to target number (3) or until we get to the end of
    the array. Lastly the counter is compared with the target number (3).
    """
    length = len(arr)
    target = 3

    if length < target:
        return False

    counter = i = 0
    while counter < target and i < length:
        if arr[i] % 2 != 0:
            counter += 1
        else:
            counter = 0

        i += 1

    return counter == target


assert not three_consecutive_odds([2, 6, 4, 1])
assert three_consecutive_odds([1, 2, 34, 3, 4, 5, 7, 23, 12])
assert three_consecutive_odds([1, 1, 2, 1, 1, 1])
assert not three_consecutive_odds([2, 2, 2])
assert not three_consecutive_odds([1, 3])

print("\nAll tests passed\n")
