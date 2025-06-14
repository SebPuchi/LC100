class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_array = []
        first = 0
        second = 0
        max_len = 0
        current_max = 0
        while first < len(s) and second != len(s):
            if s[second] not in char_array:
                char_array.append(s[second])
                current_max+=1
                if current_max > max_len:
                    max_len = current_max
                second+=1
            else:
                while s[first] != s[second]:
                    char_array.remove(s[first])
                    first+=1
                    current_max-=1
                char_array.remove(s[first])
                first+=1
                current_max-=1
        return max_len 

