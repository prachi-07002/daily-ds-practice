"""
Day 6 - 2026-10-31
NeetCode 150 - Arrays & Hashing
Problem: Encode and Decode Strings (LeetCode #271)

Problem statement:
    Design an algorithm to encode a list of strings to a single string.
    The encoded string is then decoded back to the original list of strings.
    Implement `encode(strs)` and `decode(s)`. Strings may contain any
    characters, including the delimiter you choose, so a naive
    "join with a separator" approach is NOT correct on its own.

    Example:
        Input: ["neet", "code", "love", "you"]
        Encoded: "4#neet4#code4#love3#you"
        Decoded: ["neet", "code", "love", "you"]

Solution approach:
    Length-prefix encoding. Before each string, write its length followed
    by a delimiter ('#'): "<len>#<string>". Because the decoder reads the
    length first, it knows exactly how many characters belong to the next
    string, so any character (including '#', digits, or spaces) inside a
    string is safe, and empty strings work too (encoded as "0#").

    Time complexity: O(n) for both encode and decode, where n is the total
    number of characters across all strings.
    Space complexity: O(n) for the encoded string / decoded list output.
"""


class Solution:
    def encode(self, strs: list[str]) -> str:
        """Encode a list of strings to a single string."""
        encoded_parts = []
        for s in strs:
            encoded_parts.append(f"{len(s)}#{s}")
        return "".join(encoded_parts)

    def decode(self, s: str) -> list[str]:
        """Decode a single string back to the original list of strings."""
        result = []
        i = 0
        while i < len(s):
            # Read the length prefix up to the '#'.
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            # The string itself is the next `length` characters.
            result.append(s[j + 1: j + 1 + length])
            i = j + 1 + length
        return result


if __name__ == "__main__":
    sol = Solution()

    # Test 1: the classic example.
    strs = ["neet", "code", "love", "you"]
    assert sol.decode(sol.encode(strs)) == strs
    assert sol.encode(strs) == "4#neet4#code4#love3#you"

    # Test 2: strings containing the delimiter and digits must survive.
    tricky = ["hello#world", "123", "a#b#c", ""]
    assert sol.decode(sol.encode(tricky)) == tricky

    # Test 3: empty list and single empty string edge cases.
    assert sol.decode(sol.encode([])) == []
    assert sol.decode(sol.encode([""])) == [""]

    # Test 4: strings with spaces and punctuation.
    mixed = ["hello world!", "a,b;c", "line1\nline2"]
    assert sol.decode(sol.encode(mixed)) == mixed

    print("All Day 6 tests passed!")


"""
Pattern notes:
    Pattern: length-prefix (framing) encoding -- the same idea behind
    network protocols and file formats, where a message is prefixed with
    its length so the receiver knows where it ends.

    What this problem teaches:
      - A delimiter alone is ambiguous when the payload can contain it;
        pairing a length with the delimiter removes the ambiguity.
      - Parsing with a moving index (read length, skip '#', slice exactly
        `length` characters) is a reusable two-pointer / index-walking
        technique for decoding framed data.

    How to recognize it next time:
      - Whenever you must serialize variable-length items into one string
        (or stream) and deserialize them losslessly, reach for
        length-prefix framing instead of a bare separator.
      - Watch for edge cases: empty strings, empty lists, and payloads
        that contain your delimiter or digits.
"""
