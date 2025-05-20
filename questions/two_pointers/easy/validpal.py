class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left_pointer = 0
        right_pointer = len(s) -1

        while left_pointer <= right_pointer:
            if not s[left_pointer].isalnum():
                left_pointer +=1
                continue
            if not s[right_pointer].isalnum():
                right_pointer -=1
                continue

            if s[left_pointer] != s[right_pointer]: 
                return False
            right_pointer-=1
            left_pointer+=1
        
        return True
