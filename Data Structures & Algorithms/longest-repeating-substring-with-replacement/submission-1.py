class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqmap=defaultdict(int)
        l=0
        maxfreq=0
        count=0
        for r in range(len(s)):
            freqmap[s[r]]+=1
            maxfreq=max(maxfreq,freqmap[s[r]])
            while r-l+1>maxfreq+k:
                freqmap[s[l]]-=1
                l+=1
            count=max(count,r-l+1)
        return count