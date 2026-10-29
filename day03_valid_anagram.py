"""Day 3 - 2026-10-28
NeetCode 150 - Arrays & Hashing
Problem: Valid Anagram (LeetCode 242)

Problem statement:
    Given two strings `s` and `t`, return True if `t` is an anagram of `s`,
    and False otherwise. An anagram is a word formed by rearranging the
    letters of a different word, using all the original letters exactly once.

    Example 1: s = "anagram", t = "nagaram" -> True
    Example 2: s = "rat", t = "car" -> False

    Constraints (LeetCode): s and t consist of lowercase English letters.
"""

from typing import Dict


def is_anagram(s: str, t: str) -> bool:
    """Return True if `t` is an anagram of `s`, else False.

    Approach: character frequency counting.
        Anagrams have exactly the same multiset of characters, so count
        how often each character appears in `s`, then subtract the counts
        for `t`. If every count ends at zero, the strings are anagrams.

    Time complexity: O(n) - one pass over each string, where n is the
        length of the longer string (plus O(1) work over the alphabet).
    Space complexity: O(1) - at most 26 lowercase letters are stored,
        so the count dictionary is bounded by a constant. (For general
        Unicode input it would be O(k) for k distinct characters.)

    Alternative: sort both strings and compare (O(n log n) time,
        O(n) or O(1) extra space depending on the sort). Counting is the
        standard linear-time interview answer.

    Early exit: different lengths can never be anagrams, so return
    False immediately without counting.
    """
    if len(s) != len(t):
        return False

    counts: Dict[str, int] = {}
    for ch in s:
        counts[ch] = counts.get(ch, 0) + 1
    for ch in t:
        if ch not in counts:
            return False
        counts[ch] -= 1
        if counts[ch] < 0:
            return False
    return all(count == 0 for count in counts.values())


if __name__ == "__main__":
    # Example 1 from the problem statement: same letters, rearranged.
    assert is_anagram("anagram", "nagaram") is True
    # Example 2 from the problem statement: different letters.
    assert is_anagram("rat", "car") is False
    # Same letters but different counts: not an anagram.
    assert is_anagram("aab", "abb") is False
    # Edge cases: empty strings are anagrams; different lengths are not.
    assert is_anagram("", "") is True
    assert is_anagram("a", "ab") is False
    # Single character, identical and different.
    assert is_anagram("z", "z") is True
    assert is_anagram("z", "y") is False
    print("All Valid Anagram tests passed!")


# Pattern notes:
# This problem teaches frequency counting with a hash map / array.
# Recognize it next time when a problem asks whether two collections
# contain the same elements with the same multiplicities, regardless of
# order -- anagrams, permutations, and "same multiset" checks are the
# tell. The companion pattern from Day 1/Day 2 (hash map / hash set for
# O(1) lookups) shows up here as counts instead of mere presence:
# when order does not matter but counts do, count frequencies instead
# of sorting. For a fixed small alphabet (like lowercase letters), a
# 26-slot list works in place of a dictionary.
