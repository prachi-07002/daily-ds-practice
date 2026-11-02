"""
Day 7 - 2026-11-01
NeetCode 150: Arrays & Hashing
Problem: Product of Array Except Self (LeetCode 238)

Problem statement:
Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a
32-bit integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

Example 1:
    Input: nums = [1, 2, 3, 4]
    Output: [24, 12, 8, 6]

Example 2:
    Input: nums = [-1, 1, 0, -3, 3]
    Output: [0, 0, 9, 0, 0]

Follow-up: Can you solve the problem in O(1) extra space complexity?
(The output array does not count as extra space for space complexity
analysis.)
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Prefix/suffix product approach, O(n) time and O(1) extra space
        (excluding the output array).

        Idea: answer[i] = (product of all elements before i)
                           * (product of all elements after i).
        First pass (left to right) fills answer[i] with the prefix product
        of everything before i. Second pass (right to left) multiplies in
        the suffix product of everything after i, reusing the output array
        so no extra prefix/suffix arrays are needed.

        Why no division? Division breaks on zeros (e.g. nums containing 0
        would need special-casing for one zero vs. two zeros), and the
        problem explicitly forbids it. Prefix/suffix products handle zeros
        naturally.

        Time complexity:  O(n) - two linear passes over nums.
        Space complexity: O(1) extra - only the output array plus two
                          running-product variables.
        """
        n = len(nums)
        answer = [1] * n

        # Prefix pass: answer[i] = product of nums[0..i-1]
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        # Suffix pass: multiply answer[i] by product of nums[i+1..n-1]
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


if __name__ == "__main__":
    sol = Solution()

    # Example 1 from the problem statement.
    assert sol.productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]

    # Example 2: zeros in the input - only the position of the zero gets
    # a nonzero answer (the product of everything else).
    assert sol.productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]

    # Two elements: each answer is just the other element.
    assert sol.productExceptSelf([2, 5]) == [5, 2]

    # Two zeros: every product except self still includes a zero.
    assert sol.productExceptSelf([0, 0, 3]) == [0, 0, 0]

    # Single element: product of an empty set of "other" elements is 1.
    assert sol.productExceptSelf([7]) == [1]

    # All negatives: sign flips work out via the two passes.
    assert sol.productExceptSelf([-2, -3, -4]) == [12, 8, 6]

    print("All Day 7 tests passed!")

"""
Pattern notes:
- Pattern: prefix/suffix products (a special case of "precompute running
  aggregates from both directions").
- Recognize it next time: a problem asks for something about "every element
  except the current one" (or "everything to the left/right of i") and
  forbids the naive shortcut (here, division). When the answer for index i
  cleanly splits into a left contribution and a right contribution, compute
  each side in its own linear pass and combine.
- The O(1)-extra-space trick is the same one used elsewhere: reuse the
  output array for the first pass, then fold the second pass into it.
  Watch for the follow-up phrasing "output array does not count" - it is a
  strong hint that this two-pass reuse is the intended solution.
- Contrast with yesterday's length-prefix encoding: both problems reward
  storing just enough extra information (a length, a running product) so a
  single pass in each direction does the whole job.
"""
