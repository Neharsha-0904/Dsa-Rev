class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        x=[]
        for i in range(numRows):
            if i==0:
                x.append([1])
            else:
                y=[1]
                for j in range(len(x[-1])-1):
                    y.append(x[-1][j]+x[-1][j+1])
                y.append(1)
                x.append(y)
        return x






                    


