class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        next_ = True if self.next else False
        return f"{self.__class__.__name__}[val={self.val}, next={next_}]"


def sort_linked_list(head: ListNode) -> ListNode:
    if not head:
        return

    arr = []
    while head:
        arr.append(head)
        head = head.next

    arr.sort(key=lambda x: x.val, reverse=True)

    head = arr.pop()
    current = head
    while arr:
        new = arr.pop()
        new.next = None
        current.next = new
        current = new

    return head


node5 = ListNode(4)
node4 = ListNode(2, node5)
node3 = ListNode(1, node4)
node2 = ListNode(9, node3)
node1 = ListNode(8, node2)
m = sort_linked_list(node1)
for i in range(5):
    print(m)
    m = m.next
