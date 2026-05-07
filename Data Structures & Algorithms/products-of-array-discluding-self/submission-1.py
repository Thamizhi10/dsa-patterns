class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix,postfix=1,1
        for i in range(0,len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        for j in range(len(nums)-1,-1,-1):
            res[j]*=postfix
            postfix=postfix*nums[j]
        return res  


