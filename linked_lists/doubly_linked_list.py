from typing import Any, Union


class LinkedListException(Exception):
    pass


class ListNode:
    def __init__(
        self,
        value: Any,
        prev: Union["ListNode", None] = None,
        next: Union["ListNode", None] = None,
    ):
        self.value = value
        self.prev = prev
        self.next = next

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, ListNode):
            return (
                self.value == other.value
                and self.prev == other.prev
                and self.next == other.next
            )
        return False

    def __repr__(self) -> str:
        prev_ = True if self.prev else False
        next_ = True if self.next else False
        return (
            f"{self.__class__.__name__}[val={self.value}, "
            f"prev={prev_} next={next_}]"
        )


class DoublyLinkedList:
    def __init__(self) -> None:
        self.head: ListNode = None
        self.last: ListNode = None
        self._size: int = 0

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[head={self.head}, last={self.last}]"

    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

    def insert(self, index: int, value: Any) -> None:
        index = self._check_index(index)

        if not self.head or index == 0:
            self.insert_front(value)
        elif not self.last or index == self._size - 1:
            self.insert_end(value)
        else:
            self._insert_at_index(index, value)

    def insert_front(self, value: Any) -> None:
        node = ListNode(value)

        if not self.head:
            self.head = node
            self.last = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self._size += 1

    def insert_end(self, value: Any) -> None:
        node = ListNode(value)

        if not self.head:
            self.head = node
            self.last = node
        else:
            node.prev = self.last
            self.last.next = node
            self.last = node

        self._size += 1

    def _insert_at_index(self, index: int, value: Any) -> None:
        node = ListNode(value)

        i = 0
        current_node = self.head

        while current_node.next and i < index - 1:
            current_node = current_node.next
            i += 1

        node.prev = current_node
        node.next = current_node.next
        # if next node is None, it does not have `next` or `prev`
        if current_node.next:
            current_node.next.prev = node
        else:
            self.last = node
        current_node.next = node

        self._size += 1

    # def insert_front(self, index: int, value: Any) -> None:
    #     node = ListNode(value)

    #     if not self.head:
    #         self.head = node
    #         self.last = node

    #     elif index == 0:
    #         node.next = self.head
    #         self.head.prev = node
    #         self.head = node

    #     else:
    #         i = 0
    #         current_node = self.head
    #         while current_node.next and i < index - 1:
    #             current_node = current_node.next
    #             i += 1

    #         node.prev = current_node
    #         node.next = current_node.next
    #         current_node.next = node

    #         if node.next is None:
    #             self.last = node

    #     self._size += 1

    def read(self, index: int) -> ListNode | None:
        index = self._check_index(index)
        return (
            self._read_front(index)
            if index <= self._size // 2
            else self._read_end(index)
        )

    def _read_front(self, index: int) -> ListNode | None:
        i = 0
        current_node = self.head
        while current_node.next and i != index:
            current_node = current_node.next
            i += 1
        return current_node

    def _read_end(self, index: int) -> ListNode | None:
        i = self._size
        current_node = self.last
        while current_node.prev and i != index:
            current_node = current_node.prev
            i -= 1
        return current_node

    def search(self, value: Any) -> int | None:
        i = 0
        current_node = self.head

        while current_node.next and current_node.value != value:
            current_node = current_node.next
            i += 1

        return i if current_node.value == value else None

    def delete(self, index: int) -> None:
        index = self._check_index(index)
        
        if index == 0:
            self.delete_front()
        elif index == self._size - 1:
            self.delete_end()
        else:
            self._delete_at_index(index)

    def delete_front(self) -> None:
        former_head = self.head

        if not former_head.prev and not former_head.next:
            # handle the last element deletion
            self.head = None
            self.last = None
        else:
            new_head = self.head.next
            new_head.prev = None
            self.head = new_head

        self._size -= 1
        del former_head

    def delete_end(self) -> None:
        former_last = self.last

        if not former_last.prev and not former_last.next:
            # handle the last element deletion
            self.head = None
            self.last = None
        else:
            new_last = self.last.prev
            new_last.next = None
            self.last = new_last

        self._size -= 1
        del former_last

    def _delete_at_index(self, index: int) -> None:
        i = 0
        current_node = self.head
        while current_node.next and i < index - 1:
            current_node = current_node.next
            i += 1
        former_node = current_node.next
        current_node.next = former_node.next
        former_node.next.prev = current_node

        self._size -= 1
        del former_node

    def print(self) -> None:
        current_node = self.head
        while current_node:
            print(current_node)
            current_node = current_node.next

    def is_empty(self) -> bool:
        return self.head is None

    def to_array(self) -> list[ListNode]:
        return [node for node in self]

    def _check_index(self, index: int) -> int:
        if index < 0:
            index = self._size + index
        if index >= self._size:
            raise LinkedListException(f"Index <{index}> out of range")
        return index


"""
if __name__ == "__main__":
    node = ListNode(1)
    assert node.value == 1
    assert node.next is None

    another_node = ListNode(2, node)
    assert another_node.value == 2
    assert another_node.next == node

    # test insert
    lst = DoublyLinkedList()
    assert lst.head is None

    test_values = [10, 115, 5, 9]
    for i in range(len(test_values)):
        lst.insert_front(i, test_values[i])
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
    lst.insert_front(0, 15)
    assert not lst.is_empty()
    try:
        lst.delete(3)
    except Exception as e:
        assert type(e) is LinkedListException
        assert str(e) == "Index <3> out of range"

    # test add
    lst = DoublyLinkedList()
    for i in range(5):
        lst.add(i)
    assert len(lst) == 5
    for i in range(5):
        assert lst.read(i).value == i
"""
