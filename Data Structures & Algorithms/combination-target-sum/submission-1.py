class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(i,current,total):
            if total==target:
                res.append(current.copy())
            for j in range(i,len(nums)):
                if total+nums[j]>target:
                    return
                current.append(nums[j])
                total+=nums[j]
                dfs(j,current,total)
                current.pop()    
                total-=nums[j]     
        dfs(0,[],0)
        return res