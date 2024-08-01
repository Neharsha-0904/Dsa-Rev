class Solution: 
    
    
    def selectionSort(self, a,n):
        #code here
        for i in range(n):
            for j in range(i,n):
                if a[j]<a[i]:
                    a[i]=a[j]+a[i]
                    a[j]=a[i]-a[j]
                    a[i]=a[i]-a[j]
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=list(map(int,input().strip().split()))
        Solution().selectionSort(arr,n)
        for i in range(n):
            print(arr[i],end=" ")
        print()