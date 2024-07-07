def move_zeroes(nums: list[int]) -> None:
    """
    Leetcode. 283. Move zeroes
    https://leetcode.com/problems/move-zeroes/description

    -----------------------------Description-----------------------------------
    Given an integer array nums, move all 0's to the end of it while
    maintaining the relative order of the non-zero elements. Note that you must
    do this in-place without making a copy of the array.

    -----------------------------Constraints-----------------------------------
    : 1 <= nums.length <= 10**4
    : -2**31 <= nums[i] <= 2**31 - 1

    ------------------------------Examples-------------------------------------
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]

    Example 2:
    Input: nums = [0]
    Output: [0]

    ------------------------------Algorithm------------------------------------
    Initialize an empty queue to store indexes of zeroes. Also set a zero
    counter to repopulate array with zeroes at the final stage. Iterate
    through the array for every zero store its index in queue and increment
    zero counter. For every non-zero value try to pop a zero index to place the
    value on it. After swap add current value's index to queue to mark this
    position as vacant for next values. Finally place as many zeroes at the end
    of the array as our zero counter.
    """
    from collections import deque

    length = len(nums)
    num_zeroes = 0
    queue = deque()

    for i in range(length):
        if nums[i] == 0:
            queue.append(i)
            num_zeroes += 1
        else:
            if queue:
                zero_idx = queue.popleft()
                nums[zero_idx] = nums[i]
                queue.append(i)

    for i in range(num_zeroes):
        nums[length - i - 1] = 0


a = [0, 0, 0, 1, 0, 2, 3, 0, 4]
b = [1]
c = [1, 2, 3, 4, 5]
d = [55, -1, 9, -13, 0, 1]
e = [0, 1, 0, 3, 12]
move_zeroes(a)
move_zeroes(b)
move_zeroes(c)
move_zeroes(d)
move_zeroes(e)

assert a == [1, 2, 3, 4, 0, 0, 0, 0, 0]
assert b == [1]
assert c == [1, 2, 3, 4, 5]
assert d == [55, -1, 9, -13, 1, 0]
assert e == [1, 3, 12, 0, 0]

print("\nAll tests passed\n")
