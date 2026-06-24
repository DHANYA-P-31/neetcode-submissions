class Solution:
    def foreignDictionary(self, words):
        adj = {c:set() for w in words for c in w}
        indegree = {c:0 for c in adj}
        
        n = len(words)
        for i in range(n-1):
            w1 = words[i]
            w2 = words[i+1]
            minlen = min(len(w1),len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]:
                return ""
            for j in range(minlen):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]] += 1
                    break
        
        q = deque([c for c in indegree if indegree[c] == 0])
        ans = []
        while q:
            p = q.popleft()
            ans.append(p)
            for n in adj[p]:
                indegree[n] -= 1
                if indegree[n] == 0:
                    q.append(n)
        
        if len(ans) != len(indegree):
            return ""
        return "".join(ans)
