class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        for i in range(32):
            count += (1 & (n >> i))

        return count
        
        
