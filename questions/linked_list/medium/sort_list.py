# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_tracker = []

        if head:
            # collect values
            current = head
            while current:
                node_tracker.append(current.val)
                current = current.next
            
            # pop from heap
            heapq.heapify(node_tracker)
            dummy = ListNode()
            heap_current = dummy
            while len(node_tracker) != 0:
                current_val = heapq.heappop(node_tracker)
                new_node = ListNode()
                new_node.val = current_val
                heap_current.next = new_node
                heap_current = heap_current.next
            
            return dummy.next

        else:
            return head
