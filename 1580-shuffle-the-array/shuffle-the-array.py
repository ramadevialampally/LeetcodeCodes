class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        i=0
        j=n
        ans=[]
        while i<n and j<2*n:
            ans.append(nums[i])
            ans.append(nums[j])
            i+=1
            j+=1
        return ans

        