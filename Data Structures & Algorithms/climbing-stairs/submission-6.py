class Solution:
    def climbStairs(self, n: int) -> int:
        #my version of bottom up reducingspace complexity
        first=1
        second=2
        if n<=2:
            return n
        for i in range(3, n+1):
            sum=first+second
            if i==n:
                return sum
            first=second
            second=sum