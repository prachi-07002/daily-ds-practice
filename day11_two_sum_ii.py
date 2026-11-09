"""
Day 11 - 2026-11-08
NeetCode 150: Two Pointers
Problem: Two Sum II - Input Array Is Sorted (LeetCode 167)

Problem statement:
Given a 1-indexed array of integers `numbers` that is already sorted
in non-decreasing order, find two numbers such that they add up to a
specific `target` number. Return the indices of the two numbers,
`index1` and `index2`, added by one as an integer array
`[index1, index2]` of length 2.

The tests are generated such that there is exactly one solution. You
may not use the same element twice. Your solution must use only
constant extra space.

Example 1:
    Input: numbers = [2, 7, 11, 15], target = 9
    Output: [1, 2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1,
    index2 = 2. We return [1, 2].

Example 2:
    Input: numbers = [2, 3, 4], target = 6
    Output: [1, 3]
    Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1,
    index2 = 3. We return [1, 3].

Example 3:
    Input: numbers = [-1, 0], target = -1
    Output: [1, 2]
    Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 1,
    index2 = 2. We return [1, 2].
"""


def two_sum(numbers, target):
    """
    Return the 1-indexed positions of the two numbers that sum to
    `target`.

    Approach: two pointers, one at each end. Because the array is
    sorted, the sum of the pointed-to pair tells us which way to
    move: if the sum is too small, the left number must grow, so
    move the left pointer right; if the sum is too large, the right
    number must shrink, so move the right pointer left. When the
    sum matches, the pointers are the answer (converted to
    1-indexed). Exactly one solution is guaranteed, so the loop
    always finds it.

    Time complexity: O(n) -- each pointer moves at most n steps.
    Space complexity: O(1) -- only the two pointers are stored.
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1
    return []  # Unreachable when exactly one solution exists.


if __name__ == "__main__":
    # Classic example: the pair sits at the two ends of the search.
    assert two_sum([2, 7, 11, 15], 9) == [1, 2]
    # Pair uses the first and last elements.
    assert two_sum([2, 3, 4], 6) == [1, 3]
    # Negative numbers work the same way; sorting still orders them.
    assert two_sum([-1, 0], -1) == [1, 2]
    # Pair is in the middle of the array.
    assert two_sum([5, 25, 75], 100) == [2, 3]
    # Duplicate values: the two 4s are distinct positions.
    assert two_sum([1, 2, 4, 4, 5], 8) == [3, 4]
    # Two-element array, the only possible pair.
    assert two_sum([3, 5], 8) == [1, 2]
    print("All Two Sum II tests passed!")

# Pattern notes:
# Two Pointers (opposite ends, sorted input): when the input is
# sorted and the question is about a pair with a target sum, start
# one pointer at each end and let the sorted order steer you -- the
# sum being too small means the left value must grow, too large
# means the right value must shrink. This is the same opposite-ends
# idea as Valid Palindrome (Day 10), but here the pointers move
# based on a comparison instead of skipping characters. It beats a
# hash map here because it needs O(1) extra space, and it only
# works because the array is sorted -- on an unsorted array (Two
# Sum, Day 1) the hash map is the right tool instead. Recognize
# this pattern next time you see "sorted array + pair + target".
