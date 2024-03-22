from typing import *


def insertion_sort(l: List[int]):
    for i in range(1, len(l)):
        j: int = i - 1
        item: int = l[i]
        if item < l[j]:
            while j >= 0 and item < l[j]:
                l[j + 1] = l[j]
                j -= 1
            l[j + 1] = item
