# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head:
            first, second = head, head
            while first:
                first = first.next
                if second.next and second.next.next:
                    second = second.next.next
                else:
                    break
                
                if first == second:
                    return True
        
        return False
