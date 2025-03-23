class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        i=0
        c=0
        j=len(people)-1
        people=sorted(people)
        while i<=j:
            if(people[i]+people[j]<=limit):
                i+=1
            j-=1
            c+=1
        return c