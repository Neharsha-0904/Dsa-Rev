class Solution:
	def editDistance(self, str1, str3):
		# Code here
		m=len(str1)
		n=len(str3)
		matrix=[[0 for i in range(n+1)] for j in range(m+1)]
		for i in range(m+1):
		    for j in range(n+1):
		        if i==0:
		            matrix[i][j]=j
		        elif j==0:
		            matrix[i][j]=i
		        elif str1[i-1]==str3[j-1]:
		            matrix[i][j]=matrix[i-1][j-1]
		        else:
		            matrix[i][j]=1+min(matrix[i][j-1],matrix[i-1][j],matrix[i-1][j-1])
		return matrix[m][n]
		            