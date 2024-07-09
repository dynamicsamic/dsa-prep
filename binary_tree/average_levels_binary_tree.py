def average_of_levels(root: "TreeNode") -> list[float]:
    """
    Leetcode. 637. Average of Levels in Binary Tree
    https://leetcode.com/problems/average-of-levels-in-binary-tree/description

    -----------------------------Description-----------------------------------
    Given the root of a binary tree, return the average value of the nodes on
    each level in the form of an array. Answers within 10**-5 of the actual
    answer will be accepted.

    -----------------------------Constraints-----------------------------------
    : The number of nodes in the tree is in the range [1, 10**4].
    : -2**31 <= Node.val <= 2**31-1

    ------------------------------Examples-------------------------------------
    Example 1:
    Input: root = [3,9,20,null,null,15,7]
    Output: [3.00000,14.50000,11.00000]
    Explanation: The average value of nodes on level 0 is 3, on level 1
    is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].

    Example 2:
    Input: root = [3,9,20,15,7]
    Output: [3.00000,14.50000,11.00000]

    ------------------------------Algorithm------------------------------------
    We use the DFS style binary tree traversing. We add root to the queue and
    start a loop. On each iteration of the outer while loop we start an inner
    for loop in which we count sum of all the descendants of previous level
    and also add all descendatnts of the next level to count them in next run.
    After inner loop finished, it means we counted all values from the
    previous level and can add the average to resulting array.
    """
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


class TreeNode[T]:
    def __init__(
        self,
        val: T,
        left: "TreeNode" = None,
        right: "TreeNode" = None,
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


t3 = TreeNode(3)
t2 = TreeNode(1)
t1 = TreeNode(2, t2, t3)
assert average_of_levels(t1) == [2.0, 2.0]

t5 = TreeNode(9)
t4 = TreeNode(7)
t3 = TreeNode(8, t4, t5)
t2 = TreeNode(1)
t1 = TreeNode(6, t2, t3)
assert average_of_levels(t1) == [6.0, 4.5, 8.0]

t5 = TreeNode(7)
t4 = TreeNode(15)
t3 = TreeNode(20, t4, t5)
t2 = TreeNode(9)
t1 = TreeNode(3, t2, t3)
assert average_of_levels(t1) == [3.0, 14.5, 11.0]

t1 = TreeNode(1)
assert average_of_levels(t1) == [1.0]

print("\nAll tests passed\n")
