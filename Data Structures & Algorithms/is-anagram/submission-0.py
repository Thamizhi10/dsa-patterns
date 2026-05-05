class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq_map1={}
        freq_map2={}
        for ch in range(len(s)):
            freq_map1[s[ch]]=freq_map1.get(s[ch],0)+1
            freq_map2[t[ch]]=freq_map2.get(t[ch],0)+1
        return freq_map1==freq_map2

        
        