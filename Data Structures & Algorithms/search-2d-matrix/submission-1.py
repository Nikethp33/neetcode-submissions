class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix) - 1
        m = len(matrix)
        n = len(matrix[0])

        while l <= r:
            mid = (l + r) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][n-1]:
                l = 0
                r = n - 1
                while l <= r:
                    mid2 = (l + r) // 2
                    
                    if matrix[mid][mid2] == target:
                        return True
                    elif matrix[mid][mid2] < target:
                        l = mid2 + 1
                    elif matrix[mid][mid2] > target:
                        r = mid2 - 1

                return False

            
            elif target > matrix[mid][n-1]:
                l = mid + 1
            
            elif target < matrix[mid][0]:
                r = mid - 1
        return False

        