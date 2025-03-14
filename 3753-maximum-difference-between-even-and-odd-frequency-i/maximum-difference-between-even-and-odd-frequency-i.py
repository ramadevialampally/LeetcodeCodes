class Solution:
    def maxDifference(self, s: str) -> int:
        m={}
        for i in s:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        
        odd=0
        even=float('inf')
        for v in m.values():
            if v%2==0:
                even=min(even,v)
            else:
                odd=max(odd,v) 
        return odd-even      