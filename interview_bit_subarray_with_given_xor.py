    def solve(self, A, B):
        prefix_xor = 0
        count = 0
        freq_map = {0: 1}  # Initialize with 0:1 to handle cases where prefix_xor itself is B
    
        for num in A:
            prefix_xor ^= num
        
        # Calculate the required prefix_xor that would satisfy the condition
            target_xor = prefix_xor ^ B
        
        # Check if target_xor is in the hash map
            if target_xor in freq_map:
                count += freq_map[target_xor]
        
        # Update the frequency map with the current prefix_xor
            if prefix_xor in freq_map:
                freq_map[prefix_xor] += 1
            else:
                freq_map[prefix_xor] = 1
    
        return count