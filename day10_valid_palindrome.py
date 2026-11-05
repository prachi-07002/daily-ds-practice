"""
Day 10 - 2026-11-04
NeetCode 150: Two Pointers
Problem: Valid Palindrome (LeetCode 125)

Problem statement:
Given a string `s`, return true if it is a palindrome, or false
otherwise. A phrase is a palindrome if, after converting all uppercase
letters into lowercase letters and removing all non-alphanumeric
characters, it reads the same forward and backward.

Example 1:
    Input: s = "A man, a plan, a canal: Panama"
    Output: true
    Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
    Input: s = "race a car"
    Output: false
    Explanation: "raceacar" is not a palindrome.

Example 3:
    Input: s = " "
    Output: true
    Explanation: s is an empty string "" after removing
    non-alphanumeric characters. Since an empty string reads the
    same forward and backward, it is a palindrome.
"""


def is_palindrome(s):
    """
    Return True if `s` is a palindrome after ignoring case and
    non-alphanumeric characters.

    Approach: two pointers, one at each end, walking inward. Skip
    any character that is not alphanumeric, compare the remaining
    pair case-insensitively, and return False at the first mismatch.
    If the pointers meet without a mismatch, the string reads the
    same both ways. No cleaned copy of the string is built, so
    this uses only constant extra space.

    Time complexity: O(n) -- each character is visited at most once.
    Space complexity: O(1) -- only the two pointers are stored.
    """
    left, right = 0, len(s) - 1
    while left < right:
        # Skip non-alphanumeric characters on both sides.
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    # Classic palindrome phrase, with punctuation and mixed case.
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    # Same letters but not a palindrome once spaces are ignored.
    assert is_palindrome("race a car") is False
    # Only a space: nothing left after filtering, so it counts.
    assert is_palindrome(" ") is True
    # Digits count as alphanumeric; punctuation is ignored.
    assert is_palindrome("0P") is False
    assert is_palindrome("No 'x' in Nixon") is True
    assert is_palindrome("") is True
    print("All Valid Palindrome tests passed!")

# Pattern notes:
# Two Pointers (opposite ends): when a problem asks about symmetry,
# ordering, or comparing a sequence from both sides, start one pointer
# at each end and move them toward each other. The key moves here are
# skipping characters that don't matter (non-alphanumerics) and
# normalizing before comparing (lowercase). Recognize this pattern
# next time you see "reads the same forward and backward", a sorted
# array with a target sum, or any check that pairs elements from
# opposite ends -- and remember that skipping/filtering in place
# keeps the solution O(1) in extra space versus building a cleaned copy.
