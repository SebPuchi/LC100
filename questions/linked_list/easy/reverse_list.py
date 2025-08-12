# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
         
        if head:
            while current:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return prev
        return head

# Solution 2 Aug 11:
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = None
        current = head
        prev = dummy

        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        return prev

