class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, arr):
        #Code here
        arr[:]=arr[::-1]
        high=arr[0]
        s=[]
        for i in range(n):
            if arr[i]>=high:
                high=arr[i]
                s.append(high)
        return s[::-1]