# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    current_min = None

    def recurse (self, current, p, q):
        if current == None:
            return None
        
        left = self.recurse(current.left, p , q)
        right = self.recurse(current.right, p, q)

        if left and right:
            if left.val == p.val and right.val == q.val:
                self.current_min = current
                return None
            
            if left.val == q.val and right.val ==p.val:
                self.current_min = current
                return None

        if left:
            if left.val == p.val or left.val == q.val:
                if current.val == p.val and left.val == q.val:
                    self.current_min = current
                    return None
                if current.val == q.val and left.val == p.val:
                    self.current_min = current
                    return None
                return left

        if right:
            if right.val == p.val or right.val == q.val:
                if current.val == p.val and right.val == q.val:
                    self.current_min = current
                    return None
                if current.val == q.val and right.val == p.val:
                    self.current_min = current
                    return None
                return right

        if current.val == p.val or current.val == q.val:
            return current
        else:
            return None

        
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.recurse(root, p, q)
        return(self.current_min)
        
