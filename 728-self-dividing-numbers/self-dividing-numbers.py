class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for i in range(left,right+1):
            k=i
            flag=True
            while k>0:
                r=k%10
                print(r)
                if r==0 or i%r!=0:
                    flag=False
                    break
                k=k//10
            if flag:
                res.append(i)
        return res
                
        