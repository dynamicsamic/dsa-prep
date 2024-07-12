from typing import Optional


def remove_nth_from_end(
    head: Optional["ListNode"], n: int
) -> Optional["ListNode"]:
    """
    Leetcode. 19. Remove Nth Node From End of List
    https://leetcode.com/problems/remove-nth-node-from-end-of-list//description

    -----------------------------Description-----------------------------------
    Given the head of a linked list, remove the nth node from the end of the
    list and return its head.

    -----------------------------Constraints-----------------------------------
    : The number of nodes in the list is sz.
    : 1 <= sz <= 30
    : 0 <= Node.val <= 100
    : 1 <= n <= sz

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: head = [1,2,3,4,5], n = 2
    Output: [1,2,3,5]

    Example 2:
    Input: head = [1], n = 1
    Output: []

    Example 3:
    Input: head = [1,2], n = 1
    Output: [1]

    ------------------------------Algorithm------------------------------------
    Traverse the list once to count its size. Perform checks on n to ensure we
    are able to make such a deletion. Traverse the list again and stop before
    the to-be-deleted node. Set current nodes next pointer to the node after
    the one to-be-deleted. Return head.
    """
    size = 0
    current = head

    while current:
        size += 1
        current = current.next

    if n > size or size == 0:
        return head

    idx = size - n

    if idx == 0:
        return head.next

    current = head
    for _ in range(idx - 1):
        current = current.next

    current.next = current.next.next
    return head


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

assert to_list(remove_nth_from_end(node1, 2)) == [1, 2, 3, 5]
assert to_list(remove_nth_from_end(node1, 1)) == [1, 2, 3]

node2 = ListNode(2)
node1 = ListNode(1, node2)
assert to_list(remove_nth_from_end(node1, 2)) == [2]

print("\nAll tests passed")
