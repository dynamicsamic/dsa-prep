"""
Leetcode. 2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers/description

-----------------------------Description---------------------------------------
You are given two non-empty linked lists representing two non-negative integers
The digits are stored in reverse order, and each of their nodes contains a 
single digit. Add the two numbers and return the sum as a linked list.You may 
assume the two numbers do not contain any leading zero, except the 
number 0 itself.

-----------------------------Constraints---------------------------------------
: The number of nodes in each linked list is in the range [1, 100].
: 0 <= Node.val <= 9
: It is guaranteed that the list represents a number that does not have leading
  zeros.

------------------------------Examples-----------------------------------------
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
"""

import time
from typing import Optional


def add_two_numbers_stringify(
    l1: Optional["ListNode"], l2: Optional["ListNode"]
) -> "ListNode":
    """
    ------------------------------Algorithm------------------------------------
    Here we use a bold approach. We iterate both lists sequentially and store
    their digits as strings in two arrays. After iteration we reverse theese
    arrays turn them into integers, sum them together and turn the result back
    into string. Then we iterate from the back of the resulting string, convert
    string digits into integers and constructing the new list.
    """
    if not l1:
        return l2
    elif not l2:
        return l1

    c1 = []
    c2 = []

    node1 = l1
    node2 = l2

    while node1:
        c1.append(str(node1.val))
        node1 = node1.next

    while node2:
        c2.append(str(node2.val))
        node2 = node2.next

    c1.reverse()
    c2.reverse()
    num1 = int("".join(c1))
    num2 = int("".join(c2))
    num = str(num1 + num2)

    new_list = ListNode()
    head = new_list

    for i in range(len(num) - 1, -1, -1):
        head.val = int(num[i])
        if i == 0:
            break
        head.next = ListNode()
        head = head.next

    return new_list


def add_two_numbers(
    l1: Optional["ListNode"], l2: Optional["ListNode"]
) -> "ListNode":
    """
    ------------------------------Algorithm------------------------------------
    We iterate over both lists simultaneously. For each node from both arrays
    we take its value or 0, if one of the lists is already empty. We sum those
    digits and update the carry if the sum is greater than 9. We store the sum
    in a new node and point our new tree's current node to this node. After we
    move any of the two lists pointers forward. In the end we return the
    pointer to the new lists head.
    """
    new_head = ListNode()
    current = new_head
    carry = 0

    while l1 or l2 or carry:
        d1 = l1.val if l1 else 0
        d2 = l2.val if l2 else 0

        sum_ = d1 + d2 + carry
        value = sum_ % 10
        carry = sum_ // 10

        node = ListNode(value)
        current.next = node
        current = node

        if l1:
            l1 = l1.next

        if l2:
            l2 = l2.next

    return new_head.next


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        next_ = True if self.next else False
        return f"{self.__class__.__name__}[val={self.val}, next={next_}]"


def to_list(head: Optional[ListNode]) -> list[int]:
    """Testing function."""
    res = []
    while head:
        res.append(head.val)
        head = head.next

    return res


# l1 = [2,4,3], l2 = [5,6,4]
n3 = ListNode(3)
n2 = ListNode(4, n3)
n1 = ListNode(2, n2)

n6 = ListNode(4)
n5 = ListNode(6, n6)
n4 = ListNode(5, n5)

# l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
n77 = ListNode(9)
n66 = ListNode(9, n77)
n55 = ListNode(9, n66)
n44 = ListNode(9, n55)
n33 = ListNode(9, n44)
n22 = ListNode(9, n33)
n11 = ListNode(9, n22)

n222 = ListNode(9)
n111 = ListNode(9, n222)
n99 = ListNode(9, n111)
n88 = ListNode(9, n99)

# l1 = [2], l2 = [0]
n444 = ListNode(0)
n333 = ListNode(2)

# l1 = [0], l2 = [0]
n666 = ListNode(0)
n555 = ListNode(0)

start = time.perf_counter_ns()
assert to_list(add_two_numbers_stringify(n1, n4)) == [7, 0, 8]
assert to_list(add_two_numbers_stringify(n11, n88)) == [8, 9, 9, 9, 0, 0, 0, 1]
assert to_list(add_two_numbers_stringify(n333, n444)) == [2]
assert to_list(add_two_numbers_stringify(n555, n666)) == [0]
end = time.perf_counter_ns()
print(f"Stringify approcah takes {end-start} nanosec")

start = time.perf_counter_ns()
assert to_list(add_two_numbers(n1, n4)) == [7, 0, 8]
assert to_list(add_two_numbers(n11, n88)) == [8, 9, 9, 9, 0, 0, 0, 1]
assert to_list(add_two_numbers(n333, n444)) == [2]
assert to_list(add_two_numbers(n555, n666)) == [0]
end = time.perf_counter_ns()
print(f"Iterative approcah takes {end-start} nanosec")
