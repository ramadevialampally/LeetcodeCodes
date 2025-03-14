class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        if s==goal:
            return len(set(s))<len(s)
        diff=[(s[i],goal[i]) for i in range(len(s)) if s[i]!=goal[i]]
        return len(diff)==2 and diff[0]==diff[1][::-1]

        