class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=set(nums)
        c,k=-1,-1
        for i in n:
            t=nums.count(i)
            if t>c:
                k=i
                c=t
        return k

