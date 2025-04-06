class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        res=[]
        for k,v in d.items():
            if v>=2:
                res.append(k)

        for i in range(1,len(nums)+1):
            if i not in nums:
                res.append(i)
        return res        