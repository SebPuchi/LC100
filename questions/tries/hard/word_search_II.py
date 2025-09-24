class Node:
    def __init__(self):
        self.children = {}
        self.end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Create trie 
        treeRoot = Node()
        for word in words:
            current = treeRoot
            for let in word:
                if let in current.children:
                    current = current.children[let]
                else:
                    current.children[let] = Node()
                    current = current.children[let]
            current.end = True

        n = len(board)
        m = len(board[0])
        valid_words = []

        def backtrack(i, j, current, path):
            # print("current path", path)
            # print("CURRENT NODE", current.children)
            if i >= n or i<0:
                return 

            if j >= m or j<0:
                return 

            letter = board[i][j]

            if letter not in current.children or board[i][j] == "#":
                return  

            path.append(letter)
            next_node = current.children[letter] 

            if next_node.end:
                valid_words.append(path.copy())

            # mark current node 
            board[i][j] = "#"

            backtrack(i+1, j, next_node, path)
            backtrack(i, j+1, next_node, path)
            backtrack(i-1, j, next_node, path)
            backtrack(i, j-1, next_node, path)
            
            # unmark node
            board[i][j] = letter
            path.pop()

        for i in range(n):
            for j in range(m):
                current_letter = board[i][j]
                if current_letter in treeRoot.children:
                    backtrack(i, j, treeRoot, [])
        
        output = set()
        for i in range(len(valid_words)):
            word = valid_words[i]
            output.add("".join(word))
        return(list(output))
