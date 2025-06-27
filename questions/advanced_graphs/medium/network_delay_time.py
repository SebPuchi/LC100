import heapq

class Solution:
    def findNode(self, times, node):
        for i in range(len(times)):
            if times[i][0] == node:
                return times[i]

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        start_node = self.findNode(times, k)
        print("START NODE", start_node)
        distances = {start_node[0]: 0}
        priority_queue = []
        priority_queue.append(start_node) 
        while len(priority_queue) != 0:
            current = priority_queue.pop()
            if current:
                priority_queue.append(self.findNode(times, current[1]))
                if current[1] in distances:
                    if current[2] + distances[current[0]] < distances[current[1]]:
                        distances[current[1]] = current[2] + distances[current[0]]
                else:
                    distances[current[1]] = current[2] + distances[current[0]]
                heapq.heapify(priority_queue)
                print(distances)
        
        for i in range(1, n+1):
            print(i)
            if i not in distances.keys():
                return -1
        return max(distances.values())
