# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def explore(self, current, visited): 
        if current == None: 
            visited.append(None) 
            return 
        visited.append(current.val) 
        self.explore(current.left, visited)
        self.explore(current.right, visited)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        visited_one = []
        visited_two = []

        self.explore(p, visited_one)
        self.explore(q, visited_two)
        return visited_one == visited_two
        
