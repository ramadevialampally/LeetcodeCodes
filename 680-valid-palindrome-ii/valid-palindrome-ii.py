class Solution:
    def validPalindrome(self, s: str) -> bool:
        if(s==s[::-1]):
            return True
        i=0
        j=len(s)-1
        a=list(s)
        while i<=j:
            if(s[i]!=s[j]):
                temp1=s[:i]+s[i+1:]
                temp2=s[:j]+s[j+1:]
                return temp1==temp1[::-1] or temp2==temp2[::-1]
            i+=1
            j-=1
        return False

        
        

        