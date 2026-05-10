class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq_map=defaultdict(int)
        for num in nums:
            freq_map[num]=freq_map[num]+1
            if freq_map[num]>1:
                return True
        return False
        
        