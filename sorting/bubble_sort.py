def bubble_sort[T](arr: list[T]) -> None:
    """Sort array inplace."""
    if not arr:
        return arr
    
    for i in range(len(arr) - 1):
        was_swapped = False
        for j in range(len(arr) - 1):
            if i != j and arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                was_swapped = True

        if not was_swapped:
            break


print(bubble_sort([6, 5, 4, 2, 7]))
# print(bubble_sort([1, 6, 4, 6, 7]))
