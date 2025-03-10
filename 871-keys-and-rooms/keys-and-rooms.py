class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque
        q=deque()
        q.append(0)
        visited=[False]*(len(rooms))
        visited[0]=True
        while q:
            a=q.popleft()
            for i in rooms[a]:
                if not visited[i]:
                    q.append(i)
                    visited[i]=True
        for i in visited:
            if i==False:
                return False
        return True
                
        