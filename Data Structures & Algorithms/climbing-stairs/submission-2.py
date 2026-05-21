class Solution:
    def climbStairs(self, n: int) -> int:
        #bottom up dp
        dp=[0]*(n+1)
        for i in range(0,n+1):
            if i<=2:
                dp[i]=i
            else:
                dp[i]=dp[i-1]+dp[i-2]
        return dp[n]