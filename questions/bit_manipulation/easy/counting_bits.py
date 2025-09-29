class Solution:
    def countBits(self, n: int) -> List[int]:
        memo = [0] * (n +1)
        prefix = 1
        for i in range(1, n+1):
            if prefix * 2 == i:
                prefix = i
            memo[i] = 1 + memo[i - prefix]
        return memo

