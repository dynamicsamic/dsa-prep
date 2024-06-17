from typing import Optional


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


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if not root:
        return False

    elif not root.left and not root.right:
        return target_sum == root.val

    has_left = has_path_sum(root.left, target_sum - root.val)
    has_right = has_path_sum(root.right, target_sum - root.val)

    return has_left or has_right


t7 = TreeNode(7)
t6 = TreeNode(15)


t5 = TreeNode(3)
t4 = TreeNode(1)
t3 = TreeNode(20, t6, t7)
t2 = TreeNode(9, t4, t5)
t1 = TreeNode(3, t2, t3)

print(has_path_sum(t1, 38))

t0 = TreeNode()

# t10 = TreeNode(3)
t9 = TreeNode(2)
t8 = TreeNode(1, None, t9)
# print(max_depth(t8))
