def insertion_sort[T](arr: list[T]) -> list[T]:
    if not arr:
        return arr

    for i in range(1, len(arr)):
        temp = arr[i]
        j = i
        while j > 0 and arr[j - 1] > temp:
            arr[j] = arr[j - 1]
            j -= 1

        if i != j:
            arr[j] = temp

    return arr


ar = [1,-2]
srtdar = insertion_sort(sorted(ar, reverse=True))
print(srtdar)
