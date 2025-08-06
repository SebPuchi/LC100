class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        memoTwo = {}

        j = 0
        for i in range(len(text1)):
            current_char = text1[i]

            j_stash = j
            while j < len(text2):
                if current_char == text2[j]:
                    memo[current_char] = 1
                    j+=1
                    break
                j+=1
            if (j == len(text2)):
                j = j_stash
            print("J", j)
            print("J_STASH", j_stash)


        j = 0
        for i in range(len(text2)):
            current_char = text2[i]

            j_stash = j
            while j < len(text1):
                if current_char == text1[j]:
                    memoTwo[current_char] = 1
                    j+=1
                    break
                j+=1
            if (j == len(text1)):
                j = j_stash
        
        print(memo)
        print(memoTwo)
    
        max_first = sum(memo.values()) if(len(memo.keys()) !=0) else  0
        max_second = sum(memoTwo.values()) if(len(memoTwo.keys()) !=0) else  0
        return  max(max_first, max_second
