"""Day 4 - 2026-10-29
NeetCode 150 - Arrays & Hashing
Problem: Group Anagrams (LeetCode 49)

Problem statement:
    Given an array of strings `strs`, group the anagrams together.
    You can return the answer in any order. An anagram is a word formed
    by rearranging the letters of a different word, using all the
    original letters exactly once.

    Example 1: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
        -> [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    Example 2: strs = [""] -> [[""]]
    Example 3: strs = ["a"] -> [["a"]]

    Constraints (LeetCode): 1 <= strs.length <= 10^4,
    0 <= strs[i].length <= 100, strs[i] consists of lowercase
    English letters.
"""

from collections import defaultdict
from typing import Dict, List, Tuple


def group_anagrams(strs: List[str]) -> List[List[str]]:
    """Group anagrams together, returning the groups in any order.

    Approach: canonical key via character counts.
        Anagrams share exactly the same multiset of letters, so a
        26-length count tuple is a perfect grouping key: every anagram
        of a word maps to the same key, and no non-anagram does. Build
        the key for each word and append the word to its group in a
        hash map, then return the groups.

    Time complexity: O(n * k) - n words, each scanned once to count
        its k letters (the 26-slot tuple itself is constant size).
    Space complexity: O(n * k) - storing all words in the groups, plus
        one key per distinct anagram class.

    Alternative: sort each word and use the sorted word as the key.
        That is simpler to write but costs O(n * k log k) time, so the
        count-tuple key is the standard interview answer.

    Edge cases: an empty string gets the all-zeros key and forms its
        own group; an empty input list returns an empty list.
    """
    groups: Dict[Tuple[int, ...], List[str]] = defaultdict(list)
    for word in strs:
        counts = [0] * 26
        for ch in word:
            counts[ord(ch) - ord("a")] += 1
        groups[tuple(counts)].append(word)
    return list(groups.values())


def _normalized(groups: List[List[str]]) -> List[List[str]]:
    """Sort each group and sort the groups, for order-insensitive tests."""
    return sorted(sorted(group) for group in groups)


if __name__ == "__main__":
    # Example 1 from the problem statement (order-insensitive).
    assert _normalized(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == [
        ["ate", "eat", "tea"],
        ["bat"],
        ["nat", "tan"],
    ]
    # Example 2: a single empty string is its own group.
    assert group_anagrams([""]) == [[""]]
    # Example 3: a single letter is its own group.
    assert group_anagrams(["a"]) == [["a"]]
    # No anagrams at all: every word is alone.
    assert _normalized(group_anagrams(["abc", "def", "ghi"])) == [
        ["abc"],
        ["def"],
        ["ghi"],
    ]
    # All words are anagrams of each other: one group.
    assert _normalized(group_anagrams(["listen", "silent", "enlist"])) == [
        ["enlist", "listen", "silent"]
    ]
    # Empty input: no groups.
    assert group_anagrams([]) == []
    # Repeated words stay together in the same group.
    assert _normalized(group_anagrams(["eat", "eat", "tea"])) == [
        ["eat", "eat", "tea"]
    ]
    print("All Group Anagrams tests passed!")


# Pattern notes:
# This problem teaches grouping by a canonical key with a hash map.
# Recognize it next time when a problem asks you to bucket items that
# are "the same up to rearrangement / transformation": find a key that
# is identical for equivalent items and different otherwise, then let
# a hash map do the grouping in one pass. It builds directly on Day 3
# (Valid Anagram): there the count told you whether two words matched;
# here the same count becomes the key that groups many words at once.
# When order does not matter but counts do, count frequencies -- and
# when you need to group by those counts, use the count tuple as the
# dictionary key instead of sorting each word.
