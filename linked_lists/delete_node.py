"""
Leetcode. 237. Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/description

-----------------------------Description---------------------------------------
There is a singly-linked list head and we want to delete a node node in it.
You are given the node to be deleted node. You will not be given access to the 
first node of head. All the values of the linked list are unique, and it is 
guaranteed that the given node node is not the last node in the linked list.
Delete the given node. Note that by deleting the node, we do not mean removing 
it from memory. We mean:
    - The value of the given node should not exist in the linked list.
    - The number of nodes in the linked list should decrease by one.
    - All the values before node should be in the same order.
    - All the values after node should be in the same order.


-----------------------------Constraints---------------------------------------
: The number of the nodes in the given list is in the range [2, 1000].
: -1000 <= Node.val <= 1000
: The value of each node in the list is unique.
: The node to be deleted is in the list and is not a tail node.

------------------------------Examples-----------------------------------------
Example 1:
Input: head = [4,5,1,9], node = 5
Output: [4,1,9]
Explanation: You are given the second node with value 5, the linked list should
become 4 -> 1 -> 9 after calling your function.

Example 2:
Input: head = [4,5,1,9], node = 1
Output: [4,5,9]
Explanation: You are given the third node with value 1, the linked list should 
become 4 -> 5 -> 9 after calling your function.
"""


def delete_node(node: "ListNode") -> None:
    """
    Copy next node's value to current node, replace current node's next
    pointer by its next's next pointer. Simple and efficient.
    """
    node.val = node.next.val
    node.next = node.next.next


def delete_node2(node: "ListNode") -> None:
    """
    Traverse through nodes and stop before the last valid node.
    On each step copy next node's value to current node, replace current
    node's next pointer by its next's next pointer. After traversing handle
    the last node. Less efficient.
    """
    while node.next.next:
        node.val = node.next.val
        node = node.next
    node.val = node.next.val
    node.next = None


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        next_ = True if self.next else False
        return f"{self.__class__.__name__}[val={self.val}, next={next_}]"


n4 = ListNode(9)
n3 = ListNode(1, n4)
n2 = ListNode(5, n3)
n1 = ListNode(4, n2)

delete_node(n2)
n = n1
for i in range(3):
    assert n.val == [n1, n3, n4][i].val
    n = n.next

n4 = ListNode(9)
n3 = ListNode(1, n4)
n2 = ListNode(5, n3)
n1 = ListNode(4, n2)

delete_node2(n3)
n = n1
for i in range(3):
    assert n.val == [n1, n2, n4][i].val
    n = n.next

print("\nAll tests passed\n")
