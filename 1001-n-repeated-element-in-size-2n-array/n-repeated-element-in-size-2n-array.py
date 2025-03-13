class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        a={}
        for i in nums:
            if i not in a:
                a[i]=1
            else:
                a[i]+=1
        val=len(nums)//2
        for k,v in a.items():
            if v==val:
                return k