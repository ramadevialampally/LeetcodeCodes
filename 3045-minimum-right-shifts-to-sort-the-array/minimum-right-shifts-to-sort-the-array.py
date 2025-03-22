class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        if(nums==sorted(nums)):
            return 0
        c=0
        for i in range(1,len(nums)):
            if(nums[i]<nums[i-1]):
                c+=1
        if(nums[0]<nums[-1]):
            c+=1
        if(c>=2):
            return -1
        c=0
        while True:
            a=nums[0]
            nums[0]=nums[-1]
            for i in range(1,len(nums)):
                t=nums[i]
                nums[i]=a
                a=t
            print(nums)


            c+=1
            if(nums==sorted(nums)):
                return c