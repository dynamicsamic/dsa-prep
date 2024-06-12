from collections import Counter


def ransome_note(rnote: str, magazine: str) -> bool:
    if len(magazine) < len(rnote):
        return False

    c1 = Counter(rnote)
    c2 = Counter(magazine)

    return c2 >= c1


def ransome_note2(note: str, magazine: str) -> bool:
    if len(magazine) < len(note):
        return False

    substr = 97

    c1 = [0] * 27
    c2 = [0] * 27

    for i in range(len(note)):
        c1[ord(note[i]) - substr] += 1

    for i in range(len(magazine)):
        c2[ord(magazine[i]) - substr] += 1

    for i in range(len(c1)):
        if c1[i] > c2[i]:
            return False

    return True


# for i in (("a", "b"), ("aa", "b"), ("aa", "aab")):
# print(ransome_note2(*i))
print(ransome_note2("fihjjjjei", "hjibagacbhadfaefdjaeaebgi"))
