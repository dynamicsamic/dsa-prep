def max_area(height: list[int]) -> int:
    """
    Leetcode. 11. Container With Most Water
    https://leetcode.com/problems/container-with-most-water/description

    -----------------------------Description-----------------------------------
    You are given an integer array height of length n. There are n vertical 
    lines drawn such that the two endpoints of the ith line are (i, 0) 
    and (i, height[i]).

    Find two lines that together with the x-axis form a container,
    such that the container contains the most water.

    Return the maximum amount of water a container can store.

    Notice that you may not slant the container.

    ----------------------------Clarification----------------------------------
    The description of the problem is very unclear.
    The problem may stated something like:
    Given an array of integers find a subarray such that has the number
    of all its inner elements multiplied by the lesser of its borders
    produces the greatest number.    

    -----------------------------Constraints-----------------------------------    
    : n == height.length
    : 2 <= n <= 105
    : 0 <= height[i] <= 104

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: height = [1,8,6,2,5,4,8,3,7]
    Output: 49
    Explanation: The above vertical lines are represented by array 
    [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) 
    the container can contain is 49.
    
    Example 2:
    Input: height = [1,1]
    Output: 1

    ------------------------------Algorithm------------------------------------
    Since we need to look after border from both sides of the array/subarrays,
    we define two pointers which we bring closer on every step in order 
    to calculate the maximum `area`.
    On each step we define the lesser of two borders, multiply number of 
    elements in the array/subarray by this border and compare resulting
    number with the area we've seen so far.
    """
    left = 0
    right = len(height) - 1
    area = 0

    while left < right:
        current_area = min(height[left], height[right]) * (right - left)
        area = max(area, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return area


assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert max_area([1,1]) == 1
