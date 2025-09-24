import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # add to min by default:
        # min heap will store negative values to simulate a max heap
        heapq.heappush(self.min_heap, num * -1)

        if self.max_heap and self.min_heap and (self.min_heap[0] * -1) > self.max_heap[0]:
            mini = heapq.heappop(self.min_heap) * -1
            heapq.heappush(self.max_heap, mini)

        if abs(len(self.min_heap) - len(self.max_heap)) > 1:
            if len(self.min_heap) > len(self.max_heap):
                mini = heapq.heappop(self.min_heap) * -1
                heapq.heappush(self.max_heap, mini)
            else:
                maxi = heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, maxi * -1)


    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return -1 * self.min_heap[0]
        elif len(self.min_heap) < len(self.max_heap):
            return self.max_heap[0]
        else:
            return ((-1 * self.min_heap[0]) + self.max_heap[0]) / 2
