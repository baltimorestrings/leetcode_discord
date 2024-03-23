from typing import TypeVar, Optional, Generic

T = TypeVar("Comparable")
class OrderedArray(Generic[T]):
    """
    Simple ordered array. Has an inner array it grows, mimicing what the actual array clases do.

    Insertion/Deletion are O(N) thanks to reshuffling needed
    finding is O(log N), random access is O(1)
    """
    _default_initial_size: int = 10

    _internal_array: Optional[list[T]] = None

    _num_objects: int = 0
    def __init__(self, initial_size: int = _default_initial_size):
        self._internal_array = [None] * initial_size

    def size(self) -> int:
        return self._num_objects

    def _find_insertion_point(self, object_to_find: T) -> int:
        """ binary search O(log N)

        returns insertion point if it doesn't find the target
        """
        left: int = 0
        right: int = self.size - 1
        while left <= right:
            mid = (left + right) // 2
            if (val := self.get(mid)) == object_to_find:
                return mid
            elif val <= object_to_find:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def find(self, object_to_find: T) -> int:
        """ public search, returns -1 if element isn't present """
        result: int = self._find_insertion_point(object_to_find)
        if self.get(result) != object_to_find:
            return -1
        return result


    def add(self, object: T):
        if self.size == len(self._internal_array):
            self._grow()
        insertion_index: int = self._find_insertion_point(object)
        self._internal_array[insertion_index + 1:]



    @property
    def size(self) -> int:
        return self._num_objects

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

breakpoint()
