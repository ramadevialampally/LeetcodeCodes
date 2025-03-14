class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        c=0
        a=[]
        for i in range(n):
            b=[]
            for j in range(n):
                b.append(c)
                c+=1
            a.append(b)
        res=[[0,1],[-1,0],[0,-1],[1,0]]
        x,y=0,0
        for i in commands:
            if i=="RIGHT":
                x=x+res[0][0]
                y=y+res[0][1]
            elif i=="DOWN":
                x=x+res[3][0]
                y=y+res[3][1]
               
            elif i=="UP":
                x=x+res[1][0]
                y=y+res[1][1]
            else:
                x=x+res[2][0]
                y=y+res[2][1]
        return a[x][y]
        

        