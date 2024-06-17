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


def invert_binary_tree(root: Optional[TreeNode])-> Optional[TreeNode]:
    if not root:
        return root
    
    root.left, root.right = root.right, root.left
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)
    return root

t7 = TreeNode(9)
t6 = TreeNode(6)
t5 = TreeNode(3)
t4 = TreeNode(1)
t3 = TreeNode(7, t6, t7)
t2 = TreeNode(2, t4, t5)
t1= TreeNode(4, t2, t3)

t0 = TreeNode()

t10 = TreeNode(3)
t9 = TreeNode(2)
t8 = TreeNode(1, t9, t10)



r = invert_binary_tree(t0)
print(r)