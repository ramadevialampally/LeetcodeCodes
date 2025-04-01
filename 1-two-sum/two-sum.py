class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        res=[]
        for i in range(len(nums)):
            d[nums[i]]=i
        for i in range(len(nums)):
            x=target-nums[i]
            if x==nums[i] and i!=d[nums[i]]:
                res.append(i)
                res.append(d[nums[i]])
                break
            if x in nums:
                v=nums.index(x)
                print(v)
                if(v>i):
                    res.append(i)
                    res.append(nums.index(x))
                    break
        return res

        
                

            