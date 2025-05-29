class Solution:
    def explore(self, current, depth) -> int:
        if current:
            depth+=1
            left = self.explore(current.left, depth)
            right =self.explore(current.right, depth)
            return max(left, right)
        else:
            return depth

    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.explore(root, 0)     
        
