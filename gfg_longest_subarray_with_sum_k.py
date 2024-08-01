class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        sum_dic={}
        s=0
        l=0
        for i in range(n):
            s+=arr[i]
            if s==k:
                l=i+1
            if s-k in sum_dic:
                l=max(l,i-sum_dic[s-k])
            if s not in sum_dic:
                sum_dic[s]=i
        return l
