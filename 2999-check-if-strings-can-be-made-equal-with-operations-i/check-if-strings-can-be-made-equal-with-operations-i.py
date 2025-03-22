class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        j=2
        i=0
        s1=list(s1)
        s2=list(s2)
        while i<len(s1) and j<len(s2):
            if(s1[i]!=s2[i]):
                s2[i],s2[j]=s2[j],s2[i]
            if(s1==s2):
                return True
            i+=1
            j=i+2
        return False
            
        