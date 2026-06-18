class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxvol = 0
        i = 0 
        j = len(height)-1
        while(i<j):
            h = min(height[i],height[j])
            b = j - i
            vol = h*b
            maxvol = max(maxvol,vol)
            if h== height[i]:
                i+=1
            else:
                j-=1
        return maxvol
        
        