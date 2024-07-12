from typing import Optional


def get_intersection_node(
    headA: "ListNode", headB: "ListNode"
) -> Optional["ListNode"]:
    """
    Leetcode. 160. Intersection of Two Linked Lists
    https://leetcode.com/problems/intersection-of-two-linked-lists/description

    -----------------------------Description-----------------------------------
    Given the heads of two singly linked-lists headA and headB, return the node
    at which the two lists intersect. If the two linked lists have no
    intersection at all, return null. The linked lists must retain their
    original structure after the function returns.

    -----------------------------Constraints-----------------------------------
    : The number of nodes of listA is in the m.
    : The number of nodes of listB is in the n.
    : 1 <= m, n <= 3 * 10**4
    : 1 <= Node.val <= 10**5
    : 0 <= skipA < m
    : 0 <= skipB < n
    : intersectVal is 0 if listA and listB do not intersect.
    : intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5],
    skipA = 2, skipB = 3
    Output: Intersected at '8'

    Example 2:
    Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3,
    skipB = 1
    Output: Intersected at '2'

    Example 3:
    Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3,
    skipB = 2
    Output: No intersection

    ------------------------------Algorithm------------------------------------
    The problem maybe stated as: we have two lists of potentially different
    sizes and one of the lists' nodes may be pointing to a node from the other
    list forming an intersection. From that intersection node the two lists in
    fact become one. The challenge here is that to get to the intersection node
    we need to traverse both lists of different sizes. The good is that this
    lists sorted in ascending order and we can compare values to determine
    which list we need to traverse next. We start with counting size of both
    lists. As a side effect of being in the last node we can compare last nodes
    values and return early, if this values does not match. Next we traverse
    both lists again until we find a node which value is equal in for both
    lists. By this point the remaining length of lists should equal. We
    traverse lists simultaneously in search for intersection node.
    """
    asize, bsize = 1, 1
    atemp, btemp = headA, headB

    while atemp.next:
        asize += 1
        atemp = atemp.next

    while btemp.next:
        bsize += 1
        btemp = btemp.next

    if atemp.val != btemp.val:
        return

    ahead, bhead = headA, headB

    while asize > bsize:
        ahead = ahead.next
        asize -= 1

    while bsize > asize:
        bhead = bhead.next
        bsize -= 1

    while ahead and bhead:
        if ahead is bhead:
            return ahead
        ahead = ahead.next
        bhead = bhead.next


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        next_ = True if self.next else False
        return f"{self.__class__.__name__}[val={self.val}, next={next_}]"


n5 = ListNode(4)
n4 = ListNode(2, n5)
n3 = ListNode(1, n4)
n2 = ListNode(9, n3)
n1 = ListNode(1, n2)

n6 = ListNode(3, n4)
assert get_intersection_node(n1, n6) is n4


n66 = ListNode(5)
n55 = ListNode(4, n66)
n44 = ListNode(8, n55)
n33 = ListNode(1, n44)
n22 = ListNode(6, n33)
n11 = ListNode(5, n22)

n88 = ListNode(1, n44)
n77 = ListNode(5, n88)
assert get_intersection_node(n11, n77) is n44

print("\nAll tests passed")
