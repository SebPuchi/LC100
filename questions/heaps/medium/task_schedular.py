import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        hash_map = {}
        for i in range(len(tasks)):
            hash_map[tasks[i]] = 1 + hash_map.get(tasks[i], 0)

        for key in hash_map:
            heap.append((0,(hash_map[key], key)))
        heapq.heapify(heap) 

        count = 0
        while len(heap) !=0:
            print(heap)
            if heap[0][0] == 0:
                current = heapq.heappop(heap)
                cooldown, val = current
                letter_count, letter = val
                letter_count-=1
                if letter_count != 0:
                    heapq.heappush(heap, (n+1,(letter_count, letter)))
            for i in range(len(heap)):
                current = heap[i]
                cooldown, val = current
                if cooldown != 0:
                    heap[i] = (cooldown-1, val)
            heapq.heapify(heap) 
            count+=1
        print(count)
