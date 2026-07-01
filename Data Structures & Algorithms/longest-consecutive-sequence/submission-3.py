class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h=set(nums)
        res,lres=0,0
        for n in nums:
            res=1
            start=n
            while start+1 in h:
                res+=1
                start+=1
            if res>lres:
                lres=res
        return lres