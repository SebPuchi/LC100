# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy_node = ListNode()
        dummy_node.next = head
        current = dummy_node

        node_count = 0
        while current.next:
            node_count+=1
            current = current.next

        current = dummy_node 
        for i in range((node_count - n)):
            print("VAL", current.val)
            current = current.next 

        if current.next.next:
            current.next = current.next.next
        else:
            current.next = None
        return dummy_node.next
