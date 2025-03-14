class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        m={}
        n={}
        for i in words1:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        for i in words2:
            if i not in n:
                n[i]=1
            else:
                n[i]+=1
        c=0
        common=m.keys()&n.keys()
        for i in common:
            if m[i]==1 and n[i]==1:
                c+=1
        return c
        