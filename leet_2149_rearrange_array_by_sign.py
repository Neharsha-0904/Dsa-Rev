class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p,n=0,1
        x=[0]*len(nums)
        for i in nums:
            if i>0:
                x[p]=i
                p+=2
            else:
                x[n]=i
                n+=2
        return x
        