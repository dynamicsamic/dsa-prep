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


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True
    elif not p or not q:
        return False
    elif p.val != q.val:
        return False

    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

t7 = TreeNode(1)
t6 = TreeNode(20, t7)
t5 = TreeNode(9)
t4 = TreeNode(3, t5, t6)

t3 = TreeNode(20)
t2 = TreeNode(9)
t1 = TreeNode(3, t2, t3)

print(is_same_tree(t1 ,t4))

t0 = TreeNode()

# t10 = TreeNode(3)
t9 = TreeNode(2)
t8 = TreeNode(1, None, t9)
# print(max_depth(t8))
