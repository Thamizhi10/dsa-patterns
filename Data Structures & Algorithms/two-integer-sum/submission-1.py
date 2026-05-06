class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_index={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in diff_index:
                return [diff_index[diff],i]
            else:
                diff_index[nums[i]]=i
        '''nums=sorted(nums)
        i=0
        j=len(nums)-1
        while i<j:
            print(i,j)
            if nums[i]+nums[j]==target:
                return [i,j]
            elif nums[i]+nums[j]>target:
                j-=1
            else:
                i+=1
        return[i,j]'''
        