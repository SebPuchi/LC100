import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        hash_map = {}
        for i in range(len(tasks)):
            hash_map[tasks[i]] = 1 + hash_map.get(tasks[i], 0)

        for key in hash_map:
            heap.append((-1 * hash_map[key], key))
        heapq.heapify(heap) 

        queue = []
        count = 0
        while len(heap) != 0 or len(queue) != 0:
            if len(heap) > 0:
                num, val = heapq.heappop(heap)
                if num+1 != 0:
                    queue.append((n+count, num+1, val))
            if len(queue) != 0:
                if queue[0][0] == count:
                    cooldown, num, val = queue.pop(0)
                    heapq.heappush(heap, (num, val))
            count+=1
        return(count)

