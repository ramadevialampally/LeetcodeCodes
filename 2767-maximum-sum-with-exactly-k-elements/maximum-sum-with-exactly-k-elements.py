class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        s=0
        nums=sorted(nums)
        while k>0:
            v=nums.pop()
            s+=v
            nums.append(v+1)
            k-=1
        return s

        