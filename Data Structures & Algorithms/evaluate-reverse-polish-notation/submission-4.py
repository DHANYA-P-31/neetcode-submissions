class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        val = []
        for t in tokens:
            if t.lstrip("-").isdigit():
                val.append(int(t))
            else:
                b = val.pop()
                a = val.pop()
                if t == "+":
                    v = a+b
                elif t == "-":
                    v = a-b
                elif t == "*":
                    v = a*b
                elif t == "/":
                    v = int(a/b)
                val.append(v)
        return val[-1]

                
