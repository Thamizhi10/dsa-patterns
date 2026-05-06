class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=defaultdict(int)
        freq=[[] for i in range(len(nums)+1)]
        for n in nums:
            count[n]+=1
        for n,c in count.items():
            freq[c].append(n)
        res=[]
        for f in range(len(freq)-1,0,-1):
            for num in freq[f]:
                res.append(num)
                if len(res)==k:
                    return res

