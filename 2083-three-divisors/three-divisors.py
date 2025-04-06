class Solution:
    def isThree(self, n: int) -> bool:
        d=0
        for i in range(1,n+1):
            if n%i==0:
                d+=1
        if d==3:
            return True
        return False
        