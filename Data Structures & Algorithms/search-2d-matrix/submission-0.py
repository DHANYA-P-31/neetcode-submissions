class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_low = 0
        row_high = len(matrix) - 1
        col_low = 0
        col_high = len(matrix[0]) -  1
        row = 0
        while row_low <= row_high:
            row_mid = row_low + (row_high - row_low) // 2
            if matrix[row_mid][col_low] <= target and target<=matrix[row_mid][col_high]:
                row = row_mid
                break
            elif matrix[row_mid][col_low] > target:
                row_high = row_mid - 1
            else:
                row_low = row_mid + 1
        while col_low <= col_high:
            col_mid = col_low + (col_high - col_low) // 2
            if matrix[row][col_mid] < target:
                col_low = col_mid + 1
            elif matrix[row][col_mid] > target:
                col_high = col_mid - 1
            else:
                return True
        return False