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


def remove_nodes(head: ListNode | None) -> ListNode | None:
    new_list = ListNode()
    new_head = new_list
    current = head
    was_removed = False

    while current.next:
        if current.next.val > current.val:
            new_list.next = current.next
            new_list = new_list.next
            was_removed = True
        current = current.next

    if was_removed:
        return new_head.next

    return head


def reverse_linked_list(head: ListNode) -> ListNode:
    prev = None
    current = head

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev


def remove_nodes2(head: ListNode | None) -> ListNode | None:
    new_list = reverse_linked_list(head)
    current = new_list
    max_val = current.val

    while current.next:
        if current.next.val < max_val:
            current.next = current.next.next
        else:
            max_val = current.next.val
            current = current.next
    
    return reverse_linked_list(new_list)


# node6 = ListNode(5)
node5 = ListNode(8)
node4 = ListNode(3, node5)
node3 = ListNode(13, node4)
node2 = ListNode(2, node3)
node1 = ListNode(5, node2)

# node5 = ListNode(1)
# node4 = ListNode(1, node5)
# node3 = ListNode(1, node4)
# node2 = ListNode(1, node3)
# node1 = ListNode(1, node2)


h = remove_nodes2(node1)
print(h)
print(h.next)
# for _ in range(1):
    # print(h.next)
    # h = h.next
