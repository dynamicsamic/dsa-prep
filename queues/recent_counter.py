from collections import deque


class RecentCounter:
    def __init__(self) -> None:
        self._data = deque()

    def ping(self, t: int) -> int:
        self._data.append(t)

        while self._data[0] < t - 3000:
            self._data.popleft()

        return len(self._data)


# [[], [1], [100], [3001], [3002]]
c = RecentCounter()
print(c.ping(1))
print(c.ping(100))
print(c.ping(3001))
print(c.ping(3002))
print(c._data)
