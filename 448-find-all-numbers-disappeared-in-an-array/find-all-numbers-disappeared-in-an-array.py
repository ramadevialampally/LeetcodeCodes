class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            ind=abs(num)-1
            nums[ind]=-abs(nums[ind])
        res=[]
        for i in range(len(nums)):
            if nums[i]>0:
                res.append(i+1)
        return res
        