class Solution:
    def climbStairs(self, n: int) -> int:
        #my version of bottom up reducing space complexity
        first=1
        second=2
        if n<=2:
            return n
        for i in range(3, n+1):
            curr=first+second
            first=second
            second=curr
        return curr