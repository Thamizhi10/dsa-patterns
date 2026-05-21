class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        return max(self.helper(nums[:-1]),self.helper(nums[1:]))
    
    def helper(self, arr: List[int]) -> int:
        if len(arr)==1:
            return arr[0]
        money=[0]*len(arr)
        money[0]=arr[0]
        money[1]=max(arr[0],arr[1])
        for i in range(2,len(arr)):
            money[i]=max(money[i-1],arr[i]+money[i-2])
        return money[-1]
