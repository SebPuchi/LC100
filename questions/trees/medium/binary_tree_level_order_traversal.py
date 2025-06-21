# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def explore(self, level, queue):
        current, level = queue.pop(0)

        if current.left:
            queue.append((current.left, level+1))
        if current.right:
            queue.append((current.right, level+1))
        return (current.val, level)

        
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        level = 0
        answer_arr = []
        if root:
            queue.append((root, level))
            while queue:     
                num, level = self.explore(level, queue)
                if len(answer_arr) <= level:
                    answer_arr.append([num])
                else:
                    answer_arr[level].append(num)
        return answer_arr


