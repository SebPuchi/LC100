class Solution:
    def valid(self, k, piles, h):
        total_hours = 0
        for pile in piles:
            total_hours += (pile + k - 1) // k  
        return total_hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        k_range = range(1, max(piles) +1)

        left = k_range[0]
        right = k_range[len(k_range) -1]

        valid_k = math.inf

        while left <= right:
            current_k = left + ((right - left) // 2)
            if self.valid(current_k, piles, h) and current_k < valid_k: 
                valid_k = current_k
                right = current_k -1
            
            else: 
                left= current_k + 1
        return valid_k

