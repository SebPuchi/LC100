import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {} 
        for i in range(amount+1):
            memo[i] = math.inf
        memo[0] = 0

        for i in range(1, amount+1):
            for j in range(len(coins) -1, -1, -1):
                if i - coins[j] >= 0:
                    remainder = i - coins[j]
                    memo[i] = min(memo[i], memo[remainder] + 1)

        return memo[amount] if memo[amount] != math.inf else -1
