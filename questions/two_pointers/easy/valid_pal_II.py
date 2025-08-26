class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        skipped = False
        valid_pal = True
        while left <= right:
            if not s[left].isalnum():
                left +=1
                continue
            if not s[right].isalnum():
                right -=1
                continue
            if s[left] == s[right]:
                left+=1
                right-=1
                continue
            elif s[left + 1] == s[right] and not skipped:
                skipped = True
                left+=1
                continue
            elif s[right - 1] == s[left] and not skipped:
                skipped = True
                right-=1
                continue
            valid_pal = False
            break


        if valid_pal == False:
            valid_pal = True
            skipped = False
            left = 0
            right = len(s) - 1
            while left <= right:
                if not s[left].isalnum():
                    left +=1
                    continue
                if not s[right].isalnum():
                    right -=1
                    continue
                if s[left] == s[right]:
                    left+=1
                    right-=1
                    continue
                elif s[right - 1] == s[left] and not skipped:
                    skipped = True
                    right-=1
                    continue
                elif s[left + 1] == s[right] and not skipped:
                    skipped = True
                    left+=1
                    continue
                valid_pal = False
                break
         
        return(valid_pal)


