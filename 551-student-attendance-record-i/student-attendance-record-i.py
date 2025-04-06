class Solution:
    def checkRecord(self, s: str) -> bool:
        abc=0
        lac=0
        for i in s:
            if i=='P':
                lac=0
            elif i=='A':
                abc+=1
                lac=0
            else:
                lac+=1
            if abc>=2 or lac>=3:
                return False
        return True
        