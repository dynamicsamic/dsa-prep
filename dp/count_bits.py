def count_bits(n: int) -> list[int]:
    return [bin(i).count("1") for i in range(n + 1)]


def count_bits_bitwise(n: int) -> list[int]:
    count = [0] * (n + 1)

    for i in range(1, n + 1):
        count[i] = count[i // 2] + (i % 2)
    return count


print(count_bits_bitwise(6))
