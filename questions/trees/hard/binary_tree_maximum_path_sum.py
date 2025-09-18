# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math
class Solution:
    max_path = -math.inf
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # Explore helper
        def explore(current, current_sum):
            if current == None:
                return 0

            left = explore(current.left, current_sum)
            right = explore(current.right, current_sum)

            current_max_path = max(current.val + left, right + current.val, left + right + current.val, current.val)
            self.max_path = max(current_max_path, self.max_path)

            return max(current.val + left, current.val +right, current.val)


        if root: 
            explore(root, root.val)
            return self.max_path
        else: 
            return root
        
