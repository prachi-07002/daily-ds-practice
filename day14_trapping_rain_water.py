"""
Day 14 - 2026-10-24
NeetCode 150: Two Pointers
Problem: Trapping Rain Water (LeetCode 42)

Problem statement:
Given `n` non-negative integers representing an elevation map
where the width of each bar is 1, compute how much water it can
trap after raining.

Example 1:
    Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    Output: 6
    Explanation: The above elevation map (black section) is
    represented by array [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1].
    In this case, 6 units of rain water (blue section) are being
    trapped.

Example 2:
    Input: height = [4, 2, 0, 3, 2, 5]
    Output: 9
"""


def trap(height):
    """
    Return the total units of rain water trapped.

    Approach: two pointers at opposite ends, tracking the tallest
    bar seen so far from each side (`left_max`, `right_max`). Water
    above a bar is capped by the shorter of the tallest bars on
    either side, so the side with the smaller max is the limiting
    one -- and on that side the trapped water is exactly
    `max_height - height[pointer]`, because the other side is
    guaranteed to be at least as tall. Process the limiting side,
    add its water, and move that pointer inward.

    Time complexity: O(n) -- each pointer moves at most n steps.
    Space complexity: O(1) -- only the two pointers and the two
    running maxima are stored.
    """
    if not height:
        return 0
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water


if __name__ == "__main__":
    # Classic example: 6 units trapped.
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    # Deep valley between two tall bars.
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    # Flat ground traps nothing.
    assert trap([0, 0, 0]) == 0
    # Monotonic slopes trap nothing.
    assert trap([1, 2, 3, 4]) == 0
    assert trap([4, 3, 2, 1]) == 0
    # Single bowl: two bars of 3 with a 0 between them.
    assert trap([3, 0, 3]) == 3
    print("All Trapping Rain Water tests passed!")

# Pattern notes:
# Two Pointers (opposite ends, running maxima): this is the same
# "move the limiting side" idea as Container With Most Water
# (Day 13), but the pointers carry state -- the tallest bar seen
# from each side. Water at any position is decided by the shorter
# of the two side-maxima, so the side with the smaller max is
# always safe to settle. Recognize this next time a problem asks
# how much fits between heights: think per-position water level
# = min(left max, right max) - height, and find a way to know
# one side's max before the other.
