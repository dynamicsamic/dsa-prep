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


def print_node(current_node) -> None:
    while current_node:
        print(current_node)
        current_node = current_node.next


def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    if not list1:
        return list2
    elif not list2:
        return list1

    new_list = ListNode()
    head = new_list

    node1 = list1
    node2 = list2

    while node1 and node2:
        if node1.val < node2.val:
            new_list.next = node1
            node1 = node1.next
        else:
            new_list.next = node2
            node2 = node2.next

        new_list = new_list.next

    if node1:
        new_list.next = node1

    if node2:
        new_list.next = node2

    return head.next


node3 = ListNode(4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)

node6 = ListNode(4)
node5 = ListNode(3, node6)
node4 = ListNode(1, node5)

h = merge_two_lists(node1, node4)
print_node(h)
# print_node(merge_two_lists(ListNode(), ListNode()))
