class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        d = {}
        n = len(numbers)
        for i in range(n):
            dif = target - numbers[i]
            if dif in d:
                return [d[dif]+1,i+1]
            d[numbers[i]] = i