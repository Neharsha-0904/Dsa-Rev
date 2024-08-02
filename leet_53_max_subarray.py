class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        sum = 0
        for num in nums:
            if sum < 0:
                sum = 0
            sum = sum + num
            if sum > max_sum:
                max_sum = sum
        return max_sum