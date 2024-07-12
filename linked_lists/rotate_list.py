"""
Leetcode. 61. Rotate List
https://leetcode.com/problems/rotate-list/description

-----------------------------Description-----------------------------------
Given the head of a linked list, rotate the list to the right by k places.

-----------------------------Constraints-----------------------------------
: 1 <= nums.length <= 3 * 10**4
: -100 <= nums[i] <= 100
: nums is sorted in non-decreasing order.

------------------------------Examples-------------------------------------
Input: nums = [1,1,2]
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""

import time
from collections import deque
from typing import Optional


def rotate_right_queue(
    head: Optional["ListNode"], k: int
) -> Optional["ListNode"]:
    """
    ------------------------------Algorithm------------------------------------
    To be able to move k elements we need to find out how many nodes there
    are in the list in total. We traverse through the list and count number of
    its nodes simultaneoulsy adding them to the queue. After that we restrict
    number of rotates to be less than the size. We perform rotations by poping
    a node from queue's rear and pushing it to queue's front. After the
    rotation we construct a new list from the queue and return the new head.
    """
    if not head or not head.next or not k:
        return head

    size = 0
    queue = deque()

    node = head
    while node:
        queue.append(node)
        size += 1
        node = node.next

    for _ in range(k % size):
        queue.appendleft(queue.pop())

    new_list = ListNode()
    new_head = new_list
    for el in queue:
        el.next = None
        new_head.next = el
        new_head = new_head.next

    return new_list.next


def rotate_right(head: Optional["ListNode"], k: int) -> Optional["ListNode"]:
    """
    ------------------------------Algorithm------------------------------------
    Here we decided to go without queue (thus savig up some space). Again we
    count the size of the list to not let the rotation go off the range. We
    traverse the list again each time stopping on the second to last node. We
    update pointers and then repeat this process. After every step of the loop
    we have our last node set as head and pointing at the former head, and our
    second to last node pointing to None.
    """
    if not head or not head.next or not k:
        return head

    size = 0
    current = head

    while current:
        size += 1
        current = current.next

    for _ in range(k % size):
        current = head
        lead = head
        while getattr(current.next, "next", None):
            current = current.next

        current.next.next = lead
        head = current.next
        current.next = None

    return head


def rotate_right_circular(
    head: Optional["ListNode"], k: int
) -> Optional["ListNode"]:
    """
    ------------------------------Algorithm------------------------------------
    This algorithm uses a little hack with making the list circular, i.e.
    connecting the last and head nodes. Again first we count the number of
    nodes, but this time we stop at the last node. That's why we start our
    count from 1 (not 0). After counting was finished, we connect our last node
    to the head. Next we need to traverse the list one more time, but this time
    we need to stop just before our future head node. I.e. if we out of 5 nodes
    we need to rotate 2 nodes, it means that node4 will be our future head.
    That's why we stop just before it at node3. We take node3's next pointer
    (which points to our future head) and save it for later use. We then remove
    node3's next pointer, turning this list back into a singly linked and
    making node3 the last element in the list. We return our new head, pointer
    to which we saved earlier.
    """
    if not head or not head.next or not k:
        return head

    size = 1
    current = head

    while current.next:
        size += 1
        current = current.next

    current.next = head
    for _ in range(1, size - (k % size)):
        head = head.next

    current = head.next
    head.next = None

    return current


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


node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

n3 = ListNode(2)
n2 = ListNode(1, n3)
n1 = ListNode(0, n2)

start = time.perf_counter_ns()
assert to_list(rotate_right(node1, 2)) == [4, 5, 1, 2, 3]
assert to_list(rotate_right(n1, 4)) == [2, 0, 1]
end = time.perf_counter_ns()
print(f"General approach takes {end-start} nanosec")

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

n3 = ListNode(2)
n2 = ListNode(1, n3)
n1 = ListNode(0, n2)

start = time.perf_counter_ns()
assert to_list(rotate_right_queue(node1, 2)) == [4, 5, 1, 2, 3]
assert to_list(rotate_right_queue(n1, 4)) == [2, 0, 1]
end = time.perf_counter_ns()
print(f"Queue approach takes {end-start} nanosec")

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

n3 = ListNode(2)
n2 = ListNode(1, n3)
n1 = ListNode(0, n2)

start = time.perf_counter_ns()
assert to_list(rotate_right_circular(node1, 2)) == [4, 5, 1, 2, 3]
assert to_list(rotate_right_circular(n1, 4)) == [2, 0, 1]
end = time.perf_counter_ns()
print(f"Circular approach takes {end-start} nanosec")

print("\nAll tests passed")