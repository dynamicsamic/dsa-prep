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


def rotate_right(head: ListNode | None, k: int) -> ListNode | None:
    from collections import deque

    if not head or not k:
        return head

    size = 0

    queue = deque()
    new_list = ListNode()
    new_head = new_list

    node = head
    while node:
        queue.append(node)
        size += 1
        node = node.next

    for _ in range(k % size):
        queue.appendleft(queue.pop())

    for el in queue:
        el.next = None
        new_head.next = el
        new_head = new_head.next

    return new_list.next


def rotate_right2(head: ListNode | None, k: int) -> ListNode | None:
    if not head or not head.next:
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


node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
n = rotate_right2(node1, 2)
# print(n)
# for _ in range(5):
#     print(getattr(n, "next"))
#     n=n.next

n3 = ListNode(2)
n2 = ListNode(1, n3)
n1 = ListNode(0, n2)

nn = rotate_right2(n1, 4)
print(nn)
for _ in range(3):
    print(getattr(nn, "next"))
    nn = nn.next
