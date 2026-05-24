class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        prefix,suffix=0,0
        for i in range(len(nums)):
            if prefix==0:
                prefix=nums[i]*1
            else:
                prefix=nums[i]*prefix
            if suffix==0:
                suffix=nums[len(nums)-1-i]*1
            else:
                suffix=nums[len(nums)-1-i]*suffix
            res=max(res,prefix,suffix)
        return res