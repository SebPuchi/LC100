# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
 
        ordering = []
        queue = []
        if root:
            queue.append((root,0))
        
        while len(queue) !=0:
            current = queue.pop(0)
            node, count = current 
            ordering.append((node.val, count))
            count+=1
            if node.left:
                queue.append((node.left, count))
            if node.right:
                queue.append((node.right, count))
        answer = []
        for i in range(len(ordering)):
            val, count = ordering[i]
            if i+1 == len(ordering):
                answer.append(val)
            else:
                val_next, count_next = ordering[i+1]
                if count_next != count:
                    answer.append(val)
        return(answer)

        
