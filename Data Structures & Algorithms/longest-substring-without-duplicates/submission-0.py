class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap={}
        l=0
        count=0
        for r in range(len(s)):
            if s[r] in hashmap:
                l=max(hashmap[s[r]]+1,l)
            hashmap[s[r]]=r
            count=max(count,r-l+1)
        return count


