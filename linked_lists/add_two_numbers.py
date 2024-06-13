class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        next_ = True if self.next else False
        return f"{self.__class__.__name__}[val={self.val}, next={next_}]"


def add_two_numbers(l1: ListNode | None):
    if not l1:
        return ""

    return str(l1.val) + add_two_numbers(l1.next)


def add_two_numbers2(l1: ListNode | None, l2: ListNode | None) -> int:
    if not l1:
        return l2
    elif not l2:
        return l1

    c1 = []
    c2 = []

    node1 = l1
    node2 = l2

    while node1:
        c1.append(str(node1.val))
        node1 = node1.next

    while node2:
        c2.append(str(node2.val))
        node2 = node2.next

    c1.reverse()
    c2.reverse()
    num1 = int("".join(c1))
    num2 = int("".join(c2))
    num = str(num1 + num2)

    new_list = ListNode()
    head = new_list

    for i in range(len(num) - 1, -1, -1):
        # print(head)
        head.val = int(num[i])
        if i == 0:
            break
        head.next = ListNode()
        head = head.next

    return new_list


node3 = ListNode(3)
node2 = ListNode(4, node3)
node1 = ListNode(2, node2)


node6 = ListNode(4)
node5 = ListNode(6, node6)
node4 = ListNode(5, node5)


print(add_two_numbers2(node1, node4).next.next.next)
