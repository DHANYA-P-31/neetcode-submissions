class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for src,dest in prerequisites:
            indegree[dest] += 1
            adj[src].append(dest)
        q = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)
        finished = 0
        while q:
            p = q.popleft()
            finished += 1
            for n in adj[p]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        return finished == numCourses