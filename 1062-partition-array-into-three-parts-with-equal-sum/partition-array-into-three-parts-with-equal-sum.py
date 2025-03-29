class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if all( i==0 for i in arr):
            return True
        
        s=sum(arr)
        if s%3!=0:
            return False
        print(s)
        r=s//3
        c=0
        su=0
        for i in arr:
            su+=i
            if su==r:
                c+=1
                su=0
        if c>=3:
            return True
        return False

        