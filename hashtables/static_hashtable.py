from collections import namedtuple
from typing import Any


class HashTableException(Exception):
    pass


MapItem = namedtuple("Mapitem", ["key", "value"])


class HashTable:

    DEFAULT_CAPACITY = 20

    def __init__(self, capacity: int = 0) -> None:
        capacity = capacity or self.DEFAULT_CAPACITY
        self.capacity = capacity
        self._store: list[MapItem | list[MapItem]] = [None] * self.capacity
        self._size: int = 0
        self._prime: int = 50331653  # big prime number used for hashing

    def __len__(self) -> int:
        return self._size

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}{self._store}"

    def insert(self, key: str, val: Any) -> None:
        self._validate_key(key)

        if self._size == self.capacity:
            raise HashTableException(
                "Hashmap overflow warning! "
                "To insert an element remove one first."
            )

        override = False
        new_item = MapItem(key, val)
        idx = self._hash(key)

        if self._is_index_available(idx):
            self._store[idx] = new_item
        else:
            override = self._chain_item(idx, new_item)

        if not override:
            self._size += 1

    def get(self, key: str, default: Any = None) -> Any:
        self._validate_key(key)

        match item := self._get_item(key):
            case MapItem():
                return item.value
            case list():
                for subitem in item:
                    if subitem.key == key:
                        return subitem.value
            case _:
                return default

    def remove(self, key: str) -> bool:
        self._validate_key(key)

        idx = self._hash(key)

        match item := self._store[idx]:
            case MapItem():
                self._store[idx] = None
                self._size -= 1
                return True
            case list():
                for i in range(len(item)):
                    if item[i].key == key:
                        item[i] = None
                        self._size -= 1
                        return True
            case _:
                return False

    def has_key(self, key: str) -> bool:
        self._validate_key(key)
        return self._get_item(key) is not None

    def keys(self) -> list[str]:
        return [item.key for item in self._store if item is not None]

    def values(self) -> list[Any]:
        return [item.value for item in self._store if item is not None]

    def is_empty(self) -> bool:
        return self._size < 1

    def _chain_item(self, index: int, new_item: MapItem) -> bool:
        override = False
        match item := self._store[index]:
            case list():
                for i in range(len(item)):
                    if item[i].key == new_item.key:
                        item[i] = new_item
                        override = True
                if not override:
                    item.append(new_item)
            case MapItem():
                if item.key == new_item.key:
                    self._store[index] = new_item
                    override = True
                else:
                    itemlist = [item, new_item]
                    self._store[index] = itemlist
            case _:
                raise HashTableException(
                    f"Items in hashmap must be of type MapItem or list[MapItem], not <{type(item)}>"
                )
        return override

    def _hash(self, key) -> int:
        return hash(key) % self._prime % self.capacity

    def _get_item(self, key: str) -> MapItem | None:
        idx = self._hash(key)
        return self._store[idx]

    def _is_index_available(self, index: int) -> bool:
        return self._store[index] is None

    def _validate_key(self, key: str) -> None:
        if not key or not isinstance(key, str):
            raise HashTableException("Key must be of type str and not empty!")


if __name__ == "__main__":
    hmap = HashTable()
    assert hmap.capacity == HashTable.DEFAULT_CAPACITY
    hmap.insert("hello", 20)
    assert len(hmap) == 1
    assert not hmap.is_empty()
    assert hmap.get("hello") == 20
    assert hmap.keys() == ["hello"]
    assert hmap.values() == [20]
    assert hmap.has_key("hello")
    assert not hmap.has_key("invalid")
    hmap.insert("hello", "new_value")  # override existing value
    assert hmap.get("hello") == "new_value"
    assert len(hmap) == 1
    assert hmap.remove("invalid") is False  # remove non-existent key is False
    assert hmap.remove("hello") is True  # remove existing key is True
    assert len(hmap) == 0
    assert hmap.keys() == []
    assert hmap.values() == []
    assert hmap.remove("hello") is False  # remove non-existent key

    try:
        hmap.insert("", "new_val")
    except Exception as e:
        assert type(e) is HashTableException
        assert str(e) == "Key must be of type str and not empty!"
    else:
        assert False, "HashMapException wasn't triggered"
