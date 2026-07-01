class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        i,j=0,len(height)-1
        leftmax,rightmax=height[i],height[j]
        res=0
        while i<j:
            if leftmax<rightmax:
                i+=1
                leftmax=max(leftmax,height[i])
                res+=leftmax-height[i]
            else:
                j-=1
                rightmax=max(rightmax,height[j])
                res+=rightmax-height[j]
        return res
