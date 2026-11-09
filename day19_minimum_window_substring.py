"""
Day 19 - 2026-11-07
NeetCode 150: Sliding Window
Problem: Minimum Window Substring (LeetCode 76)

Problem statement:
Given two strings `s` and `t`, return the minimum window
substring of `s` such that every character in `t` (including
duplicates) is included in the window. If there is no such
substring, return the empty string "".

Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes
    'A', 'B', and 'C' from string t.

Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.

Example 3:
    Input: s = "a", t = "aa"
    Output: ""
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return "".
"""


def min_window(s, t):
    """
    Return the shortest substring of `s` containing all
    characters of `t` (with duplicates), or "" if none exists.

    Approach: sliding window with two count maps. First count
    what `t` needs. Expand the right edge, adding characters to
    the window's counts; track how many distinct needed letters
    are satisfied (`formed`). Once every needed letter is
    satisfied, the window is valid -- then shrink the left edge
    as far as possible while it stays valid, recording the
    shortest valid window seen. Each character enters and leaves
    the window once.

    Time complexity: O(n + m) -- one pass over `s` (n) plus
    counting `t` (m).
    Space complexity: O(1) -- the maps hold at most the alphabet
    (here treated as bounded; in general O(distinct chars)).
    """
    if not t:
        return ""
    need = {}
    for ch in t:
        need[ch] = need.get(ch, 0) + 1
    window = {}
    formed = 0
    required = len(need)
    left = 0
    best = (float("inf"), 0, 0)  # (length, start, end)
    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        if ch in need and window[ch] == need[ch]:
            formed += 1
        while formed == required:
            if right - left + 1 < best[0]:
                best = (right - left + 1, left, right)
            left_ch = s[left]
            window[left_ch] -= 1
            if left_ch in need and window[left_ch] < need[left_ch]:
                formed -= 1
            left += 1
    if best[0] == float("inf"):
        return ""
    return s[best[1]:best[2] + 1]


if __name__ == "__main__":
    # Classic example: "BANC" is the shortest window with A, B, C.
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    # The whole string is the window.
    assert min_window("a", "a") == "a"
    # t needs two a's but s has only one.
    assert min_window("a", "aa") == ""
    # Window must include duplicates from t.
    assert min_window("ab", "bba") == ""
    # Multiple valid windows: the shortest wins.
    assert min_window("abca", "ac") == "ca"
    # t is a single character.
    assert min_window("xyzabc", "b") == "b"
    print("All Minimum Window Substring tests passed!")

# Pattern notes:
# Sliding Window (variable size, "formed" counter): the classic
# hard sliding-window problem, and the capstone of Days 16-18.
# The `formed` counter is the key idea -- instead of comparing
# whole maps on every step, count how many distinct letters have
# met their required frequency, and shrink the window the moment
# all of them are met. Expand until valid, shrink until just
# barely valid, record the best. Recognize this next time a
# problem asks for the smallest substring containing a set of
# required characters: need map, window map, formed counter.
