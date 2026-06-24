class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        at = set()
        pc = set()
        m = len(heights)
        n = len(heights[0])
        def check(r,c,v,prev):
            if r < 0 or c < 0 or c >= n or r >= m or (r,c) in v or heights[r][c] < prev:
                return
            v.add((r,c))
            check(r-1,c,v,heights[r][c])
            check(r+1,c,v,heights[r][c])
            check(r,c-1,v,heights[r][c])
            check(r,c+1,v,heights[r][c])
            
        for i in range(m):
            check(i,0,pc,heights[i][0])
            check(i,n-1,at,heights[i][n-1])
        for j in range(n):
            check(0,j,pc,heights[0][j])
            check(m-1,j,at,heights[m-1][j])
        ans = []
        for i in range(m):
            for j in range(n):
                if (i,j) in pc and (i,j) in at:
                    ans.append([i,j])
        return ans