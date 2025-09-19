# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math
class Solution:    
    def findValid (self, lists):
        valid = [False] * len(lists)
        for i in range(len(valid)):
            node = lists[i]
            if node != None:
                valid[i] = True
        
        return valid

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummyNode = ListNode()
        valid_start = self.findValid(lists)

        current_node = dummyNode
        while True in valid_start:
            current_min = math.inf
            min_index = None
            for i in range(len(valid_start)):
                if valid_start[i] and lists[i].val < current_min:
                    current_min = lists[i].val
                    min_index = i
            lists[min_index] = lists[min_index].next
            updated_node = ListNode(current_min)
            current_node.next = updated_node
            current_node = updated_node
            if lists[min_index] == None:
                valid_start[min_index] = False
        
        return dummyNode.next

