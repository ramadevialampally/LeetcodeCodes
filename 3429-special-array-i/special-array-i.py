class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        i=nums[0]
        for i in range(1,len(nums)):
            if (nums[i-1]%2==0 and nums[i]%2!=0) or(nums[i-1]%2!=0 and nums[i]%2==0):
                continue
            else:
                return False
        return True
        