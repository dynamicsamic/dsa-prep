from typing import Optional


def invert_binary_tree(root: Optional["TreeNode"]) -> Optional["TreeNode"]:
    """
    Leetcode. 226. Invert Binary Tree
    https://leetcode.com/problems/invert-binary-tree/description

    -----------------------------Description-----------------------------------
    Given the root of a binary tree, invert the tree, and return its root.

    -----------------------------Constraints-----------------------------------
    : The number of nodes in the tree is in the range [0, 100].
    : -100 <= Node.val <= 100

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

    Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

    Example 3:
    Input: root = []
    Output: []

    ------------------------------Algorithm------------------------------------
    We use BFS preorder traversal. We swap left and right branches and make
    two recursive calls to apply those changes to all branches.
    """
    if not root:
        return root

    root.left, root.right = root.right, root.left
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    return root


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
t3 = TreeNode(7, t6, t7)
t2 = TreeNode(2, t4, t5)
t1 = TreeNode(4, t2, t3)
inverted1 = invert_binary_tree(t1)
assert inverted1 == t1
assert t1.right.val == t2.val and t1.left.val == t3.val
assert t2.right.val == t4.val and t2.left.val == t5.val
assert t3.right.val == t6.val and t3.left.val == t7.val

t10 = TreeNode(3)
t9 = TreeNode(2)
t8 = TreeNode(1, t9, t10)
inverted2 = invert_binary_tree(t8)
assert inverted2 == t8
assert t8.right.val == t9.val
assert t8.left.val == t10.val

assert invert_binary_tree(None) is None

print("\nAll tests passed\n")
