# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    max_diameter = 0
    def explore(self, current):
        if current == None:
            return -1
        left_path = 1 + self.explore(current.left)
        right_path = 1 + self.explore(current.right)
        print(current.val, left_path, right_path)
        self.max_diameter = max(self.max_diameter, left_path + right_path)
        return max(left_path, right_path) 

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.explore(root)
        return self.max_diameter

