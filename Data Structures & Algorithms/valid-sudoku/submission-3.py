class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                
                v = board[i][j] 
                k= (i//3)*3+ (j//3)
                
                if v == '.':
                    continue
                if v in rows[j]:
                    return False
                rows[j].add(v)
                if v in cols[i]:
                    return False
                cols[i].add(v)
                if v not in box[k]:
                    return False
                box[k].add(v)
                
        return True

        