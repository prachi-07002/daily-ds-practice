"""
Day 17 - 2026-11-05
NeetCode 150: Sliding Window
Problem: Longest Repeating Character Replacement (LeetCode 424)

Problem statement:
You are given a string `s` and an integer `k`. You can choose
any character of the string and change it to any other uppercase
English character. You can perform this operation at most `k`
times.

Return the length of the longest substring containing the same
letter you can get after performing the above operations.

Example 1:
    Input: s = "ABAB", k = 2
    Output: 4
    Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:
    Input: s = "AABABBA", k = 1
    Output: 4
    Explanation: Replace the one 'A' in the middle with 'B' and
    form "AABBBBA". The substring "BBBB" has the longest
    repeating letters, which is 4. There may be other ways to
    achieve this answer.
"""


def character_replacement(s, k):
    """
    Return the longest substring that can be made all one letter
    with at most `k` replacements.

    Approach: sliding window with a frequency count of the letters
    inside it. A window is valid when the number of characters
    that are NOT the most frequent letter in the window is at most
    `k` -- those are exactly the ones we would replace. If the
    window is invalid, move the left edge right until it is valid
    again. The most frequent count never needs to decrease when
    the window shrinks, because we only care about the longest
    window ever seen. The best window length seen is the answer.

    Time complexity: O(n) -- each character enters and leaves the
    window once, and the frequency map has at most 26 entries.
    Space complexity: O(1) -- the map holds at most 26 letters.
    """
    counts = {}
    left = 0
    max_freq = 0
    best = 0
    for right, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        max_freq = max(max_freq, counts[ch])
        while (right - left + 1) - max_freq > k:
            counts[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best


if __name__ == "__main__":
    # Two replacements turn the whole string into one letter.
    assert character_replacement("ABAB", 2) == 4
    # One replacement makes "BBBB".
    assert character_replacement("AABABBA", 1) == 4
    # No replacements allowed: longest run of one letter.
    assert character_replacement("ABAB", 0) == 1
    # Already uniform: the whole string counts.
    assert character_replacement("AAAA", 2) == 4
    # Empty string has no substring.
    assert character_replacement("", 2) == 0
    # k larger than the string: the whole string counts.
    assert character_replacement("ABC", 5) == 3
    print("All Longest Repeating Character Replacement tests passed!")

# Pattern notes:
# Sliding Window (variable size, frequency map): this is Day 16
# with a budget -- instead of "no duplicates allowed", the rule
# is "at most k characters differ from the majority letter". The
# validity check is `window length - most frequent count <= k`.
# The trick is that `max_freq` never decreases: a shrunken window
# can never beat the best window already found, so there is no
# need to recompute it. Recognize this next time a problem gives
# a small budget of changes to make a window uniform: count
# frequencies, and check replacements needed against the budget.
