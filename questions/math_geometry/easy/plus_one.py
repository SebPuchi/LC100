class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry == 1:
                if digits[i] < 9:
                    digits[i] = digits[i] +1
                    carry = 0
                else:
                    digits[i] = 0
        if carry == 1:
            return [1] + digits
        else:
           return digits
