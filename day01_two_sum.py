"""
Day 1 - Two Sum (Arrays / Hash Map pattern)
Date: 2026-10-21
Topic: Arrays, Hashing
Course tie-in: ECE 36800 - hash tables & array traversal

Problem:
  Given an array of integers nums and an integer target, return the
  indices of the two numbers that add up to target.
  Assume exactly one solution exists and you may not use the same
  element twice.

Examples:
  nums = [2, 7, 11, 15], target = 9  -> [0, 1]  (2 + 7 = 9)
  nums = [3, 2, 4],      target = 6  -> [1, 2]  (2 + 4 = 6)
  nums = [3, 3],         target = 6  -> [0, 1]
"""


def two_sum_brute(nums, target):
    """O(n^2) time, O(1) space - check every pair."""
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum(nums, target):
    """
    O(n) time, O(n) space - one pass with a hash map.

    Key idea: for each value x, we need its complement (target - x).
    Store values we have already seen (value -> index). If the
    complement is already in the map, we have our pair.
    This trades memory for speed - the classic hashing pattern
    behind a lot of interview problems.
    """
    seen = {}  # value -> index
    for i, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return [seen[complement], i]
        seen[x] = i
    return []


if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
    assert two_sum_brute([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum_brute([3, 2, 4], 6) == [1, 2]
    print("Day 1: all Two Sum tests passed.")

# Notes / pattern to remember:
# - When you need to look up a partner value fast, think hash map.
# - One-pass hashing works when the complement check happens
#   BEFORE inserting the current value (avoids using an element twice).
# - Complexity trade-off: brute force saves memory, hashing saves time.
