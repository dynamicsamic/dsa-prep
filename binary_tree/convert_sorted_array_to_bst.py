def sorted_array_to_bst(nums: list[int]) -> "TreeNode":
    """
    Leetcode. 108. Convert Sorted Array to Binary Search Tree
    https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree

    -----------------------------Description-----------------------------------
    Given an integer array nums where the elements are sorted in ascending
    order, convert it to a height-balanced binary search tree.

    -----------------------------Constraints-----------------------------------
    : 1 <= nums.length <= 10**4
    : -10**4 <= nums[i] <= 10**4
    : nums is sorted in a strictly increasing order.

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: nums = [-10,-3,0,5,9]
    Output: [0,-3,9,-10,null,5]
    Explanation: [0,-10,5,null,-3,null,9] is also accepted:

    Example 2:
    Output: [3,1]
    Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.

    ------------------------------Algorithm------------------------------------
    We will use binary search strategy. On each recursive call we choose the
    middle value from the array. This would be the current node. For each
    current node we traverse halves of the array and attach subnodes as
    current's nodes children. When we reach a leaf node its both children
    nodes will be None. After we found a leaf node we start to go up and left
    returning nodes on each function finish. Lower nodes got attached to higher
    nodes from left to right.
    """
    if not nums:
        return

    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    left_branch = sorted_array_to_bst(nums[:mid])
    right_branch = sorted_array_to_bst(nums[mid + 1 :])
    node.left = left_branch
    node.right = right_branch

    return node


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


ar1 = [-10, -3, 0, 5, 9]
bst1 = sorted_array_to_bst(ar1)
ar2 = [1, 2, 3]
bst2 = sorted_array_to_bst(ar2)


def dfs_inorder(root: TreeNode) -> list[int]:
    """Little check function."""
    res = []

    def traverse(node: TreeNode | None) -> None:
        if not node:
            return
        traverse(node.left)
        res.append(node.val)
        traverse(node.right)

    traverse(root)
    return res


assert dfs_inorder(bst1) == ar1
assert dfs_inorder(bst2) == ar2

print("\nAll tests passed\n")
