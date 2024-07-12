from typing import Optional


def merge_two_lists(
    list1: Optional["ListNode"], list2: Optional["ListNode"]
) -> "ListNode":
    """
    Leetcode. 21. Merge Two Sorted Lists
    https://leetcode.com/problems/merge-two-sorted-lists/description

    -----------------------------Description-----------------------------------
    You are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. The list should be made by
    splicing together the nodes of the first two lists. Return the head of the
    merged linked list.

    -----------------------------Constraints-----------------------------------
    : The number of nodes in both lists is in the range [0, 50].
    : -100 <= Node.val <= 100
    : Both list1 and list2 are sorted in non-decreasing order.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: list1 = [1,2,4], list2 = [1,3,4]
    Output: [1,1,2,3,4,4]

    Example 2:
    Input: list1 = [], list2 = []
    Output: []

    Example 3:
    Input: list1 = [], list2 = [0]
    Output: [0]

    ------------------------------Algorithm------------------------------------
    Create a new head, which will be collecting all the other nodes. Traverse
    both list and determine, which one's node has the lowest current value and
    move its pointer next. On each iteration move current pointer of the new
    tree. Since we may traverse one of the lists faster than the other, we
    additionally check and taverse both of them separately. If any of them
    is not fihished, there may be only bigger numbers left, so we add them at
    the end of the list. Finally we return the next node our head is pointing
    to, since our head is an empty node.
    """
    if not list1:
        return list2
    elif not list2:
        return list1

    new_list = ListNode()
    head = new_list

    node1 = list1
    node2 = list2

    while node1 and node2:
        if node1.val < node2.val:
            new_list.next = node1
            node1 = node1.next
        else:
            new_list.next = node2
            node2 = node2.next

        new_list = new_list.next

    if node1:
        new_list.next = node1

    if node2:
        new_list.next = node2

    return head.next


class ListNode:
    def __init__(self, val=0, next=None):
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


node3 = ListNode(4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

node6 = ListNode(4)
node5 = ListNode(3, node6)
node4 = ListNode(1, node5)

merged = merge_two_lists(node1, node4)
assert to_list(merged) == [1, 1, 2, 3, 4, 4]


node3 = ListNode(6)
node2 = ListNode(4, node3)
node1 = ListNode(2, node2)

node6 = ListNode(5)
node5 = ListNode(3, node6)
node4 = ListNode(1, node5)

merged = merge_two_lists(node1, node4)
assert to_list(merged) == [1, 2, 3, 4, 5, 6]

print("\nAll tests passed")
