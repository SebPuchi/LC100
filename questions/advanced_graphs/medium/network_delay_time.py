import heapq
import math

class Solution:
    def getNeighbors( self, times, node):
        neighbors = []
        for i in range(len(times)):
            if times[i][0] == node:
                neighbors.append((times[i][2], times[i][1]))
        return neighbors


    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}  
        for u, v, w in times:
            if u not in adj:
                adj[u] = []
            adj[u].append((v, w))

        distances = {i: math.inf for i in range(1, n+1)}
        distances[k] = 0
        min_heap = [(0, k)]
        while len(min_heap) != 0:
            curr_dist, u = heapq.heappop(min_heap)
            if curr_dist > distances[u]:
                continue

            neighbors = adj[u] if u in adj else []

            for v, w in neighbors:
                print(v, w)
                if distances[v] > curr_dist + w:
                    distances[v] = curr_dist + w
                    heapq.heappush(min_heap, (distances[v], v))

        for key in distances:
            if distances[key] == math.inf:
                return -1
        return max(distances.values())
