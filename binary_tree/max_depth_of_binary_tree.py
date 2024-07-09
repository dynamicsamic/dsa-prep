from typing import Optional


def max_depth(root: Optional["TreeNode"]) -> int:
    """
    Leetcode. 104. Maximum Depth of Binary Tree
    https://leetcode.com/problems/maximum-depth-of-binary-tree/description

    -----------------------------Description-----------------------------------
    Given the root of a binary tree, return its maximum depth. A binary tree's
    maximum depth is the number of nodes along the longest path from the root
    node down to the farthest leaf node.

    -----------------------------Constraints-----------------------------------
    : The number of nodes in the tree is in the range [0, 10**4].
    : -100 <= Node.val <= 100

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 3

    Example 2:
    Input: root = [1,null,2]
    Output: 2

    ------------------------------Algorithm------------------------------------
    We use BFS inorder traversal. Firstly we go to the lowest leftmost leaf
    node. When we hit a leaf node, we get 1. After that we start our path
    upwards and for each node we choose the maximum from left and right
    branches, incrementing the result.
    """
    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))


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


t7 = TreeNode(7)
t6 = TreeNode(15)
t3 = TreeNode(20, t6, t7)
t2 = TreeNode(9)
t1 = TreeNode(3, t2, t3)
assert max_depth(t1) == 3

t9 = TreeNode(2)
t8 = TreeNode(1, None, t9)
assert max_depth(t8) == 2
assert max_depth(None) == 0

print("\nAll tests passed\n")
