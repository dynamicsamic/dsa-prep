from collections import deque
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


def flatten(root: Optional[TreeNode]) -> None:
    def collect_nodes(root: Optional[TreeNode], q: deque[TreeNode]) -> deque[TreeNode]:
        if not root:
            return
        q.append(root)
        collect_nodes(root.left, q)
        collect_nodes(root.right, q)
        return q
    
    if not root:
        return 
        
    q = collect_nodes(root, deque())
    
    root = q.popleft()
    node = root
    while q:
        node.left = None
        node.right = q.popleft()
        node = node.right
    return root

def flatten2(root: Optional[TreeNode]) -> None:
    prev = None
    def _flatten(root: Optional[TreeNode])-> None:
        nonlocal prev

        if not root:
            return
    
        _flatten(root.right)
        _flatten(root.left)
        root.right = prev
        root.left = None
        prev = root

    _flatten(root)

def flatten3(root: Optional[TreeNode]) -> None:
    if not root:
        return
    
    stack = [root]
    current = None

    while stack:
        node = stack.pop()

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

        if not current:
            current = node
        else:
            current.right = node
            current.left = None
        
            current = current.right


t7 = TreeNode(7)
t6 = TreeNode(15)


t5 = TreeNode(3)
t4 = TreeNode(1)
t3 = TreeNode(20, t6, t7)
t2 = TreeNode(9, t4, t5)
t1 = TreeNode(3, t2, t3)

print(flatten2(t1))
print(t1.right)

t0 = TreeNode()

# t10 = TreeNode(3)
t9 = TreeNode(2)
t8 = TreeNode(1, None, t9)
# print(max_depth(t8))
