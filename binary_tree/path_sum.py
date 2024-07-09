from typing import Optional


def has_path_sum(root: Optional["TreeNode"], target_sum: int) -> bool:
    """
    Leetcode. 112. Path Sum
    https://leetcode.com/problems/path-sum/description

    -----------------------------Description-----------------------------------
    Given the root of a binary tree and an integer targetSum, return true if
    the tree has a root-to-leaf path such that adding up all the values along
    the path equals targetSum. A leaf is a node with no children.

    -----------------------------Constraints-----------------------------------
    The number of nodes in the tree is in the range [0, 5000].
    -1000 <= Node.val <= 1000
    -1000 <= targetSum <= 1000

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
    Output: true
    Explanation: The root-to-leaf path with the target sum is shown.

    Example 2:
    Input: root = [1,2,3], targetSum = 5
    Output: false
    Explanation: There two root-to-leaf paths in the tree:
    (1 --> 2): The sum is 3.
    (1 --> 3): The sum is 4.
    There is no root-to-leaf path with sum = 5.

    Example 3:
    Input: root = [], targetSum = 0
    Output: false
    Explanation: Since the tree is empty, there are no root-to-leaf paths.

    ------------------------------Algorithm------------------------------------
    We use BFS preorder traversal. On every recursive call we decrease the
    target sum by the current node's val. By the time we will have reached the
    leaf node, the target sum should have been decreased to fit the leaf node's
    value. If this two numbers are not equal, we return False. After the
    both recursive calls we check if either of the two branches satisfy the
    the condition.
    """
    if not root:
        return False

    elif not root.left and not root.right:
        return target_sum == root.val

    has_left = has_path_sum(root.left, target_sum - root.val)
    has_right = has_path_sum(root.right, target_sum - root.val)

    return has_left or has_right


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
t5 = TreeNode(3)
t4 = TreeNode(1)
t3 = TreeNode(20, t6, t7)
t2 = TreeNode(9, t4, t5)
t1 = TreeNode(3, t2, t3)
assert has_path_sum(t1, 38)
assert not has_path_sum(t1, 138)

t10 = TreeNode(3)
t9 = TreeNode(2)
t8 = TreeNode(1, t9, t10)
assert has_path_sum(t8, 3)
assert not has_path_sum(t8, 5)
assert not has_path_sum(None, 1)

print("\nAll tests passed\n")
