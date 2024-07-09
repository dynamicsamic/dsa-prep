from typing import Optional


def is_same_tree(p: Optional["TreeNode"], q: Optional["TreeNode"]) -> bool:
    """
    Leetcode. 100. Same tree
    https://leetcode.com/problems/same-tree/description

    -----------------------------Description-----------------------------------
    Given the roots of two binary trees p and q, write a function to check if
    they are the same or not. Two binary trees are considered the same if they
    are structurally identical, and the nodes have the same value.

    -----------------------------Constraints-----------------------------------
    : The number of nodes in both trees is in the range [0, 100].
    : -10**4 <= Node.val <= 10**4

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: p = [1,2,3], q = [1,2,3]
    Output: true

    Example 2:
    Input: p = [1,2], q = [1,null,2]
    Output: false

    Example 3:
    Input: p = [1,2,1], q = [1,1,2]
    Output: false

    ------------------------------Algorithm------------------------------------
    We use BFS preorder traversal. On every recursive call we decrease we chech
    three conditions:
        -if we passed beyond the tree with, it means we haven't catch any false
        conditions, therefore trees are same;
        -if any node is not represented in one of the trees, it means the
        condition is violated;
        -if any pair of nodes on the same position hase different values, it
        violates the condition.
    """

    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


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


t6 = TreeNode(20)
t5 = TreeNode(9)
t4 = TreeNode(3, t5, t6)

t3 = TreeNode(20)
t2 = TreeNode(9)
t1 = TreeNode(3, t2, t3)
assert is_same_tree(t1, t4)

t7 = TreeNode(1)
t6 = TreeNode(20, t7)
t5 = TreeNode(9)
t4 = TreeNode(3, t5, t6)

t3 = TreeNode(20)
t2 = TreeNode(9)
t1 = TreeNode(3, t2, t3)
assert not is_same_tree(t1, t4)

t4 = TreeNode(2)
t3 = TreeNode(1, right=t4)

t2 = TreeNode(2)
t1 = TreeNode(1, left=t2)
assert not is_same_tree(t1, t3)

print("\nAll tests passed\n")
