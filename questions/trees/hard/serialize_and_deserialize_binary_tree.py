# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        encoded = []

        def explore(current):
            if current == None:
                encoded.append("None")
                return

            encoded.append(str(current.val))
            explore(current.left)
            explore(current.right)
            
        explore(root)
        return(",".join(encoded))
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        print(data)
        self.index = 0
        def dfs():
            if data[self.index] == "None":
                self.index +=1
                return None

            # create a new node: 
            node = TreeNode(int(data[self.index]))
            self.index +=1
            node.left = dfs()
            node.right = dfs()
            return node
        root = dfs()
        return root
        
