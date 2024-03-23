def _merge_sort(left: list[int], right: list[int]) -> list[int]:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge(l: list[int]) -> list[int]:
    if len(l) < 2:
        return l
    middle = len(l) // 2
    left = merge(l[:middle])
    right = merge(l[middle:])
    return _merge_sort(left, right)
