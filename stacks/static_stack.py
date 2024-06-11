from typing import Any


class StackException(Exception):
    pass


class StaticStack:
    DEFAULT_CAPACITY = 20

    def __init__(self, *, capacity: int = 0) -> None:
        capacity = capacity or self.DEFAULT_CAPACITY
        self.capacity = capacity
        self.size = 0
        self._data = [None] * self.capacity

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self._data}"

    def _pop_index(self) -> int:
        return self.size - 1

    def push(self, value: Any) -> None:
        """
        Add a value to the top of the stack.

        Args:
            value: The value to be added to the stack.

        Raises:
            StackException: If the stack is full.

        Returns:
            None
        """
        if self.size == self.capacity:
            raise StackException("Stack is full. Pop a value first.")
        self._data[self.size] = value
        self.size += 1

    def pop(self) -> Any:
        """
        Removes and returns the top element from the stack.

        Raises:
            StackException: If the stack is empty.

        Returns:
            Any: The top element of the stack.
        """
        if self.size == 0:
            raise StackException("Stack is empty. Push a value first.")
        value = self._data[self._pop_index()]
        self._data[self._pop_index()] = None
        self.size -= 1
        return value

    def peek(self) -> Any:
        """
        Returns the top element of the stack without removing it.

        Raises:
            StackException: If the stack is empty.

        Returns:
            Any: The top element of the stack.
        """
        if self.size == 0:
            raise StackException("Stack is empty. Push a value first.")
        return self._data[self._pop_index()]


if __name__ == "__main__":
    # test default capacity
    stack = StaticStack()
    assert stack.capacity == StaticStack.DEFAULT_CAPACITY
    assert stack.size == 0

    # test push method
    stack = StaticStack(capacity=5)
    stack.push(1)
    assert stack.size == 1
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    assert stack.size == 5

    # test peek method
    assert stack.peek() == 5

    # test pop method
    assert stack.pop() == 5
    assert stack.size == 4

    # test push exception
    stack = StaticStack(capacity=1)
    stack.push(1)
    try:
        stack.push(2)
    except Exception as e:
        assert type(e) is StackException
        assert str(e) == "Stack is full. Pop a value first."

    # test pop exception
    stack = StaticStack()
    try:
        stack.pop()
    except Exception as e:
        assert type(e) is StackException
        assert str(e) == "Stack is empty. Push a value first."

    # test exception
    try:
        stack.peek()
    except StackException as e:
        assert str(e) == "Stack is empty. Push a value first."

    stack = StaticStack()
    for i in range(StaticStack.DEFAULT_CAPACITY):
        assert stack.size == i
        stack.push(i)
    assert stack.size == stack.capacity

    for _ in range(StaticStack.DEFAULT_CAPACITY):
        assert stack._pop_index() == stack.pop()
    assert stack.size == 0
