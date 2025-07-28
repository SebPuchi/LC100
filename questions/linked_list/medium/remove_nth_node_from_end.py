class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        head_node = head
        current = head

        node_count = 0
        while current:
            node_count+=1
            current = current.next

        current = head 

        for i in range((node_count - n) -1):
            print(current.val)
            current = current.next 
        print("VAL", current.val)
        current.next = current.next.next
        
        print("VAL", current.val)
        return head_node

        
