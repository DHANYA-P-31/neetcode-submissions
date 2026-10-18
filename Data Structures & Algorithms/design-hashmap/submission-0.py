class MyHashMap:

    def __init__(self):
        self.mymapkey = []
        self.mymapvalue = []

    def put(self, key: int, value: int) -> None:
        if key not in self.mymapkey:
            self.mymapkey.append(key)
            self.mymapvalue.append(value)
        else:
            i = self.mymapkey.index(key)
            self.mymapvalue[i] = value

    def get(self, key: int) -> int:
        if key in self.mymapkey:
            i = self.mymapkey.index(key)
            return self.mymapvalue[i]
        else:
            return -1        

    def remove(self, key: int) -> None:
        if key in self.mymapkey:
            i = self.mymapkey.index(key)
            self.mymapkey.pop(i)
            self.mymapvalue.pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)