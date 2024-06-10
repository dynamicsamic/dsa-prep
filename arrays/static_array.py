from typing import Any, Type


class StaticArray:
    """A basic representation of a static array in Python.
    - Allows to store values only of one type.
    Type of array determined when first value gets inserted.
    - Allows to override existing values when inserting.
    - Does not support negative indexing.

    """

    DEFAULT_CAPACITY = 20

    def __init__(self, *, capacity: int = 0) -> None:
        self.capacity = capacity or self.DEFAULT_CAPACITY
        self.size: int = 0
        self._type: Type[Any] = None
        self._data: list[Any] = [None] * self.capacity

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self._data}"

    def _check_index(self, index: int) -> None:
        if index < 0 or index >= self.capacity:
            raise IndexError(
                f"Expected index from 0 to {self.capacity - 1}, got {index}"
            )

    def insert(self, index: int, value: Any) -> None:
        self._check_index(index)

        val_type = type(value)
        if self._type is None:
            self._type = val_type
        else:
            if val_type is not self._type:
                raise TypeError(
                    f"Value type {val_type} incompatible "
                    f"with array type {self._type}"
                )

        self._data[index] = value
        self.size += 1

    def delete(self, index: int) -> None:
        self._check_index(index)
        self._data[index] = None
        self.size -= 1

    def index(self, index: int) -> Any:
        self._check_index(index)
        return self._data[index]

    def search(self, value: Any) -> int:
        for i in range(self.capacity):
            if self._data[i] == value:
                return i
        return -1


if __name__ == "__main__":
    array = StaticArray()
    assert array.capacity == StaticArray.DEFAULT_CAPACITY
    assert array.size == 0
    array.insert(0, "hello")
    assert array.index(0) == "hello"
    assert array.size == 1
    assert array._type == str

    array.insert(10, "world")
    assert array.size == 2
    assert array.search("world") == 10
    assert array.search("non-existent") == -1

    array.delete(10)
    assert array.size == 1
    assert array.index(10) is None

    try:
        array.insert(2000, "invalid")
    except Exception as e:
        assert type(e) is IndexError

    try:
        array.insert(1, 2000)
    except Exception as e:
        assert type(e) is TypeError

    array2 = StaticArray(capacity=20)
    assert array2.capacity == 20
