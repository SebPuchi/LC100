"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {}
        current = head

        while current:
            copy[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            rand_pointer = None if current.random == None else current.random
            if rand_pointer == None:
                copy[current].random = None
            else:
                copy[current].random = copy[rand_pointer]
            
            copy[current].next = None if current.next == None else copy[current.next] 
            current = current.next
        for key in copy:
            print("key", copy[key], "rand", copy[key].random ) 

        if len(copy) != 0:
            return copy[head] 
        else: 
            return head
