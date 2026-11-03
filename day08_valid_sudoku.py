"""
Day 8 - 2026-11-02
NeetCode 150: Arrays & Hashing
Problem: Valid Sudoku (LeetCode 36)

Problem statement:
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need
to be validated according to the following rules:

1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the
   digits 1-9 without repetition.

Note:
- A Sudoku board (partially filled) could be valid but is not
  necessarily solvable.
- Only the filled cells need to be validated.

Example 1:
    Input: board =
    [["5","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
    Output: true

Example 2:
    Input: board =
    [["8","3",".",".","7",".",".",".","."],
     ["6",".",".","1","9","5",".",".","."],
     [".","9","8",".",".",".",".","6","."],
     ["8",".",".",".","6",".",".",".","3"],
     ["4",".",".","8",".","3",".",".","1"],
     ["7",".",".",".","2",".",".",".","6"],
     [".","6",".",".",".",".","2","8","."],
     [".",".",".","4","1","9",".",".","5"],
     [".",".",".",".","8",".",".","7","9"]]
    Output: false
    Explanation: The same number 8 appears twice in the top-left
    3 x 3 sub-box (and in the first column).
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        One-pass hash set approach: O(1) time and space in practice
        (the board is always 9 x 9, so at most 81 cells are visited).

        Idea: for every filled cell, record three keys in one set --
        (row, digit), (column, digit), and (3x3 box, digit). The box
        index is (row // 3, col // 3). If any key is seen twice, some
        digit repeats in a row, column, or box, and the board is
        invalid. Empty cells (".") are skipped, since only filled
        cells need validation.

        Time: O(81) = O(1) for a fixed 9 x 9 board.
        Space: O(81) = O(1) for the same reason.
        """
        seen = set()
        for row in range(9):
            for col in range(9):
                digit = board[row][col]
                if digit == ".":
                    continue
                row_key = ("row", row, digit)
                col_key = ("col", col, digit)
                box_key = ("box", row // 3, col // 3, digit)
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)
        return True


if __name__ == "__main__":
    sol = Solution()

    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert sol.isValidSudoku(valid_board) is True

    # Same board, but the top-left box now has two 8s -> invalid.
    invalid_box = [row[:] for row in valid_board]
    invalid_box[0][0] = "8"
    assert sol.isValidSudoku(invalid_box) is False

    # Duplicate digit in a single row -> invalid.
    invalid_row = [row[:] for row in valid_board]
    invalid_row[0][1] = "5"
    assert sol.isValidSudoku(invalid_row) is False

    # Duplicate digit in a single column -> invalid.
    invalid_col = [row[:] for row in valid_board]
    invalid_col[1][0] = "5"
    assert sol.isValidSudoku(invalid_col) is False

    # A completely empty board is valid (nothing to contradict).
    empty_board = [["."] * 9 for _ in range(9)]
    assert sol.isValidSudoku(empty_board) is True

    print("All Valid Sudoku tests passed!")


"""
Pattern notes:
- Pattern: single-pass validation with hash sets / encoded keys.
  This is the same "seen set" idea from Contains Duplicate (Day 2),
  extended to three simultaneous constraints by tagging each key with
  which constraint it belongs to (row / column / box).
- How to recognize it next time: a problem asks "is this grid (or
  sequence) valid?" with a small fixed set of rules about repeats --
  track one key per rule per value in a single set and fail fast on
  the first duplicate. The box trick (row // 3, col // 3) is the
  reusable bit: integer division groups cells into blocks, which also
  shows up in grid/block problems beyond Sudoku.
- Watch out: only filled cells are checked ("." is skipped), and a
  valid board need not be solvable -- validity is not solving.
"""
