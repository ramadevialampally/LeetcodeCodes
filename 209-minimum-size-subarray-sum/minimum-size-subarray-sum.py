class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        s=0
        su=float('inf')
        j=0
        for i in range(len(nums)):
            s+=nums[i]
            while s>=target and j<=i:
                su=min(su,i-j+1)
                s-=nums[j]
                j+=1
        return su
    