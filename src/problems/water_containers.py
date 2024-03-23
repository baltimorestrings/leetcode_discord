def maxArea(heights: List[int]) -> int:
    """
    A is the vertical side of the water, B is the width.

    Algorithm is to simply sliding window, track the max, and just keep moving in the shorter side (C)
    """
    left: int = 0
    right: int = len(heights) - 1

    max_area = min(heights[left], heights[right]) * (right - left)
    """         A                                   B              """

    while left < right:
        max_area = max(
            min(heights[left], heights[right]) * (right - left),  # A
            max_area  # B
        )
        if heights[left] < heights[right]:  # C
            left += 1
        else:
            right -= 1
    return max_area
