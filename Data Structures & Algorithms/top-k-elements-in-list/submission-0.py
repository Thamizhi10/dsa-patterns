class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap=defaultdict(int)
        for n in nums:
            hashmap[n]+=1
        #count=sorted(hashmap.values())
        count=[]
        for n,freq in hashmap.items():
            count.append([freq,n])
        count.sort()
        #print(hashmap)
        result=[]
        while len(result)<k:
            result.append(count.pop()[1])
        return result
