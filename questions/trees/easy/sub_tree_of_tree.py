# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:   
    def check(self, current, sub_tree):
        if current == None and sub_tree == None:
            return True
        if current != None and sub_tree != None: 
            matched =  False
            if current.val == sub_tree.val: 
                matched = True

            left_matched = self.explore(current.left, sub_tree.left)
            right_matched = self.explore(current.right, sub_tree.right)

            return matched and left_matched and right_matched
            
        else: 
            return False

    def explore(self, current, target):
        if current == None: 
            return False
        
        is_subtree = False
        if current.val == target.val:
            is_subtree = self.check(current, target)
        
        if is_subtree: 
            return is_subtree
        else: 
            self.explore(current.left, target)
            self.explore(current.right, target)

            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.explore(root, subRoot)
