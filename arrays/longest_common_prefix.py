def longest_common_prefix(words: list[str]) -> str:
    longest = words[0]

    for word in words[1:]:
        i = 0
        long_count = 0
        while i < len(longest) and i < len(word):
            if longest[i] == word[i]:
                long_count += 1
                i += 1

            else:
                break

        if long_count == 0:
            return ""

        longest = longest[:long_count]

    return longest


strs = ["flower", "flow", "flight"]
strs1 = ["dog", "racecar", "car"]
print(longest_common_prefix(strs))
print(longest_common_prefix(strs1))
