class Solution:
    def firstUniqChar(self, s: str) -> int:
        m={}
        for i in s:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        for k,v in m.items():
            if v==1:
                return s.index(k)
        return -1
        