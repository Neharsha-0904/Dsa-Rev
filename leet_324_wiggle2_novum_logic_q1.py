class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)<=1:
            return nums
        final=[]
        nums.sort()
        if len(nums)%2==0:
            l=nums[:len(nums)//2]
            r=nums[len(nums)//2:]
        else:
            l=nums[:len(nums)//2+1]
            r=nums[len(nums)//2+1:]
        if l[-1]==r[0]:
            l=l[::-1]
        r=r[::-1]
        for i,j in zip(l,r):
            final.append(i)
            final.append(j)
        if len(l)>len(r):
            final.append(l[-1])
        elif len(r)>len(l):
            final.append(r[-1])
        nums[:]=final