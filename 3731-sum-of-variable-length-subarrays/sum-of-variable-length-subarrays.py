class Solution:
    def subarraySum(self, nums: List[int]) -> int:
        p=[]
        for i in range(len(nums)):
            s=0
            start=max(0,i-nums[i])
            for j in range(start,i+1):
                s+=nums[j]
            print(s)
            p.append(s)
        return sum(p)
            
