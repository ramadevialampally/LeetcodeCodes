class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        d=dict(sorted(d.items(), key=lambda x: x[1],reverse=True))
        i=0
        a=[]
        for ke,v in d.items():
            if i==k :
                break
            i+=1
            a.append(ke)
            
        return a
        
        