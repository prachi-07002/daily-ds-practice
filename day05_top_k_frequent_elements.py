"""
Day 5 - 2026-10-30
NeetCode 150: Arrays & Hashing
Problem: Top K Frequent Elements (LeetCode #347)

Problem statement:
    Given an integer array nums and an integer k, return the k most
    frequent elements. You may return the answer in any order.

    Example 1:
        Input: nums = [1, 1, 1, 2, 2, 3], k = 2
        Output: [1, 2]
    Example 2:
        Input: nums = [1], k = 1
        Output: [1]

    Constraints (LeetCode): 1 <= nums.length <= 10^5, -10^4 <= nums[i] <= 10^4,
    k is in the range [1, number of unique elements in the array].
    Your algorithm's time complexity must be better than O(n log n),
    where n is the array's size.
"""

from collections import Counter
from typing import List


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    """Return the k most frequent elements in nums.

    Approach: bucket sort by frequency.
      1. Count each value's frequency with a hash map: O(n).
      2. Drop each value into a bucket indexed by its frequency.
         Frequencies range from 1 to n, so there are n + 1 buckets: O(n).
      3. Walk the buckets from highest frequency down, collecting
         values until we have k of them: O(n) worst case.

    Time complexity: O(n) -- counting, bucketing, and the final scan
        are each linear. This beats the O(n log k) heap approach and
        the O(n log n) sort-by-frequency approach.
    Space complexity: O(n) -- the frequency map and the buckets
        together hold at most n entries.
    """
    counts = Counter(nums)

    # buckets[f] = list of values that appear exactly f times.
    buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)

    result: List[int] = []
    for freq in range(len(nums), 0, -1):
        for num in buckets[freq]:
            result.append(num)
            if len(result) == k:
                return result
    return result


if __name__ == "__main__":
    # Example 1 from the statement.
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    # Example 2 from the statement: a single element.
    assert top_k_frequent([1], 1) == [1]
    # All elements equally frequent: any k of them is valid.
    assert len(top_k_frequent([4, 5, 6, 7], 2)) == 2
    assert set(top_k_frequent([4, 5, 6, 7], 2)) <= {4, 5, 6, 7}
    # Negative numbers and a clear winner.
    assert top_k_frequent([-1, -1, -2, -2, -2, 3], 1) == [-2]
    # k equals the number of unique elements: return everything.
    assert sorted(top_k_frequent([9, 9, 8], 2)) == [8, 9]
    print("All Day 5 tests passed!")


# Pattern notes:
#   This problem teaches FREQUENCY COUNTING + BUCKET SORT.
#   - Whenever a problem asks for "most/least frequent" or "top k",
#     start by counting frequencies in a hash map -- that turns the
#     array problem into a frequency problem.
#   - Frequencies are bounded by n, so they can be used as bucket
#     indices. Bucket sort converts an O(n log n) sort into O(n)
#     whenever the sort key lives in a small, known range.
#   - Recognize it next time: "top k frequent" / "sort by frequency"
#     / "k most common" -> count, then bucket (or heap if you only
#     need the heap's O(n log k) bound). The heap version keeps a
#     min-heap of size k keyed by frequency; the bucket version is
#     faster here because frequencies are bounded by n.
