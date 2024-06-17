from typing import Optional, TypeVar

T = TypeVar("T")


class TreeNode[T]:
    def __init__(
        self,
        value: T,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        left = True if self.left else False
        right = True if self.right else False
        return (
            f"{self.__class__.__name__}[val={self.value}, "
            f"left={left} right={right}]"
        )


class BinarySearchTree:
    def __init__(self, root: Optional[TreeNode[T]] = None):
        self.root = root
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def insert(self, value: T, node: Optional[TreeNode[T]] = None) -> None:
        def _insert(value: T, node: Optional[TreeNode[T]] = None) -> None:
            if value <= node.value:
                if not node.left:
                    node.left = TreeNode(value)
                else:
                    _insert(value, node.left)
            else:
                if not node.right:
                    node.right = TreeNode(value)
                else:
                    _insert(value, node.right)

        if not self.root:
            self.root = TreeNode(value)
        else:
            _insert(value, node or self.root)
        self._size += 1

    def search(
        self, value: T, node: Optional[TreeNode[T]] = None
    ) -> TreeNode[T] | None:
        def _search(value: T, node: Optional[TreeNode[T]] = None):
            if node is None or node.value == value:
                return node
            elif value < node.value:
                return _search(value, node.left)
            else:
                return _search(value, node.right)

        return _search(value, node or self.root)


if __name__ == "__main__":
    tn = TreeNode(10)
    bst = BinarySearchTree(tn)
    bst.insert(12)
    print(len(bst))
    s = bst.search(12,bst.root.right)
    print(s)
    print(bst.root.right)
    # bst.root = tn


"""
             |_|
        |_|      |_|



"""
