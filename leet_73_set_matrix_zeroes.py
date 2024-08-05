class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        buff=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    buff.append([i,j])
        for i,j in buff:
            for k in range(len(matrix[0])):
                matrix[i][k]=0
            for l in range(len(matrix)):
                matrix[l][j]=0
            
                    
        print(matrix)