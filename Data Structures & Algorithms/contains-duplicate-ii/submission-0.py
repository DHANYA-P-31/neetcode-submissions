class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        lastSeen = {}

        n = len(nums)

        for i in range(n):
            if nums[i] in lastSeen and (i - lastSeen[nums[i]]) <= k:
                return True
            lastSeen[nums[i]] = i
        return False