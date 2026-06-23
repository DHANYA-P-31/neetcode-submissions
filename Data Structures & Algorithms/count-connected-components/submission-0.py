class DSU:
    def __init__(self,n):
        self.parent = [i for i in range(n)]
        self.rank = [1]*n
    
    def find(self, n):
        c= n
        while c!=self.parent[c]:
            self.parent[c] = self.parent[self.parent[c]]
            c = self.parent[c]
        return c
    
    def union(self,u,v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return False
        if self.rank[v] > self.rank[u]:
            u,v = v,u
        self.parent[v] = u
        self.rank[u] += self.rank[v]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        res = n
        for u,v in edges:
            if dsu.union(u,v):
                res -=1
        return res