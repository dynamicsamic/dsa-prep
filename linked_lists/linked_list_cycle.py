"""
Leetcode. 141. Linked List Cycle
https://leetcode.com/problems/linke-list-cycle/description

-----------------------------Description---------------------------------------
Given head, the head of a linked list, determine if the linked list has a cycle
in it. There is a cycle in a linked list if there is some node in the list that
can be reached again by continuously following the next pointer. Internally, 
pos is used to denote the index of the node that tail's next pointer is 
connected to. Note that pos is not passed as a parameter. Return true if there
is a cycle in the linked list. Otherwise, return false.

-----------------------------Constraints---------------------------------------
: The number of the nodes in the list is in the range [0, 10**4].
: -10**5 <= Node.val <= 10**5
: pos is -1 or a valid index in the linked-list.

------------------------------Examples-----------------------------------------
Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to 
the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to 
the 0th nod

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
"""


def has_cycle_set(head: "ListNode") -> bool:
    """
    ------------------------------Algorithm------------------------------------
    Define a set. Traverse the tree and for every node check if its value is
    already in set. If not, add it. If yes, we found a cycle, return true.
    """
    seen = set()

    node = head
    while node:
        if node.val in seen:
            return True
        seen.add(node.val)
        node = node.next
    return False


def has_cycle_fast_slow(head: "ListNode") -> bool:
    """
    ------------------------------Algorithm------------------------------------
    This one is based on Floyd's Cycle detection (so they say on the internet).
    The idea is, if we set two pointers, which traverse the list with defferent
    speed, we will eventually detect a cycle if it exists, or end the loop.
    We set two pointers and traverse the list while the fast pointer exists.
    On each step we increment slow pointer and double increment the fast one.
    We then check values of nodes which these pointers point to.
    """
    slow = head
    fast = head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast.val == slow.val:
            return True

    return False


class ListNode:
    def __init__(self, x, next: "ListNode" = None):
        self.val = x
        self.next = next

    def __repr__(self) -> str:
        next_ = True if self.next else False
        return f"{self.__class__.__name__}[val={self.val}, next={next_}]"


n4 = ListNode(4)
n3 = ListNode(0, n4)
n2 = ListNode(2, n3)
n1 = ListNode(3, n2)
n4.next = n2
assert has_cycle_set(n1)
assert has_cycle_fast_slow(n1)

n2 = ListNode(2)
n1 = ListNode(1, n2)
n2.next = n1
assert has_cycle_set
assert has_cycle_fast_slow(n1)

assert not has_cycle_set(ListNode(1))
assert not has_cycle_fast_slow(ListNode(1))

print("\nAll tests passed")
