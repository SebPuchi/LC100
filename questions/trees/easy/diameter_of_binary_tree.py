# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    max_diameter = -1
    def explore(self, current):
        if current == None:
            return 0

        left = self.explore(current.left)
        right = self.explore(current.right)

        self.max_diameter = max(self.max_diameter, left + right)

        return 1 + max(left, right)


    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.explore(root)
        return self.max_diameter

