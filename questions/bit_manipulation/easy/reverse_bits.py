class Solution:
    def reverseBits(self, n: int) -> int:
        output = 0

        for i in range(32):
            bit = (1 & (n >> i))
            output += (bit << (31 - i))
        return output
