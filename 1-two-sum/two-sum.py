class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
 
        for i in range(len(nums)):
            x=nums[i]
            for j in range(i+1,len(nums)):

                y=x+nums[j]
                if(y==target):
                    a.append(i)
                    a.append(j)
                    return a
                

            