class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        a=[]
        nums=sorted(nums)
        s=0
        end=len(nums)-1
        while s<end:
            k=(nums[s]+nums[end])/2
            s+=1
            end-=1
            a.append(k)
        return min(a)
        