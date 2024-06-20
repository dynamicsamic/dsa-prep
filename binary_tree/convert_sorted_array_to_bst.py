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


def sorted_array_to_bst(nums: list[int]) -> TreeNode:
    if not nums:
        return

    mid = len(nums) // 2
    node = TreeNode(nums[mid])
    left_branch = sorted_array_to_bst(nums[:mid])
    right_branch = sorted_array_to_bst(nums[mid + 1 :])
    node.left = left_branch
    node.right = right_branch

    return node


bst = sorted_array_to_bst([-10, -3, 0, 5, 9])
print(bst)
