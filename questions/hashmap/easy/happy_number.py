class Solution:
    def isHappy(self, n: int) -> bool:
        tracked_numbers = set()
        number = str(n)
        while True:
            summation = 0
            for i in number:
                n = int(i)
                squared = n**2
                summation+= squared
            if summation in tracked_numbers:
                return False
            tracked_numbers.add(summation)
            if summation == 1:
                return True
            number = str(summation)
