def find_winner(n: int, k: int) -> int:
    nums = list(range(1, n + 1))
    size = n
    i = 0
    count = 0

    while size > 1:
        if count == k:
            nums[(i - 1) % n] = None
            size -= 1
            count = 0

        if nums[i % n]:
            count += 1

        i += 1

    return [i for i in nums if i][0]


[1, 2, 3, 4, 5]
print(find_winner(6, 5))
