from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        next_ = True if self.next else False
        return f"{self.__class__.__name__}[val={self.val}, next={next_}]"


def remove_nth_from_end(
    head: Optional[ListNode], n: int
) -> Optional[ListNode]:
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

    last_node = current.next
    current.next = last_node.next

    return head


node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

print(remove_nth_from_end(node1, 2).next.next)
