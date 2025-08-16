# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def recurse(self, current):
        if current == None:
            return (None, None, True)

        left_min, left_max, valid_left = self.recurse(current.left)
        right_min, right_max, valid_right = self.recurse(current.right)

        is_valid = valid_left and valid_right

        if left_min != None and left_min >= current.val:
            is_valid = False

        if left_min != None and left_min >= current.val:
            is_valid = False

        return (subtree_min, subtree_max, is_valid)

        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        answer = self.recurse(root)
        return(answer[2]
