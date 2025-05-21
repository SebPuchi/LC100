class Solution(object):
    def isValid(self, s):
        open_chars = ['[', '(', '{']
        close_chars = [']', ')', '}']
        
        stack = []
        for char in s:
            print(char)
            if char not in open_chars and char not in close_chars:
                print("first Fail")
                return False

            if char in open_chars:
                stack.append(char)

            if char in close_chars:
                if stack and stack[-1]== open_chars[close_chars.index(char)]:
                    stack.pop()
                else:
                    print("second Fail")
                    return False

        if len(stack) != 0:
            return False
        return True
