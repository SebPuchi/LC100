# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        first = head
        second = head.next
        while second and second.next:
            first = first.next
            second = second.next.next
        
        current = first.next
        first.next = None
        temp = None
        #reverse second half portion
        while current:
            next_node = current.next
            current.next = temp
            temp = current
            current = next_node
        
        first = head
        second = temp
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next

