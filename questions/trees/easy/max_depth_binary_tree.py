class Solution:
    def explore(self, current, depth) -> int:
        if current:
            depth+=1
            left = self.explore(current.left, depth)
            right = self.explore(current.right, depth)
            return max(left, right)
        else:
            return depth

    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.explore(root, 0)     

# Max depth iterative
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root:
            stack = []
            stack.append((root, 0))
            current_max = -1
            while len(stack) != 0:
                current = stack.pop()
                node, depth = current
                if node:
                    stack.append((node.left, depth+1))
                    stack.append((node.right, depth+1))
                elif depth > current_max:
                    current_max = depth
            return current_max
        return 
