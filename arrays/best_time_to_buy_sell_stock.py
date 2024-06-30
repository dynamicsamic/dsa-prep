"""
Leetcode. 122. Best Time to Buy and Sell Stock II
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description

-----------------------------Description-----------------------------------
You are given an integer array prices where prices[i] is the price of a given 
stock on the ith day. On each day, you may decide to buy and/or sell the stock. 
You can only hold at most one share of the stock at any time. 
However, you can buy it then immediately sell it on the same day.
Find and return the maximum profit you can achieve.

-----------------------------Constraints-----------------------------------
: 1 <= prices.length <= 3 * 104
: 0 <= prices[i] <= 104

------------------------------Examples-------------------------------------
Example 1:
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
"""


def best(prices: list[int]) -> int:
    """
    ------------------------------Algorithm------------------------------------
    Set two pointers. First ponter - `i` will traverse the prices array and
    check every two adjacent numbers. If the left number is less than the
    right number it means we encoutered a growing trend in stock prices. We
    keep moving the i pointer front and check the maximum difference between
    stock prices. If the right number is less or equal to the previous one,
    it means we encountered a decline in stock prices. So we increment the
    total sum by the current sum and move second pointer to check if next
    sections of array have growing trends.
    After the loop we check our current sum, and if it is greater than zero,
    we add it to our total sum.
    """
    total = 0
    current_sum = 0
    buy_index = 0

    for i in range(1, len(prices)):
        if prices[i] <= prices[i - 1]:
            total += current_sum
            current_sum = 0
            buy_index = i

        else:
            current_sum = max(current_sum, prices[i] - prices[buy_index])

    if current_sum:
        total += current_sum

    return total


def max_pfofit(prices: list[int]) -> int:
    """
    ------------------------------Algorithm------------------------------------
    We traverse the array, and add every positive difference between two
    adjacent numbers to our total. The idea is that no matter between which
    two numbers this positive difference exists, it should be added to the
    total result to maximaize the profit.
    """
    total = 0

    for i in range(1, len(prices)):
        total += max(0, prices[i] - prices[i - 1])

    return total


a = [5, 4, 6, 1, 2, 5]
b = [7, 1, 5, 3, 6, 4]
c = [1, 2, 3, 4, 5]
d = [7, 6, 4, 3, 1]
e = [1, 1]

assert best(a) == max_pfofit(a) == 6
assert best(b) == max_pfofit(b) == 7
assert best(c) == max_pfofit(c) == 4
assert best(d) == max_pfofit(d) == 0
assert best(e) == max_pfofit(e) == 0
