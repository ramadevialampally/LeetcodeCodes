class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inedge=[0]*(n+1)
        outedge=[0]*(n+1)

        for i,j in trust:
            outedge[i]+=1
            inedge[j]+=1
        for i in range(1,n+1):
            if outedge[i]==0 and inedge[i]==n-1:
                return i
        return -1

        
        