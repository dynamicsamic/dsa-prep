def first_bad_version(n: int) -> bool:
    """
    Leetcode. 278. First Bad Version
    https://leetcode.com/problems/first-bad-version/description

    -----------------------------Description-----------------------------------
    You are a product manager and currently leading a team to develop a new
    product. Unfortunately, the latest version of your product fails the
    quality check. Since each version is developed based on the previous
    version, all the versions after a bad version are also bad. Suppose you
    have n versions [1, 2, ..., n] and you want to find out the first bad one,
    which causes all the following ones to be bad.You are given an API bool
    isBadVersion(version) which returns whether version is bad. Implement a
    function to find the first bad version. You should minimize the number of
    calls to the API.

    -----------------------------Constraints-----------------------------------
    : 1 <= bad <= n <= 2**31-1

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: n = 5, bad = 4
    Output: 4
    Explanation:
    call isBadVersion(3) -> false
    call isBadVersion(5) -> true
    call isBadVersion(4) -> true
    Then 4 is the first bad version.

    Example 2:
    Input: n = 1, bad = 1
    Output: 1

    ------------------------------Algorithm------------------------------------
    Since all product version go in ascending order, we use binary search, to
    minimize calls to external API. If we found a version which the API detects
    as bad, we need to also check the previous version. If previous version is
    ok, it means we found the bad version. If previous version is also bad we
    need to find the first bad version amongst the lower versions. If found
    version is ok, we need to find bad version amongst the higher versions.
    """
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


is_bad_version = lambda x: x >= 4
assert first_bad_version(5) == 4
assert first_bad_version(1) == -1

is_bad_version = lambda x: x == 2
assert first_bad_version(4) == 2

print("\nAll tests passed\n")