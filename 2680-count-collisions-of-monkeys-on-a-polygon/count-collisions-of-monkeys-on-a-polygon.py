class Solution:
    def monkeyMove(self, n: int) -> int:
        mod=(10**9)+7
        t=pow(2,n,mod)
        no=2
        return (t-no+mod)%(mod)
        