class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        n = len(numbers)
        for i in range(n):
            v = target - numbers[i]
            if v in h:
                return [h[v]+1,i+1]
            else:
                h[numbers[i]] = i
        