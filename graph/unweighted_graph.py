from collections import deque
from typing import TypeVar

T = TypeVar("T")


class Vertex[T]:
    def __init__(
        self, value: T, neighbors: list["Vertex"] | None = None
    ) -> None:
        self.value = value
        self.neighbors = neighbors or []

    def __repr__(self) -> str:
        return (
            f"{self.__class__.__name__}[{self.value}, "
            f"len={len(self.neighbors)}]"
        )


def dfs(
    vertex: Vertex[T], value: T, visited: set[Vertex[T]] = None
) -> Vertex[T] | None:
    if vertex.value == value:
        return vertex

    visited.add(vertex)

    for ver in vertex.neighbors:
        if ver not in visited:
            find_recursive = dfs(ver, value, visited)
            if find_recursive:
                return find_recursive


def bfs(vertex: Vertex[T], value: T) -> Vertex[T] | None:
    if vertex.value == value:
        return vertex
    visited = set()
    queue = deque()
    visited.add(vertex)
    queue.append(vertex)

    while queue:
        current = queue.popleft()
        for ver in current.neighbors:
            if ver.value == value:
                return ver
            if ver not in visited:
                visited.add(current)
                queue.append(ver)


sm = Vertex("Sm")
nat = Vertex("Nat")
st = Vertex("ST")
dm = Vertex("Dm")
le = Vertex("Le")
ma = Vertex("Ma")
vo = Vertex("Vo")

sm.neighbors.append(nat)
sm.neighbors.append(st)
sm.neighbors.append(dm)
nat.neighbors.append(sm)
nat.neighbors.append(le)
nat.neighbors.append(st)
st.neighbors.append(ma)
ma.neighbors.append(st)
st.neighbors.append(sm)
dm.neighbors.append(vo)
vo.neighbors.append(dm)
dm.neighbors.append(sm)
# print(sm.neighbors)
# print(dfs(sm, "St", set()))
b = dfs(ma, "Sm", set())
# print(b)
# print(bfs(vo))
d = bfs(sm, "Le")
print(d)
