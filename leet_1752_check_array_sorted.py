class Solution(object):
    def check(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        si=nums.index(min(nums))
        c=nums.count(nums[si])
        if c>1:
            n=len(nums)
            x=0
            if si==0:
                while nums[n-1]==nums[si] and x<len(nums)-1:
                    si=n-1
                    n-=1
                    x+=1

        new=nums[si:]+nums[:si]
        print(new)
        for i in range(len(new)-1):
            if new[i]>new[i+1]:
                return False
        return True



