from typing import TypeVar, Optional, Generic

T = TypeVar("T")
class Array(Generic[T]):
    _default_initial_size: int = 10

    _internal_array: Optional[list[T]] = None

    _num_objects: int = 0
    def __init__(self, initial_size: int = _default_initial_size):
        self._internal_array = [None] * initial_size

    def size(self) -> int:
        return self._num_objects

    def append(self, object: T):
        """Add at end"""
        if self._num_objects == len(self._internal_array):
            self._grow()
        self._internal_array[self._num_objects] = object
        self._num_objects += 1

    def find(self, object: T) -> int:
        """Returns index of obj, -1 if no"""
        for i in range(self.size):
            if self.get(i) == object:
                return i
        return -1

    @property
    def size(self) -> int:
        return self._num_objects
    def insert(self, index: int, object: T):
        """Insert at ..."""
        if self.size + 1 >= len(self._internal_array):
            self._grow()
        if index < 0:
            index = index % self.size
        for i in range(self.size, index, -1):
            self._internal_array[i] = self._internal_array[i - 1]
        self._internal_array[index] = object
        self._num_objects += 1

    def set(self, index, object: T):
        self._raise_if_bad_index(index)
        self._internal_array[index] = object

    def append(self, object: T):
        """Insert at end"""
        if self.size == len(self._internal_array):
            self._grow()
        self._internal_array[self.size] = object
        self._num_objects += 1

    def get(self, index: int):
        self._raise_if_bad_index(index)
        if index < 0:
            index = index % self.size
        return self._internal_array[index]

    def delete_all(self, object: T) -> bool:
        while (i := self.find(object)) != -1:
            for j in range(i, self.size - 1):
                self.set(j, self.get(j + 1))
            self._internal_array[j + 1] = None
            self._num_objects -= 1
    def _grow(self):
        """Yes, python doesn't need to do any of this."""
        new_array: list[T] = [None] * len(self._internal_array) * 2
        for i in range(self.size):
            new_array[i] = self._internal_array[i]
        self._internal_array = new_array

    def __iter__(self):
        for i in range(self.size):
            yield self.get(i)

    def _raise_if_bad_index(self, index: int):
        if index >= self.size or index < (-1 * self.size):
            raise IndexError(f"Index {index} out of bounds")
