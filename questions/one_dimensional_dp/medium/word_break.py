class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        memo[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for word in wordDict:
                if s[i: i+len(word)] == word:
                    print(i+len(word))
                    if i+len(word) < len(s):
                        if memo[i+len(word)]:
                            memo[i] = memo[i+len(word)]
                            break
                    else:
                        memo[i] = True
            if i not in memo:
                memo[i] = False
            print(memo)
        return memo[0]
