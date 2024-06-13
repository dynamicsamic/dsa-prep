class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        next_ = True if self.next else False
        return f"{self.__class__.__name__}[val={self.val}, next={next_}]"


def reverse_linked_list(head: ListNode | None) -> ListNode:
    if not head:
        return

    stack = []
    node = head

    while node:
        stack.append(node)
        node = node.next

    new_head = stack.pop()
    new_list = new_head
    while stack:
        new_list.next = stack.pop()
        new_list = new_list.next

    new_list.next = None  # invalidate the former head pointer
    return new_head


def reverse_linked_list2(head: ListNode | None) -> ListNode:
    current = head
    prev = None

    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp

    return prev


node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
# reverse_linked_list(node1)
assert reverse_linked_list2(node1).val == node3.val
