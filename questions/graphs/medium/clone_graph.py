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
            new_nodes = {}
            
            visited = []
            stack = []
            stack.append(node)
            while len(stack) !=0:
                current = stack.pop(0)
                # Mark as visited 
                visited.append(current)
                if current.val not in new_nodes:
                    new_nodes[current.val] = Node(current.val)
                for neighbor in current.neighbors:
                    if neighbor not in visited:
                        stack.append(neighbor)
                    if neighbor.val not in new_nodes:
                        new_nodes[neighbor.val] = Node(neighbor.val)
                    neighbor_list = new_nodes[current.val].neighbors
                    print("NE", neighbor.val)
                    if neighbor not in neighbor_list:
                        neighbor_list.append(new_nodes[neighbor.val])
            return new_nodes[1]
        else:
            return node

