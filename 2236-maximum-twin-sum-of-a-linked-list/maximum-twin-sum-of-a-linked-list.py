# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        a=[]
        t1=head
        while t1:
            a.append(t1.val)
            t1=t1.next
        n=len(a)
        l=0
        r=n-1
        m=float("-inf")
        while l<r:
            s=a[l]+a[r]
            m=max(m,s)
            l+=1
            r-=1
        return m

        