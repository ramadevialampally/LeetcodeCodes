class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        for i in arr2:
            res.append(i)
        nesq=[]
        arr1=sorted(arr1)
        d=Counter(arr1)
        res=[]
        for i in arr2:
            res.append(i)
            d[i]-=1
        for k,v in d.items():
            if v>0:
                if k in res:
                    a=res.index(k)
                    for i in range(v):
                        res.insert(a,k)
                else:
                    for i in range(v):

                        res.append(k)

        return res
        
        
        