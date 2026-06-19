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

                k= (i//3)*3+ (j//3)
                
                
                if v in rows[i]:
                    return False
                rows[i].add(v)

                if v in cols[j]:
                    return False
                cols[j].add(v)
                if v in box[k]:
                    return False
                box[k].add(v)
                
        return True

        