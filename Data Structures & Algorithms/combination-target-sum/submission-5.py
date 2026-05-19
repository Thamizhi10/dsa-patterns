class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def dfs(i,current,total):
            if total==target: #base condition
                res.append(current.copy())
                return
            for j in range(i,len(nums)):
                if total+nums[j]>target: #prunind condition
                    return
                current.append(nums[j]) # making choice
                dfs(j,current,total+nums[j]) #exploring choice
                current.pop() #undo choice
        dfs(0,[],0)
        return res