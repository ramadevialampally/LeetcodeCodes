class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if  n==0 :
            return True
        if len(flowerbed)<=2 and all(i==0 for i in flowerbed) and n<=1:
            return True
        if len(flowerbed)<=2 :
            return False
        if flowerbed[1]==0 and flowerbed[0]==0:
            flowerbed[0]=1
            n-=1
        for i in range(1,len(flowerbed)-1):
            print(n,i)
            if n==0:
                return True
            if(flowerbed[i-1]==0 and flowerbed[i]==0 and flowerbed[i+1]==0):
                flowerbed[i]=1
                n-=1
        if(flowerbed[len(flowerbed)-1]==0 and flowerbed[len(flowerbed)-2]==0):
            n-=1
        return n==0
            
        