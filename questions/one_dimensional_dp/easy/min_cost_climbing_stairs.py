class Solution:
    def memoStairs(self, step, cost, memo):
        print(step, memo)
        if step == 1 or step ==0:
            return memo[step]
        current_cost = 0 if len(cost) == step else cost[step]

        memo[step] = current_cost + min(self.memoStairs(step-1, cost, memo), self.memoStairs(step-2,cost, memo))
        print(step, memo)
        return memo[step]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo= {0: cost[0],1: cost[1] }
        return self.memoStairs(len(cost), cost, memo)
       
