class Solution:
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count=0
        total=0
        totals={0:1}
        for num in nums:
            total+=num
            if total-k in totals:
                count+=totals[total-k]
            if total in totals:
                totals[total]+=1
            else:
                totals[total]=1
        return count
            