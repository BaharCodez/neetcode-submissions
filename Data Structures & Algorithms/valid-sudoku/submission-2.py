class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                
                v = board[i][j] 
                
                if v == '.':
                    continue
                if v not in rows[j]:
                    rows[j].add(v)
                if v not in cols[i]:
                    cols[i].add(v)
                if v not in box[(i//3)*3+ (j//3)]:
                    box[(i//3)*3+ (j//3)].add(v)
                else:
                    return False
        return True

        