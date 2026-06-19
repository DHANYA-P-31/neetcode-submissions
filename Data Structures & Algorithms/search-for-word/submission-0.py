class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        idx = set()
        n = len(board)
        m = len(board[0])
        def check(r,c,i):
            if i == len(word):
                return True
            
            if r < 0 or c < 0 or r>=n or c >= m or board[r][c] != word[i] or (r,c) in idx:
                return False
            
            idx.add((r,c))
            res = check(r+1,c,i+1) or check(r-1,c,i+1) or check(r,c+1,i+1) or check(r,c-1,i+1)
            idx.remove((r,c))
            return res

        for i in range(n):
            for j in range(m):
                if check(i,j, 0):
                    return True
        return False
