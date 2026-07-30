class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            print(row[-1], row[0])
            if target <= row[-1] and target >= row[0]:
                l = 0
                r = len(row) -1
                while l <= r:
                    mid = (l + r) + l //2
                    print(mid)
                    if target == row[mid]:
                        return True
                    elif target > row[mid]:
                        l = mid + 1
                    else:
                        r = mid -1
                return False

                
                '''for num in row:
                    if num == target:
                        return True
                    elif num > target: 
                        return False'''
                    
        return False
    
    