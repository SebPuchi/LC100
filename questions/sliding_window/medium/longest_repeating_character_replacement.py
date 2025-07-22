# Cleaned up version 
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_count = 0
        left = 0
        result = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            # If we need to replace more than k characters, shrink the window
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)

        return result


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count_hash = {}
        left, right = 0
        
        while left <= right and right < len(s):
            length = right - left

            current_max = (None, -1)
            for i in range(left, right + 1):
                if s[i] in count_hash:
                    count_hash[s[i]] +=1
                else:
                    count_hash[s[i]] = 1
                if count_hash[s[i]] > current_max[1]:
                    current_max = (s[i], count_hash[s[i]])
            if length - current_max[1] <= k
                # replace
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Psuedocode
        # Begin by couting all the freqs of each character within the input s
        # This can be up to 26
        # Withing each window, check to see what the current max freq element is
        # Next check to see if the lenght of the current string allows for k many relpacements 
        # If so, make the repalcmeents, and update, if not, change the position of the pointers to the next

