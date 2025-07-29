# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def solution(self, current):
        if current == None:
            return 0
        
        print(current.val)
        left = 1 + self.solution(current.left)
        right = 1 + self.solution(current.right)
        if right >= left:
            return right
        else:
            return left - right 
    
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        print(self.solution(root)
