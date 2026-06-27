class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.lstrip("-").isdigit():
                stack.append(i)
            else:
                b = int(stack.pop())
                a = int(stack.pop())
                if i == "+":
                    stack.append(str(a+b))
                elif i == "-":
                    stack.append(str(a-b))
                elif i == "*":
                    stack.append(str(a*b))
                elif i == "/":
                    stack.append(str(int(a/b)))
        return int(stack[-1])
        