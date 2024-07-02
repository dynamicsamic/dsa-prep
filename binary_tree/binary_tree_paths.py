def tree_path(root: "TreeNode"):
    """
    Leetcode. 257. Binary Tree Paths
    https://leetcode.com/problems/binary-tree-paths/description

    -----------------------------Description-----------------------------------
    Given the root of a binary tree, return all root-to-leaf paths in any order.
    A leaf is a node with no children.

    -----------------------------Constraints-----------------------------------
    : The number of nodes in the tree is in the range [1, 100].
    : -100 <= Node.val <= 100

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: root = [1,2,3,null,5]
    Output: ["1->2->5","1->3"]

    Example 2:
    Input: root = [1]
    Output: ["1"]

    ------------------------------Algorithm------------------------------------
    We initialize an empty array to hold the results of tree traversal.
    In the inner func we traverse a binary tree using dfs preorder technique.
    Base case 1: if we moved past the leaves, we just return.
    Base case 2: if we are at a leaf node it means that by this time we've
    already collected all nodes, so we add the collected path string to
    result array.
    Recursive case: we concatenate the path string with a formatted node value
    and call recurse the left and right nodes.
    """
    res = []

    def preorder(node: TreeNode, path: str) -> None:
        if not node:
            return
        if not node.left and not node.right:
            path = str(node.val) if not path else path + "->" + str(node.val)
            res.append(path)
            return

        path = str(node.val) if not path else path + "->" + str(node.val)

        preorder(node.left, path)
        preorder(node.right, path)

    preorder(root, "")
    return res


def tree_path_backtrack(root: "TreeNode") -> list[str]:
    """
    ------------------------------Algorithm------------------------------------
    This algorithm is very similar to the previous one, but uses backtracking
    for generating paths. We have a `path` array, which serves a container
    or accumulator for values we've seen so far. On each function call we
    either add a value to the path array or add path's contents to the
    resulting array. We keep deleting the last value on every successfull
    function call, thus preserving the unique paths combinations.
    """
    res = []

    def backtrack(node: TreeNode, path: list[str]) -> None:
        if not node:
            return
        if not node.left and not node.right:
            path.append(str(node.val))
            res.append("->".join(path))
            path.pop()
            return

        path.append(str(node.val))

        backtrack(node.left, path)
        backtrack(node.right, path)

        path.pop()

    backtrack(root, [])
    return res


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


t4 = TreeNode(5)
t3 = TreeNode(3)
t2 = TreeNode(2, right=t4)
t1 = TreeNode(1, t2, t3)

assert tree_path(t1) == tree_path_backtrack(t1) == ["1->2->5", "1->3"]

t0 = TreeNode(1)
assert tree_path(t0) == tree_path_backtrack(t0) == ["1"]

print("\nAll tests passed\n")
