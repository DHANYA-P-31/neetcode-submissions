class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.mat = matrix
        n = len(matrix) 
        m = len(matrix[0]) 
        for i in range(n):
            s = 0
            for j in range(m):
                s+=matrix[i][j]
                self.mat[i][j] = s
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        s = 0
        for i in range(row1,row2+1):
            if col1 == 0:
                s+=self.mat[i][col2]
            else:
                s += self.mat[i][col2] - self.mat[i][col1-1]
        return s

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)