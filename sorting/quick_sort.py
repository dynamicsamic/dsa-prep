def partition[T](arr: list[T], left: int, right: int) -> int:
    pivot_idx = right
    pivot_val = arr[pivot_idx]
    right -= 1

    while True:
        while arr[left] < pivot_val:
            left += 1

        while arr[right] > pivot_val:
            right -= 1

        if left >= right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1

    arr[left], arr[pivot_idx] = arr[pivot_idx], arr[left]
    return left


def quicksort[T](arr: list[T]) -> None:
    def _quicksort[T](arr: list[T], left: int, right: int) -> None:
        if left >= right:
            return

        pivot_idx = partition(arr, left, right)
        _quicksort(arr, left, pivot_idx - 1)
        _quicksort(arr, pivot_idx + 1, right)

    return _quicksort(arr, 0, len(arr) - 1)


a = [4, 3, 2, 1]
quicksort(a)
print(a)
