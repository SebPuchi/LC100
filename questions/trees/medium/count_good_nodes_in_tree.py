# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math
class Solution:
    count = 0
    def recurse(self, current, max_val):
        if current == None:
            return 
        if current.val >= max_val:
            self.count+=1
        self.recurse(current.left, max(max_val, current.val))
        self.recurse(current.right,  max(max_val, current.val))


    def goodNodes(self, root: TreeNode) -> int:
        self.recurse(root, -math.inf)
        
        return(self.count)
