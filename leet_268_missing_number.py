class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1=sum([i for i in range(0,len(nums)+1)])
        return sum1-sum(nums)