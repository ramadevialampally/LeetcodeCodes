class Solution:
    def maxSum(self, nums: List[int]) -> int:
        ans=-1
        for i,v in enumerate(nums):
            for j in nums[i+1:]:
                k=v+j
                if ans<k and max(str(v))==max(str(j)):
                    ans=k
        return ans