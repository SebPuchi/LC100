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


### BETTER SOLUTION: 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    valid = False
    def exploreList(self, current, explore_list):
            if current == None:
                explore_list.append(None)
                return 
            explore_list.append(current.val)

            self.exploreList(current.left, explore_list)
            self.exploreList(current.right, explore_list)


    def explore(self, current, sub_list):
        if current == None: 
            return 
        
        if current.val == sub_list[0]:
            root_list = []
            self.exploreList(current, root_list)
            if root_list == sub_list:
                self.valid = True
        left = self.explore(current.left, sub_list)
        right = self.explore(current.right, sub_list)
            
    def isSubtree(self, root, subRoot):
        sub_tree_explore_list = []
        self.exploreList(subRoot, sub_tree_explore_list)  
        self.explore(root, sub_tree_explore_list)
        return self.valid
