class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        res=[]
        arr=sorted(arr)
        m=float('inf')
        for i in range(1,len(arr)):
            l=arr[i]-arr[i-1]
            m=min(l,m)
        for i in range(1,len(arr)):
            l=arr[i]-arr[i-1]
            r=[]
            if (l==m):
                r.append(arr[i-1])
                r.append(arr[i])
            if r:
                res.append(r)
        return res