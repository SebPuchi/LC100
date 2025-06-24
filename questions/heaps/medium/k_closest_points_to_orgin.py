import heapq
import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hash_map = {}
        heap = [] 
        for i in range(len(points)):
            x, y = points[i][0], points[i][1]
            dist = math.sqrt((abs(x)**2 + abs(y)**2))
            heap.append(dist)
            if dist in hash_map:
                hash_map[dist].append((x,y))
            else: 
                hash_map[dist] = [(x,y)]
        
        heapq.heapify(heap)
        answer_arr = []
        print(hash_map)
        for i in range(k):
            dist = heapq.heappop(heap) 
            answer_arr.append(list(hash_map[dist].pop()))
        return answer_arr

