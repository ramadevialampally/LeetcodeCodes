class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a=[]
        m=0
        j=0
        for i in range(len(s)):
            if s[i] in a:
                while s[i]  in a and j<i:
                    a.pop(0)
            a.append(s[i])
            m=max(m,len(a))
        return m            
