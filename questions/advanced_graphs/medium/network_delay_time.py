import heapq

class Solution:
    def findNode(self, times, node):
        valid_nodes = []
        for i in range(len(times)):
            if times[i][0] == node:
                valid_nodes.append(times[i])
        
        return valid_nodes

    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        start_node = self.findNode(times, k)
        print("START NODE", start_node)
        distances = {start_node[0]: 0}
        priority_queue = []
        priority_queue.append(start_node) 
        while len(priority_queue) != 0:
            current = priority_queue.pop()
            if current:
                neigbors = self.findNode(times, current[1])
                for i in range(len(neigbors)):
                    priority_queue.append(neigbors[i])

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

# Another broken attempt :/ 
import heapq

class Solution:

    def getTime(self, times, source, dest):
        for i in range(len(times)):
            if times[i][0] == source and times[i][1] == dest:
                return times[i][2]
    def getNeighbors(self, times, node):
        neighbors = []
        for i in range(len(times)):
            if times[i][0] == node:
                neighbors.append(times[i][1])
        return neighbors
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = {k: 0}
        priority_queue = []
        priority_queue.append((0, k)) 
        while len(priority_queue) != 0:
            dist, current = priority_queue.pop()
            neighbors = self.getNeighbors(times, current)
            print(neighbors)
            for neigh in neighbors:
                weight = self.getTime(times, current, neigh)
                if neigh in distances:
                    if distances[current] + weight < distances[neigh]:
                        distances[neigh] = distances[current] + weight
                else:
                    distances[neigh] = distances[current] + weight
                priority_queue.append((distances[current]+ weight, neigh)) 
                heapq.heapify(priority_queue)
        
        for i in range(1, n+1):
            print(i)
            if i not in distances.keys():
                return -1
        return max(distances.values())

