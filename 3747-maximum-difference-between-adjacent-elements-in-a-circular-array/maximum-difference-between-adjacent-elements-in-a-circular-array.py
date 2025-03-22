class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        d=float('-inf')
        for i in range(1,len(nums)):
            r=abs(nums[i-1]-nums[i])
            d=max(d,r)
        r=abs(nums[0]-nums[-1])
        return max(d,r)