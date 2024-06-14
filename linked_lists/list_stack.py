from typing import Any

from doubly_linked_list import DoublyLinkedList


class StackException(Exception):
    pass


class ListStack:
    def __init__(self) -> None:
        self._stack = DoublyLinkedList()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self._stack}"

    def __len__(self) -> int:
        return len(self._stack)

    def __contains__(self, value) -> bool:
        return self._stack.search(value) is not None

    def __iter__(self) -> DoublyLinkedList:
        return iter(self._stack)

    def _check_not_empty(self) -> None:
        if len(self._stack) == 0:
            raise StackException(
                "Pop/peek from empty stack. Push a value first."
            )

    def push(self, value: Any) -> None:
        self._stack.insert_front(value)

    def pop(self) -> Any:
        self._check_not_empty()
        value = self._stack.head.value
        self._stack.delete_front()
        return value

    def peek(self) -> Any:
        self._check_not_empty()
        return self._stack.head.value


if __name__ == "__main__":
    stack = ListStack()
    assert len(stack) == 0

    # test push method
    stack = ListStack()
    stack.push(1)
    assert len(stack) == 1
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    assert len(stack) == 5

    # test peek method
    assert stack.peek() == 5

    # test pop method
    assert stack.pop() == 5
    assert len(stack) == 4

    # test pop exception
    stack = ListStack()
    try:
        stack.pop()
    except Exception as e:
        assert type(e) is StackException
        assert str(e) == "Pop/peek from empty stack. Push a value first."
    else:
        assert False, "StackException has not been triggered!"

    # test exception
    try:
        stack.peek()
    except StackException as e:
        assert str(e) == "Pop/peek from empty stack. Push a value first."
    else:
        assert False, "StackException has not been triggered!"

    stack = ListStack()
    for i in range(10):
        assert len(stack) == i
        stack.push(i)
    assert len(stack) == 10
    stack_vals = [node.value for node in stack._stack.to_array()]
    assert stack_vals == list(range(9, -1, -1))

    for _ in range(10):
        stack.pop()
    assert len(stack) == 0

    print("All tests passed!")
