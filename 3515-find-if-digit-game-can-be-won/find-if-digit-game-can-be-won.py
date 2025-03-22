class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        so=0
        ss=0
        for i in nums:
            if i<=9:
                so+=i
            else:
                ss+=i
        if so>ss or ss>so:
            return True
        return False
        