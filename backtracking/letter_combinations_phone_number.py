def letter_combinations(digits: str) -> list[list[int]]:
    """
    Leetcode. 17. Letter Combinations of a Phone Number
    https://leetcode.com/problems/letter-combinations-of-a-phone-number/

    -----------------------------Description-----------------------------------
    Given a string containing digits from 2-9 inclusive, return all
    possible letter combinations that the number could represent.
    Return the answer in any order.
    A mapping of digits to letters (just like on the telephone buttons)
    is given below. Note that 1 does not map to any letters.

    -----------------------------Constraints-----------------------------------
    : 0 <= digits.length <= 4
    : digits[i] is a digit in the range ['2', '9'].

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    Example 2:

    Input: digits = ""
    Output: []

    Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]

    ------------------------------Algorithm------------------------------------
    This is a combinations-like problem, so we implement a solution that
    uses recursion and backtracking. First we define resulting array and a
    mapping from string numbers to their corresponding letters.
    In the inner recursive function we recursively iterate through letters
    and add them to result when their length becomes equal to number of
    given digits.
    The recursive function follows this pattern: for every number (leeter)
    it starts a for loop and add letter combinations to an intermediate array.
    That's why first number letters always come first - they are in the outer
    loop. Once a combination is reached we dipose the last letter to get a
    new unique combination.
    """

    res = []
    buttons = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    def backtrack(i: int, comb: list[int]) -> None:

        if len(comb) == len(digits):
            res.append("".join(comb.copy()))
            return

        for char in buttons[digits[i]]:
            comb.append(char)

            backtrack(i + 1, comb)
            comb.pop()

    if digits:
        backtrack(0, [])

    return res


assert letter_combinations("23") == [
    "ad",
    "ae",
    "af",
    "bd",
    "be",
    "bf",
    "cd",
    "ce",
    "cf",
]

assert letter_combinations("") == []
assert letter_combinations("2") == ["a", "b", "c"]

print("\nAll tests passed\n")
