class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_hash = {}
        s2_hash = {}

        for i in range(len(s1)):
            s1_hash[s1[i]] = 1 + s1_hash.get(s1[i], 0)
        print(s1_hash)

        left = 0
        right = 0
        while right < len(s2):
            if s2[right] in s1_hash.keys():
                s2_hash[s2[right]] = 1 + s2_hash.get(s2[right], 0)
                while s2_hash[s2[right]] > s1_hash[s2[right]]:
                    s2_hash[s2[left]] -=1
                    left+=1 
                right+=1
            else:
                s2_hash = {}
                left+=1 
                right = left

            if s1_hash == s2_hash:
                return True
        return False
