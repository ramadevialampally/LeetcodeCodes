# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        d={}
        while head:
            v=head.val
            if v in d:
                d[v]+=1
            else:
                d[v]=1
            head=head.next
        a=[]
        for k,v in d.items():
            if v==1:
                a.append(k)
        if len(a)==0:
            return None
        a=sorted(a)
        head=ListNode(a[0])
        temp=head
        for i in range(1,len(a)):
            temp.next=ListNode(a[i])
            temp=temp.next
        return head
            