class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        letters = {}
        letters2 = {}

        for i in range(len(s)):
            letters[s[i]] = letters.get(s[i],0) + 1
            letters2[t[i]] = letters2.get(t[i],0) + 1

        return letters == letters2
