def sum_of_left_leaves(root: "TreeNode", s: int = 0) -> int:
    """
    Leetcode. 404. Sum of Left Leaves
    https://leetcode.com/problems/sum-of-left-leaves/description

    -----------------------------Description-----------------------------------
    Given the root of a binary tree, return the sum of all left leaves.
    A leaf is a node with no children. A left leaf is a leaf that is the left
    child of another node.

    -----------------------------Constraints-----------------------------------
    : The number of nodes in the tree is in the range [1, 1000].
    : -1000 <= Node.val <= 1000

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: 24
    Explanation: There are two left leaves in the binary tree, with values
    9 and 15 respectively.

    Example 2:
    Input: root = [1]
    Output: 0

    ------------------------------Algorithm------------------------------------
    Define the main function which we'll be a closure and provide the
    accumulator variable `s` for inner function.
    In the inner function start pre-order traversal and increment accumulator
    on every found left leaf.
    """

    def _sum_of_left_leaves(root: TreeNode | None) -> None:
        nonlocal s

        if not root:
            return

        if root.left and not (root.left.left or root.left.right):
            s += root.left.val

        _sum_of_left_leaves(root.left)
        _sum_of_left_leaves(root.right)

    _sum_of_left_leaves(root)

    return s


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


t6 = TreeNode(7)
t5 = TreeNode(15)
t3 = TreeNode(20, t5, t6)
t2 = TreeNode(9)
t1 = TreeNode(3, t2, t3)
assert sum_of_left_leaves(t1) == 24

t0 = TreeNode(1)
assert sum_of_left_leaves(t0) == 0

print("\nAll tests passed\n")
