def find_index_of_first_occurrence_in_string(
    haystack: str, needle: str
) -> int:
    if len(needle) > len(haystack):
        return -1
    idx = -1
    pointer = 0

    for i in range(len(haystack)):
        if haystack[i] == needle[pointer]:
            print(i)
            if idx == -1:
                idx = i
            pointer += 1
        else:
            pointer = 0
            idx = -1

        if needle[idx:pointer] == needle:
            break
        # if pointer == len(needle):
        # break

    return idx


haystack = "mississippi"
needle = "issipi"
# print(find_index_of_first_occurrence_in_string(haystack, needle))


def find_index_of_first_occurrence_in_string2(
    haystack: str, needle: str
) -> int:
    if len(needle) > len(haystack):
        return -1

    i = j = k = 0
    while i < len(haystack):
        while (
            k < len(needle) and j < len(haystack) and haystack[j] == needle[k]
        ):
            j += 1
            k += 1
        if k == len(needle):
            return i
        i += 1
        j = i
        k = 0

    return -1


print(find_index_of_first_occurrence_in_string2(haystack, needle))
