class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        num_rows = len(matrix)
        num_cols = len(matrix[0])
        
        if num_rows == 0:
            return False
        
        lo = 0
        hi = num_rows * num_cols - 1
        
        while lo <= hi:
            mid = (lo + hi) //2
            elem = matrix[mid // num_cols][mid % num_cols]
            if target == elem:
                return True
            else:
                if target < elem :
                    hi = mid - 1
                else:
                    lo = mid + 1
        return False
            