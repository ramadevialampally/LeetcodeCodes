class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        m=[]
        for i in nums:
            heapq.heappush(m,i)
            if len(m)>k:
                heapq.heappop(m)
        return m[0]
        