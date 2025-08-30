# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def explore(self, current, arr):
        if current == None:
            return 
        self.explore(current.left, arr)
        arr.append(current.val)
        self.explore(current.right, arr)

        return

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if root:
            arr = []
            self.explore(root, arr)
            return(arr[k-1])
        else:
            return root
