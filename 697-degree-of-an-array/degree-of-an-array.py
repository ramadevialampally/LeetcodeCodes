class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        a=defaultdict(int)
        f,l={},{}
        for i,num in enumerate(nums):
            a[num]+=1
            if num not in f:
                f[num]=i
            l[num]=i
        print(a)
        print(f)
        print(l)
        degree=max(a.values())
        maxlen=float('inf')
        for k,v in a.items():
            if v==degree:
                r=l[k]-f[k]
                maxlen=min(r,maxlen)
            
        return maxlen+1
        