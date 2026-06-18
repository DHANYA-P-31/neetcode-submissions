class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [set() for _ in range(9)]
        column =  [set() for _ in range(9)]
        boxes = [[set() for _ in range(3)] for _ in range(3)]
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val.isdigit():
                    val = int(val)
                    if val not in row[i]:
                        row[i].add(val)
                    else:
                        return False
                    if val not in column[j]:
                        column[j].add(val)
                    else:
                        return False
                    box_r, box_c = i // 3, j // 3
                    if val not in boxes[box_r][box_c]:
                        boxes[box_r][box_c].add(val)
                    else:
                        return False
        return True