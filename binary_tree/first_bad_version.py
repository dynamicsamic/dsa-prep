def is_bad_version(version_num: int) -> bool:
    # leetcode api simulation
    print("is_bad_version called")
    return version_num >= 4


def first_bad_version(n: int) -> bool:
    left = 1
    right = n

    while left <= right:
        m = (left + right) // 2
        if is_bad_version(m) and not is_bad_version(m - 1):
            return m
        elif not is_bad_version(m):
            left = m + 1
        else:
            right = m - 1
    return -1


print(first_bad_version(1))
