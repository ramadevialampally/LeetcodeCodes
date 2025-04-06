class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capc=0
        loc=0
        for i in word:
            if i.islower():
                capc+=1
            else:
                loc+=1
        if capc==len(word) or loc==len(word):
            return True
        c=0
        if word[0].isupper():
            c+=1
        for i in range(1,len(word)):
            if word[i].isupper():
                return False
        if c==1:
            return True
        return False