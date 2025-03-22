class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        c=0
        for i in range(len(nums)-1):
            left=sum(nums[:i+1])
            right=sum(nums[i+1:len(nums)])
            r=left-right
            print(r)
            if(r%2==0):
                c+=1
        return c
        