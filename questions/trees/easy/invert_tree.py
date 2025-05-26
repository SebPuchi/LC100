# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


class Solution:
    def explore(self, current, visited_nodes):
        if current:
            visited_nodes.append(current)

            temp = TreeNode()
            temp = current.left
            current.left = current.right
            current.right = temp

            self.explore(current.left, visited_nodes)
            self.explore(current.right, visited_nodes)
        else:
            return
        

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        visited_nodes = []
        
        self.explore(root, visited_nodes)
        return root

