def insertion_sort(l: list[int]):
    """
    As simple as a sort can be.

    For each item i, we look behind it by running j backwards (A)

    We shift everything behind it one to the right (B), and when we're done we stick i back there (C)
    """
    for i in range(1, len(l)):
        item: int = l[i]
        j: int = i - 1
        if item < l[j]:
            while j >= 0 and item < l[j]: # A
                l[j + 1] = l[j] # B
                j -= 1
            l[j + 1] = item # C
