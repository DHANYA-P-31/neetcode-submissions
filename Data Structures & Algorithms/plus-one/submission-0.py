class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = -1
        n = len(digits)
        ans = digits[index]+1
        while index>-n:
            if ans<10:
                digits[index] = ans
                return digits
            else:
                digits[index] = ans%10
                index -= 1
                ans = digits[index]+ ans//10
        if index == -n and ans<10:
            digits[index] = ans
        else:
            digits[index] = ans%10
            digits.insert(0,ans//10)
        return digits

        