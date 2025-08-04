"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node:
            visited = []
            stack = []
            stack.append(node)
            start_node = None 
            count = 0
            while len(stack) !=0:
                new_node = Node()
                current = stack.pop(0)
                # Mark as visited 
                visited.append(current.val)
                new_node.val = current.val
                temp_adj_list = []
                for neighbor in current.neighbors:
                    if neighbor.val not in visited:
                        print("NODE", current.val, "NEIGHBOR", neighbor.val)
                        stack.append(neighbor)
                    temp_adj_list.append(neighbor)
                new_node.neighbors = temp_adj_list
                if count == 0:
                    start_node = new_node
                count+=1
                print(stack)
            return start_node
        else:
            return node cloneGraph(self, node: Optional['Node']) -> Optional['Node']
