def selection_sort[T](arr: list[T]) -> None:
    """Sort array inplace"""
    if not arr:
        return arr

    for i in range(len(arr)):
        min_idx = i

        for j in range(i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        if i != min_idx:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]


class ModuloThree:
    def __init__(self, val: int) -> None:
        self.val = val

    def __gt__(self, other: "ModuloThree") -> bool:
        return self.val % 3 > other.val % 3

    def __repr__(self) -> str:
        return str(self.val)


remainder_one = ModuloThree(13)
remainder_two = ModuloThree(1)
remainder_zero = ModuloThree(3)


# print(f<b)
# print(dir(b))
# if __name__ == "__main__":


# print(selection_sort([4, 2, 1, 0]))
# srtdarr = selection_sort([7, 4, 9, 1, 0])
# print(selection_sort([remainder_one, remainder_two, remainder_zero]))
# print(srtdarr)
a = [4, 2, 1, 0]
selection_sort(a)
print(a)
