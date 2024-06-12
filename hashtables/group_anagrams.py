def group_anagrams(strs: list[str]) -> list[list[str]]:
    seen = {}
    grouped = []
    pointer = 0

    for s in strs:
        normalized = "".join(sorted(s))
        if normalized not in seen:
            seen[normalized] = pointer
            grouped.append([s])
            pointer += 1
        else:
            idx = seen[normalized]
            grouped[idx].append(s)

    return grouped


def group_anagrams2(strs: list[str]) -> list[list[str]]:
    from collections import defaultdict

    grouped = defaultdict(list)
    for word in strs:
        grouped["".join(sorted(word))].append(word)

    return grouped.values()


tests = [
    (
        ["eat", "tea", "tan", "ate", "nat", "bat"],
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
    ),
    ([""], [[""]]),
    (["a"], [["a"]]),
]

for s, res in tests:

    print(group_anagrams(s))
print("All tests passed")
