class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        x1=m-1
        x2=n-1
        x=m+n-1
        while x1>=0 and x2>=0:
            if nums1[x1]<nums2[x2]:
                nums1[x]=nums2[x2]
                x2-=1
            else:
                nums1[x]=nums1[x1]
                x1-=1
            x-=1
        while x2>=0:
            nums1[x]=nums2[x2]
            x-=1
            x2-=1
        return nums1

            
        