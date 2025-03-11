class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a=[[] for _ in range(len(edges)+2)]
        for i,j in edges:
            a[i].append(j)
            a[j].append(i)
        print(a)
        for i in range(1,len(a)):
            if len(a[i])==len(edges):
                return i