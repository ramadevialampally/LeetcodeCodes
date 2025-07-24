class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        import heapq
        dirs=[(0,1),(1,0),(-1,0),(0,-1)]
        heap=[(0,0,0)]
        n=len(heights)
        m=len(heights[0])
        effort=[[float('inf')]*m for i in range(n)]
        effort[0][0]=0
        while heap:
            eff,x,y=heapq.heappop(heap)
            if(x==n-1 and y==m-1):
                return eff
            for dx,dy in dirs:
                nx=x+dx
                ny=y+dy
                if(0<=nx<n and 0<=ny<m):
                    neweff=max(eff,abs(heights[x][y]-heights[nx][ny]))
                    if(neweff<effort[nx][ny]):
                        effort[nx][ny]=neweff
                        heapq.heappush(heap,(neweff,nx,ny))
        return -1

        