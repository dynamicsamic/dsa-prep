from typing import Optional


class TrieNode:
    def __init__(self) -> None:
        self.nodes = {}

    def __iter__(self):
        for item in self.nodes.values():
            yield item

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self.nodes}"


class Trie:
    WORD_END = "~~"

    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def __repr__(self) -> str:
        return str(self.root)

    def insert(self, word: str) -> None:
        current = self.root

        for char in word:
            if char in current.nodes:
                current = current.nodes[char]
            else:
                current.nodes[char] = TrieNode()
                current = current.nodes[char]

        current.nodes[self.WORD_END] = None

    def find_prefix(self, prefix: str) -> TrieNode | None:
        current = self.root

        for char in prefix:
            if char in current.nodes:
                current = current.nodes[char]
            else:
                return

        return current

    def has_prefix(self, prefix: str) -> bool:
        return True if self.find_prefix(prefix) else False

    def has_word(self, text):
        if node := self.find_prefix(text):
            return self.WORD_END in node.nodes
        return False

    def delete(self, text: str) -> TrieNode:
        current = self.root
        text_length = len(text)

        for i in range(text_length):
            char = text[i]

            # Stop at the second to last node
            if i == text_length - 1:
                # Check if the last char is present in this node
                # to ensure its a valid word.
                if (
                    char in current.nodes
                    and self.WORD_END in current.nodes[char].nodes
                ):
                    # Unset complete word flag.
                    current.nodes[char].nodes.pop(self.WORD_END)
                    return True

            elif char in current.nodes:
                current = current.nodes[char]

            else:
                return False

        return False

    def to_array(
        self,
        current_node: Optional[TrieNode] = None,
        words: Optional[list[str]] = None,
    ) -> list[str]:
        def _to_array(
            current_node: Optional[TrieNode],
            words: list[str],
            current_word: str = "",
        ):
            for key, node in current_node.nodes.items():
                if key == self.WORD_END:
                    words.append(current_word)

                else:
                    _to_array(node, words, current_word + key)

            return words

        words = words or []
        current_node = current_node or self.root
        return _to_array(current_node, words)

    def count_words(self) -> int:
        current = self.root
        stack = [current]
        count = 0

        while stack:
            node = stack.pop()
            for item in node:
                if item:
                    stack.append(item)
                    if self.WORD_END in item.nodes:
                        count += 1
        return count


if __name__ == "__main__":
    trie = Trie()
    assert trie.count_words() == 0
    trie.insert("apple")
    trie.insert("app")
    assert trie.count_words() == 2

    # Assert find_prefix returns next node.
    pref = trie.find_prefix("a")
    assert isinstance(pref, TrieNode)
    assert trie.root.nodes["a"] is pref

    assert trie.has_word("app")
    assert trie.has_word("apple")
    assert not trie.has_word("a")

    assert trie.has_prefix("app")
    assert trie.has_prefix("a")
    assert not trie.has_prefix("bob")

    trie.insert("a")
    assert trie.count_words() == 3
    assert trie.has_word("a")

    assert trie.delete("a")
    assert not trie.has_word("a")
    assert trie.has_prefix("a")
    assert trie.count_words() == 2

    assert not trie.delete("a")
    assert trie.count_words() == 2

    assert not trie.delete("hello")
    assert trie.count_words() == 2

    trie.insert("apples")
    trie.insert("appled")

    assert sorted(trie.to_array()) == sorted(
        ["apples", "appled", "apple", "app"]
    )
