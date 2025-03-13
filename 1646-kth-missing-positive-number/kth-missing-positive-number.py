class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        ans=[]
        i=1
        while i<max(arr):
            if i not in arr:
                ans.append(i)
            i+=1
        if len(ans)>=k:
            return ans[k-1]
        else:
            print(ans)
            l=k-len(ans)
            return arr[-1]+l

        