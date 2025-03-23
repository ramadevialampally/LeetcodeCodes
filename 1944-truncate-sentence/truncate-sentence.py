class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        s=s.split()
        k=s[:k]
        return " ".join(k)
        