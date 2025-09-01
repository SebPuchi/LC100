class Solution:
    def longestPalindrome(self, s: str) -> str:
        left = 0
        right = 0
        curr_max = 0
        for z in range(len(s)):
            i, j = z, z
            while (i>=0 and j < len(s)) and s[i] == s[j] :
                if (j - i + 1) > curr_max:
                    curr_max = (j - i + 1)
                    left = i
                    right = j
                i -=1
                j +=1

            i, j = z, z+1
            while (i>=0 and j < len(s)) and s[i] == s[j] :
                if (j - i + 1) > curr_max:
                    curr_max = (j - i + 1)
                    left = i
                    right = j
                i -=1
                j +=1
        output = ""
        for x in range(left, right+1):
            output+= s[x]
        return(output)



         


        
