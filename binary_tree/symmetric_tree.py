def is_symmetric(root: "TreeNode") -> bool:
    """
    Leetcode. 101. Symmetric tree
    https://leetcode.com/problems/symmetric-tree/description

    -----------------------------Description-----------------------------------
    Given the root of a binary tree, check whether it is a mirror of itself
    (i.e., symmetric around its center).

    -----------------------------Constraints-----------------------------------
    : The number of nodes in the tree is in the range [1, 1000].
    : -100 <= Node.val <= 100

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: true

    Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false

    ------------------------------Algorithm------------------------------------
    Define the main function which is a closure that provides its root as
    starting points to the inner function. In the inner function we compare
    given nodes p and q as separate trees following this logic:
    if both trees became None, it means the trees are symmetric, since we
    managed to reach the end of both trees and did not violate any conditions.
    If only one of the trees is present, it means this trees surely can not be
    symmetric. After we compare values of trees and make two recursive calls
    now comparing left and right branches of each tree.
    .
    """

    def symmetric_trees(p: "TreeNode", q: "TreeNode") -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        return (
            p.val == q.val
            and symmetric_trees(p.left, q.right)
            and symmetric_trees(p.right, q.left)
        )

    return symmetric_trees(root, root)


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


t8 = TreeNode(3)
t7 = TreeNode(4)
t6 = TreeNode(4)
t5 = TreeNode(3)
t3 = TreeNode(2, t7, t8)
t2 = TreeNode(2, t5, t6)
t1 = TreeNode(1, t2, t3)

t66 = TreeNode(3)
t55 = TreeNode(3)
t33 = TreeNode(2, right=t66)
t22 = TreeNode(2, right=t55)
t11 = TreeNode(1, t22, t33)

assert is_symmetric(t1)
assert not is_symmetric(t11)

print("\nAll tests passed\n")
