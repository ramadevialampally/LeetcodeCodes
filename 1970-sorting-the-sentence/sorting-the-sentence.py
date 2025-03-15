class Solution:
    def sortSentence(self, s: str) -> str:
        r=s.split()
        print(r)
        ans=[""]*(len(r))
        for i in r:
            k=int(i[-1])
            ans[k-1]=i[:len(i)-1]
        return " ".join(ans)
    
        
        