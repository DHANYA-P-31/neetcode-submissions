class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(','}':'{',']':'['}
        stack =[]
        for c in s:
            if c in d:
                if stack and d[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False