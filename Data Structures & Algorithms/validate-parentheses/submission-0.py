class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoopen={')':'(','}':'{',']':'['}
        for c in s: 
            if c not in closetoopen:
                stack.append(c)
            else:
                if stack and stack[-1]==closetoopen[c]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False
