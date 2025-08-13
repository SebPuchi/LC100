class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        result = 0
        left = 0
        right = 0
        while right < len(s):
            count[s[right]] = 1 + count.get(s[right], 0)
            if ((right-left) +1) - max(count.values()) <= k:
                result = max(result, (right-left) + 1)
                right+=1
            else:
                count[s[left]]-=1
                left+=1
                right+=1
            print(count)
            print(result)
        return(result)

