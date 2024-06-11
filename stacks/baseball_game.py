def calculate_points(operations: list[str]) -> int:
    stack = []

    for el in operations:
        if el == "+":
            stack.append(stack[-1] + stack[-2])
        elif el == "D":
            stack.append(stack[-1] * 2)
        elif el == "C":
            stack.pop()
        else:
            stack.append(int(el))

    return sum(stack)


ops = [
    ["5", "2", "C", "D", "+"],
    ["5", "-2", "4", "C", "D", "9", "+", "+"],
    ["1", "C"],
]
for i in ops:
    print(calculate_points(i))
