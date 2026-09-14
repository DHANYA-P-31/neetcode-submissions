class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        square = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                v = board[i][j]
                if v == ".":
                    continue
                if v in rows[i] or v in columns[j] or v in square[i//3][j//3]:
                    return False
                rows[i].add(v)
                columns[j].add(v)
                square[i//3][j//3].add(v)
        return True
