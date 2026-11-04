"""
Day 9 - 2026-11-03
NeetCode 150: Arrays & Hashing
Problem: Longest Consecutive Sequence (LeetCode 128)

Problem statement:
Given an unsorted array of integers `nums`, return the length of the
longest consecutive elements sequence. You must write an algorithm
that runs in O(n) time.

Example 1:
    Input: nums = [100, 4, 200, 1, 3, 2]
    Output: 4
    Explanation: The longest consecutive elements sequence is
    [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
    Input: nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    Output: 9

Example 3:
    Input: nums = []
    Output: 0
"""


def longest_consecutive(nums):
    """
    Return the length of the longest consecutive sequence in `nums`.

    Approach: put every number in a hash set for O(1) lookups, then
    only start counting from numbers that begin a sequence -- that is,
    numbers whose predecessor (n - 1) is NOT in the set. From each
    start, walk forward (n + 1, n + 2, ...) while the numbers exist.
    Each number is visited at most twice (once as a candidate start
    check, once inside a single forward walk), so the total work is
    linear even though the input is unsorted -- no sorting needed.

    Time complexity: O(n) -- one pass to build the set, plus at most
    one forward walk per element across all starts combined.
    Space complexity: O(n) -- the set holds every element of `nums`.
    """
    num_set = set(nums)
    longest = 0

    for num in num_set:
        # Only start a sequence here if num - 1 is absent; otherwise
        # this number is in the middle of a sequence counted elsewhere.
        if num - 1 not in num_set:
            length = 1
            current = num
            while current + 1 in num_set:
                current += 1
                length += 1
            longest = max(longest, length)

    return longest


if __name__ == "__main__":
    # LeetCode examples.
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
    assert longest_consecutive([]) == 0
    # Duplicates must not inflate the length.
    assert longest_consecutive([1, 2, 2, 3]) == 3
    # Negatives and a single element.
    assert longest_consecutive([-1, -2, 0, 1]) == 4
    assert longest_consecutive([42]) == 1
    print("All tests passed!")


"""
Pattern notes:
- Pattern: hash set + "sequence start" trick. When a problem asks for
  consecutive runs in an unsorted array in O(n) time, sorting (O(n log n))
  is the trap -- a set gives O(1) membership checks instead.
- Recognize it next time: "longest consecutive", "unsorted array", and
  an O(n) requirement together point here. The key insight is to only
  count from a true start (n - 1 missing), which keeps the work linear
  instead of re-walking the same sequence from every element.
- This closes out NeetCode's Arrays & Hashing section: the next section
  is Two Pointers, starting with Valid Palindrome (LeetCode 125).
"""
