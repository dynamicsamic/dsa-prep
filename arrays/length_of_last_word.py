def length_of_last_word(sentence: str) -> int:
    return len(sentence.split()[-1])


def length_of_last_word2(sentence: str) -> int:
    i = len(sentence) - 1
    count = 0

    while i >= 0:
        if sentence[i] != " ":
            while sentence[i] != " ":
                if i < 0:
                    break
                count += 1
                i -= 1
            return count
        i -= 1


s1 = "hello world"
s2 = "   fly me   to   the moon  "
s3 = "luffy is still joyboy"
for i in s1, s2, s3:
    print(length_of_last_word2(i))
