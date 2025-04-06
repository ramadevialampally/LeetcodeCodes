class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        a=[]
        res=[0]*len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                res[i]=nums[(i+nums[i])%(len(nums))]
            else:
                res[i]=nums[(i-abs(nums[i]))%(len(nums))]   
        return res   