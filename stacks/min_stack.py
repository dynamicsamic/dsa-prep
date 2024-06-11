class MinStack:
    def __init__(self):
        self._data: list[tuple[int]] = []
        self._minval: int = None

    def push(self, val: int) -> None:
        if self._minval is None or val < self._minval:
            self._minval = val
        self._data.append((val, self._minval))

    def pop(self) -> None:
        self._data.pop()
        if not self._data:
            self._minval = None
        else:
            self._minval = self._data[-1][1]

    def top(self) -> int:
        return self._data[-1][0]

    def getMin(self) -> int:
        return self._minval


stack = MinStack()
stack.push(2147483646)
stack.push(2147483646)
stack.push(2147483647)
print(stack.top())
stack.pop()
print(stack.getMin())
stack.pop()
print(stack.getMin())
stack.pop()
stack.push(2147483647)
print(stack.top())
print(stack.getMin())
stack.push(-2147483648)
print(stack.top())
print(stack.getMin())
stack.pop()
print(stack.getMin())
