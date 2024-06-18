from typing import Optional, TypeVar

T = TypeVar("T")


class TreeNode[T]:
    def __init__(
        self,
        val: T,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ) -> None:
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        left = True if self.left else False
        right = True if self.right else False
        return (
            f"{self.__class__.__name__}[val={self.val}, "
            f"left={left} right={right}]"
        )


def average_of_levels(root: Optional[TreeNode]) -> list[float]:
    from collections import deque

    queue = deque()
    result = []
    queue.append(root)

    while queue:
        level_sum = 0
        qlength = len(queue)

        for _ in range(qlength):
            el = queue.popleft()
            level_sum += el.val

            if el.left:
                queue.append(el.left)
            if el.right:
                queue.append(el.right)

        result.append(level_sum / qlength)

    return result
