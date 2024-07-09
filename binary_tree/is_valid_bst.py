def is_valid_bst(root: "TreeNode") -> bool:
    """
    Leetcode. 98. Validate Binary Search Tree
    https://leetcode.com/problems/validate-binary-search-tree/description

    -----------------------------Description-----------------------------------
    Given the root of a binary tree, determine if it is a valid binary search
    tree (BST). A valid BST is defined as follows:
        - The left subtree of a node contains only nodes with keys less than
          the node's key.
        - The right subtree of a node contains only nodes with keys greater
          than the node's key.
        - Both the left and right subtrees must also be binary search trees.

    -----------------------------Constraints-----------------------------------
    : The number of nodes in the tree is in the range [1, 10**4].
    : -2**31 <= Node.val <= 2**31 - 1

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: root = [2,1,3]
    Output: true

    Example 2:
    Input: root = [5,1,4,null,null,3,6]
    Output: false
    Explanation: The root node's value is 5 but its right child's value is 4.

    ------------------------------Algorithm------------------------------------
    We use the DFS style binary tree traversing. Starting with root we traverse
    all its left descendants. After that we pop the lowest left descendant and
    compare with the lowest value seen so far. The lowest left descendant's
    value is greater, we know it violates the bst rule, so we return false.
    Otherwise we update the lowest value seen so far and try traversing the
    right descendants.
    """
    stack = []
    min_value = float("-inf")
    current = root

    while stack or current:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()

        if current.val <= min_value:
            return False

        min_value = current.val
        current = current.right

    return True


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


t3 = TreeNode(3)
t2 = TreeNode(1)
t1 = TreeNode(2, t2, t3)
assert is_valid_bst(t1)


t5 = TreeNode(6)
t4 = TreeNode(3)
t3 = TreeNode(4, t4, t5)
t2 = TreeNode(1)
t1 = TreeNode(5, t2, t3)
assert not is_valid_bst(t1)

t5 = TreeNode(9)
t4 = TreeNode(7)
t3 = TreeNode(8, t4, t5)
t2 = TreeNode(1)
t1 = TreeNode(6, t2, t3)
assert is_valid_bst(t1)

t2 = TreeNode(1)
t1 = TreeNode(1, left=t2)
assert not is_valid_bst(t1)

print("\nAll tests passed\n")
