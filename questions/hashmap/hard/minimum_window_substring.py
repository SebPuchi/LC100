import math
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_hash = {}
        s_hash = {}
        for let in t:
            t_hash[let] = 1 + t_hash.get(let, 0)
            s_hash[let] = 0

        left, right = 0, 0 

        # results
        min_length = math.inf
        r_left = -1
        r_right = -1

        have, need = 0, len(t_hash)
        while right < len(s):
            print("s_hash", s_hash)
            c = s[right]
            print("s hash", s_hash)
            if c in t_hash:
                s_hash[c] += 1
                if s_hash[c] == t_hash[c]:
                    have +=1


            while have == need:
                if (right - left + 1) < min_length:
                    min_length = right - left + 1
                    r_left, r_right = left, right
            
                if s[left] in t_hash:
                    s_hash[s[left]] -= 1
                    if s_hash[s[left]] < t_hash[s[left]]:
                        have -= 1
                left += 1

            right+=1
        return(s[r_left: r_right+1])

