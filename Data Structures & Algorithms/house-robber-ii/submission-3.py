class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[1:]),self.helper(nums[:-1]))
    def helper(self, arr: List[int]) -> int:
        first,second=0,0
        for a in arr:
            curr=max(second,a+first)
            first=second
            second=curr
        return second