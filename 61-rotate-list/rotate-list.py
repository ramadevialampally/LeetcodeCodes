# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        a=[]
        while head:
            a.append(head.val)
            head=head.next
        a=a[::-1]
        b=a[k%(len(a)):][::-1]
        c=a[:k%len(a)][::-1]
        res=[]
        for i in c:
            res.append(i)
        for i in b:
            res.append(i)
        head=ListNode(res[0])
        temp=head
        for i in range(1,len(res)):
            temp.next=ListNode(res[i])
            temp=temp.next
        return head



        
        