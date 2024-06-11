def valid_parentheses(parens: str) -> bool:
    if len(parens) % 2 == 0:
        return False

    lookup = {"(": ")", "{": "}", "[": "]"}
    stack = []

    for paren in parens:
        if paren in lookup:
            stack.append(lookup[paren])
        else:
            if not stack:
                return False

            valid_paren = stack.pop()
            if paren != valid_paren:
                return False
    if stack:
        return False

    return True


p1 = "([])"
p2 = "(]"
p3 = "()"
p4 = "()[]{}"

for p in p1, p2, p3, p4:
    print(valid_parentheses(p))
