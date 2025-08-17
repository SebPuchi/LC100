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

        # Assume valid unless proven otherwise
        is_valid = valid_left and valid_right

        # Check left subtree's max value
        if left_max is not None and left_max >= current.val:
            is_valid = False

        # Check right subtree's min value
        if right_min is not None and right_min <= current.val:
            is_valid = False

        # Calculate the min value for this subtree
        subtree_min = left_min if left_min is not None else current.val

        # Calculate the max value for this subtree
        subtree_max = right_max if right_max is not None else current.val

        return (subtree_min, subtree_max, is_valid)

        

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        answer = self.recurse(root)
        return(answer[2])
