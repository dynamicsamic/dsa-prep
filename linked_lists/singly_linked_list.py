from typing import Any, Union


class LinkedListException(Exception):
    pass


class ListNode:
    def __init__(self, value: Any, next: Union["ListNode", None] = None):
        self.value = value
        self.next = next

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ListNode):
            return self.value == other.value and self.next == other.next
        return False

    def __repr__(self) -> str:
        next_ = True if self.next else False
        return f"{self.__class__.__name__}[val={self.value}, next={next_}]"


class LinkedList:
    def __init__(self) -> None:
        self.head: ListNode = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[head={self.head}]"

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def insert(self, index: int, value: Any) -> None:
        node = ListNode(value)

        if index == 0 or not self.head:
            node.next = self.head
            self.head = node

        else:
            i = 0
            current_node = self.head
            while current_node.next and i < index - 1:
                current_node = current_node.next
                i += 1

            node.next = current_node.next
            current_node.next = node

        self._size += 1

    def add(self, value: Any) -> None:
        self.insert(self._size, value)

    def read(self, index: int) -> ListNode | None:
        i = 0
        current_node = self.head
        while current_node.next and i != index:
            current_node = current_node.next
            i += 1

        if i != index:
            raise LinkedListException(f"Index <{index}> out of range")

        return current_node

    def search(self, value: Any) -> int | None:
        i = 0
        current_node = self.head

        while current_node.next and current_node.value != value:
            current_node = current_node.next
            i += 1

        return i if current_node.value == value else None

    def delete(self, index: int) -> None:
        if self.is_empty():
            raise LinkedListException(
                "The list is empty. Insert a value first"
            )
        if index == 0:
            former_head = self.head
            self.head = former_head.next
            del former_head
        else:
            i = 0
            current_node = self.head
            while current_node.next and i < index - 1:
                current_node = current_node.next
                i += 1

            if current_node.next is None:
                raise LinkedListException(f"Index <{index}> out of range")

            current_node.next = current_node.next.next
        self._size -= 1

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next

    def is_empty(self) -> bool:
        return self.head is None

    def to_array(self) -> list[ListNode]:
        return [node for node in self]


if __name__ == "__main__":
    node = ListNode(1)
    assert node.value == 1
    assert node.next is None

    another_node = ListNode(2, node)
    assert another_node.value == 2
    assert another_node.next == node

    # test insert
    lst = LinkedList()
    assert lst.head is None

    test_values = [10, 115, 5, 9]
    for i in range(len(test_values)):
        lst.insert(i, test_values[i])
    assert len(lst) == 4
    assert lst.head.value == test_values[0]
    assert not lst.is_empty()

    # test iterable
    assert all(isinstance(node, ListNode) for node in lst)

    # test to array
    node4 = ListNode(test_values[3])
    node3 = ListNode(test_values[2], node4)
    node2 = ListNode(test_values[1], node3)
    node1 = ListNode(test_values[0], node2)
    assert lst.to_array() == [node1, node2, node3, node4]

    # test read
    assert lst.read(0) == node1
    assert lst.read(3) == node4

    # test read raises on unexisting index
    try:
        assert lst.read(5)
    except Exception as e:
        assert type(e) is LinkedListException
        assert str(e) == f"Index <{5}> out of range"
    else:
        assert False, "LinkedListException was not triggered!"

    # test read raises on negative index
    try:
        assert lst.read(-1)
    except Exception as e:
        assert type(e) is LinkedListException
        assert str(e) == "Index <-1> out of range"
    else:
        assert False, "LinkedListException was not triggered!"

    # test search
    assert lst.search(node1.value) == 0
    assert lst.search(node2.value) == 1
    assert lst.search("random_value") is None

    # test delete
    lst.delete(0)
    assert lst.head == node2
    assert len(lst) == 3
    lst.delete(1)
    lst.delete(1)
    assert len(lst) == 1
    assert lst.head.next is None
    lst.delete(0)
    assert lst.head is None
    assert len(lst) == 0
    assert lst.is_empty()

    # test delete from empty
    try:
        lst.delete(0)
    except Exception as e:
        assert type(e) is LinkedListException
        assert str(e) == "The list is empty. Insert a value first"
    else:
        assert False, "LinkedListException was not triggered!"

    # delete by non-exisent id
    lst.insert(0, 15)
    assert not lst.is_empty()
    try:
        lst.delete(3)
    except Exception as e:
        assert type(e) is LinkedListException
        assert str(e) == "Index <3> out of range"

    # test add
    lst = LinkedList()
    for i in range(5):
        lst.add(i)
    assert len(lst) == 5
    for i in range(5):
        assert lst.read(i).value == i
