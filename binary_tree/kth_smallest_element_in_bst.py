def kth_smallest(root: "TreeNode", k: int) -> int:
    """
    Leetcode. 230. Kth Smallest Element in a BST
    https://leetcode.com/problems/kth-smallest-element-in-a-bst/description

    -----------------------------Description-----------------------------------
    Given the root of a binary search tree, and an integer k, return the kth
    smallest value (1-indexed) of all the values of the nodes in the tree.

    -----------------------------Constraints-----------------------------------
    : The number of nodes in the tree is n.
    : 1 <= k <= n <= 10**4
    : 0 <= Node.val <= 10**4

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: root = [3,1,4,null,2], k = 1
    Output: 1

    Example 2:
    Input: root = [5,3,6,2,4,null,null,1], k = 3
    Output: 3

    ------------------------------Algorithm------------------------------------
    Define a closure to provide intitial setup. In the inner function start a
    bfs in-order traversal and collect all the values in the resulting array.
    Because we're traversing a binary search tree, we can be sure that in-order
    traversal will populte will resulting array with values sorted in ascending
    order. After the inner function finished, we make some sanity checks and
    return a value from the resulting array (we take `k-1` index because k
    expects indexes start from 1, not from 0).
    """

    values = []

    def add_values(node: "TreeNode") -> int:
        if not node:
            return

        if len(values) == k:
            return

        add_values(node.left)
        values.append(node.val)
        add_values(node.right)

    add_values(root)

    if not (1 <= k <= len(values)):
        return -1

    return values[k - 1]


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


t6 = TreeNode(1)
t5 = TreeNode(4)
t4 = TreeNode(2, t6)
t3 = TreeNode(6)
t2 = TreeNode(3, t4, t5)
t1 = TreeNode(5, t2, t3)

assert kth_smallest(t1, 6) == t3.val
assert kth_smallest(t1, 1) == t6.val
assert kth_smallest(t1, 2) == t4.val
assert kth_smallest(t1, 7) == -1

print("\nAll tests passed\n")
