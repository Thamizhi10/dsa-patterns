class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res+=str(len(s))
            res+='#'
            res+=s
        return res

    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            n=0
            while s[i]!='#':
                n=n*10+int(s[i])
                i+=1
            if s[i]=='#':
                word=''
                i+=1
                for j in range(n):
                    word+=s[i]
                    i+=1
                res.append(word)
        return res

            
            

        
            
