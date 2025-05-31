# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def explore(self, current):
        if current == None:
            return 0 

        left =  1 + self.explore(current.left)
        right =  1 + self.explore(current.right)
        if abs(left - right) == 1 or abs(left-right) == 0:
            return 0 
        else: 
            return 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.explore(root) == 1
