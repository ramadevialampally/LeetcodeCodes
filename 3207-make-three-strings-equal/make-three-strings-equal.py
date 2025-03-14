class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        a=min(len(s1),len(s2))
        b=min(len(s3),a)
        c=0
        for i in range(b):
            if not (s1[i]==s2[i]==s3[i]):
                break
            c+=3
        if c==0:
            return -1
        return len(s1)+len(s2)+len(s3)-c
        