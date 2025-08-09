class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool
        rows = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        columns = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[]}
        segments = {(0,0):[],
                    (0,1):[],
                    (0,2):[],
                    (1,0):[],
                    (1,1):[],
                    (1,2):[],
                    (2,0):[],
                    (2,1):[],
                    (2,2):[]
                    }

        for i in range(len(board)):
            for j in range(len(board[0])):
                current = board[i][j]
                if current == '.':
                    continue
                if current in rows[i]:
                    return False
                else: 
                    rows[i].append(current)
                if current in columns[j]:
                    return False
                else: 
                    columns[j].append(current)
                if current in segments[(i//3,j//3)]:
                    return False
                else: 
                    segments[(i//3, j//3)].append(current)

        return True
