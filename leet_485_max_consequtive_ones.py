class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        m=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                m=m if m>c else c
            else:
                c=0
        return m
