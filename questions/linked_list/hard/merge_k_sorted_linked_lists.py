# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyNode = ListNode()
        heap = []

        for i, node in enumerate(lists):
            if node != None:
                heap.append((node.val, i, node))
        heapq.heapify(heap)

        current = dummyNode
        while heap:
            min_val, i,  node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next != None:
                heapq.heappush(heap, (node.next.val, i, node.next))
        return dummyNode.next
