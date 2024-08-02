class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        z,o,t=0,0,0
        for i in range(len(nums)):
            if nums[i]==0:
                z+=1
            elif nums[i]==1:
                o+=1
            else:
                t+=1
        nums[:] = [0] * z + [1] * o + [2] * t
