class Solution:
    def maxLen(self, n, arr):
        # Dictionary to store the first occurrence of each cumulative sum
        sum_map = {}
        # Initialize the cumulative sum and max_len
        cumulative_sum = 0
        max_len = 0
        
        for i in range(n):
            # Update the cumulative sum
            cumulative_sum += arr[i]
            
            if cumulative_sum == 0:
                max_len = i + 1
            elif cumulative_sum in sum_map:
                # Update max_len if this subarray is longer than the previous max
                max_len = max(max_len, i - sum_map[cumulative_sum])
            else:
                # Store the first occurrence of the cumulative sum
                sum_map[cumulative_sum] = i
        
        return max_len
