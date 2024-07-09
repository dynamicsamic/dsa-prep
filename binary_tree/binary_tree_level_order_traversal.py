from collections import deque
from typing import Optional


def level_order(root: Optional["TreeNode"]) -> list[list[int]]:
    """
    Leetcode. 102. Binary Tree Level Order Traversal
    https://leetcode.com/problems/binary-tree-level-order-traversal/description

    -----------------------------Description-----------------------------------
    Given the root of a binary tree, return the level order traversal of
    its nodes' values. (i.e., from left to right, level by level).

    -----------------------------Constraints-----------------------------------
    : The number of nodes in the tree is in the range [0, 2000].
    : -1000 <= Node.val <= 1000

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [[3],[9,20],[15,7]]

    Example 2:
    Input: root = [1]
    Output: [[1]]

    Example 3:
    Input: root = []
    Output: []

    ------------------------------Algorithm------------------------------------
    We use the DFS style binary tree traversing. We add root to the queue and
    start a loop. On each iteration of the outer while loop we start an inner
    for loop in which we collect all the descendants of previous level
    and also add all descendatnts of the next level to the queue to collect
    them in next run. After inner loop finished, it means we collected all
    values from the previous level and can add this array to resulting array.
    """
    if not root:
        return []

    queue = deque()
    result = []
    queue.append(root)

    while queue:
        current_level = []
        for _ in range(len(queue)):
            el = queue.popleft()

            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)
            current_level.append(el.val)

        result.append(current_level)

    return result


class TreeNode[T]:
    def __init__(
        self,
        val: T,
        left: "TreeNode" = None,
        right: "TreeNode" = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        left = True if self.left else False
        right = True if self.right else False
        return (
            f"{self.__class__.__name__}[val={self.val}, "
            f"left={left} right={right}]"
        )


t3 = TreeNode(3)
t2 = TreeNode(1)
t1 = TreeNode(2, t2, t3)
assert level_order(t1) == [[2], [1, 3]]

t5 = TreeNode(9)
t4 = TreeNode(7)
t3 = TreeNode(8, t4, t5)
t2 = TreeNode(1)
t1 = TreeNode(6, t2, t3)
assert level_order(t1) == [[6], [1, 8], [7, 9]]


t1 = TreeNode(1)
assert level_order(t1) == [[1]]

assert level_order(None) == []

print("\nAll tests passed\n")
