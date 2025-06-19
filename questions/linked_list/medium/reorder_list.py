class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        one = ListNode()
        one_pointer = one
        two = ListNode()
        current = head
        count = 0
        while current: 
            node = ListNode()
            node.val = current.val
            if (count % 2) == 0:
                one.next = node
                one = one.next
            else:
                two.next = node
                two = two.next
            current = current.next
        current = one_pointer.next
        
        while current: #and check next
