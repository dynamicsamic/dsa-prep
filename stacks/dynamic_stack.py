from typing import Any


class StackException(Exception):
    pass


class DynamicStack:
    DEFAULT_CAPACITY = 20

    def __init__(self, *, capacity: int = 0) -> None:
        capacity = capacity or self.DEFAULT_CAPACITY
        self.capacity = capacity
        self.size = 0
        self._data = [None] * self.capacity

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self._data}"

    def _check_not_empty(self) -> None:
        if self.size == 0:
            raise StackException("Stack is empty. Push a value first.")

    def _pop_index(self) -> int:
        return self.size - 1

    def _resize(self, resize_rate: int) -> None:
        new_capacity = round(self.capacity * resize_rate)
        new_data = [None] * new_capacity
        for i in range(self.size):
            new_data[i] = self._data[i]
        old_data = self._data
        self._data = new_data
        self.capacity = new_capacity
        del old_data

    def push(self, value: Any) -> None:
        """
        Pushes a value onto the stack.

        Args:
            value (Any): The value to be pushed onto the stack.

        Returns:
            None

        Note:
            The `_resize` method doubles the capacity of the stack.

        """
        if self.size == self.capacity:
            self._resize(2)
        self._data[self.size] = value
        self.size += 1

    def pop(self) -> Any:
        self._check_not_empty()
        value = self._data[self._pop_index()]
        self._data[self._pop_index()] = None
        self.size -= 1
        if self.size < self.capacity // 4:
            self._resize(0.5)
        return value

    def peek(self) -> Any:
        self._check_not_empty()
        return self._data[self._pop_index()]


if __name__ == "__main__":
    # test default capacity
    stack = DynamicStack()
    assert stack.capacity == DynamicStack.DEFAULT_CAPACITY
    assert stack.size == 0

    # test push method with resize
    stack = DynamicStack(capacity=1)
    assert stack.capacity == 1
    stack.push(1)
    stack.push(2)
    assert stack.capacity == 2
    stack.push(3)
    assert stack.capacity == 4
    stack.push(4)
    stack.push(5)
    assert stack.capacity == 8

    # test peek method
    assert stack.peek() == 5

    # test pop method with resize
    stack = DynamicStack(capacity=20)
    assert stack.capacity == 20
    stack.push(1)
    stack.push(2)
    assert stack.pop() == 2
    assert stack.size == 1
    assert stack.capacity == 10

    # test pop exception
    stack = DynamicStack()
    try:
        stack.pop()
    except Exception as e:
        assert type(e) is StackException
        assert str(e) == "Stack is empty. Push a value first."
    else:
        assert False

    # test peek exception
    try:
        stack.peek()
    except StackException as e:
        assert str(e) == "Stack is empty. Push a value first."
    else:
        assert False

    stack = DynamicStack()
    for i in range(DynamicStack.DEFAULT_CAPACITY):
        assert stack.size == i
        stack.push(i)
    assert stack.size == stack.capacity

    for _ in range(DynamicStack.DEFAULT_CAPACITY):
        assert stack._pop_index() == stack.pop()
    assert stack.size == 0

    print("All tests passed!")
