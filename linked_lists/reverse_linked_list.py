"""
Leetcode. 2487. Remove Nodes From Linked List
https://leetcode.com/problems/remove-nodes-from-linked-list/description

-----------------------------Description---------------------------------------
You are given the head of a linked list. Remove every node which has a node 
with a greater value anywhere to the right side of it. Return the head of the 
modified linked list.

-----------------------------Constraints---------------------------------------
: The number of the nodes in the given list is in the range [1, 10**5].
: 1 <= Node.val <= 10**5

------------------------------Examples-----------------------------------------
Example 1:
Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.

Example 2:
Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
"""

import time
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        next_ = True if self.next else False
        return f"{self.__class__.__name__}[val={self.val}, next={next_}]"


def reverse_linked_list_stack(head: ListNode | None) -> ListNode:
    """
    ------------------------------Algorithm------------------------------------
    We use stack to collect all the nodes in reverse order. After that we
    pop every node out of the stack pointing previous nodes to next, thus
    creating a new tree.
    """
    if not head:
        return

    stack = []
    node = head

    while node:
        stack.append(node)
        node = node.next

    new_head = stack.pop()
    new_list = new_head
    while stack:
        new_list.next = stack.pop()
        new_list = new_list.next

    new_list.next = None  # invalidate the former head pointer
    return new_head


def reverse_linked_list(head: ListNode | None) -> ListNode:
    """
    ------------------------------Algorithm------------------------------------
    We set the prev variable that will represent the previous node, other nodes
    whill point to. Traverse through the list, for every node take its next
    pointer and save it. If we lost it, we could resume the iteration. Set the
    current's node pointer to point to previous node (which initially is None).
    Than define the current node as previous, so that the next node could point
    to it. After that resume iteration by taking our saved next pointer make it
    our current node.
    """
    current = head
    prev = None

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev


def to_list(head: Optional[ListNode]) -> list[int]:
    """Testing function."""
    res = []
    while head:
        res.append(head.val)
        head = head.next

    return res


n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

n7 = ListNode(1)
n6 = ListNode(2, n7)

start = time.perf_counter_ns()
assert to_list(reverse_linked_list_stack(n1)) == [5, 4, 3, 2, 1]
assert to_list(reverse_linked_list_stack(n6)) == [1, 2]
assert to_list(reverse_linked_list_stack(None)) == []
end = time.perf_counter_ns()
print(f"Stack approach takes {end-start} nanosec")


n5 = ListNode(5)
n4 = ListNode(4, n5)
n3 = ListNode(3, n4)
n2 = ListNode(2, n3)
n1 = ListNode(1, n2)

n7 = ListNode(1)
n6 = ListNode(2, n7)

start = time.perf_counter_ns()
assert to_list(reverse_linked_list(n1)) == [5, 4, 3, 2, 1]
assert to_list(reverse_linked_list(n6)) == [1, 2]
assert to_list(reverse_linked_list(None)) == []
end = time.perf_counter_ns()
print(f"O(1) space approach takes {end-start} nanosec")

print("\nAll tests passed")
