from typing import Any


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ListNode):
            return self.val == other.val and self.next == other.next
        return False

    def __repr__(self) -> str:
        next_ = True if self.next else False
        return f"{self.__class__.__name__}[val={self.val}, next={next_}]"


def get_intersection_node(headA: ListNode, headB: ListNode) -> ListNode | None:
    asize, bsize = 0, 0
    atemp, btemp = headA, headB

    while atemp.next:
        asize += 1
        atemp = atemp.next

    while btemp.next:
        bsize += 1
        btemp = btemp.next

    if atemp.val != btemp.val:
        return

    asize += 1
    bsize += 1

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


node5 = ListNode(4)
node4 = ListNode(2, node5)
node3 = ListNode(1, node4)
node2 = ListNode(9, node3)
node1 = ListNode(1, node2)

node6 = ListNode(3, node4)

node6 = ListNode(5)
node5 = ListNode(4, node6)
node4 = ListNode(8, node5)
node3 = ListNode(1, node4)
node2 = ListNode(6, node3)
node1 = ListNode(5, node2)

node8 = ListNode(1, node4)
node7 = ListNode(5, node8)


print(get_intersection_node(node1, node7))
# node6 = ListNode(15, node2)
# print(id(node1.next) == id(node6.next))
# node7 = ListNode(1, node2)
