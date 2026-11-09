"""
Day 18 - 2026-11-06
NeetCode 150: Sliding Window
Problem: Permutation in String (LeetCode 567)

Problem statement:
Given two strings `s1` and `s2`, return `True` if `s2` contains
a permutation of `s1`, or `False` otherwise.

In other words, return `True` if one of `s1`'s permutations is
the substring of `s2`.

Example 1:
    Input: s1 = "ab", s2 = "eidbaooo"
    Output: True
    Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
    Input: s1 = "ab", s2 = "eidboaoo"
    Output: False
"""


def check_inclusion(s1, s2):
    """
    Return True if any permutation of `s1` appears as a substring
    of `s2`.

    Approach: a permutation is just a rearrangement, so what
    matters is the count of each character, not their order.
    Slide a fixed-size window of length `len(s1)` across `s2`
    and compare character counts. Count the characters of `s1`
    once, then maintain the window's counts as it moves: add the
    entering character, remove the leaving one. If the two count
    maps match at any position, a permutation is present.

    Time complexity: O(n) -- one pass over `s2`, with O(1) map
    comparisons (at most 26 letters).
    Space complexity: O(1) -- two count maps of at most 26
    letters each.
    """
    if len(s1) > len(s2):
        return False
    need = {}
    for ch in s1:
        need[ch] = need.get(ch, 0) + 1
    window = {}
    for i, ch in enumerate(s2):
        window[ch] = window.get(ch, 0) + 1
        if i >= len(s1):
            left_ch = s2[i - len(s1)]
            window[left_ch] -= 1
            if window[left_ch] == 0:
                del window[left_ch]
        if window == need:
            return True
    return False


if __name__ == "__main__":
    # "ba" is a permutation of "ab" inside s2.
    assert check_inclusion("ab", "eidbaooo") is True
    # No arrangement of "ab" appears as a substring.
    assert check_inclusion("ab", "eidboaoo") is False
    # s1 equals s2 exactly.
    assert check_inclusion("abc", "abc") is True
    # s1 longer than s2: impossible.
    assert check_inclusion("abcd", "abc") is False
    # A repeated-letter permutation.
    assert check_inclusion("aab", "baa") is True
    # Single character, present.
    assert check_inclusion("a", "zaz") is True
    print("All Permutation in String tests passed!")

# Pattern notes:
# Sliding Window (fixed size, frequency match): this is the
# fixed-size cousin of Days 16-17. Instead of growing and
# shrinking, the window is exactly `len(s1)` wide and slides one
# step at a time, updating two counts per step. A permutation is
# a frequency signature, so comparing count maps is the whole
# test -- order never matters. Recognize this next time a problem
# asks whether a rearrangement of one string appears inside
# another: fixed window, count characters, compare maps.
