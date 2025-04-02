class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        d={}
        for i in grid:

            i=tuple(i)
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        print(d)
        c=0
        for i in range(len(grid[0])):
            a=[]
            for j in range(len(grid)):
                a.append(grid[j][i])
            k=tuple(a)
            print(k)
            if k in d:
                c+=d[k]
        return c
