# Most recent solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def explore(self, p, q):
        if p == None and q == None: 
            return True
        elif p == None and q or q == None and p:
            return False 

        left = self.explore(p.left, q.left)
        right = self.explore(p.right, q.right)

        same_values = left and right and p.val == q.val

        return same_values


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return self.explore(p, q)
        elif not p and not q:
            return True
        else:
            return Fals




# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def explore(self, current, visited): 
        if current == None: 
            visited.append(None) 
            return 
        visited.append(current.val) 
        self.explore(current.left, visited)
        self.explore(current.right, visited)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        visited_one = []
        visited_two = []

        self.explore(p, visited_one)
        self.explore(q, visited_two)
        return visited_one == visited_two
        

# Solution 2: More efficient: 
class Solution:
    def explore(self, current1, current2): 
        if current1 == None and current2 == None: 
            return True
        elif current1 != None and current2 != None: 
            matched = False
    
            if current1.val == current2.val: 
                matched = True
            left_matched = self.explore(current1.left, current2.left)
            right_matched = self.explore(current1.right, current2.right)
    
            return matched and left_matched and right_matched
        else: 
            return False
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.explore(p, q)
        
