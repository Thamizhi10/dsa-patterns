class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[0]*len(nums)
        suffix=[0]*len(nums)
        prefix[0]=1
        suffix[len(nums)-1]=1
        res=[0]*len(nums)
        for i in range(1,len(nums)):
            prefix[i]=prefix[i-1]*nums[i-1]
        for j in range(len(nums)-2,-1,-1):
            suffix[j]=suffix[j+1]*nums[j+1]
        for r in range(0,len(nums)):
            res[r]=prefix[r]*suffix[r]
        return res

