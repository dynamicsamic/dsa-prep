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


def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return 1 + max_depth(root.left) + max_depth(root.right)


t7 = TreeNode(7)
t6 = TreeNode(15)


t5 = TreeNode(5)
t4 = TreeNode(4)
t3 = TreeNode(3)
t2 = TreeNode(2, t4, t5)
t1 = TreeNode(1, t2, t3)

print(max_depth(t1))

t0 = TreeNode()

# t10 = TreeNode(3)
t9 = TreeNode(2)
t8 = TreeNode(1, None, t9)
# print(max_depth(t8))
