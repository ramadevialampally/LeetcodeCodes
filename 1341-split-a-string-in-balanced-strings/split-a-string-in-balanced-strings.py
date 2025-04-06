class Solution:
    def balancedStringSplit(self, s: str) -> int:
        lc=0
        rc=0
        c=0
        for i in s:
            if i=='L':
                lc+=1
            else:
                rc+=1
            if lc==rc:
                c+=1
                lc=0
                rc=0
        return c