import operator
from math import trunc


def eval_rpn(tokens: list[str]) -> int:
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": None,
    }
    operands = []

    for char in tokens:
        if char in operators:
            n2 = operands.pop()
            n1 = operands.pop()
            if char == "/":
                expr = trunc(n1 / n2)
            else:
                expr = operators.get(char)(n1, n2)
            operands.append(expr)
        else:
            operands.append(int(char))

    return operands.pop()


tokens1 = ["2", "1", "+", "3", "*"]
tokens = ["4", "13", "5", "/", "+"]
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(eval_rpn(tokens))
