def partition_labels(s: str) -> list[int]:
    """
    Leetcode. 763. Partition Labels
    https://leetcode.com/problems/partition-labels/description

    -----------------------------Description-----------------------------------
    You are given a string s. We want to partition the string into as many
    parts as possible so that each letter appears in at most one part.
    Note that the partition is done so that after concatenating all the parts
    in order, the resultant string should be s.
    Return a list of integers representing the size of these parts.

    -----------------------------Constraints-----------------------------------
    : 1 <= s.length <= 500
    : s consists of lowercase English letters.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: s = "ababcbacadefegdehijhklij"
    Output: [9,7,8]
    Explanation:
    The partition is "ababcbaca", "defegde", "hijhklij".
    This is a partition so that each letter appears in at most one part.
    A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it
    splits s into less parts.

    Example 2:
    Input: s = "eccbbbbdec"
    Output: [10]

    ------------------------------Algorithm------------------------------------
    First we need to determine where the last occurance of each character
    may be found. So we iterate through the string `s` and collect all its
    chars into `char_idx` dict. Indexes of repeated chars that placed last
    will replace the ones that we placed first.
    This will give us the info where the last occurance in every char
    may be found, so we could safely make a partition.
    Next we declare two pointers that will track the size of each partition.
    Right pointer will check the max index of every char.
    If a max index of a char is found it means that this char will no longer
    appear in the string, that's why it is a partition.
    We store the distance between left and right pointers and add 1
    because of 0-based index counting. After we update left pointer to
    point to the next char of the string, which is a start of a new
    partition.
    """
    char_idx = {}
    part_sizes = []

    for i, char in enumerate(s):
        char_idx[char] = i

    left = right = 0

    for i, char in enumerate(s):
        right = max(right, char_idx[char])
        if i == right:
            part_sizes.append(right - left + 1)
            left = i + 1

    return part_sizes


assert partition_labels("ababcbacadefegdehijhklij") == [9, 7, 8]
assert partition_labels("eccbbbbdec") == [10]
assert partition_labels("c") == [1]
