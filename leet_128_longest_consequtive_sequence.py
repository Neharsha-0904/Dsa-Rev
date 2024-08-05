class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        curr_l=1
        lon_l=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                curr_l+=1
            else:
                lon_l=max(curr_l,lon_l)
                curr_l=1
        return max(curr_l,lon_l)
        