"""
Day 13 - 2026-10-23
NeetCode 150: Two Pointers
Problem: Container With Most Water (LeetCode 11)

Problem statement:
You are given an integer array `height` of length `n`. There are
`n` vertical lines drawn such that the two endpoints of the `i`th
line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such
that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
    Input: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    Output: 49
    Explanation: The above vertical lines are represented by array
    [1, 8, 6, 2, 5, 4, 8, 3, 7]. In this case, the max area of
    water the container can hold is 49.

Example 2:
    Input: height = [1, 1]
    Output: 1
"""


def max_area(height):
    """
    Return the maximum water area between any two lines.

    Approach: two pointers at opposite ends. The area of a pair is
    `min(height[left], height[right]) * (right - left)`. The width
    only shrinks as the pointers move inward, so the only way to
    beat the current best is to find a taller line -- and the taller
    line can only be found by moving the pointer at the *shorter*
    line, because moving the taller one keeps the height capped by
    the shorter side while the width shrinks. So at each step,
    record the area, then move the shorter pointer inward.

    Time complexity: O(n) -- each pointer moves at most n steps.
    Space complexity: O(1) -- only the two pointers and the best
    area are stored.
    """
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        width = right - left
        if height[left] < height[right]:
            best = max(best, height[left] * width)
            left += 1
        else:
            best = max(best, height[right] * width)
            right -= 1
    return best


if __name__ == "__main__":
    # Classic example: lines 8 and 7, distance 7, height 7.
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    # Two lines of height 1, width 1.
    assert max_area([1, 1]) == 1
    # Tallest lines are adjacent in the middle.
    assert max_area([1, 2, 1]) == 2
    # Descending heights: best is the first two lines.
    assert max_area([5, 4, 3, 2, 1]) == 6
    # Ascending heights: best is the last two lines.
    assert max_area([1, 2, 3, 4, 5]) == 6
    # Best pair is not at the ends.
    assert max_area([2, 3, 4, 5, 18, 17, 6]) == 17
    print("All Container With Most Water tests passed!")

# Pattern notes:
# Two Pointers (opposite ends, greedy move): unlike Two Sum II
# (Day 11) and 3Sum (Day 12), the pointers here do not move by
# comparing a sum to a target -- they move by a greedy rule. The
# area is capped by the shorter line, so only moving the shorter
# pointer can ever improve the answer; moving the taller one can
# only shrink the width. Recognize this next time a problem asks
# for a max over pairs with a width-times-height shape: start at
# the ends, keep the best, and always move the limiting side.
