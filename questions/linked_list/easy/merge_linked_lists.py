# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode() 
        current = new_head
        while list1 and list2:
            node = ListNode() 
            print(list1.val, list2.val)
            if list1.val <= list2.val:
                node.val  = list1.val
                list1 = list1.next
            else:
                node.val = list2.val
                list2 = list2.next
            current.next = node
            current = current.next

        if list1:
            current.next = list1
        elif list2: 
            current.next = list2
        return new_head.next


