"""
Day 21 — 2026-11-12
NeetCode 150 — Stack
Problem: Valid Parentheses (LeetCode 20)

Problem statement:
Given a string s containing just the characters '(', ')', '{', '}',
'[' and ']', determine if the input string is valid.

An input string is valid if:
  1. Open brackets must be closed by the same type of brackets.
  2. Open brackets must be closed in the correct order.
  3. Every close bracket has a corresponding open bracket of the same
     type.

Example:
    Input:  s = "()[]{}"
    Output: True

    Input:  s = "(]"
    Output: False

Constraints: 1 <= len(s) <= 10^4, s consists of parentheses only.
"""

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        """
        Stack of expected closing brackets.

        Walk the string once. For every opening bracket, push the
        bracket it must eventually close with. For every closing
        bracket, it must match the top of the stack — pop and check.
        Anything left on the stack at the end means an unclosed opener.

        Pushing the *expected closer* (instead of the opener) makes
        the match check a single comparison, with no lookup table
        needed at pop time.

        Time:  O(n) — one pass over the string.
        Space: O(n) — the stack holds at most n openers.
        """
        stack: List[str] = []
        pairs = {"(": ")", "[": "]", "{": "}"}

        for ch in s:
            if ch in pairs:
                # Remember what this opener must close with.
                stack.append(pairs[ch])
            else:
                # A closer must match the most recent unmatched opener.
                if not stack or stack.pop() != ch:
                    return False

        return not stack


if __name__ == "__main__":
    sol = Solution()

    # Basic valid pairs.
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True

    # Mismatched types.
    assert sol.isValid("(]") is False

    # Correct types, wrong nesting order.
    assert sol.isValid("([)]") is False

    # Nested valid.
    assert sol.isValid("{[]}") is True
    assert sol.isValid("((()))") is True

    # Empty string is valid (nothing to mismatch).
    assert sol.isValid("") is True

    # Unclosed openers.
    assert sol.isValid("(((") is False

    # Closer with no opener.
    assert sol.isValid("]") is False
    assert sol.isValid("())") is False

    # Longer mixed valid string.
    assert sol.isValid("{[()()]}") is True

    print("All Day 21 tests passed!")


# ---------------------------------------------------------------------------
# Pattern notes
# ---------------------------------------------------------------------------
# Pattern: stack for matching / nesting.
#
# What it teaches:
#   A stack is the natural tool whenever the most recent unmatched item
#   is the one that must be resolved next — "last in, first out"
#   mirrors how brackets nest. Pushing the expected closer instead of
#   the opener is the small trick that keeps the code short.
#
# How to recognize it next time:
#   - The problem involves pairs that must match in reverse order
#     (brackets, tags, undo/redo) -> reach for a stack.
#   - "Process in order, but resolve the newest first" is the tell.
#   - Two failure modes to check: a closer with an empty stack, and
#     leftovers on the stack at the end. Both must return False.
#   - This is the first Stack problem in NeetCode 150 — the same stack
#     idea powers Min Stack, Evaluate Reverse Polish Notation, and
#     Daily Temperatures next.
#
# Next up: Stack — Min Stack (LeetCode 155).
