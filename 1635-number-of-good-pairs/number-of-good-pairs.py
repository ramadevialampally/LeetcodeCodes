class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq={}
        for i in nums:
            if i not in freq:
                freq[i]=1
            else:
                freq[i]+=1
        c=0
        print(freq)
        for k,v in freq.items():
            c+=(v*(v-1))//2
        return c
        