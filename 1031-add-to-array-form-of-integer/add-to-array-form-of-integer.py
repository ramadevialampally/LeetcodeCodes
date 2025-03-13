import sys
sys.set_int_max_str_digits(100000)
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        su=0
        for i in num:
            su=su*10+i
        su=su+k
        r=list(str(su))
        a=[]
        for i in r:
            a.append(int(i))
        return a
        