def combine(n: int, k: int) -> list[list[int]]:
    """
    Leetcode. 77. Combinations
    https://leetcode.com/problems/combinations/description

    -----------------------------Description-----------------------------------
    Given two integers n and k, return all possible combinations of k numbers
    chosen from the range [1, n].
    You may return the answer in any order.

    -----------------------------Constraints-----------------------------------
    : 1 <= n <= 20
    : 1 <= k <= n

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: n = 4, k = 2
    Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    Explanation: There are 4 choose 2 = 6 total combinations.
    Note that combinations are unordered, i.e., [1,2] and [2,1]
    are considered to be the same combination.

    Example 2:
    Input: n = 1, k = 1
    Output: [[1]]
    Explanation: There is 1 choose 1 = 1 total combination.

    ------------------------------Algorithm------------------------------------
    This is a combinations problem, so we implement a solution that
    uses recursion and backtracking. First we define resulting array.
    In the inner recursive function we recursively iterate through numbers
    from 1 to n and add them to result when their length becomes equal to `k`.
    The recursive function follows this pattern: for every number
    it starts a for loop and add letter combinations to an intermediate array.
    That's why first number always come at first positions - they are
    in the outer loop. Once a combination is reached we dipose the last number
    to get a new unique combination.
    """

    res = []

    def backtrack(index: int, comb: list[int]) -> None:

        if len(comb) == k:
            res.append(comb.copy())
            return

        for j in range(index, n + 1):
            comb.append(j)

            backtrack(j + 1, comb)
            comb.pop()

    backtrack(1, [])
    return res


assert combine(4, 3) == [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
assert combine(4, 2) == [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
assert combine(1, 1) == [[1]]

print("\nAll tests passed\n")
