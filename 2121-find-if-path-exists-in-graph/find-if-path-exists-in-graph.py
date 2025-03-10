class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if n==1 and len(edges)==0:
            return True
        def build(edges,n):
            a=[[] for _ in range(n)]
            for i in edges:
                a[i[0]].append(i[1])
                a[i[1]].append(i[0])
            return a
        adj_list=build(edges,n)

        from collections import deque
        q=deque()
        v=[False]*n
        q.append(source)
        v[source]=True
        while q:
            a=q.popleft()
            for i in adj_list[a]:
                if i==destination:
                    return True
                if not v[i]:
                    q.append(i)
                    v[i]=True
               
        return False
        