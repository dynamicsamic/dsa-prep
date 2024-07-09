from typing import Optional


def get_minimum_difference(root: Optional["TreeNode"]) -> Optional["TreeNode"]:
    """
    Leetcode. 530. Minimum Absolute Difference in BST
    https://leetcode.com/problems/minimum-absolute-difference-in-bst/

    -----------------------------Description-----------------------------------
    Given the root of a Binary Search Tree (BST), return the minimum absolute
    difference between the values of any two different nodes in the tree.

    -----------------------------Constraints-----------------------------------
    : The number of nodes in the tree is in the range [2, 10**4].
    : 0 <= Node.val <= 10**5

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: root = [4,2,6,1,3]
    Output: 1

    Example 2:
    Input: root = [1,0,48,null,null,12,49]
    Output: 1

    ------------------------------Algorithm------------------------------------
    We use BFS inorder traversal. Firstly we go to the lowest leftmost leaf
    node. For each valid node we calculate its difference with previously seen
    value and update global minimum value. We also update previously seen value
    to be the current value.
    """
    max_diff = float("inf")
    prev_val = None

    def traverse(root: Optional[TreeNode]):
        nonlocal max_diff, prev_val

        if not root:
            return

        traverse(root.left)

        if prev_val is not None:
            max_diff = min(abs(root.val - prev_val), max_diff)

        prev_val = root.val

        traverse(root.right)

    traverse(root)
    return max_diff


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        if self is None:
            return str(None)
        left = True if self.left else False
        right = True if self.right else False
        return (
            f"{self.__class__.__name__}[val={self.val}, "
            f"left={left} right={right}]"
        )


t7 = TreeNode(9)
t6 = TreeNode(6)
t5 = TreeNode(3)
t4 = TreeNode(1)
t3 = TreeNode(6)
t2 = TreeNode(2, t4, t5)
t1 = TreeNode(4, t2, t3)
assert get_minimum_difference(t1) == 1

t10 = TreeNode(15)
t9 = TreeNode(5)
t8 = TreeNode(1, t9, t10)
assert get_minimum_difference(t8) == 4

print("\nAll tests passed\n")
