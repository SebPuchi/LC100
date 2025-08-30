import heapq
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ad_list = {}
        for i in range(numCourses):
            ad_list[i] = []

        for i in range(len(prerequisites)):
            incoming_edge = prerequisites[i][1]
            ad_list[prerequisites[i][0]].append(incoming_edge)

        heap = []
        for key in ad_list:
            heap.append((len(ad_list[key]), key, ad_list[key]))
        heapq.heapify(heap)
        while len(heap) != 0:
            current = heapq.heappop(heap)
            num_incoming, key, edges = current
            print(num_incoming, key, edges)
            if num_incoming != 0:
                return False
            
            for i in range(len(heap)):
                n_num_incoming, n_key, n_edges = heap[i]
                if n_edges and key in n_edges:
                    heap[i] = (n_num_incoming -1, n_key, n_edges)
            heapq.heapify(heap)

        return True
