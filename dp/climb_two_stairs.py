def climb_two_stairs(n: int, memo: dict[int, int]) -> int:
    if n < 0:
        return 0

    if n == 1 or n == 0:
        return 1

    if n in memo:
        return memo[n]

    res = climb_two_stairs(n - 1, memo) + climb_two_stairs(n - 2, memo)
    memo[n] = res
    return res


print(climb_two_stairs(4, {}))


def climb2stairs(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    a = 1
    b = 2

    for _ in range(2, n):
        a, b = b, a + b
    
    return b

print(climb2stairs(5))

"""
1 1 1 1 
1 2 1
1 1 2
2 1 1
2 2
"""
