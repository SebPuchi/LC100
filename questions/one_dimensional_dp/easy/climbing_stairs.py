# Recursive Solution
class Solution:
    def memoClimb(self, n, memo):
        if n == 1 or n == 2:
            return memo[n] 
        memo[n] = self.memoClimb(n-1, memo) + self.memoClimb(n-2, memo)
        return memo[n] 


    def climbStairs(self, n: int) -> int:
        memo = {1:1, 2:2} 
    
        return self.memoClimb(n, memo

# Iterative Solution (faster because it doesn't use the call stack)
class Solution(object):
    def memoClimb(self, n, memo):
        if n == 1 or n == 2:
            return memo[n] 
        else:
            for i in range(3, n+1):
                memo[i] = memo[i-1] + memo[i-2]
        return memo[n] 

    def climbStairs(self, n):
        memo = {1:1, 2:2} 
    
        return self.memoClimb(n, memo
