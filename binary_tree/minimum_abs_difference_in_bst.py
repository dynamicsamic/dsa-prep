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


def get_minimum_difference(root: Optional[TreeNode]) -> Optional[TreeNode]:
    max_diff = float("inf")
    prev_val = None

    def traverse(root: Optional[TreeNode]):
        nonlocal max_diff, prev_val

        if not root:
            return

        traverse(root.left)

        if prev_val is not None:
            max_diff = min(abs(root.val - prev_val), max_diff)

        prev_val = root.val

        traverse(root.right)

    traverse(root)
    return max_diff


t7 = TreeNode(9)
t6 = TreeNode(6)
t5 = TreeNode(3)
t4 = TreeNode(1)
t3 = TreeNode(6)
t2 = TreeNode(2, t4, t5)
t1 = TreeNode(4, t2, t3)

# get_minimum_difference(t1)
# print(min(a))
print(get_minimum_difference(t1))
t0 = TreeNode()

t10 = TreeNode(3)
t9 = TreeNode(2)
t8 = TreeNode(1, t9, t10)


# r = get_minimum_difference(t0)
# print(r)
