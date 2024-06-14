from typing import Any

from doubly_linked_list import DoublyLinkedList


class ListQueueException(Exception):
    pass


class ListQueue:
    def __init__(self) -> None:
        self._queue = DoublyLinkedList()

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self._queue}"

    def __len__(self) -> int:
        return len(self._queue)

    def __contains__(self, value) -> bool:
        return self._queue.search(value) is not None

    def __iter__(self)-> DoublyLinkedList:
        return iter(self._queue)

    def _check_not_empty(self) -> None:
        if len(self._queue) == 0:
            raise ListQueueException(
                "Dequeue/peek from empty queue. Enqueue a value first."
            )

    def enqueue(self, value: Any) -> None:
        self._queue.insert_end(value)

    def dequeue(self) -> Any:
        self._check_not_empty()
        val = self._queue.head.value
        self._queue.delete_front()
        return val

    def peek(self) -> Any:
        self._check_not_empty()
        return self._queue.head.value


if __name__ == "__main__":
    queue = ListQueue()
    assert len(queue) == 0

    for i in range(10):
        queue.enqueue(i)
        assert len(queue) == i + 1
        assert queue.peek() == 0

    queue_vals = [node.value for node in queue._queue.to_array()]
    assert queue_vals == list(range(10))

    for i in range(10):
        assert queue.dequeue() == i
        assert len(queue) == 10 - i - 1
    queue_vals = [node.value for node in queue._queue.to_array()]
    assert queue_vals == []

    # test dequeue exception
    queue = ListQueue()
    try:
        queue.dequeue()
    except Exception as e:
        assert type(e) is ListQueueException
        assert (
            str(e) == "Dequeue/peek from empty queue. Enqueue a value first."
        )
    else:
        assert False, "ListQueueException has not been triggered"

    # test peek exception
    queue = ListQueue()
    try:
        queue.peek()
    except Exception as e:
        assert type(e) is ListQueueException
        assert (
            str(e) == "Dequeue/peek from empty queue. Enqueue a value first."
        )
    else:
        assert False, "ListQueueException has not been triggered"

    print("All tests passed!")
