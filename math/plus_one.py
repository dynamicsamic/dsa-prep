def plus_one(digits: list[int]) -> list[int]:
    i = len(digits) - 1
    carry, r = divmod(digits[i] + 1, 10)
    digits[i] = r

    while i > 0 and carry:
        i -= 1
        carry, r = divmod(digits[i] + carry, 10)
        digits[i] = r

    if carry:
        return [1] + digits

    return digits


assert plus_one([9, 9, 9]) == [1, 0, 0, 0]
assert plus_one([9, 8]) == [9, 9]
assert plus_one([3, 4]) == [3, 5]


def plus_one2(digits: list[int]) -> list[int]:
    num = int("".join((str(d) for d in digits)))
    return [int(d) for d in str(num + 1)]


assert plus_one2([9, 9, 9]) == [1, 0, 0, 0]
assert plus_one2([9, 8]) == [9, 9]
assert plus_one2([3, 4]) == [3, 5]
