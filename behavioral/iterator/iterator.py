from collections.abc import Iterator, Iterable
from typing import Any, Union

# https://refactoring.guru/design-patterns/iterator/python/example#lang-features

"""
    iterable -> w/ __iter__ -> return an iterator (list, dict, tuple etc.)
    iterator -> w/ __next__ & __iter__ (inherit from iterable class)

    A collection -> some iterators for certain data structures
    -> extract them to be COMMON funcs to create
    uniquely implemented iterator classes
    The key is to extract those iterator out !
"""


class WordsCollection(Iterable):
    # concrete collection

    def __init__(self, collection: Union[list[Any], None] = None) -> None:
        self._collection = collection or []

    def __getitem__(self, idx: int) -> Any:
        return self._collection[idx]

    def __iter__(self) -> "AlphabeticalOrderIterator":
        """
        The __iter__() method returns the iterator object itself, by default
        we return the iterator in ascending order.
        """
        return AlphabeticalOrderIterator(self)

    def get_reverse_iterator(self) -> "AlphabeticalOrderIterator":
        return AlphabeticalOrderIterator(self, True)

    def add_item(self, item: Any) -> None:
        self._collection.append(item)


class AlphabeticalOrderIterator(Iterator):
    # concrete iterator

    def __init__(self, collection: WordsCollection, reverse: bool = False) -> None:
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if self._reverse else 0

    def __next__(self) -> Any:
        try:
            value = self._collection[self._position]  # __getitem__
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


if __name__ == "__main__":
    collection = WordsCollection()
    collection.add_item("First")
    collection.add_item("Second")
    collection.add_item("Third")

    print("Straight traversal:")
    print("\n".join(collection))
    print("")

    print("Reverse traversal:")
    print("\n".join(collection.get_reverse_iterator()), end="")
