class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def toNum(n):
            ans = 0
            for i in n:
                if i == '0':
                    val = 0
                elif i == '1':
                    val = 1
                elif i == '2':
                    val = 2
                elif i == '3':
                    val = 3
                elif i == '4':
                    val = 4
                elif i == '5':
                    val = 5
                elif i == '6':
                    val = 6
                elif i == '7':
                    val = 7
                elif i == '8':
                    val = 8
                elif i == '9':
                    val = 9
                ans = ans * 10 + val
            return ans
        return str(toNum(num1)*toNum(num2))


