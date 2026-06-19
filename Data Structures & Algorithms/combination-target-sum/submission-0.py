class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def find(i,cur,total):
            if total == target:
                ans.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return
            cur.append(candidates[i])
            find(i,cur,total+candidates[i])
            cur.pop()
            find(i+1,cur,total)
        find(0,[],0)
        return ans