class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        a=[releaseTimes[0]]
        for i in range(1,len(releaseTimes)):
            a.append(releaseTimes[i]-releaseTimes[i-1])
        m=float('-inf')
        for i in a:
            m=max(i,m)
        r=[]
        for i in range(len(a)):
            if a[i]==m:
                r.append(keysPressed[i])
        return max(r)