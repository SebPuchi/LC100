class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {len(s) : 1}

        for i in range(len(s)-1, -1, -1):
            if int(s[i]) == 0:
                memo[i] = 0
                continue
            else:
                memo[i] = memo[i+1]

            if i+1 < len(s) and (int(s[i]) == 1 or (int(s[i]) == 2 and int(s[i+1]) <=6)):
                memo[i] += memo[i+2] 
            
        return memo[0]

