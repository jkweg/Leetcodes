class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        n = len(matrix)
        m = len(matrix[0])
        i = 0
        while  i < n and matrix[i][0] <= target:
            i+= 1
        i -= 1
        for j in range(m):
            if matrix[i][j] == target:
                return True
        return False        
        