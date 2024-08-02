class Solution:
    def pairWithMaxSum(self, arr):
        n = len(arr)
        if n < 2:
            return None  
        
        max_sum = float('-inf')
        
        
        for i in range(n - 1):
            current_sum = arr[i] + arr[i + 1]
            max_sum = max(max_sum, current_sum)
        
        return max_sum