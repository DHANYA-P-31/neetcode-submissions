class Solution:
    def isValid(self, s: str) -> bool:
        d={'}':'{',')':'(',']':'['}
        stack = []
        for i in s:
            if i in d.values():
                stack.append(i)
            elif len(stack) == 0 or  stack.pop() != d[i]:
                    return False
        return len(stack) == 0 
        