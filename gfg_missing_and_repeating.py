class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        sum_n = n * (n + 1) // 2
        sum_n_sq = n * (n + 1) * (2 * n + 1) // 6
        
        sum_arr = sum(arr)
        sum_arr_sq = sum(x * x for x in arr)
        
        diff = sum_n - sum_arr  # missing - repeating
        sum_diff = (sum_n_sq - sum_arr_sq) // diff  # missing + repeating
        
        missing = (diff + sum_diff) // 2
        repeating = sum_diff - missing
        
        return [repeating, missing]