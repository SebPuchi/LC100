# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def explore(self, current):
        if current == None:
            return (0, True)

        left_tup =  self.explore(current.left)
        right_tup =  self.explore(current.right)
        left, left_bal =  left_tup[0] + 1, left_tup[1]
        right, right_bal =  right_tup[0] + 1, right_tup[1]
        is_bal = False 

        if abs(left-right) == 0 or abs(left-right) == 1:
            print("IN HERE")
            is_bal = True
            print("current_bal", is_bal)
        print(current.val, is_bal, abs(left - right))
        return (max(left, right), (is_bal and left_bal and right_bal))
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.explore(root)[1]
