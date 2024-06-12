def is_isomorphic(s: str, t: str) -> bool:
    mappings = {}
    mappings_occupied = set()

    for i in range(len(s)):
        if s[i] not in mappings:
            if t[i] not in mappings_occupied:
                mappings[s[i]] = t[i]
                mappings_occupied.add(t[i])
            else:
                return False
        else:
            if mappings[s[i]] != t[i]:
                return False

    return True


def is_isomorphic2(a, b):
    mappings = {}

    for val, mapper in zip(a, b):
        if val in mappings:
            if mapper != mappings[val]:
                return False
        else:
            if mapper in mappings.values():
                return False
            mappings[val] = mapper

    return True


exmpls = [("egg", "add"), ("foo", "bar"), ("paper", "title"), ("badc", "baba")]
for i in exmpls:
    print(is_isomorphic2(*i))
