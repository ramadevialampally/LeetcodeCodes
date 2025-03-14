class Solution:
    def makeGood(self, s: str) -> str:
        def isbad(a,b):
            return a!=b and a.lower()==b.lower()
        ans=[]
        for i in s:
            if ans and isbad(ans[-1],i):
                ans.pop()
            else:
                ans.append(i)
        return "".join(ans)
