"""
Day 12 - 2026-10-22
NeetCode 150: Two Pointers
Problem: 3Sum (LeetCode 15)

Problem statement:
Given an integer array `nums`, return all the triplets
`[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and
`j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

Example 1:
    Input: nums = [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
    Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1, 0, 1] and [-1, -1, 2].

Example 2:
    Input: nums = [0, 1, 1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

Example 3:
    Input: nums = [0, 0, 0]
    Output: [[0, 0, 0]]
    Explanation: The only possible triplet sums up to 0.
"""


def three_sum(nums):
    """
    Return all unique triplets that sum to zero.

    Approach: sort the array first, then fix one element at index
    `i` and run the Two Sum II two-pointer scan on the rest of the
    array for the target `-nums[i]`. Sorting makes duplicates sit
    next to each other, so they are skipped: skip a repeated value
    of `nums[i]`, and after finding a triplet, skip repeated values
    at both pointers before moving on. Stop early when `nums[i] > 0`,
    because a sorted array can no longer sum to zero from there.

    Time complexity: O(n^2) -- n choices of `i`, each with a linear
    two-pointer scan.
    Space complexity: O(1) extra besides the output (sorting is
    in place).
    """
    nums = sorted(nums)
    result = []
    n = len(nums)
    for i in range(n - 2):
        if nums[i] > 0:
            break
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left, right = i + 1, n - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return result


if __name__ == "__main__":
    # Classic example: two distinct triplets.
    assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
    # No triplet sums to zero.
    assert three_sum([0, 1, 1]) == []
    # All zeros: exactly one triplet, no duplicates.
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
    # Duplicates in the input must not produce duplicate triplets.
    assert three_sum([-2, 0, 0, 2, 2]) == [[-2, 0, 2]]
    # Empty and tiny inputs have no triplets at all.
    assert three_sum([]) == []
    assert three_sum([1, 2]) == []
    print("All 3Sum tests passed!")

# Pattern notes:
# Two Pointers, extended: 3Sum is Two Sum II (Day 11) with one
# element fixed. Sort first, then for each `i` run opposite-end
# pointers on the remainder for target `-nums[i]`. The new skill
# is duplicate handling: sorted order puts equal values side by
# side, so skipping a value you have already used as `nums[i]`
# (or at either pointer) guarantees unique triplets without a set.
# Recognize this next time a problem asks for unique combinations
# that sum to a target -- sort, fix one, two-pointer the rest,
# and skip duplicates at every level.
