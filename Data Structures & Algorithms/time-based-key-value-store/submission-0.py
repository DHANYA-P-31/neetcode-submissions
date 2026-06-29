class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] =[]
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        ans = ""
        low = 0
        high = len(self.store[key]) - 1
        while low <= high:
            mid = low + (high - low)//2
            if self.store[key][mid][0] <= timestamp:
                ans = self.store[key][mid][1]
                low = mid + 1
            else:
                high = mid - 1
            
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)