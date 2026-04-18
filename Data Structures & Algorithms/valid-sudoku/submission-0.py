class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # check rows
        for i in board:
            digits = []
            for x in i:
                if x != ".":
                    digits.append(int(x))
            if len(set(digits)) != len(digits):
                return False
        
        # check columns
        for i in range(len(board)):
            digits = []
            for x in range(len(board)):
                if board[x][i] != ".":
                    digits.append(int(board[x][i]))
            if len(set(digits)) != len(digits):
                return False

        # check squares
        for i in range(0,9,3):
            for x in range(0,9,3):
                digits = []
                for a in range(0,3):
                    for b in range(0,3):
                        if board[i+a][x+b] != ".":
                            digits.append(int(board[i+a][x+b]))
                if len(set(digits)) != len(digits):
                    return False
        
        return True





