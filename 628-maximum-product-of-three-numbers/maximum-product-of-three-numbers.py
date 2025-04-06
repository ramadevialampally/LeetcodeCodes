class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)
        nec=0
        pos=0
        for i in nums:
            if i<0:
                nec+=1
            else:
                pos+=1
        res1=float('-inf')
        res2=float('-inf')
        res3=float('-inf')
        if pos>=3:
            res1=(nums[len(nums)-1]*nums[len(nums)-2]*nums[len(nums)-3])
        if nec>=2 and pos>=1:
            res2=(nums[0]*nums[1]*nums[len(nums)-1])
        if pos==0 and nec>=3:
            res2=nums[-1]*nums[-2]*nums[-3]
        else:
            res3=nums[0]*nums[1]*nums[2]
        res1=max(res1,res3)
            
        print(res1,res2)
        return max(res1,res2)

