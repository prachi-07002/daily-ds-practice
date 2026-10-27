"""Day 2 - 2026-10-26
NeetCode 150 - Arrays & Hashing
Problem: Contains Duplicate (LeetCode 217)

Problem statement:
    Given an integer array `nums`, return True if any value appears at
    least twice in the array, and return False if every element is distinct.

    Example 1: nums = [1, 2, 3, 1] -> True
    Example 2: nums = [1, 2, 3, 4] -> False
    Example 3: nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] -> True
"""

from typing import List


def contains_duplicate(nums: List[int]) -> bool:
    """Return True if any value appears at least twice, else False.

    Approach: hash set for O(1) membership checks.
        Walk the array once, remembering every value seen so far.
        If the current value is already in the set, we found a duplicate
        and can stop early. Otherwise add it and keep going.

    Time complexity: O(n) - one pass over the array, O(1) set lookups.
    Space complexity: O(n) - in the worst case (all distinct) the set
        holds every element.

    Alternative: sort first (O(n log n) time, O(1) extra space if sorting
        in place) and check adjacent pairs. The hash-set version is the
        standard interview answer because it is linear time.
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


if __name__ == "__main__":
    # Example from the problem statement: duplicate 1.
    assert contains_duplicate([1, 2, 3, 1]) is True
    # All distinct: no duplicate.
    assert contains_duplicate([1, 2, 3, 4]) is False
    # Multiple duplicates scattered through the array.
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    # Edge cases: empty array and a single element have no duplicates.
    assert contains_duplicate([]) is False
    assert contains_duplicate([5]) is False
    # Duplicate only at the very end.
    assert contains_duplicate([1, 2, 3, 4, 5, 5]) is True
    # Negative numbers work the same way.
    assert contains_duplicate([-1, -2, -1]) is True
    print("All Contains Duplicate tests passed!")

# Pattern notes:
#   This is the hash-set / seen-set pattern: when a problem asks "have
#   I seen this before?" (duplicates, pairs summing to a target, anagrams
#   by frequency), reach for a set (membership) or dict (counts/indices)
#   instead of a nested loop. The brute-force O(n^2) pairwise check is
#   the trap this pattern avoids.
#   How to recognize it next time: the question is about repetition,
#   uniqueness, or "does X already exist?" over a single pass - and you
#   only need existence, not order or position. If you also need the
#   index of the first occurrence (like Two Sum), upgrade the set to a
#   dict mapping value -> index. That one upgrade connects Day 1 and
#   Day 2: same pattern, different payload.
