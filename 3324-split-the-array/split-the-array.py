class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        if len(nums)%2!=0:
            return False
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for k,v in d.items():
            if v>2:
                return False
        return True
        