class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            print(row)
            if target <= row[-1]:
                for num in row:
                    if num == target:
                        return True
                    elif num > target: 
                        return False
                    
           
        return False