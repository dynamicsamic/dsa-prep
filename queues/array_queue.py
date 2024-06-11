from typing import Any


class QueueException(Exception):
    pass


class StaticQueue:
    DEFAULT_CAPACITY = 20

    def __init__(self, *, capacity: int = 0) -> None:
        capacity = capacity or self.DEFAULT_CAPACITY
        self.capacity = capacity
        self.size: int = 0
        self._data: list[Any] = [None] * self.capacity

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self._data}"

    def __len__(self) -> int:
        return self.size

    def __eq__(self, other) -> bool:
        if not isinstance(other, StaticQueue):
            return NotImplemented

        return self._data == other._data

    def __contains__(self, value) -> bool:
        return value in self._data

    def _check_not_empty(self) -> None:
        if self.size == 0:
            raise QueueException(
                "Dequeue/peek from empty queue. Enqueue a value first."
            )

    def enqueue(self, value: Any) -> None:
        if self.size == self.capacity:
            raise QueueException(
                f"Cannot add value <{value}> to the queue. "
                "Queue is full. Pop a value first."
            )
        self._data[self.size] = value
        self.size += 1

    def dequeue(self) -> Any:
        self._check_not_empty()
        value = self._data[0]
        for i in range(self.size - 1):
            self._data[i] = self._data[i + 1]
        self._data[self.size - 1] = None
        self.size -= 1
        return value

    def peek(self) -> Any:
        self._check_not_empty()
        return self._data[0]


if __name__ == "__main__":
    queue = StaticQueue()
    assert queue.capacity == StaticQueue.DEFAULT_CAPACITY

    for i in range(StaticQueue.DEFAULT_CAPACITY):
        queue.enqueue(i)
        assert queue.size == i + 1
        assert queue.peek() == 0
    assert queue._data == list(range(StaticQueue.DEFAULT_CAPACITY))

    for i in range(StaticQueue.DEFAULT_CAPACITY):
        assert queue.dequeue() == i
        assert queue.size == StaticQueue.DEFAULT_CAPACITY - i - 1
    assert queue._data == [None] * StaticQueue.DEFAULT_CAPACITY

    # test enqueue exception
    queue = StaticQueue(capacity=1)
    queue.enqueue(1)
    try:
        queue.enqueue(2)
    except Exception as e:
        assert type(e) is QueueException
        assert str(e) == (
            "Cannot add value <2> to the queue. Queue is full. "
            "Pop a value first."
        )
    else:
        assert False

    # test dequeue exception
    queue = StaticQueue(capacity=1)
    try:
        queue.dequeue()
    except Exception as e:
        assert type(e) is QueueException
        assert (
            str(e) == "Dequeue/peek from empty queue. Enqueue a value first."
        )
    else:
        assert False

    # test peek exception
    queue = StaticQueue(capacity=1)
    try:
        queue.peek()
    except Exception as e:
        assert type(e) is QueueException
        assert (
            str(e) == "Dequeue/peek from empty queue. Enqueue a value first."
        )
    else:
        assert False

    print("All tests passed!")
