def countig_sort(arr: list[int]) -> list[int] | None:
    "Does not work with negative integers."
    max_idx = max(arr)
    if max_idx > 9999:
        return None

    counter = [0] * (max_idx + 1)
    for n in arr:
        counter[n] += 1

    size = len(arr)
    result = [None] * size

    i = k = 0

    while i < size:
        if not counter[k]:
            k += 1
        else:
            while counter[k]:
                result[i] = k
                counter[k] -= 1
                i += 1

    return result


arr = [10, 7, 3, 0, 2, 1]
print(countig_sort(arr))
