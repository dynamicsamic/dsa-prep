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

from typing import Optional


def remove_nodes_stack(head: Optional["ListNode"]) -> "ListNode":
    """
    ------------------------------Algorithm------------------------------------
    We can restate this problem as following: find the maximum lists node, if
    there are nodes after it find max node out of the rest of the list, and
    so on. We define a stack, that will hold both true max nodes as well as
    temporary maximums. We traverse through the list, check if the last item
    in stack is less than the current node. If it is, we pop out all the values
    that are lower than current node and add current node to the stack. This is
    how we ensure that we chose the greatest node. Nodes will keep poping out
    of the stack each time we find a greater node, until we find the highest
    one. After we found the maximum we keep adding other nodes, until we find
    the next maximum. We will repeat this process until the end of the list.
    After the iteration is over, we collected all valid nodes but in the
    reverse order - the first value on the stack is the least one. We need to
    assemble the list in a descending order. Here we will employ the practice
    from reversing the list: pop a node from the stack, point its next pointer
    to previous and make this node previous.
    """
    stack = []

    current = head

    while current:
        while stack and stack[-1].val < current.val:
            stack.pop()
        stack.append(current)
        current = current.next

    prev = None
    while stack:
        current = stack.pop()
        current.next = prev
        prev = current

    return prev


def remove_nodes_reverse(head: Optional["ListNode"]) -> "ListNode":
    """
    ------------------------------Algorithm------------------------------------
    Here we reverse the list and go from its tail to the head. Here our
    strategy would be such: we define a current maximum value which at first
    would be our last node's value; we start traversing the list backwards and
    skip every node that is less than our current max value. If we found a node
    that is greater than the current max, we update current max set this node
    as our current node. Doing so we connect to each other only local maximums.
    After the iteration is over we have a list connected in ascending order
    with the head pointing to the lowest node. We reverse this list once again.
    """

    def _reverse_linked_list(head: ListNode) -> ListNode:
        prev = None
        current = head

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

    new_list = _reverse_linked_list(head)
    current = new_list
    max_val = current.val

    while current.next:
        if current.next.val < max_val:
            current.next = current.next.next
        else:
            max_val = current.next.val
            current = current.next

    return _reverse_linked_list(new_list)


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode" = None):
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


node5 = ListNode(8)
node4 = ListNode(3, node5)
node3 = ListNode(13, node4)
node2 = ListNode(2, node3)
node1 = ListNode(5, node2)
assert to_list(remove_nodes_reverse(node1)) == [13, 8]

node5 = ListNode(1)
node4 = ListNode(1, node5)
node3 = ListNode(1, node4)
node2 = ListNode(1, node3)
node1 = ListNode(1, node2)
assert to_list(remove_nodes_reverse(node1)) == [1, 1, 1, 1, 1]


node5 = ListNode(8)
node4 = ListNode(3, node5)
node3 = ListNode(13, node4)
node2 = ListNode(2, node3)
node1 = ListNode(5, node2)
assert to_list(remove_nodes_stack(node1)) == [13, 8]

node5 = ListNode(1)
node4 = ListNode(1, node5)
node3 = ListNode(1, node4)
node2 = ListNode(1, node3)
node1 = ListNode(1, node2)
assert to_list(remove_nodes_stack(node1)) == [1, 1, 1, 1, 1]

print("\nAll tests passed")
