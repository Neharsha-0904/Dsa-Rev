class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic={}
        num=[]
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1        
        for i,j in dic.items():
            if j>len(nums)/3:
                num.append(i)
        return num


            