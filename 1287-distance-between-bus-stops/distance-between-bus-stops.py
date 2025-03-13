class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        r=0
        l=0
        s=start
        d=destination
        while (s%len(distance)!=destination):
            r+=distance[s%len(distance)]
            s+=1
       
           
        while destination%(len(distance))!=start:
            l+=distance[destination%len(distance)]
            destination+=1
        return min(l,r)
        