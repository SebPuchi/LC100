# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        current_one = l1
        current_two = l2
        current_three = dummy
        count = 0
        while current_one or current_two or carry == 1:
            new_node = ListNode()
            current_sum = 0 

            if current_one:
                current_sum+=current_one.val
                current_one = current_one.next

            if current_two:
                current_sum+=current_two.val
                current_two = current_two.next

            if carry == 1:
                current_sum+=1
                carry = 0

            if current_sum > 9:
                carry = 1
                new_node.val = current_sum - 10
            else:
                carry = 0
                new_node.val = current_sum
            current_three.next = new_node
            current_three = current_three.next
            count+=1

        return dummy.next

