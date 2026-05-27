class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum=len(nums)
        for i,n in enumerate(nums):
            sum+=i
            sum-=n
        return sum