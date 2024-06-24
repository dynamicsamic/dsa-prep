def sqrt(x: int) -> int:
    """Return the square root of x
    or the closest integer number to x"""
    if x == 0:
        return 0
    elif x < 4:
        return 1

    for i in range(2, x // 2 + 1):
        if i * i > x:
            return i - 1
    return i


assert sqrt(2) == 1
assert sqrt(4) == 2
assert sqrt(6) == 2
assert sqrt(25) == 5
assert sqrt(11) == 3

