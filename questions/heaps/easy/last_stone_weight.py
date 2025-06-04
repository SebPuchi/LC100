import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)): 
            stones[i] = -1 * stones[i]
        heapq.heapify(stones)
        print(stones)
        while len(stones) > 1: 
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)
            if x == y:
                continue
            elif y > x:
                heapq.heappush(stones, x - y)
            print(stones)
        if stones: 
            return stones[0] * -1
        else:
            return 0

