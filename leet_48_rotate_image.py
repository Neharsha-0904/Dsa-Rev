class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix[:]=list(zip(*matrix))
        matrix[:]=[list(i[::-1]) for i in matrix]
        print(matrix)