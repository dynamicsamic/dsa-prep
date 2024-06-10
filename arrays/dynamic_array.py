import math
import warnings
from typing import Any, Type


class DynamicArray:

    DEFAULT_CAPACITY = 20

    def __init__(self, *, capacity: int = 0) -> None:
        self.capacity = capacity or self.DEFAULT_CAPACITY
        self.size: int = 0
        self._type: Type[Any] = None
        self._data: list[Any] = [None] * self.capacity

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self._data}"

    def _check_index(self, idx: int) -> None:
        if idx < 0 or idx >= self.capacity:
            raise IndexError(
                f"Expected idx from 0 to {self.capacity - 1}, got {idx}"
            )

    def _grow(self, multiplier: int | float) -> None:
        """
        Increase the capacity of the array by a given multiplier.

        Args:
            multiplier (int | float): The factor by which to increase the capacity. If not provided, defaults to 2.

        Returns:
            None

        This function grows the capacity of the array by creating a new list
        with a size equal to the current capacity multiplied by the given multiplier.
        It then copies the elements from the old data list to the new list and updates the capacity attribute. Finally, it deletes the old data list.

        Note:
            The capacity of the array is rounded up to the nearest integer using the `math.ceil` function.

        Example:
            >>> dynamic_array = DynamicArray(capacity=10)
            >>> dynamic_array._data = [1, 2, 3, 4, 5]
            >>> dynamic_array.capacity
            10
            >>> dynamic_array._grow(2)
            >>> dynamic_array._data
            [1, 2, 3, 4, 5, None, None, None, None, None]
            >>> dynamic_array.capacity
            20
        """
        multiplier = multiplier or 2
        old_data = self._data
        new_capacity = math.ceil(self.capacity * multiplier)
        self._data = [None] * new_capacity
        for i in range(self.capacity):
            self._data[i] = old_data[i]
        self.capacity = new_capacity
        del old_data

    def _shrink(self, max_shrink_by: int | float) -> None:
        if self.capacity // self.size >= max_shrink_by:
            # Traverse form the end of the array
            # and shift right border to then cut off all spare slots.
            idx = self.capacity - 1
            while (
                self._data[idx] is None
                and self.capacity // self.size >= max_shrink_by
            ):
                idx -= 1

            self.capacity = idx + 1
            old_data = self._data
            self._data = [None] * self.capacity
            for i in range(self.capacity):
                self._data[i] = old_data[i]
            del old_data

    def insert(self, index: int, value: Any) -> None:
        self._check_index(index)
        if self.capacity - self.size < 4:
            self._grow(2)

        if self._data[index] is not None:
            idx = index
            new_val = value

            while idx < self.capacity and self._data[idx] is not None:
                shift_val = self._data[idx]
                self._data[idx] = new_val
                new_val = shift_val
                idx += 1
            if idx == self.capacity:
                # Type of situation where values being continuously inserted
                # at the end of the array despite it the array being empty at
                # the start or in the middle
                self._grow(1.3)
                warnings.warn(
                    "You are inserting at the end of the array despite having "
                    "spare slots in other parts of it."
                    "This results in growing the the array's capacity which "
                    "causes more memory allocation and more CPU power "
                    "to copy the former contents of the array."
                    "Consider inserting the value in a spare slot "
                    "at the start or in the middle of the array."
                )

            self._data[idx] = new_val
        else:
            self._data[index] = value

        self.size += 1

    def delete(self, index: int) -> None:
        self._check_index(index)
        self._data[index] = None
        self.size -= 1
        self._shrink(2)

    def index(self, index: int) -> Any:
        self._check_index(index)
        return self._data[index]

    def search(self, value: Any) -> int:
        for i in range(self.capacity):
            if self._data[i] == value:
                return i
        return -1


if __name__ == "__main__":
    # check default capacity
    array = DynamicArray()
    assert array.capacity == DynamicArray.DEFAULT_CAPACITY

    # check capacity grows when there are less than 4 spare slots left
    array = DynamicArray(capacity=4)
    initial_capacity = array.capacity
    array.insert(0, 1)
    array.insert(1, 2)
    assert array.capacity == initial_capacity * 2

    # check correct values at correct indexes
    assert array.index(0) == 1
    assert array.index(1) == 2

    # check values are being moved, not overwritten
    array.insert(0, 0)
    assert array.index(0) == 0
    assert array.index(1) == 1
    assert array.index(2) == 2

    # check new slots are being added when inserting at the end
    former_last_idx = array.capacity - 1
    array.insert(former_last_idx, 11)
    assert array.index(former_last_idx) == 11
    array.insert(former_last_idx, 10)
    assert array.index(former_last_idx) == 10
    assert array.index(former_last_idx + 1) == 11
    assert array.capacity > former_last_idx + 1

    # check search returns works correctly
    assert array.search(0) == 0
    assert array.search(1) == 1
    assert array.search(10) == former_last_idx
    assert array.search(11) == former_last_idx + 1

    # check delete gently shrinks array's capacity
    current_capacity = array.capacity
    array.delete(former_last_idx + 1)
    assert array.search(11) == -1
    assert array.capacity < current_capacity
    assert array.search(10) == former_last_idx
