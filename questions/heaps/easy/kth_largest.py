import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kth_largest = k
        heapq.heapify(nums)
        self.stream = nums

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val) 
        while len(self.stream) > self.kth_largest:
            heapq.heappop(self.stream)
        return self.stream[0]
