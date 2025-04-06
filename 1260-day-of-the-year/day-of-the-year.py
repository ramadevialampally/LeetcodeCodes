class Solution:
    def dayOfYear(self, date: str) -> int:
        from datetime import datetime
        x=datetime.strptime(date,"%Y-%m-%d")
        return int(x.strftime("%j"))
        