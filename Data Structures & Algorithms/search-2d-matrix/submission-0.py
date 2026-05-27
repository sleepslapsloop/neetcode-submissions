class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        #row search
        top, bottom = 0, len(matrix) - 1
        rowInd = None
        while top <= bottom:
            mid = (top + bottom) // 2
            init, fin = matrix[mid][0], matrix[mid][-1]

            if init <= target <= fin:
                rowInd = mid
                break
            elif target > init:
                top = mid + 1
            else:
                bottom = mid - 1

        if rowInd == None:
            return False
        
        #colsearch
        arr = matrix[rowInd]
        left, right = 0, len(arr) - 1
        colInd = None

        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                colInd = mid
                break
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False if colInd == None else True