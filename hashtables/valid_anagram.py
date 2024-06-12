from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


def is_anagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


def is_anagram3(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    scount, tcount = {}, {}

    for char in s:
        scount[char] = scount.get(char, 0) + 1

    for char in t:
        tcount[char] = tcount.get(char, 0) + 1

    if len(scount) != len(tcount):
        return False

    for key, val in scount.items():
        if val != tcount.get(key):
            return False

    return True


tests = [("anagram", "nagaram"), ("rat", "car"), ("rat", "tar")]

for s, t in tests:
    print(is_anagram3(s, t))
