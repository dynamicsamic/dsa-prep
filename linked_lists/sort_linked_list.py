from typing import Optional


def sort_linked_list(head: Optional["ListNode"]) -> "ListNode":
    """
    Leetcode. 148. Sort List
    https://leetcode.com/problems/sort-list/description

    -----------------------------Description-----------------------------------
    Given the head of a linked list, return the list after sorting it in
    ascending order.

    -----------------------------Constraints-----------------------------------
    :The number of nodes in the list is in the range [0, 5 * 10**4].
    :-10**5 <= Node.val <= 10**5

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: head = [4,2,1,3]
    Output: [1,2,3,4]

    Example 2:
    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]

    Example 3:
    Input: head = []
    Output: []

    ------------------------------Algorithm------------------------------------
    Traverse the linked list and store it in the array. Sort this array using
    builtin function. Restore the linked list from sorted nodes.
    """
    if not head:
        return

    array = []
    while head:
        array.append(head)
        head = head.next

    array.sort(key=lambda x: x.val, reverse=True)

    head = array.pop()
    current = head
    while array:
        new = array.pop()
        new.next = None
        current.next = new
        current = new

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


n5 = ListNode(4)
n4 = ListNode(2, n5)
n3 = ListNode(1, n4)
n2 = ListNode(9, n3)
n1 = ListNode(8, n2)
assert to_list(sort_linked_list(n1)) == [1, 2, 4, 8, 9]

n66 = ListNode(0)
n55 = ListNode(4, n66)
n44 = ListNode(-22, n55)
n33 = ListNode(3, n44)
n22 = ListNode(5, n33)
n11 = ListNode(-1, n22)
assert to_list(sort_linked_list(n11)) == [-22, -1, 0, 3, 4, 5]
assert to_list(sort_linked_list(None)) == []

print("\nAll tests passed")
