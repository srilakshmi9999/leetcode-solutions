partition array for maximum sum 



class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        n = len(A)
        dp =[0] * (n + 1)
        for i in range(1, n + 1):
            currMax = 0
            for k in range(1, min(i, K) + 1):
                currMax = max(currMax, A[i - k])
                dp[i] = max(dp[i], dp[i - k] + currMax * k)
        return dp[n]