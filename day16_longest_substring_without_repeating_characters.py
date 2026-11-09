"""
Day 16 - 2026-10-27
NeetCode 150: Sliding Window
Problem: Longest Substring Without Repeating Characters (LeetCode 3)

Problem statement:
Given a string `s`, find the length of the longest substring
without duplicate characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
    Notice that the answer must be a substring, "pwke" is a
    subsequence and not a substring.
"""


def length_of_longest_substring(s):
    """
    Return the length of the longest substring with all unique
    characters.

    Approach: sliding window with a set of the characters inside
    it. The right edge expands one character at a time; if the new
    character is already in the set, the left edge moves right --
    dropping characters -- until the duplicate is gone. The set
    always holds exactly the current window's characters, so its
    size is the window length, and the best size seen is the
    answer. Each character enters and leaves the window once.

    Time complexity: O(n) -- each character is added and removed
    at most once.
    Space complexity: O(min(n, alphabet)) -- the set holds the
    current window's distinct characters.
    """
    seen = set()
    left = 0
    best = 0
    for right, ch in enumerate(s):
        while ch in seen:
            seen.remove(s[left])
            left += 1
        seen.add(ch)
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    # Classic example: "abc" repeats, longest is 3.
    assert length_of_longest_substring("abcabcbb") == 3
    # All the same character: longest is 1.
    assert length_of_longest_substring("bbbbb") == 1
    # "wke" is the longest; "pwke" is not a substring.
    assert length_of_longest_substring("pwwkew") == 3
    # Empty string has no substring.
    assert length_of_longest_substring("") == 0
    # No repeats at all: the whole string counts.
    assert length_of_longest_substring("abcdef") == 6
    # The longest window sits at the end.
    assert length_of_longest_substring("abba") == 2
    print("All Longest Substring Without Repeating Characters tests passed!")

# Pattern notes:
# Sliding Window (variable size, set membership): the window is
# "the longest valid stretch ending here". Expanding the right
# edge can only break validity one way -- a duplicate -- and
# shrinking the left edge until the duplicate leaves restores it.
# The set makes the duplicate check O(1). Recognize this next
# time a problem asks for the longest subarray/substring with a
# "no duplicates" or "at most K of X" rule: grow the right edge,
# shrink the left edge until the rule holds again, and track the
# best window seen.
